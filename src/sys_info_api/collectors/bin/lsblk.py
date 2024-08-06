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

from sys_info_api.common import formatted_string_to_bytes
from sys_info_api.common.bin_collector import BinCollector
from sys_info_api.common.bin_collector_test import BinCollectorTest
from sys_info_api.common.exceptions import MetricNotAvailable


class Lsblk(BinCollector):

	def __init__(self):
		super().__init__()

		self.bin = 'lsblk'
		self.arguments = ['-On', '--json']
		self.parser = self.PARSER_JSON
		self._disk_lookup = {}
		self._partition_lookup = {}
		self._filesystem_lookup = {}

	def parse(self):
		super().parse()

		# Store the cache lookups for common objects
		for i in range(len(self.data['blockdevices'])):
			if self.data['blockdevices'][i]['type'] == 'disk':
				self._disk_lookup[self.data['blockdevices'][i]['name']] = i

				if self.data['blockdevices'][i]['fstype'] is not None:
					self._filesystem_lookup[self.data['blockdevices'][i]['name']] = [i]

				if 'children' in self.data['blockdevices'][i]:
					for c in range(len(self.data['blockdevices'][i]['children'])):
						if self.data['blockdevices'][i]['children'][c]['type'] == 'part':
							self._partition_lookup[self.data['blockdevices'][i]['children'][c]['name']] = [i, c]

							if self.data['blockdevices'][i]['children'][c]['fstype'] is not None:
								self._filesystem_lookup[self.data['blockdevices'][i]['children'][c]['name']] = [i, c]

	def _get_disk_idx(self, name: str) -> int:
		"""
		:param name: Disk name to lookup
		:return:
		:raises MetricNotAvailable:
		"""
		self.ensure_ready()
		try:
			return self._disk_lookup[name]
		except KeyError:
			raise MetricNotAvailable

	def _get_partition_idx(self, name: str) -> List[int]:
		self.ensure_ready()
		try:
			return self._partition_lookup[name]
		except KeyError:
			raise MetricNotAvailable

	def _get_filesystem_idx(self, name: str) -> List[int]:
		self.ensure_ready()
		try:
			return self._filesystem_lookup[name]
		except KeyError:
			raise MetricNotAvailable

	def get_disk_names(self) -> List[str]:
		"""
		:return list: List of disk names detected

		:raises MetricNotAvailable:
		"""

		self.ensure_ready()
		return list(self._disk_lookup.keys())

	def get_partition_names(self) -> List[str]:
		self.ensure_ready()
		return list(self._partition_lookup.keys())

	def get_filesystem_names(self) -> List[str]:
		self.ensure_ready()
		return list(self._filesystem_lookup.keys())

	def get_disk_path(self, disk: str) -> str:
		"""
		:param disk: Disk name to lookup
		:return:
		:raises MetricNotAvailable:
		"""
		return self._get(['blockdevices', self._get_disk_idx(disk), 'path'])

	def get_disk_uuid(self, disk: str) -> str:
		"""
		:param disk: Disk name to lookup
		:return:
		:raises MetricNotAvailable:
		"""
		return self._gets([
			['blockdevices', self._get_disk_idx(disk), 'uuid'],
			['blockdevices', self._get_disk_idx(disk), 'ptuuid']
		])

	def get_disk_partitioning(self, disk: str) -> str:
		return self._get(['blockdevices', self._get_disk_idx(disk), 'pttype'])

	def get_disk_hotplug(self, disk: str) -> bool:
		"""
		:param disk: Disk name to lookup
		:return:
		:raises MetricNotAvailable:
		"""
		return self._get(['blockdevices', self._get_disk_idx(disk), 'hotplug'])

	def get_disk_model(self, disk: str) -> str:
		"""
		:param disk: Disk name to lookup
		:return:
		:raises MetricNotAvailable:
		"""
		return self._get(['blockdevices', self._get_disk_idx(disk), 'model'])

	def get_disk_serial(self, disk: str) -> str:
		"""
		:param disk: Disk name to lookup
		:return:
		:raises MetricNotAvailable:
		"""
		return self._get(['blockdevices', self._get_disk_idx(disk), 'serial'])

	def get_disk_size(self, disk: str) -> int:
		"""
		:param disk: Disk name to lookup
		:return:
		:raises MetricNotAvailable:
		"""
		return formatted_string_to_bytes(self._get(['blockdevices', self._get_disk_idx(disk), 'size']))

	def get_disk_state(self, disk: str) -> str:
		"""
		:param disk: Disk name to lookup
		:return:
		:raises MetricNotAvailable:
		"""
		return self._get(['blockdevices', self._get_disk_idx(disk), 'state'])

	def get_disk_rotational(self, disk: str) -> bool:
		"""
		:param disk: Disk name to lookup
		:return:
		:raises MetricNotAvailable:
		"""
		return bool(self._get(['blockdevices', self._get_disk_idx(disk), 'rota']))

	def get_disk_transport(self, disk: str) -> str:
		"""
		:param disk: Disk name to lookup
		:return:
		:raises MetricNotAvailable:
		"""
		return self._get(['blockdevices', self._get_disk_idx(disk), 'tran'])

	def get_disk_rev(self, disk: str) -> str:
		"""
		:param disk: Disk name to lookup
		:return:
		:raises MetricNotAvailable:
		"""
		return self._get(['blockdevices', self._get_disk_idx(disk), 'rev'])

	def get_disk_vendor(self, disk: str) -> str:
		"""
		:param disk: Disk name to lookup
		:return:
		:raises MetricNotAvailable:
		"""
		value = self._get(['blockdevices', self._get_disk_idx(disk), 'vendor']).strip()

		if value == 'ATA' or value == 'None':
			raise MetricNotAvailable
		else:
			return value

	def get_partition_type(self, partition: str) -> str:
		idx = self._get_partition_idx(partition)
		return self._get(['blockdevices', idx[0], 'children', idx[1], 'parttypename'])

	def get_partition_path(self, partition: str) -> str:
		idx = self._get_partition_idx(partition)
		return self._get(['blockdevices', idx[0], 'children', idx[1], 'path'])

	def get_partition_uuid(self, partition: str) -> str:
		idx = self._get_partition_idx(partition)
		return self._get(['blockdevices', idx[0], 'children', idx[1], 'uuid'])

	def get_partition_size(self, partition: str) -> int:
		idx = self._get_partition_idx(partition)
		return formatted_string_to_bytes(self._get(['blockdevices', idx[0], 'children', idx[1], 'size']))

	def get_filesystem_type(self, filesystem: str) -> str:
		idx = self._get_filesystem_idx(filesystem)
		if len(idx) == 2:
			return self._get(['blockdevices', idx[0], 'children', idx[1], 'fstype'])
		else:
			return self._get(['blockdevices', idx[0], 'fstype'])

	def get_filesystem_version(self, filesystem: str) -> str:
		idx = self._get_filesystem_idx(filesystem)
		if len(idx) == 2:
			return self._get(['blockdevices', idx[0], 'children', idx[1], 'fsver'])
		else:
			return self._get(['blockdevices', idx[0], 'fsver'])

	def get_filesystem_size(self, filesystem: str) -> int:
		idx = self._get_filesystem_idx(filesystem)
		if len(idx) == 2:
			return formatted_string_to_bytes(self._get(['blockdevices', idx[0], 'children', idx[1], 'fssize']))
		else:
			return formatted_string_to_bytes(self._get(['blockdevices', idx[0], 'fssize']))

	def get_filesystem_used(self, filesystem: str) -> int:
		idx = self._get_filesystem_idx(filesystem)
		if len(idx) == 2:
			return formatted_string_to_bytes(self._get(['blockdevices', idx[0], 'children', idx[1], 'fsused']))
		else:
			return formatted_string_to_bytes(self._get(['blockdevices', idx[0], 'fsused']))

	def get_filesystem_label(self, filesystem: str) -> str:
		idx = self._get_filesystem_idx(filesystem)
		if len(idx) == 2:
			return self._get(['blockdevices', idx[0], 'children', idx[1], 'label'])
		else:
			return self._get(['blockdevices', idx[0], 'label'])

	def get_filesystem_mount(self, filesystem: str) -> str:
		idx = self._get_filesystem_idx(filesystem)
		if len(idx) == 2:
			return self._get(['blockdevices', idx[0], 'children', idx[1], 'mountpoint'])
		else:
			return self._get(['blockdevices', idx[0], 'mountpoint'])


