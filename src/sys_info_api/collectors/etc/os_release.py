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
from typing import List
from sys_info_api.common.bin_collector import BinCollector
from sys_info_api.common.bin_collector_test import BinCollectorTest
from sys_info_api.common.exceptions import MetricNotAvailable


class OsRelease(BinCollector):
	"""
	Provides a simple API to read /etc/os-release data

	Compatibility:

	{%img_linux_all%} {%img_freebsd%} {%img_proxmox%} {%img_truenas%}

	@see https://www.man7.org/linux/man-pages/man5/os-release.5.html
	"""

	def __init__(self):
		"""
		:raises MetricNotAvailable:
		"""
		super().__init__()
		self.bin = 'cat'

		if os.path.exists('/etc/os-release'):
			self.arguments = ['/etc/os-release']
		elif os.path.exists('/usr/lib/os-release'):
			self.arguments = ['/usr/lib/os-release']
		else:
			self.bin = 'false'

		self.parser = self.PARSER_LINES_KEY_VALUE
		self.parser_options = {
			'sep': '=',
			'comment': '#'
		}

	def get_name(self) -> str:
		"""
		A string identifying the operating system, without a version
		component, and suitable for presentation to the user.

		:return:
		:raises MetricNotAvailable:
		"""
		return self._get('NAME')

	def get_version(self) -> dict:
		"""
		Get the version as a dictionary of values

		A string identifying the operating system version, excluding
		any OS name information, possibly including a release code
		name, and suitable for presentation to the user.

		:return dict: 'major', 'minor', 'point', 'modifier', 'release', 'codename'
		:raises MetricNotAvailable:
		"""

		version = self._get('VERSION')
		ret = {
			'major': None,
			'minor': None,
			'point': None,
			'modifier': None,
			'codename': None
		}

		if 0 < version.index('(') < version.index(')'):
			# Extract codename, eg: VERSION="20.04.6 LTS (Focal Fossa)"
			ret['codename'] = version[version.index('(') + 1:version.index(')')]
			version = version[:version.index('(')].strip()

		if ' LTS' in version:
			# LTS release, eg: VERSION="20.04.6 LTS (Focal Fossa)"
			ret['modifier'] = 'LTS'
			version = version.replace(' LTS', '')

		if '-RELEASE-' in version:
			# FreeBSD release, eg: VERSION="13.1-RELEASE-p9"
			ret['modifier'] = 'Release ' + version[version.index('-RELEASE-') + 9:]
			version = version[:version.index('-RELEASE-')]

		version = version.split('.')
		if len(version) >= 1:
			ret['major'] = version[0]
		if len(version) >= 2:
			ret['minor'] = version[1]
		if len(version) >= 3:
			ret['point'] = version[2]

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

				if version['point'] is not None:
					parts.append(version['point'])

		if version['modifier'] is not None:
			return '.'.join(parts) + ' ' + version['modifier']
		else:
			return '.'.join(parts)

	def get_version_codename(self) -> str:
		"""
		Get the codename of this OS version
		:return: str
		:raises MetricNotAvailable:
		"""
		return self.get_version()['codename']

	def get_id(self) -> str:
		return self._get('ID').lower()

	def get_like(self) -> List[str]:
		"""
		Get a list of "like" operating systems

		A lower-case string (no spaces or other characters outside of 0-9, a-z, ".", "_" and "-") identifying the
		operating system, excluding any version information and suitable for processing by scripts or usage in
		generated filenames. If not set, defaults to "ID=linux". Example: "ID=fedora" or "ID=debian".
		:return:
		"""

		try:
			id_name = self._get('ID').lower()
		except MetricNotAvailable:
			id_name = 'linux'

		try:
			id_like = self._get('ID_LIKE').lower().split(' ')
		except MetricNotAvailable:
			id_like = []

		return [id_name] + id_like

	def like_os(self, name: str) -> bool:
		"""
		Check if this OS is "like" the requested OS.

		This checks if it is a derivative, but also checks if the OS itself is what's being checked

		:param name: OS name to check, lowercase
		:return: If this appears to be the matching OS
		"""

		return name.lower() in self.get_like()


class OsReleaseTest(BinCollectorTest):
	def setUp(self):
		self.collector = OsRelease()

		self.keys = {
			'name': self.collector.get_name,
			'version_codename': self.collector.get_version_codename,
			'version_string': self.collector.get_version_string,
			'like': self.collector.get_like,
			'id': self.collector.get_id
		}
