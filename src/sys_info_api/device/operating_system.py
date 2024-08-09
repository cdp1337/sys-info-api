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
from sys_info_api.collectors.bin.dpkg import DpkgListInstalled as BinDpkgListInstalled
from sys_info_api.collectors.bin.pkg import PkgListInstalled as BinPkgListInstalled
from sys_info_api.collectors.bin.pveversion import PveVersion as BinPveVersion
from sys_info_api.collectors.bin.uname import UnameMachine as BinUnameMachine
from sys_info_api.collectors.bin.uptime import Uptime as BinUptime
from sys_info_api.collectors.bin.sysctl import SysctlKernBoottime as BinSysctlKernBoottime
from sys_info_api.collectors.bin.who import WhoBootTime as BinWhoBootTime
from sys_info_api.collectors.bin.yum import YumListInstalled as BinYumListInstalled, YumUpdates
from sys_info_api.collectors.etc.version import Version as EtcVersion
from sys_info_api.collectors.etc.os_release import OsRelease as EtcOsRelease
from sys_info_api.common.cmd import check_binary_exists
from sys_info_api.common.exceptions import MetricNotAvailable


def get_name() -> str:
	"""
	Try to get the name of the device OS based on hints in /etc
	"""

	# Check for appliance name first; we'll prefer this over the base OS
	try:
		return EtcVersion().get_name()
	except MetricNotAvailable:
		pass

	try:
		BinPveVersion().get_version()
		return 'Proxmox VE'
	except MetricNotAvailable:
		pass

	try:
		return EtcOsRelease().get_name()
	except MetricNotAvailable:
		pass

	# MacOS
	# try:
	# 	return system_profiler.SystemProfiler.software().system_name()
	# except MetricNotAvailable:
	# 	pass

	return 'Unknown'


def get_version() -> str:
	"""
	Try to get the name of the device OS based on hints in /etc
	"""

	# Check for appliance version first; we'll prefer this over the base OS
	try:
		return EtcVersion().get_version()
	except MetricNotAvailable:
		pass

	try:
		return BinPveVersion().get_version()
	except MetricNotAvailable:
		pass

	try:
		return EtcOsRelease().get_version_string()
	except MetricNotAvailable:
		pass

	# MacOS
	# try:
	# 	return system_profiler.SystemProfiler.software().system_version()
	# except MetricNotAvailable:
	# 	pass

	return ''


def get_arch() -> str:
	"""
	Get the architecture of this OS
	"""

	return BinUnameMachine().get_data()


def get_boottime() -> Union[datetime.datetime, None]:
	# Boot Time Detection

	try:
		return BinUptime().get_data()
	except MetricNotAvailable:
		pass

	try:
		# Let's try BSD's approach.
		return BinSysctlKernBoottime().get_data()
	except MetricNotAvailable:
		pass

	try:
		# uptime -s failed, try who -b instead.
		return BinWhoBootTime().get_data()
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
		return BinDpkgListInstalled().get_data()
	elif check_binary_exists('yum'):
		return BinYumListInstalled().get_data()
	elif check_binary_exists('pkg'):
		return BinPkgListInstalled().get_data()
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
		return EtcOsRelease().like_os(family)
	except MetricNotAvailable:
		pass

	# *shrugs*
	return False
