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
from typing import List

from sys_info_api.common.bin_collector import BinCollector
from sys_info_api.common.bin_collector_test import BinCollectorTest
from sys_info_api.common.cmd import run_returncode
from sys_info_api.common.exceptions import MetricNotAvailable
from sys_info_api.common.key_value_parser import KeyValueParser


class _AptCollection:
	def __init__(self):
		self.data = None

	def ensure_ready(self):
		# noop
		pass

	def get_data(self) -> list:
		self.ensure_ready()
		return self.data

	def get_package_names(self) -> List[str]:
		self.ensure_ready()
		return [package['package'] for package in self.data]

	def get_package_by_name(self, name: str) -> dict:
		self.ensure_ready()
		for package in self.data:
			if package['package'] == name:
				return package
		raise MetricNotAvailable


class AptUpdates(BinCollector, _AptCollection):
	def __init__(self):
		super().__init__()
		self.bin = 'apt-get'
		self.arguments = ['-s', 'dist-upgrade']
		self.parser = self.PARSER_LINES

	def fetch(self):
		# Prior to fetching package updates, ensure the repo list is up to date!
		run_returncode(['apt-get', 'update'])
		super().fetch()

	def parse(self):
		super().parse()

		out = []
		for line in self.data:
			# Inst base-files [11ubuntu5] (11ubuntu5.3 Ubuntu:20.04/focal-updates [amd64])
			line = line.strip()
			if line.startswith('Inst'):
				# Strip "Inst "
				line = line[5:]

				# Grab the package name and trim off
				name = line[0:line.index(' ')]
				line = line[len(name) + 1:]

				# Grab the current version
				if line[0:1] == '[':
					line = line[1:]
					installed_version = line[:line.index(']')]
					line = line[len(installed_version) + 3:]
				else:
					installed_version = None
					line = line[1:]

				# Grab the new version
				version = line[:line.index(' ')]
				line = line[len(version) + 2:]
				# Grab the architecture
				arch = line[line.index('[') + 1:line.index(']')]

				out.append({
					'package': ':'.join([name, arch]) + '=' + version,
					'name': name,
					'version': version,
					'arch': arch
				})

		self.data = out


class AptShow(BinCollector, _AptCollection):
	def __init__(self, package: str):
		super().__init__()
		self.bin = 'apt-cache'
		self.arguments = ['show', package]
		self.parser = self.PARSER_RAW

	def parse(self):
		super().parse()

		package_groups = self.data.split('\n\n')
		packages = []
		package_parser = KeyValueParser()
		package_parser.set_opts({
			'quotes': 'none',
			'sep': ':',
			'continuation': ' '
		})

		for package_group in package_groups:
			package_data = package_parser.to_dict(package_group)
			name = package_data['Package']
			arch = package_data['Architecture']
			vers = package_data['Version']

			packages.append({
				'package': ':'.join([name, arch]) + '=' + vers,
				'name': name,
				'version': vers,
				'arch': arch,
				'installed': ('Status' in package_data and 'installed' in package_data['Status'])
			})

		self.data = packages


class AptUpdatesTest(BinCollectorTest):
	def setUp(self):
		self.collector = AptUpdates()
		self.keys = {
			'packages': self.collector.get_package_names,
		}


class AptShowTest(BinCollectorTest):
	def setUp(self, package: str):
		self.collector = AptShow(package)
		self.keys = {
			'packages': self.collector.get_package_names,
		}
