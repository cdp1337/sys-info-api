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
import os


class Df(BinCollector):
	"""
	Execute `df` to get the list of filesystems.

	Compatibility:

	{%img_linux_all%} {%img_freebsd%} {%img_proxmox%} {%img_truenas%}
	"""

	def __init__(self):
		"""
		:raises MetricNotAvailable:
		"""
		super().__init__()
		self.bin = 'df'
		self.arguments = ['-TlP']
		self.parser = self.PARSER_LINES

	def parse(self):
		super().parse()

		results = []

		# Default, though BSD may change this.
		blocksize = 1024

		for line in self.data:
			if line.startswith('Filesystem') and '512-blocks' in line:
				blocksize = 512

			if not line.startswith('/dev/') and not line.startswith('zroot/'):
				# Skip any device that's a pseudo device, (eg: sysfs, devfs, tmpfs, etc).
				# This also applies to ZFS; as those partitions are all dynamic, but should still be included.
				continue

			if line.startswith('/dev/loop'):
				# Skip any "loop" device; these are also fake filesystems.
				continue

			lineparts = line.split()

			if lineparts[0].startswith('/dev/'):
				# Convert /dev aliases to their real path and return just the device itself.
				dev = os.path.realpath(lineparts[0])[5:]
			else:
				dev = lineparts[0]

			results.append({
				'device': dev,
				'format': lineparts[1],
				'total': int(lineparts[2]) * blocksize,
				'used': int(lineparts[3]) * blocksize,
				'free': int(lineparts[4]) * blocksize,
				'label': lineparts[6],
			})
		self.data = results

	def get_data(self) -> List[dict]:
		"""
		Get the filesystems as a list of dictionaries

		Example Response:

		```yaml
		- device: nvme0n1p2
		format: ext4
		free: 199701401600
		label: /
		total: 1869023645696
		used: 1574305480704
		- device: nvme0n1p1
		format: vfat
		free: 4982681600
		label: /boot/efi
		total: 4988796928
		used: 6115328
		```

		:raises MetricNotAvailable:
		"""
		self.ensure_ready()
		return self.data


class DfTest(BinCollectorTest):
	def setUp(self):
		self.collector = Df()
		self.keys = {
			'data': self.collector.get_data,
		}
