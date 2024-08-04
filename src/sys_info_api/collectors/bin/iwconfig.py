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

from sys_info_api.common import formatted_string_to_bytes
from sys_info_api.common.bin_collector import BinCollector
from sys_info_api.common.bin_collector_test import BinCollectorTest


class Iwconfig(BinCollector):
	def __init__(self):
		super().__init__()

		self.bin = 'iwconfig'
		self.parser = self.PARSER_LINES

	def parse(self):
		super().parse()

		new_data = {}
		iface = None

		for line in self.data:
			if line == '':
				# Skip blank lines
				continue

			if not line.startswith((' ', '\t')):
				iface = line.split()[0]
				new_data[iface] = {}

			if 'ESSID:' in line:
				match = re.match('.*ESSID:"(.*)"', line)
				new_data[iface]['ssid'] = match.groups()[0]

			if 'Frequency:' in line:
				match = re.match('.*Frequency:([0-9.]* [TGMk]Hz).*', line)
				new_data[iface]['frequency'] = match.groups()[0]

			if 'Access Point: ' in line:
				match = re.match('.*Access Point: ([0-9A-F:]*)', line)
				new_data[iface]['ap'] = match.groups()[0]

			if 'Bit Rate=' in line:
				match = re.match('.*Bit Rate=([0-9.]* [TGMk]b/s).*', line)
				new_data[iface]['speed'] = match.groups()[0]

			if 'Signal level=' in line:
				match = re.match('.*Signal level=([-0-9]* dBm).*', line)
				new_data[iface]['signal'] = match.groups()[0]

		self.data = new_data

	def get_names(self) -> List[str]:
		"""
		Get a list of all wireless interface names
		:return:
		"""
		self.ensure_ready()
		return list(self.data.keys())

	def get_ssid(self, iface: str) -> str:
		return self._get([iface, 'ssid'])

	def get_frequency(self, iface: str) -> str:
		return self._get([iface, 'frequency'])

	def get_access_point(self, iface: str) -> str:
		return self._get([iface, 'ap'])

	def get_speed(self, iface: str) -> int:
		return formatted_string_to_bytes(self._get([iface, 'speed']))

	def get_signal(self, iface: str) -> str:
		return self._get([iface, 'signal'])


class IwconfigTest(BinCollectorTest):
	def setUp(self):
		self.collector = Iwconfig()

	def get_test_keys(self) -> dict[str, callable]:

		keys = {
			'names': self.collector.get_names,
		}

		for iface in self.collector.get_names():
			keys[f'iface_{iface}_ssid'] = [self.collector.get_ssid, iface]
			keys[f'iface_{iface}_frequency'] = [self.collector.get_frequency, iface]
			keys[f'iface_{iface}_access_point'] = [self.collector.get_access_point, iface]
			keys[f'iface_{iface}_speed'] = [self.collector.get_speed, iface]
			keys[f'iface_{iface}_signal'] = [self.collector.get_signal, iface]

		return keys
