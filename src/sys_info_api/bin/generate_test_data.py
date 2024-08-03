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
from datetime import datetime

# from system_information.tests.collectors.bin.test_arpneighborscan import TestARPNeighborScan
# from system_information.tests.collectors.bin.test_dflist import TestDfList
# from system_information.tests.collectors.bin.test_dmimemory import TestDMIMemory
# from system_information.tests.collectors.bin.test_ifconfig import TestIfconfig
# from system_information.tests.collectors.bin.test_lldpneighborscan import TestLldpNeighborScan
# from system_information.tests.collectors.bin.test_lldpstatus import TestLldpStatus
# from system_information.tests.collectors.bin.test_mii_tool import TestMiiTool
# from system_information.tests.collectors.etc.test_os_release import TestOSRelease
# from system_information.tests.collectors.bin.test_iplinklist import TestIPLinkList
from sys_info_api.common import MetricNotAvailable
# from system_information.device.net import get_all_interface_names

from sys_info_api.collectors.bin.arp import ArpTest


def run():
	if len(sys.argv) > 1:
		only_collectors = sys.argv[1:]
		print_only = True
	else:
		only_collectors = None
		print_only = False

	# Set the target to store collected results within tests/data
	target = os.path.abspath(os.path.join(
		os.path.dirname(__file__),
		'../../../tests/data',
		'-'.join([platform.system(), platform.release(), '{:%Y%m%d%H%M%S}'.format(datetime.now())])
	))

	# List of interfaces for interface-specific tests
	# interfaces = get_all_interface_names()

	# Collection of scripts to run and try to store
	collectors = [
		# ['bin.iplinklist', TestIPLinkList, None],
		# ['bin.dflist', TestDfList, None],
		# ['bin.dmimemory', TestDMIMemory, None],
		# ['etc.os_release', TestOSRelease, None],
		# ['bin.ifconfig', TestIfconfig, None],
		# ['bin.lldpstatus', TestLldpStatus, interfaces],
		# ['bin.lldpneighborscan', TestLldpNeighborScan, interfaces],
		# ['bin.mii_tool', TestMiiTool, interfaces],
		['bin.arp', ArpTest, None],
	]

	if not print_only:
		print('Creating test data in: {}'.format(target))
		os.mkdir(target)

	for filename, collector, arguments in collectors:
		if only_collectors is None or filename in only_collectors:
			if arguments is None:
				if print_only:
					_print_test(target, filename, collector, [])
				else:
					_store_test(target, filename, collector, [])
			else:
				for argument_set in arguments:
					if argument_set is not list:
						argument_set = [argument_set]
					if print_only:
						_print_test(target, filename, collector, argument_set)
					else:
						_store_test(target, filename, collector, argument_set)

	if not print_only:
		print('Completed run, please check the data files and censor any sensitive information.')


def _store_test(target, filename, collector, arguments):
	try:
		if len(arguments) > 0:
			filename = filename + '-' + '-'.join(arguments)
			c = collector(*arguments)
		else:
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


def _print_test(target, filename, collector, arguments):
	try:
		if len(arguments) > 0:
			filename = filename + '-' + '-'.join(arguments)
			c = collector(*arguments)
		else:
			c = collector()

		print('=============== RAW DATA  ===============')
		print(c.generate_raw_data())

		print('=============== TEST DATA ===============')
		print(yaml.dump(c.generate_test_data(), default_flow_style=False))
	except MetricNotAvailable:
		print('  {} - {}'.format(filename, 'failed (Metric not available)'))
