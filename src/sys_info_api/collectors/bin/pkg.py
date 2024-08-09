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

from sys_info_api.common.bin_collector import BinCollector
from sys_info_api.common.bin_collector_test import BinCollectorTest


class PkgListInstalled(BinCollector):
	def __init__(self):
		super().__init__()
		self.bin = 'pkg'
		self.arguments = ['info']
		self.parser = self.PARSER_LINES

	def parse(self):
		super().parse()

		out = []
		for i in self.data:
			out.append({
				'name': re.sub(r'^(.*)-([^\s]*)\s*(.*)', '\\1', i),
				'version': re.sub(r'^(.*)-([^\s]*)\s*(.*)', '\\2', i),
				'architecture': None,
				'description': re.sub(r'^(.*)-([^\s]*)\s*(.*)', '\\3', i)
			})

		self.data = out

	def get_data(self) -> list:
		"""
		Get the version of the kernel running on the system
		"""
		self.ensure_ready()
		return self.data


class PkgListInstalledTest(BinCollectorTest):
	def setUp(self):
		self.collector = PkgListInstalled()
		self.keys = {
			'data': self.collector.get_data,
		}
