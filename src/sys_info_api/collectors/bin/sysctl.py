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

from sys_info_api.common import str_to_utc
from sys_info_api.common.bin_collector import BinCollector
from sys_info_api.common.bin_collector_test import BinCollectorTest


class SysctlKernBoottime(BinCollector):
	def __init__(self):
		super().__init__()
		self.bin = 'sysctl'
		self.arguments = ['-n', 'kern.boottime']
		self.parser = self.PARSER_RAW

	def get_data(self):
		"""
		Get the boot time of the system
		"""
		self.ensure_ready()
		return str_to_utc(self.data.index('}' + 2).strip(), '%a %b %d %H:%M:%S %Y')


class SysctlKernBoottimeTest(BinCollectorTest):
	def setUp(self):
		self.collector = SysctlKernBoottime()
		self.keys = {
			'data': self.collector.get_data,
		}
