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

import os

from sys_info_api.common.bin_collector import BinCollector
from sys_info_api.common.bin_collector_test import BinCollectorTest
from sys_info_api.common.exceptions import MetricNotAvailable


class Version(BinCollector):
	def __init__(self):
		super().__init__()

		self.bin = 'cat'

		if os.path.exists('/etc/version'):
			self.arguments = ['/etc/version']
		else:
			self.bin = 'false'

		self.parser = self.PARSER_RAW

	def get_name(self) -> str:
		"""
		Get the appliance name from /etc/version

		When viewing managed appliances, the base OS is rarely wanted, so this will
		retrieve the appliance name instead

		:return:

		:raises MetricNotAvailable:
		"""
		self.ensure_ready()
		# Hardcode the values for the moment, because I don't know what all craziness may be here.
		if self.data.startswith('TrueNAS-'):
			# TrueNAS-12.0-U1.1 (401ffb1d98)
			return 'TrueNAS'
		else:
			raise MetricNotAvailable

	def get_version(self) -> str:
		"""
		Get the appliance version from /etc/version

		When viewing managed appliances, the base OS is rarely wanted, so this will
		retrieve the appliance name instead

		:return:

		:raises MetricNotAvailable:
		"""
		self.ensure_ready()
		# Hardcode the values for the moment, because I don't know what all craziness may be here.
		if self.data.startswith('TrueNAS-'):
			# TrueNAS-12.0-U1.1 (401ffb1d98)
			contents = self.data[8:].split(' ')
			return contents[0]
		else:
			raise MetricNotAvailable


class VersionTest(BinCollectorTest):
	def setUp(self):
		self.collector = Version()
		self.keys = {
			'name': self.collector.get_name,
			'version': self.collector.get_version,
		}
