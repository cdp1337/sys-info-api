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

from sys_info_api.common.bin_collector import BinCollector
from sys_info_api.common.bin_collector_test import BinCollectorTest


class UnameVersion(BinCollector):
	def __init__(self):
		super().__init__()
		self.bin = 'uname'
		self.arguments = ['-r']
		self.parser = self.PARSER_RAW

	def get_data(self) -> str:
		"""
		Get the version of the kernel running on the system
		:return: str ex: 5.4.0-65-generic
		"""
		self.ensure_ready()
		return self.data


class UnameMachine(BinCollector):
	def __init__(self):
		super().__init__()
		self.bin = 'uname'
		self.arguments = ['-m']
		self.parser = self.PARSER_RAW

	def get_data(self) -> str:
		"""
		Get the machine architecture of the system
		:return: str ex: x86_64
		"""
		self.ensure_ready()
		return self.data


class UnameVersionTest(BinCollectorTest):
	def setUp(self):
		self.collector = UnameVersion()
		self.keys = {
			'data': self.collector.get_data,
		}


class UnameMachineTest(BinCollectorTest):
	def setUp(self):
		self.collector = UnameMachine()
		self.keys = {
			'data': self.collector.get_data,
		}
