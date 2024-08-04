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
from sys_info_api.common.exceptions import MetricNotAvailable


class IPLink(BinCollector):
	"""
	Gathers interface names from ip
	"""

	def __init__(self):
		"""
		:raises MetricNotAvailable:
		"""
		super().__init__()
		self.bin = 'ip'
		self.arguments = ['-br', 'link']
		self.parser = self.PARSER_LINES

	def parse(self):

		super().parse()
		interfaces = {}

		for line in self.data:
			if 'LOOPBACK' in line:
				# Skip loopback
				continue

			field_data = line.split()

			interfaces[field_data[0]] = {
				'mac': None,
				'flags': None,
			}

			if len(field_data) == 4:
				interfaces[field_data[0]]['mac'] = field_data[2]
				interfaces[field_data[0]]['flags'] = field_data[3][1:-1].split(',')
			elif len(field_data) == 3:
				interfaces[field_data[0]]['flags'] = field_data[2][1:-1].split(',')

		# Save the data
		self.data = interfaces

	def get_names(self) -> List[str]:
		"""
		Get a list of network interfaces present
		:raises MetricNotAvailable:
		"""
		self.ensure_ready()
		return list(self.data.keys())

	def get_admin_statuses(self) -> dict:
		"""
		Get the administrative status of the interfaces
		:raises MetricNotAvailable:
		"""
		admin_statuses = {}
		for interface in self.get_names():
			admin_statuses[interface] = 'UP' if 'UP' in self.data[interface]['flags'] else 'DOWN'
		return admin_statuses

	def get_statuses(self) -> dict:
		"""
		Get the status of the interfaces
		:raises MetricNotAvailable:
		"""
		statuses = {}
		for interface in self.get_names():
			statuses[interface] = 'UP' if 'LOWER_UP' in self.data[interface]['flags'] else 'DOWN'
		return statuses

	def get_status(self, iface: str) -> str:
		"""
		Get the status of the given interface
		:raises MetricNotAvailable:
		"""
		try:
			return self.get_statuses()[iface]
		except KeyError:
			raise MetricNotAvailable

	def get_mac_addresses(self) -> dict:
		"""
		Get the status of the interfaces
		:raises MetricNotAvailable:
		"""
		macs = {}
		for interface in self.get_names():
			macs[interface] = self.data[interface]['mac']
		return macs


class IPLinkTest(BinCollectorTest):
	def setUp(self):
		self.collector = IPLink()

		self.keys = {
			'names': self.collector.get_names,
			'admin_statuses': self.collector.get_admin_statuses,
			'statuses': self.collector.get_statuses,
			'macs': self.collector.get_mac_addresses,
		}
