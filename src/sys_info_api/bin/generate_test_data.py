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

from sys_info_api.collectors.bin.apt import AptUpdatesTest, AptShowTest
from sys_info_api.collectors.bin.arp import ArpTest
from sys_info_api.collectors.bin.df import DfTest
from sys_info_api.collectors.bin.dmidecode import DmiBaseboardTest, DmiMemoryTest, DmiBiosTest, DmiCacheTest, \
	DmiChassisTest, DmiProcessorTest, DmiSystemTest
from sys_info_api.collectors.bin.dpkg import DpkgListInstalledTest
from sys_info_api.collectors.bin.hostnamectl import HostnameCtlTest
from sys_info_api.collectors.bin.ifconfig import Ifconfig, IfconfigTest
from sys_info_api.collectors.bin.ip import IPLink, IPLinkTest
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
from sys_info_api.collectors.etc.os_release import OsRelease, OsReleaseTest
from sys_info_api.collectors.etc.version import VersionTest
from sys_info_api.common.exceptions import MetricNotAvailable


def run(mock_run: str = None):
	if mock_run is not None:
		only_collectors = mock_run
		print_only = True
	elif len(sys.argv) > 1:
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
	interfaces = _get_net_interfaces()
	packages = [['python3'], ['vlc'], ['xterm']]

	# Collection of scripts to run and try to store
	collectors = [
		['bin.aptshow', AptShowTest, packages],
		['bin.aptupdates', AptUpdatesTest],
		['bin.arp', ArpTest],
		['bin.df', DfTest],
		['bin.dmibaseboard', DmiBaseboardTest],
		['bin.dmibios', DmiBiosTest],
		['bin.dmicache', DmiCacheTest],
		['bin.dmichassis', DmiChassisTest],
		['bin.dmimemory', DmiMemoryTest],
		['bin.dmiprocessor', DmiProcessorTest],
		['bin.dmisystem', DmiSystemTest],
		['bin.dpkglistinstalled', DpkgListInstalledTest],
		['bin.hostnamectl', HostnameCtlTest],
		['bin.ifconfig', IfconfigTest],
		['bin.iplink', IPLinkTest],
		['bin.iwconfig', IwconfigTest],
		['bin.lldpstatus', LldpStatusTest, interfaces],
		['bin.lldpneighborscan', LldpNeighborScanTest, interfaces],
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

	if not print_only and not os.path.exists(target):
		print('Creating test data in: {}'.format(target))
		os.mkdir(target)

	for fields in collectors:
		filename = fields[0]
		collector = fields[1]
		params = fields[2] if len(fields) >= 3 else []

		if only_collectors is None or filename in only_collectors:
			if len(params):
				# Additional parameters requested
				for p in params:
					if print_only:
						_print_test(target, filename, collector, p)
					else:
						_store_test(target, filename, collector, p)
			else:
				if print_only:
					_print_test(target, filename, collector, [])
				else:
					_store_test(target, filename, collector, [])

	if not print_only:
		print('Completed run, please check the data files and censor any sensitive information.')


def _store_test(target, filename, collector, params):
	try:
		c = collector()
		if len(params):
			c.setUp(*params)
			filename = filename + '-' + '-'.join(params)
		else:
			c.setUp()

		command_output = c.generate_raw_data()
		test_data = c.generate_test_data()

		with open(os.path.join(target, filename + '.txt'), 'w') as f:
			# Write raw output from this environment, (useful because different versions will have different formatting)
			f.write(command_output)

		with open(os.path.join(target, filename + '.yaml'), 'w') as f:
			# Use the library to generate test data based on this environment, (can be corrected manually)
			f.write(yaml.dump(test_data, default_flow_style=False))

		# print(json.dumps({'raw': c.raw, 'results': c.generate_test_data()}, indent=2))
		print('  {} - {}'.format(filename, 'generated'))
	except MetricNotAvailable:
		print('  {} - {}'.format(filename, 'failed (Metric not available)'))


def _print_test(target, filename, collector, params):
	try:
		c = collector()
		if len(params):
			c.setUp(*params)
			filename = filename + '-' + '-'.join(params)
		else:
			c.setUp()

		print('=============== RAW DATA  ===============')
		print(c.generate_raw_data())

		print('=============== TEST DATA ===============')
		print(yaml.dump(c.generate_test_data(), default_flow_style=False))
	except MetricNotAvailable:
		print('  {} - {}'.format(filename, 'failed (Metric not available)'))


def _get_net_interfaces():
	names = []
	ret = []
	try:
		names = Ifconfig().get_names()
	except MetricNotAvailable:
		pass

	try:
		names = IPLink().get_names()
	except MetricNotAvailable:
		pass

	for name in names:
		ret.append([name])

	return ret


# Debug / Test
# run('bin.dpkglistinstalled')
