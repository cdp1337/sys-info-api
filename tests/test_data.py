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
import re

import yaml
from unittest import TestCase

from sys_info_api.collectors.bin.arp import ArpTest
from sys_info_api.collectors.bin.df import DfTest
from sys_info_api.collectors.bin.dmidecode import DmiBaseboardTest, DmiBiosTest, DmiCacheTest, DmiChassisTest, \
	DmiMemoryTest, DmiProcessorTest, DmiSystemTest
from sys_info_api.collectors.bin.hostnamectl import HostnameCtlTest
from sys_info_api.collectors.bin.ifconfig import IfconfigTest
from sys_info_api.collectors.bin.ip import IPLinkTest
from sys_info_api.collectors.bin.iwconfig import IwconfigTest
from sys_info_api.collectors.bin.lldptool import LldpStatusTest, LldpNeighborScanTest
from sys_info_api.collectors.bin.lsblk import LsblkTest
from sys_info_api.collectors.bin.lspci import LspciTest
from sys_info_api.collectors.bin.lsusb import LsusbTest
from sys_info_api.collectors.bin.pveversion import PveVersionTest
from sys_info_api.collectors.bin.sysctl import SysctlKernBoottimeTest
from sys_info_api.collectors.bin.uname import UnameVersionTest, UnameMachineTest
from sys_info_api.collectors.bin.uptime import UptimeTest
from sys_info_api.collectors.bin.who import WhoBootTimeTest
from sys_info_api.collectors.etc.os_release import OsReleaseTest
from sys_info_api.collectors.etc.version import VersionTest


class TestDataFiles(TestCase):
	def test_all(self):
		# Collection of scripts to run and try to store
		collectors = [
			['bin.arp', ArpTest],
			['bin.df', DfTest],
			['bin.dmibaseboard', DmiBaseboardTest],
			['bin.dmibios', DmiBiosTest],
			['bin.dmicache', DmiCacheTest],
			['bin.dmichassis', DmiChassisTest],
			['bin.dmimemory', DmiMemoryTest],
			['bin.dmiprocessor', DmiProcessorTest],
			['bin.dmisystem', DmiSystemTest],
			['bin.hostnamectl', HostnameCtlTest],
			['bin.ifconfig', IfconfigTest],
			['bin.iplink', IPLinkTest],
			['bin.iwconfig', IwconfigTest],
			['bin.lldpstatus', LldpStatusTest],
			['bin.lldpneighborscan', LldpNeighborScanTest],
			['bin.lsblk', LsblkTest],
			['bin.lspci', LspciTest],
			['bin.lsusb', LsusbTest],
			['bin.pveversion', PveVersionTest],
			['bin.sysctlkernboottime', SysctlKernBoottimeTest],
			['bin.unameversion', UnameVersionTest],
			['bin.unamemachine', UnameMachineTest],
			['bin.uptime', UptimeTest],
			['bin.whoboottime', WhoBootTimeTest],
			['etc.os_release', OsReleaseTest],
			['etc.version', VersionTest],
		]

		# Set the target to store collected results within tests/data
		target = os.path.abspath(os.path.join(
			os.path.dirname(__file__),
			'data'
		))

		for path in os.listdir(target):
			if not os.path.isdir(os.path.join(target, path)):
				continue

			print('Loading test data from {}'.format(path))
			test_files = [f for f in os.listdir(os.path.join(target, path)) if re.match(r'.*\.yaml', f)]

			for collector_file_match, collector in collectors:
				tested = False
				for test_file in test_files:
					if test_file == collector_file_match + '.yaml':
						# Simple test with no arguments
						tested = True
						self._run_test(
							collector,
							os.path.join(target, path, collector_file_match + '.txt'),
							os.path.join(target, path, collector_file_match + '.yaml'),
							[]
						)
					elif test_file.startswith(collector_file_match + '-'):
						# Test with arguments provided
						tested = True
						self._run_test(
							collector,
							os.path.join(target, path, test_file[0:-5] + '.txt'),
							os.path.join(target, path, test_file),
							test_file[len(collector_file_match) + 1:-5].split('-')
						)

				if not tested:
					print('  Skipping {}, test data not found'.format(collector_file_match))
					continue

		print(target)

	def _run_test(self, collector, raw, data, arguments):
		test_name = '-'.join([os.path.basename(os.path.dirname(raw)), os.path.basename(raw)[0:-4]])
		print('  Testing {}'.format(os.path.basename(raw)))
		with self.subTest('{}'.format(test_name)):
			# Instantiate a new Collector (of type one of the tests)
			c = collector()
			c.setUp(*arguments)

			with open(raw, 'r') as f:
				# Load the raw data from the stored test into the cache of the collector
				c.load_raw_data(f.read())

			with open(data, 'r') as f:
				# Load the expected values from the stored test
				data = yaml.safe_load(f)

			# Compare the stored values to the calculated values from the cached raw data
			c.verify_test_data(data)
