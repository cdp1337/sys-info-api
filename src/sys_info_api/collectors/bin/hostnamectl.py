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


class HostnameCtl(BinCollector):
	def __init__(self):
		super().__init__()
		self.bin = 'hostnamectl'
		self.parser = self.PARSER_LINES_KEY_VALUE
		self.parser_options = {
			'sep': ':',
		}

	def get_hostname(self) -> str:
		return self._get('Static hostname')

	def get_icon(self) -> str:
		return self._get('Icon name')

	def get_chassis(self) -> str:
		return self._get('Chassis')

	def get_machine_id(self) -> str:
		return self._get('Machine ID')

	def get_boot_id(self) -> str:
		return self._get('Boot ID')

	def get_virtualization(self) -> str:
		return self._get('Virtualization')

	def get_operating_system(self) -> str:
		return self._get('Operating System')

	def get_kernel(self) -> str:
		return self._get('Kernel')

	def get_architecture(self) -> str:
		return self._get('Architecture')

	def get_vendor(self) -> str:
		return self._get('Hardware Vendor')

	def get_model(self) -> str:
		return self._get('Hardware Model')

	def get_firmware_version(self) -> str:
		return self._get('Firmware Version')


class HostnameCtlTest(BinCollectorTest):
	def setUp(self):
		self.collector = HostnameCtl()
		self.keys = {
			'hostname': self.collector.get_hostname,
			'icon': self.collector.get_icon,
			'chassis': self.collector.get_chassis,
			'machine_id': self.collector.get_machine_id,
			'boot_id': self.collector.get_boot_id,
			'virtualization': self.collector.get_virtualization,
			'operating_system': self.collector.get_operating_system,
			'kernel': self.collector.get_kernel,
			'architecture': self.collector.get_architecture,
			'vendor': self.collector.get_vendor,
			'model': self.collector.get_model,
			'firmware_version': self.collector.get_firmware_version,
		}
