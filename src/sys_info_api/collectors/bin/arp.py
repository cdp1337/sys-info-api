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

from typing import List
from sys_info_api.common.bin_collector import BinCollector
from sys_info_api.common.bin_collector_test import BinCollectorTest


class Arp(BinCollector):
	def __init__(self):
		"""
		:raises MetricNotAvailable:
		"""
		super().__init__()
		self.bin = 'arp'
		self.arguments = ['-an']
		self.parser = self.PARSER_LINES

	def parse(self):
		super().parse()

		if len(self.data) == 1 and self.data[0].startswith('arp: '):
			# "arp: in # entries no match found"
			self.data = []
			return

		results = []
		for line in self.data:
			# Formatted in HOSTNAME (IP) at MAC [TYPE] on [INTERFACE]
			parts = line.split(" ")

			if len(parts) >= 7:
				ip = parts[1][1:-1]
				mac = parts[3]
				iface = parts[6]

				if mac == '<incomplete>':
					mac = None
				elif mac == '(incomplete)':
					mac = None
				elif mac == 'ff:ff:ff:ff:ff:ff':
					mac = None
				else:
					# MacOS will shorten the MAC address by removing prepended 0's
					mac_fragments = mac.split(':')
					for i in range(len(mac_fragments)):
						if len(mac_fragments[i]) == 1:
							mac_fragments[i] = '0' + mac_fragments[i]
					mac = ':'.join(mac_fragments)

				if ip.startswith('224.0'):
					ip = None
				elif ip.startswith('169.254'):
					ip = None

				# At least mac and ip are required
				if mac is not None and ip is not None:
					results.append({
						'ip': ip,
						'mac': mac,
						'interface': iface
					})
		self.data = results

	def get_data(self) -> List[dict]:
		"""
		Get the neighbors as a list of dictionaries

		:raises MetricNotAvailable:
		"""
		self.ensure_ready()
		return self.data

	def get_ips(self) -> List[str]:
		"""
		Get the list of IP addresses

		:raises MetricNotAvailable:
		"""
		self.ensure_ready()
		return [x['ip'] for x in self.data]

	def get_ips_on(self, iface: str) -> List[str]:
		"""
		Get the list of IP addresses on a specific interface

		:raises MetricNotAvailable:
		"""
		self.ensure_ready()
		return [x['ip'] for x in self.data if x['interface'] == iface]


class ArpTest(BinCollectorTest):
	def setUp(self):
		self.collector = Arp()

	def get_test_keys(self) -> dict[str, callable]:
		keys = {
			'data': self.collector.get_data,
			'ips': self.collector.get_ips
		}

		# Get the interfaces detected in the data and include a test key for each specific interface
		interfaces = set(x['interface'] for x in self.collector.get_data())
		for iface in interfaces:
			keys[f'ips_on_{iface}'] = [self.collector.get_ips_on, iface]

		return keys
