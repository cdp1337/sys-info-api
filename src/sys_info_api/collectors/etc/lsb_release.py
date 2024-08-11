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


class LsbRelease(BinCollector):
	"""
	Provides a simple API to read /etc/lsb-release or /etc/upstream-release/lsb-release data

	Compatibility:

	{%img_ubuntu%}
	"""

	def __init__(self, upstream=False):
		"""
		:raises MetricNotAvailable:
		"""
		super().__init__()
		self.bin = 'cat'

		if upstream:
			if os.path.exists('/etc/upstream-release/lsb-release'):
				self.arguments = ['/etc/upstream-release/lsb-release']
			else:
				self.bin = 'false'
		else:
			if os.path.exists('/etc/lsb-release'):
				self.arguments = ['/etc/lsb-release']
			else:
				self.bin = 'false'

		self.parser = self.PARSER_LINES_KEY_VALUE
		self.parser_options = {
			'sep': '=',
			'comment': '#'
		}

	def get_id(self) -> str:
		"""
		A string identifying the operating system, without a version
		component, and suitable for presentation to the user.

		:return:
		:raises MetricNotAvailable:
		"""
		return self._get('DISTRIB_ID').lower()

	def get_version(self) -> dict:
		"""
		Get the version as a dictionary of values

		A string identifying the operating system version, excluding
		any OS name information, possibly including a release code
		name, and suitable for presentation to the user.

		:return dict: 'major', 'minor'
		:raises MetricNotAvailable:
		"""

		version = self._get('DISTRIB_RELEASE')
		ret = {
			'major': None,
			'minor': 0
		}

		version = version.split('.')
		if len(version) >= 1:
			ret['major'] = version[0]
		if len(version) >= 2:
			ret['minor'] = version[1]

		return ret

	def get_version_string(self) -> str:
		"""
		Get the full version string of this OS

		:raises MetricNotAvailable:
		"""

		version = self.get_version()
		parts = []
		if version['major'] is not None:
			parts.append(version['major'])

			if version['minor'] is not None:
				parts.append(version['minor'])

		return '.'.join(parts)

	def get_version_codename(self) -> str:
		"""
		Get the codename of this OS version
		:return: str
		:raises MetricNotAvailable:
		"""
		return self._get('DISTRIB_CODENAME')


class LsbReleaseTest(BinCollectorTest):
	def setUp(self):
		self.collector = LsbRelease()

		self.keys = {
			'version_codename': self.collector.get_version_codename,
			'version_string': self.collector.get_version_string,
			'id': self.collector.get_id
		}