class LsblkTest(BinCollectorTest):
	def setUp(self):
		self.collector = Lsblk()

	def get_test_keys(self) -> dict:
		keys = {
			'disks': self.collector.get_disk_names,
			'partitions': self.collector.get_partition_names,
			'filesystems': self.collector.get_filesystem_names
		}

		disks = self.collector.get_disk_names()
		partitions = self.collector.get_partition_names()
		filesystems = self.collector.get_filesystem_names()

		for disk in disks:
			keys[f'disk_{disk}_path'] = [self.collector.get_disk_path, disk]
			keys[f'disk_{disk}_uuid'] = [self.collector.get_disk_uuid, disk]
			keys[f'disk_{disk}_partitioning'] = [self.collector.get_disk_partitioning, disk]
			keys[f'disk_{disk}_hotplug'] = [self.collector.get_disk_hotplug, disk]
			keys[f'disk_{disk}_model'] = [self.collector.get_disk_model, disk]
			keys[f'disk_{disk}_serial'] = [self.collector.get_disk_serial, disk]
			keys[f'disk_{disk}_size'] = [self.collector.get_disk_size, disk]
			keys[f'disk_{disk}_state'] = [self.collector.get_disk_state, disk]
			keys[f'disk_{disk}_rotational'] = [self.collector.get_disk_rotational, disk]
			keys[f'disk_{disk}_transport'] = [self.collector.get_disk_transport, disk]
			keys[f'disk_{disk}_rev'] = [self.collector.get_disk_rev, disk]
			keys[f'disk_{disk}_vendor'] = [self.collector.get_disk_vendor, disk]

		for partition in partitions:
			keys[f'partition_{partition}_type'] = [self.collector.get_partition_type, partition]
			keys[f'partition_{partition}_path'] = [self.collector.get_partition_path, partition]
			keys[f'partition_{partition}_uuid'] = [self.collector.get_partition_uuid, partition]
			keys[f'partition_{partition}_size'] = [self.collector.get_partition_size, partition]

		for filesystem in filesystems:
			keys[f'filesystem_{filesystem}_type'] = [self.collector.get_filesystem_type, filesystem]
			keys[f'filesystem_{filesystem}_version'] = [self.collector.get_filesystem_version, filesystem]
			keys[f'filesystem_{filesystem}_size'] = [self.collector.get_filesystem_size, filesystem]
			keys[f'filesystem_{filesystem}_used'] = [self.collector.get_filesystem_used, filesystem]
			keys[f'filesystem_{filesystem}_label'] = [self.collector.get_filesystem_label, filesystem]
			keys[f'filesystem_{filesystem}_mount'] = [self.collector.get_filesystem_mount, filesystem]

		return keys
