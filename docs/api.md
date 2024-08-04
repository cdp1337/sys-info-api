<!-- markdownlint-disable -->

# API Overview

## Modules

- [`sys_info_api`](./sys_info_api.md#module-sys_info_api)
- [`sys_info_api.collectors`](./sys_info_api.collectors.md#module-sys_info_apicollectors)
- [`sys_info_api.collectors.bin`](./sys_info_api.collectors.bin.md#module-sys_info_apicollectorsbin)
- [`sys_info_api.collectors.bin.arp`](./sys_info_api.collectors.bin.arp.md#module-sys_info_apicollectorsbinarp)
- [`sys_info_api.collectors.bin.df`](./sys_info_api.collectors.bin.df.md#module-sys_info_apicollectorsbindf)
- [`sys_info_api.collectors.bin.dmidecode`](./sys_info_api.collectors.bin.dmidecode.md#module-sys_info_apicollectorsbindmidecode)
- [`sys_info_api.collectors.bin.hostnamectl`](./sys_info_api.collectors.bin.hostnamectl.md#module-sys_info_apicollectorsbinhostnamectl)
- [`sys_info_api.collectors.bin.ifconfig`](./sys_info_api.collectors.bin.ifconfig.md#module-sys_info_apicollectorsbinifconfig)
- [`sys_info_api.collectors.bin.ip`](./sys_info_api.collectors.bin.ip.md#module-sys_info_apicollectorsbinip)
- [`sys_info_api.collectors.bin.iwconfig`](./sys_info_api.collectors.bin.iwconfig.md#module-sys_info_apicollectorsbiniwconfig)
- [`sys_info_api.collectors.bin.lldptool`](./sys_info_api.collectors.bin.lldptool.md#module-sys_info_apicollectorsbinlldptool)
- [`sys_info_api.collectors.etc`](./sys_info_api.collectors.etc.md#module-sys_info_apicollectorsetc)
- [`sys_info_api.collectors.etc.os_release`](./sys_info_api.collectors.etc.os_release.md#module-sys_info_apicollectorsetcos_release)
- [`sys_info_api.common`](./sys_info_api.common.md#module-sys_info_apicommon)
- [`sys_info_api.common.bin_collector`](./sys_info_api.common.bin_collector.md#module-sys_info_apicommonbin_collector)
- [`sys_info_api.common.bin_collector_test`](./sys_info_api.common.bin_collector_test.md#module-sys_info_apicommonbin_collector_test)
- [`sys_info_api.common.cmd`](./sys_info_api.common.cmd.md#module-sys_info_apicommoncmd)
- [`sys_info_api.common.enums`](./sys_info_api.common.enums.md#module-sys_info_apicommonenums)
- [`sys_info_api.common.exceptions`](./sys_info_api.common.exceptions.md#module-sys_info_apicommonexceptions)
- [`sys_info_api.common.key_value_parser`](./sys_info_api.common.key_value_parser.md#module-sys_info_apicommonkey_value_parser)
- [`sys_info_api.common.local_timezone`](./sys_info_api.common.local_timezone.md#module-sys_info_apicommonlocal_timezone)

## Classes

- [`arp.Arp`](./sys_info_api.collectors.bin.arp.md#class-arp): Execute `arp` to get the list of neighbors on the network.
- [`arp.ArpTest`](./sys_info_api.collectors.bin.arp.md#class-arptest)
- [`df.Df`](./sys_info_api.collectors.bin.df.md#class-df): Execute `df` to get the list of filesystems.
- [`df.DfTest`](./sys_info_api.collectors.bin.df.md#class-dftest)
- [`dmidecode.DmiBaseboard`](./sys_info_api.collectors.bin.dmidecode.md#class-dmibaseboard)
- [`dmidecode.DmiBaseboardTest`](./sys_info_api.collectors.bin.dmidecode.md#class-dmibaseboardtest)
- [`dmidecode.DmiBios`](./sys_info_api.collectors.bin.dmidecode.md#class-dmibios)
- [`dmidecode.DmiBiosTest`](./sys_info_api.collectors.bin.dmidecode.md#class-dmibiostest)
- [`dmidecode.DmiCache`](./sys_info_api.collectors.bin.dmidecode.md#class-dmicache)
- [`dmidecode.DmiCacheTest`](./sys_info_api.collectors.bin.dmidecode.md#class-dmicachetest)
- [`dmidecode.DmiChassis`](./sys_info_api.collectors.bin.dmidecode.md#class-dmichassis)
- [`dmidecode.DmiChassisTest`](./sys_info_api.collectors.bin.dmidecode.md#class-dmichassistest)
- [`dmidecode.DmiMemory`](./sys_info_api.collectors.bin.dmidecode.md#class-dmimemory)
- [`dmidecode.DmiMemoryTest`](./sys_info_api.collectors.bin.dmidecode.md#class-dmimemorytest)
- [`dmidecode.DmiProcessor`](./sys_info_api.collectors.bin.dmidecode.md#class-dmiprocessor)
- [`dmidecode.DmiProcessorTest`](./sys_info_api.collectors.bin.dmidecode.md#class-dmiprocessortest)
- [`dmidecode.DmiSection`](./sys_info_api.collectors.bin.dmidecode.md#class-dmisection)
- [`dmidecode.DmiSystem`](./sys_info_api.collectors.bin.dmidecode.md#class-dmisystem)
- [`dmidecode.DmiSystemTest`](./sys_info_api.collectors.bin.dmidecode.md#class-dmisystemtest)
- [`hostnamectl.HostnameCtl`](./sys_info_api.collectors.bin.hostnamectl.md#class-hostnamectl)
- [`hostnamectl.HostnameCtlTest`](./sys_info_api.collectors.bin.hostnamectl.md#class-hostnamectltest)
- [`ifconfig.Ifconfig`](./sys_info_api.collectors.bin.ifconfig.md#class-ifconfig): Collects information about network interfaces from the ifconfig command.
- [`ifconfig.IfconfigTest`](./sys_info_api.collectors.bin.ifconfig.md#class-ifconfigtest)
- [`ip.IPLink`](./sys_info_api.collectors.bin.ip.md#class-iplink): Gathers interface names from ip
- [`ip.IPLinkTest`](./sys_info_api.collectors.bin.ip.md#class-iplinktest)
- [`iwconfig.Iwconfig`](./sys_info_api.collectors.bin.iwconfig.md#class-iwconfig)
- [`iwconfig.IwconfigTest`](./sys_info_api.collectors.bin.iwconfig.md#class-iwconfigtest)
- [`lldptool.LldpNeighborScan`](./sys_info_api.collectors.bin.lldptool.md#class-lldpneighborscan)
- [`lldptool.LldpNeighborScanTest`](./sys_info_api.collectors.bin.lldptool.md#class-lldpneighborscantest)
- [`lldptool.LldpStatus`](./sys_info_api.collectors.bin.lldptool.md#class-lldpstatus)
- [`lldptool.LldpStatusTest`](./sys_info_api.collectors.bin.lldptool.md#class-lldpstatustest)
- [`os_release.OsRelease`](./sys_info_api.collectors.etc.os_release.md#class-osrelease): Provides a simple API to read /etc/os-release data
- [`os_release.OsReleaseTest`](./sys_info_api.collectors.etc.os_release.md#class-osreleasetest)
- [`bin_collector.BinCollector`](./sys_info_api.common.bin_collector.md#class-bincollector): Base class for collectors that run a binary command and parse the output.
- [`bin_collector_test.BinCollectorTest`](./sys_info_api.common.bin_collector_test.md#class-bincollectortest): Base class for collector tests for binary commands.
- [`cmd.CmdExecException`](./sys_info_api.common.cmd.md#class-cmdexecexception): Base command execution exception
- [`cmd.CmdExecExitCodeException`](./sys_info_api.common.cmd.md#class-cmdexecexitcodeexception): Thrown if the command exit code wasn't good
- [`cmd.CmdExecNotFoundException`](./sys_info_api.common.cmd.md#class-cmdexecnotfoundexception): Thrown if the command could not be located
- [`enums.NetDuplex`](./sys_info_api.common.enums.md#class-netduplex): An enumeration.
- [`enums.NetStatus`](./sys_info_api.common.enums.md#class-netstatus): An enumeration.
- [`exceptions.MetricNotAvailable`](./sys_info_api.common.exceptions.md#class-metricnotavailable): General exception thrown when a metric is not available
- [`key_value_parser.KeyValueParser`](./sys_info_api.common.key_value_parser.md#class-keyvalueparser): A simple key/value parser for parsing key/value pairs from a string.
- [`local_timezone.LocalTimezone`](./sys_info_api.common.local_timezone.md#class-localtimezone)

## Functions

- [`common.bps_to_formatted_string`](./sys_info_api.common.md#function-bps_to_formatted_string)
- [`common.bytes_to_formatted_string`](./sys_info_api.common.md#function-bytes_to_formatted_string): Convert bytes to a formatted string
- [`common.date_to_epoch`](./sys_info_api.common.md#function-date_to_epoch): Retrieve the time in UTC epoch of a given date.
- [`common.formatted_string_to_bits`](./sys_info_api.common.md#function-formatted_string_to_bits): Convert a string of bits to the actual number of bits included.
- [`common.formatted_string_to_bytes`](./sys_info_api.common.md#function-formatted_string_to_bytes): Convert a string of bytes to the actual number of bytes included.
- [`common.print_error`](./sys_info_api.common.md#function-print_error): Simple method to write out an error message to STDERR.
- [`common.print_warning`](./sys_info_api.common.md#function-print_warning): Simple method to write out a warning message to STDERR.
- [`common.str_to_utc`](./sys_info_api.common.md#function-str_to_utc): Similar to datetime.strptime, but will auto convert to UTC.
- [`cmd.check_binary_exists`](./sys_info_api.common.cmd.md#function-check_binary_exists): Check if a binary exists in the path
- [`cmd.run_binary`](./sys_info_api.common.cmd.md#function-run_binary): Run a command and pass stderr to the log, while capturing stdout as its raw binary output
- [`cmd.run_output`](./sys_info_api.common.cmd.md#function-run_output): Run a command and pass stderr to the log, while capturing stdout
- [`cmd.run_passthru`](./sys_info_api.common.cmd.md#function-run_passthru): Run a command and pass stdout and stderr directly to appropriate streams
- [`cmd.run_returncode`](./sys_info_api.common.cmd.md#function-run_returncode): Run a command and pass stderr to the log, ignoring output, and return the returncode


---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
