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


class YumListInstalled(BinCollector):
	def __init__(self):
		super().__init__()
		self.bin = 'yum'
		self.arguments = ['list', 'installed']
		self.parser = self.PARSER_LINES

	def parse(self):
		super().parse()

		out = []
		for i in self.data:
			parts = i.split()
			if '.' in parts[0]:
				name = parts[0][:parts[0].index('.')]
				arch = parts[0][parts[0].index('.') + 1:]
			else:
				name = parts[0]
				arch = None

			out.append({
				'name': name,
				'version': parts[1],
				'architecture': arch,
				'description': None
			})

		self.data = out

	def get_data(self) -> list:
		"""
		Get the version of the kernel running on the system
		"""
		self.ensure_ready()
		return self.data


class YumUpdates(BinCollector):
	def __init__(self):
		super().__init__()
		self.bin = 'yum'
		self.arguments = ['check-update']
		self.parser = self.PARSER_LINES
		self.return_codes = [100]

	def parse(self):
		super().parse()

		out = []
		for line in self.data:
			if line == 'Obsoleting Packages':
				# Stop processing after this line
				break
			# grub2-tools.x86_64           1:2.06-80.el9_4          baseos
			fields = line.split()
			if len(fields) == 3:
				package = fields[0]
				version = fields[1]
				name = package[0:package.index('.')]
				arch = package[package.index('.') + 1:]

				out.append({
					'package': '='.join([package, version]),
					'name': name,
					'version': version,
					'arch': arch
				})

		self.data = out

	def get_data(self) -> list:
		self.ensure_ready()
		return self.data

	def get_package_names(self) -> List[str]:
		self.ensure_ready()
		return [package['package'] for package in self.data]


class YumInstall(BinCollector):
	def __init__(self):
		super().__init__()
		self.bin = 'yum'
		self.parser = None

	def install_packages(self, packages: [str]):
		"""
		Install a set of packages using yum
		:param packages: The packages to install
		"""

		# Install the packages
		self.run(['install', '-y'] + packages)

	def install_package(self, package: str):
		"""
		Install a package using yum
		:param package: The package to install
		"""
		self.install_packages([package])


class YumListInstalledTest(BinCollectorTest):
	def setUp(self):
		self.collector = YumListInstalled()
		self.keys = {
			'data': self.collector.get_data,
		}


class YumUpdatesTest(BinCollectorTest):
	def setUp(self):
		self.collector = YumUpdates()
		self.keys = {
			'packages': self.collector.get_package_names,
		}
