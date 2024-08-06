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


class Lspci(BinCollector):
	def __init__(self):
		super().__init__()
		self.bin = 'lspci'
		self.arguments = ['-vmm', '-D', '-q']
		self.parser = self.PARSER_LINES
		self.groups = {
			'system': (
				'Host bridge',
				'IOMMU',
				'PCI bridge',
				'SMBus',
				'ISA bridge',
				'Non-Volatile memory controller',
				'Non-Essential Instrumentation [1300]',
				'USB controller',
				'SATA controller',
				'Encryption controller'
			),
			'firewire': ('FireWire (IEEE 1394)',),
			'network': ('Ethernet controller',),
			'video': ('VGA compatible controller',),
			'audio': ('Audio device',),
		}

	def parse(self):
		super().parse()

		device = None
		out = []
		for line in self.data:
			if line == '':
				# Empty line, new device
				device = None
			else:
				if device is None:
					# Create a new device, happens between records
					device = {}
					out.append(device)

				key = line[0:line.index(':')].lower()
				value = line[line.index(':') + 1:].strip()
				device[key] = value

		self.data = out

	def get_data(self) -> List[dict]:
		"""
		Get all devices located from lspci
		:return:
		"""
		self.ensure_ready()
		return self.data

	def get_system_devices(self) -> List[dict]:
		self.ensure_ready()
		# Filter data by specific device classes
		return [x for x in self.data if x['class'] in self.groups['system']]

	def get_firewire_devices(self) -> List[dict]:
		self.ensure_ready()
		# Filter data by specific device classes
		return [x for x in self.data if x['class'] in self.groups['firewire']]

	def get_network_devices(self) -> List[dict]:
		self.ensure_ready()
		# Filter data by specific device classes
		return [x for x in self.data if x['class'] in self.groups['network']]

	def get_video_devices(self) -> List[dict]:
		self.ensure_ready()
		# Filter data by specific device classes
		return [x for x in self.data if x['class'] in self.groups['video']]

	def get_audio_devices(self) -> List[dict]:
		self.ensure_ready()
		# Filter data by specific device classes
		return [x for x in self.data if x['class'] in self.groups['audio']]


class LspciTest(BinCollectorTest):
	def setUp(self):
		self.collector = Lspci()
		self.keys = {
			'system_devices': self.collector.get_system_devices,
			'firewire_devices': self.collector.get_firewire_devices,
			'network_devices': self.collector.get_network_devices,
			'video_devices': self.collector.get_video_devices,
			'audio_devices': self.collector.get_audio_devices,
		}
