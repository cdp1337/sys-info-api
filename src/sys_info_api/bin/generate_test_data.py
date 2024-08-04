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
import sys
import platform
import yaml

from sys_info_api.collectors.bin.arp import ArpTest
from sys_info_api.collectors.bin.df import DfTest
from sys_info_api.collectors.bin.dmidecode import DmiBaseboardTest, DmiMemoryTest, DmiBiosTest, DmiCacheTest, \
	DmiChassisTest, DmiProcessorTest, DmiSystemTest
from sys_info_api.collectors.bin.hostnamectl import HostnameCtlTest
from sys_info_api.collectors.etc.os_release import OsRelease, OsReleaseTest
# from sys_info_api.collectors.bin.test_dmimemory import TestDMIMemory
# from sys_info_api.collectors.bin.test_ifconfig import TestIfconfig
# from sys_info_api.collectors.bin.test_lldpneighborscan import TestLldpNeighborScan
# from sys_info_api.collectors.bin.test_lldpstatus import TestLldpStatus
# from sys_info_api.collectors.bin.test_mii_tool import TestMiiTool
# from sys_info_api.collectors.bin.test_iplinklist import TestIPLinkList
from sys_info_api.common.exceptions import MetricNotAvailable
# from system_information.device.net import get_all_interface_names


def run():
	if len(sys.argv) > 1:
		only_collectors = sys.argv[1:]
		print_only = True
	else:
		only_collectors = None
		print_only = False

	# @todo Swap this with the higher level functionality once ready
	try:
		os_info = OsRelease()
		target_dir = '-'.join([os_info.get_id(), os_info.get_version_string()])
	except MetricNotAvailable:
		target_dir = '-'.join([platform.system(), platform.release()])

	# Set the target to store collected results within tests/data
	target = os.path.abspath(os.path.join(
		os.path.dirname(__file__),
		'../../../tests/data',
		target_dir
	))

	# List of interfaces for interface-specific tests
	# interfaces = get_all_interface_names()

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
		['etc.os_release', OsReleaseTest],
		# ['bin.iplinklist', TestIPLinkList, None],
		# ['bin.ifconfig', TestIfconfig, None],
		# ['bin.lldpstatus', TestLldpStatus, interfaces],
		# ['bin.lldpneighborscan', TestLldpNeighborScan, interfaces],
		# ['bin.mii_tool', TestMiiTool, interfaces],
	]

	if not print_only and not os.path.exists(target):
		print('Creating test data in: {}'.format(target))
		os.mkdir(target)

	for filename, collector in collectors:
		if only_collectors is None or filename in only_collectors:
			if print_only:
				_print_test(target, filename, collector)
			else:
				_store_test(target, filename, collector)

	if not print_only:
		print('Completed run, please check the data files and censor any sensitive information.')


def _store_test(target, filename, collector):
	try:
		c = collector()
		c.setUp()

		with open(os.path.join(target, filename + '.txt'), 'w') as f:
			# Write raw output from this environment, (useful because different versions will have different formatting)
			f.write(c.generate_raw_data())

		with open(os.path.join(target, filename + '.yaml'), 'w') as f:
			# Use the library to generate test data based on this environment, (can be corrected manually)
			f.write(yaml.dump(c.generate_test_data(), default_flow_style=False))

		# print(json.dumps({'raw': c.raw, 'results': c.generate_test_data()}, indent=2))
		print('  {} - {}'.format(filename, 'generated'))
	except MetricNotAvailable:
		print('  {} - {}'.format(filename, 'failed (Metric not available)'))


def _print_test(target, filename, collector):
	try:
		c = collector()
		c.setUp()

		print('=============== RAW DATA  ===============')
		print(c.generate_raw_data())

		print('=============== TEST DATA ===============')
		print(yaml.dump(c.generate_test_data(), default_flow_style=False))
	except MetricNotAvailable:
		print('  {} - {}'.format(filename, 'failed (Metric not available)'))
