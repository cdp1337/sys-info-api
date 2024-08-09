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
from sys_info_api.common.exceptions import MetricNotAvailable


class PveVersion(BinCollector):
	def __init__(self):
		"""
		:raises MetricNotAvailable:
		"""
		super().__init__()
		self.bin = 'pveversion'
		self.parser = self.PARSER_LINES

	def parse(self):
		super().parse()

		# pve-manager/6.2-6/...
		v = self.data[0]
		m = re.match('pve-manager/([0-9.-]*)/.*', v)
		if m is not None:
			self.data = {'version': m.groups(1)[0]}
		else:
			raise MetricNotAvailable

	def get_version(self) -> str:
		"""
		Get the version of Proxmox running, (only really useful on PVE hypervisors)

		:raises MetricNotAvailable:
		:returns str:
		"""
		self.ensure_ready()
		return self.data['version']


class PveVersionTest(BinCollectorTest):
	def setUp(self):
		self.collector = PveVersion()
		self.keys = {
			'version': self.collector.get_version,
		}
