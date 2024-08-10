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


class RpmInstall(BinCollector):
	def __init__(self):
		super().__init__()
		self.bin = 'rpm'
		self.parser = None

	def install_file(self, filename: str):
		"""
		Install a package using dpkg
		:param filename: The filename to install
		"""

		# Install the package
		self.run(['-Uvh', filename])
