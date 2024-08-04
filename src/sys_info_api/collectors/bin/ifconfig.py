#  Copyright (c) 2024 Charlie Powell <cdp1337@veraciousnetwork.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, version 3.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import re
from typing import List
import ipcalc

from sys_info_api.common.bin_collector import BinCollector
from sys_info_api.common.bin_collector_test import BinCollectorTest
from sys_info_api.common.enums import NetStatus


class Ifconfig(BinCollector):
	"""
	Collects information about network interfaces from the ifconfig command.
	"""

	def __init__(self):
		"""
		:raises MetricNotAvailable:
		"""
		super().__init__()
		self.bin = 'ifconfig'
		self.arguments = ['-a']
		self.parser = self.PARSER_LINES

	def parse(self):
		super().parse()

		new_data = {}
		iface = None

		for line in self.data:
			if line == '':
				# Skip blank lines
				continue

			elif not line.startswith((' ', '\t')):
				# This is the start of a new interface!
				# wlp59s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
				interface_flags = re.sub('.*<([^>]*)>.*', '\\1', line).split(",")

				# Interface system name
				iface = re.sub('^([a-zA-Z0-9&._]*):.*', '\\1', line)

				new_data[iface] = {
					'addresses': []
				}

				new_data[iface]['slot'] = iface
				new_data[iface]['label'] = iface
				new_data[iface]['mtu'] = re.sub('.*mtu ([0-9]*)', '\\1', line)
				new_data[iface]['admin_status'] = NetStatus.UP if 'UP' in interface_flags else NetStatus.DOWN
				new_data[iface]['status'] = NetStatus.UP if 'RUNNING' in interface_flags else NetStatus.DOWN

			else:
				# This line starts with whitespace *AND* there is an interface defined!
				#         inet 10.100.100.103  netmask 255.255.255.0  broadcast 10.100.100.255
				#         inet6 fe80::d59d:54bb:66a7:33ab  prefixlen 64  scopeid 0x20<link>
				#         ether 00:11:22:33:44:55  txqueuelen 1000  (Ethernet)
				#         RX packets 52465  bytes 38311454 (38.3 MB)
				#         RX errors 0  dropped 0  overruns 0  frame 0
				#         TX packets 35296  bytes 9651992 (9.6 MB)
				#         TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
				line = line.strip()

				if line.startswith('media: '):
					if 'Ethernet' in line:
						new_data[iface]['type'] = 'ethernet'

				elif line.startswith('status: '):
					status = line[8:]
					if status == 'active':
						new_data[iface]['status'] = NetStatus.UP
					elif status == 'inactive':
						new_data[iface]['status'] = NetStatus.DOWN
					elif status == 'no carrier':
						new_data[iface]['status'] = NetStatus.DOWN

				elif line.startswith('ether'):
					new_data[iface]['mac'] = line[6:23]

				elif line.startswith('inet'):
					inet_data = line.split(' ')
					inet_addr = None
					inet_netmask = None

					while len(inet_data) > 0:
						inet_key = inet_data.pop(0)
						if inet_key == 'inet' or inet_key == 'inet6':
							inet_addr = inet_data.pop(0)
						elif inet_key == 'prefixlen' and inet_addr is not None:
							inet_addr += '/' + inet_data.pop(0)
						elif inet_key == 'netmask':
							inet_netmask = inet_data.pop(0)

					if inet_addr is not None and inet_netmask is not None:
						new_data[iface]['addresses'].append(ipcalc.IP(inet_addr, inet_netmask, 4))
					elif inet_addr is not None:
						new_data[iface]['addresses'].append(ipcalc.IP(inet_addr))

		# Save the data
		self.data = new_data

	def get_names(self) -> List[str]:
		"""
		Get a list of all interface names
		:return:
		"""
		self.ensure_ready()
		return list(self.data.keys())

	def get_slot(self, iface: str) -> str:
		return self._get([iface, 'slot'])

	def get_mtu(self, iface: str) -> int:
		return self._get([iface, 'mtu'])

	def get_mac(self, iface: str) -> str:
		return self._get([iface, 'mac'])

	def get_status(self, iface: str) -> NetStatus:
		return self._get([iface, 'status'])

	def get_admin_status(self, iface: str) -> NetStatus:
		return self._get([iface, 'admin_status'])

	def get_type(self, iface: str) -> str:
		return self._get([iface, 'type'])

	def get_addresses(self, iface: str) -> List[ipcalc.IP]:
		return self._get([iface, 'addresses'])


class IfconfigTest(BinCollectorTest):
	def setUp(self):
		self.collector = Ifconfig()

	def get_test_keys(self) -> dict:

		keys = {
			'names': self.collector.get_names,
		}

		for iface in self.collector.get_names():
			keys[f'iface_{iface}_addresses'] = [self.collector.get_addresses, iface]
			keys[f'iface_{iface}_mtu'] = [self.collector.get_mtu, iface]
			keys[f'iface_{iface}_mac'] = [self.collector.get_mac, iface]
			keys[f'iface_{iface}_slot'] = [self.collector.get_slot, iface]
			keys[f'iface_{iface}_status'] = [self.collector.get_status, iface]
			keys[f'iface_{iface}_admin_status'] = [self.collector.get_admin_status, iface]
			keys[f'iface_{iface}_type'] = [self.collector.get_type, iface]

		return keys

	def generate_test_data(self) -> dict:
		data = super().generate_test_data()

		# Simplify some keys
		for iface in self.collector.get_names():
			for i in range(len(data[f'iface_{iface}_addresses'])):
				data[f'iface_{iface}_addresses'][i] = '/'.join(
					[
						str(data[f'iface_{iface}_addresses'][i]),
						str(data[f'iface_{iface}_addresses'][i].subnet())
					]
				)

		return data
