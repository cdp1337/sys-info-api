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

from sys_info_api.collectors.bin.apt import _AptCollection
from sys_info_api.common.bin_collector import BinCollector
from sys_info_api.common.bin_collector_test import BinCollectorTest


class DpkgListInstalled(BinCollector, _AptCollection):
	def __init__(self):
		super().__init__()
		self.bin = 'dpkg'
		self.arguments = ['-l']
		self.parser = self.PARSER_LINES

	def parse(self):
		super().parse()

		out = []
		for line in self.data:
			line = line.strip()
			if line.startswith('ii'):
				line_data = line.split()
				name = line_data[1]
				version = line_data[2]
				arch = line_data[3]

				out.append({
					'package': ':'.join([name, arch]) + '=' + version,
					'name': name,
					'version': version,
					'arch': arch,
					'installed': True
				})

		self.data = out


class DpkgListInstalledTest(BinCollectorTest):
	def setUp(self):
		self.collector = DpkgListInstalled()
		self.keys = {
			'packages': self.collector.get_package_names,
		}
