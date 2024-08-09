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

from datetime import datetime

from sys_info_api.common import str_to_utc
from sys_info_api.common.bin_collector import BinCollector
from sys_info_api.common.bin_collector_test import BinCollectorTest


class Uptime(BinCollector):
	def __init__(self):
		super().__init__()
		self.bin = 'uptime'
		self.arguments = ['-s']
		self.parser = self.PARSER_RAW

	def get_data(self) -> datetime:
		"""
		Get the version of the kernel running on the system
		"""
		self.ensure_ready()
		return str_to_utc(self.data, '%Y-%m-%d %H:%M:%S')


class UptimeTest(BinCollectorTest):
	def setUp(self):
		self.collector = Uptime()
		self.keys = {
			'data': self.collector.get_data,
		}
