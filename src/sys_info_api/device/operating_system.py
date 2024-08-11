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
import datetime
import logging
from typing import List, Union

from sys_info_api.collectors.bin.apt import AptUpdates
from sys_info_api.collectors.bin.dpkg import DpkgListInstalled
from sys_info_api.collectors.bin.pkg import PkgListInstalled
from sys_info_api.collectors.bin.pveversion import PveVersion
from sys_info_api.collectors.bin.uname import UnameMachine
from sys_info_api.collectors.bin.uptime import Uptime
from sys_info_api.collectors.bin.sysctl import SysctlKernBoottime
from sys_info_api.collectors.bin.who import WhoBootTime
from sys_info_api.collectors.bin.yum import YumListInstalled, YumUpdates
from sys_info_api.collectors.etc.lsb_release import LsbRelease
from sys_info_api.collectors.etc.version import Version
from sys_info_api.collectors.etc.os_release import OsRelease
from sys_info_api.common.cmd import check_binary_exists
from sys_info_api.common.exceptions import MetricNotAvailable


def get_name() -> str:
	"""
	Try to get the name of the device OS based on hints in /etc
	"""

	# Check for appliance name first; we'll prefer this over the base OS
	try:
		return Version().get_name()
	except MetricNotAvailable:
		pass

	try:
		PveVersion().get_version()
		return 'Proxmox VE'
	except MetricNotAvailable:
		pass

	try:
		return OsRelease().get_name()
	except MetricNotAvailable:
		pass

	# MacOS
	# try:
	# 	return system_profiler.SystemProfiler.software().system_name()
	# except MetricNotAvailable:
	# 	pass

	return 'Unknown'


def get_upstream_id() -> str:
	"""
	Try to get the name of the upstream OS based on hints in /etc

	This may be different from the actual OS running, ie:
	Proxmox VE is considered the operating system name, (as it is a full appliance),
	but its upstream OS for installing packages is Debian.
	"""

	# Check if there is an upstream lsb-release
	try:
		return LsbRelease(upstream=True).get_id()
	except MetricNotAvailable:
		pass

	try:
		return OsRelease().get_id()
	except MetricNotAvailable:
		pass

	# MacOS
	# try:
	# 	return system_profiler.SystemProfiler.software().system_name()
	# except MetricNotAvailable:
	# 	pass

	return 'unknown'


def get_version() -> str:
	"""
	Try to get the name of the device OS based on hints in /etc
	"""

	# Check for appliance version first; we'll prefer this over the base OS
	try:
		return Version().get_version()
	except MetricNotAvailable:
		pass

	try:
		return PveVersion().get_version()
	except MetricNotAvailable:
		pass

	try:
		return OsRelease().get_version_string()
	except MetricNotAvailable:
		pass

	return ''


def get_upstream_version() -> str:
	"""
	Try to get the version of the upstream OS based on hints in /etc

	This may be different from the actual OS running, ie:
	Proxmox VE is considered the operating system name, (as it is a full appliance),
	but its upstream OS for installing packages is Debian.
	"""

	# Check if there is an upstream lsb-release
	try:
		return LsbRelease(upstream=True).get_version_string()
	except MetricNotAvailable:
		pass

	try:
		return OsRelease().get_version_string()
	except MetricNotAvailable:
		pass

	return ''


def get_upstream_version_major() -> str:
	"""
	Try to get the version of the upstream OS based on hints in /etc

	This may be different from the actual OS running, ie:
	Proxmox VE is considered the operating system name, (as it is a full appliance),
	but its upstream OS for installing packages is Debian.
	"""

	# Check if there is an upstream lsb-release
	try:
		return LsbRelease(upstream=True).get_version()['major']
	except MetricNotAvailable:
		pass

	try:
		return OsRelease().get_version()['major']
	except MetricNotAvailable:
		pass

	return ''


def get_arch() -> str:
	"""
	Get the architecture of this OS
	"""

	return UnameMachine().get_data()


def get_boottime() -> Union[datetime.datetime, None]:
	# Boot Time Detection

	try:
		return Uptime().get_data()
	except MetricNotAvailable:
		pass

	try:
		# Let's try BSD's approach.
		return SysctlKernBoottime().get_data()
	except MetricNotAvailable:
		pass

	try:
		# uptime -s failed, try who -b instead.
		return WhoBootTime().get_data()
	except MetricNotAvailable:
		pass

	# :/ well shit.
	logging.warning('System boottime detection failed')
	return None


def get_installed_software():
	"""
	Call the underlying OS's package manager to handle detection of installed software
	"""

	# @todo support MacOS
	if check_binary_exists('apt-get'):
		return DpkgListInstalled().get_data()
	elif check_binary_exists('yum'):
		return YumListInstalled().get_data()
	elif check_binary_exists('pkg'):
		return PkgListInstalled().get_data()
	else:
		return []


def get_updates() -> List[dict]:
	"""
	Get any updates that are available
	"""

	# @todo support MacOS
	# @todo support FreeBSD
	if check_binary_exists('apt-get'):
		return AptUpdates().get_data()
	elif check_binary_exists('yum'):
		return YumUpdates().get_data()
	else:
		return []


def like_os(family: str) -> bool:
	"""
	Check if this operating system is "like" another

	Useful to see if this OS is "like Debian" or "like Red Hat"

	:param family:
	:return:
	"""

	try:
		return OsRelease().like_os(family)
	except MetricNotAvailable:
		pass

	# *shrugs*
	return False


class OsDump:
	"""
	Dump all info available about the operating system (from the os module)
	"""

	def setUp(self):
		pass  # No setup needed

	def generate_raw_data(self) -> str:
		return '(dynamic)'  # Dynamic sources, no raw data

	def generate_test_data(self) -> dict:
		return {
			'name': get_name(),
			'upstream_id': get_upstream_id(),
			'version': get_version(),
			'upstream_version': get_upstream_version(),
			'upstream_version_major': get_upstream_version_major(),
			'arch': get_arch(),
			'boottime': get_boottime(),
			'installed_software': get_installed_software(),
			'updates': get_updates()
		}
