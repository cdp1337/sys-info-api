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
import time
import sys
# from .exceptions import MetricNotAvailable
# from .key_value_parser import KeyValueParser
# from .bin_collector import BinCollector
# from .bin_collector_test import BinCollectorTest
# from .local_timezone import LocalTimezone


def print_error(string):
	"""
	Simple method to write out an error message to STDERR.

	This will be available to the retrieving server but will not interfere with the standard output!
	"""
	sys.stderr.write('ERR: ' + string + "\n")


def print_warning(string):
	"""
	Simple method to write out a warning message to STDERR.

	This will be available to the retrieving server but will not interfere with the standard output!
	"""
	sys.stderr.write('WARN: ' + string + "\n")


def str_to_utc(date_value: str, format: str) -> datetime.datetime:
	"""
	Similar to datetime.strptime, but will auto convert to UTC.

	| Directive | Example                                               | Note                  |
	|-----------|-------------------------------------------------------|-----------------------|
	| %a        | Sun, Mon, …, Sat                                      | Day of week           |
	| %A        | Sunday, Monday, …, Saturday                           | Day of week           |
	| %w        | 0, 1, …, 6                                            | Day of week           |
	| %d        | 01, 02, …, 31                                         | Day of month          |
	| %b        | Jan, Feb, …, Dec                                      | Month                 |
	| %B        | January, February, …, December                        | Month                 |
	| %m        | 01, 02, …, 12                                         | Month                 |
	| %y        | 00, 01, …, 99                                         | Year                  |
	| %Y        | 0001, 0002, …, 2013, 2014, …, 9998, 9999              | Year                  |
	| %H        | 00, 01, …, 23                                         | Hour                  |
	| %I        | 01, 02, …, 12                                         | Hour (12-hour)        |
	| %p        | AM, PM                                                | AM/PM                 |
	| %M        | 00, 01, …, 59                                         | Minute                |
	| %S        | 00, 01, …, 59                                         | Seconds               |
	| %f        | 000000, 000001, …, 999999                             | Microseconds          |
	| %z        | (empty), +0000, -0400, +1030, +063415, -030712.345216 | Timezone Offset       |
	| %Z        | (empty), UTC, GMT                                     | Timezone Name         |
	| %j        | 001, 002, …, 366                                      | Day of year           |
	| %U        | 00, 01, …, 53                                         | Week of year (Sunday) |
	| %W        | 00, 01, …, 53                                         | Week of year (Monday) |
	| %c        | Tue Aug 16 21:30:00 1988                              | Locale date/time      |
	| %x        | 08/16/88                                              | Locale date           |
	| %X        | 21:30:00                                              | Locale time           |

	:param date_value:
	:param format:
	:return:
	"""
	date = datetime.datetime.strptime(date_value, format)
	if date.tzname() is None:
		# No timezone data from the format, assume local timezone
		date = date.replace(tzinfo=datetime.timezone.utc) + datetime.timedelta(seconds=-time.localtime().tm_gmtoff)
	elif date.tzname() != 'UTC':
		# Timezone present in the string, but just not UTC.
		date = date.astimezone(datetime.timezone.utc)

	return date


def date_to_epoch(date: datetime.datetime) -> int:
	"""
	Retrieve the time in UTC epoch of a given date.

	This will return an int representing the number of seconds since Jan 1, 1970 UTC.
	"""
	if date.tzname() is None:
		# No timezone data from the format, assume local timezone
		date = date.replace(tzinfo=datetime.timezone.utc) + datetime.timedelta(seconds=-time.localtime().tm_gmtoff)

	epoch = datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)
	return int((date - epoch).total_seconds())


def formatted_string_to_bytes(value: str) -> int:
	"""
	Convert a string of bytes to the actual number of bytes included.

	Supports suffixes for "k/K/M/G/T/P/E/Z/Y/R/Q"

	Assume that byte values are Gibi/Tebi/etc and not actually Giga/Tera/etc.
	Technically "1 PB" is different than "1 PiB", but most output of PB lazily just means PiB.
	These values are calculated in Base2.

	Assume that speed values are actually Giga/Tera/etc, and thus calculated in Base10.
	"""

	translations = [
		[1024, [' kB', ' KB', 'k', 'K', ' KiB']],  # kibibyte
		[1048576, [' MB', 'M', ' MiB']],  # mebibyte
		[1073741824, [' GB', 'G', ' GiB']],  # gibibyte
		[1099511627776, [' TB', 'T', ' TiB']],  # tebibyte
		[1125899906842624, [' PB', 'P', ' PiB']],  # pebibyte
		[1152921504606846976, [' EB', 'E', ' EiB']],  # exbibyte
		[1180591620717411303424, [' ZB', 'Z', ' ZiB']],  # zebibyte
		[1208925819614629174706176, [' YB', 'Y', ' YiB']],  # yobibyte
		[1237940039285380274899124224, [' RB', 'R', 'RiB']],  # robibyte
		[1267650600228229401496703205376, [' QB', 'Q', 'QiB']],  # quebibyte
		[1e3, [' kB/s', ' KB/s']],  # kilobyte
		[1e6, [' MB/s']],  # megabyte
		[1e9, [' GB/s']],  # gigabyte
		[1e12, [' TB/s']],  # terabyte
		[1e15, [' PB/s']],  # petabyte
		[1e18, [' EB/s']],  # exabyte
		[1e21, [' ZB/s']],  # zettabyte
		[1e24, [' YB/s']],  # yottabyte
		[1e27, [' RB/s']],  # ronnabyte
		[1e30, [' QB/s']],  # quettabyte
		[.125, [' b/s']],  # kilobit -> byte
		[125, [' kb/s', ' Kb/s']],  # kilobit -> byte
		[1.25e5, [' Mb/s']],  # megabit -> byte
		[1.25e8, [' Gb/s']],  # gigabit -> byte
		[1.25e11, [' Tb/s']],  # terabit -> byte
		[1.25e14, [' Pb/s']],  # petabit -> byte
		[1.25e17, [' Eb/s']],  # exabit -> byte
		[1.25e20, [' Zb/s']],  # zettabit -> byte
		[1.25e23, [' Yb/s']],  # yottabit -> byte
		[1.25e28, [' Rb/s']],  # ronnabit -> byte
		[1.25e29, [' Qb/s']]  # quettabit -> byte
	]

	for t in translations:
		for suffix in t[1]:
			if value.endswith(suffix):
				return int(float(value[0: (0 - len(suffix))]) * t[0])

	return int(value)


def formatted_string_to_bits(value: str) -> int:
	"""
	Convert a string of bits to the actual number of bits included.

	Supports suffixes for "k/K/M/G/T/P/E/Z/Y/R/Q"

	Assume that bit values are Gibi/Tebi/etc and not actually Giga/Tera/etc.
	Technically "1 Pb" is different than "1 Pib", but most output of Pb lazily just means Pib.
	These values are calculated in Base2.

	Assume that speed values are actually Giga/Tera/etc, and thus calculated in Base10.
	"""

	translations = [
		[1024, [' kb', ' Kb', ' Kib']],  # kibibit
		[1048576, [' Mb', ' Mib']],  # mebibit
		[1073741824, [' Gb', ' Gib']],  # gibibit
		[1099511627776, [' Tb', ' Tib']],  # tebibit
		[1125899906842624, [' Pb', ' Pib']],  # pebibit
		[1152921504606846976, [' Eb', ' Eib']],  # exbibit
		[1180591620717411303424, [' Zb', ' Zib']],  # zebibit
		[1208925819614629174706176, [' Yb', ' Yib']],  # yobibit
		[1237940039285380274899124224, [' Rb', 'Rib']],  # robibit
		[1267650600228229401496703205376, [' Qb', 'Qib']],  # quebibit
		[8, [' B']],  # kibibyte
		[8192, [' kB', ' KB', 'k', 'K', ' KiB']],  # kibibyte -> bit
		[8388608, [' MB', 'M', ' MiB']],  # mebibyte -> bit
		[8589934592, [' GB', 'G', ' GiB']],  # gibibyte -> bit
		[8796093022208, [' TB', 'T', ' TiB']],  # tebibyte -> bit
		[9007199254740992, [' PB', 'P', ' PiB']],  # pebibyte -> bit
		[9223372036854775808, [' EB', 'E', ' EiB']],  # exbibyte -> bit
		[9444732965739290427392, [' ZB', 'Z', ' ZiB']],  # zebibyte -> bit
		[9671406556917033397649408, [' YB', 'Y', ' YiB']],  # yobibyte -> bit
		[9903520314283042199192993792, [' RB', 'R', 'RiB']],  # robibyte -> bit
		[10141204801825835211973625643008, [' QB', 'Q', 'QiB']],  # quebibyte -> bit
		[1e3, [' kb/s', ' Kb/s']],  # kilobit
		[1e6, [' Mb/s']],  # megabit
		[1e9, [' Gb/s']],  # gigabit
		[1e12, [' Tb/s']],  # terabit
		[1e15, [' Pb/s']],  # petabit
		[1e18, [' Eb/s']],  # exabit
		[1e21, [' Zb/s']],  # zettabit
		[1e24, [' Yb/s']],  # yottabit
		[1e27, [' Rb/s']],  # ronnabit
		[1e30, [' Qb/s']],  # quettabit
		[8, [' b/s']],  # byte -> bit
		[8e3, [' kB/s', ' KB/s']],  # kilobyte -> bit
		[8e6, [' MB/s']],  # megabyte -> bit
		[8e9, [' GB/s']],  # gigabyte -> bit
		[8e12, [' TB/s']],  # terabyte -> bit
		[8e15, [' PB/s']],  # petabyte -> bit
		[8e18, [' EB/s']],  # exabyte -> bit
		[8e21, [' ZB/s']],  # zettabyte -> bit
		[8e24, [' YB/s']],  # yottabyte -> bit
		[8e27, [' RB/s']],  # ronnabyte -> bit
		[8e30, [' QB/s']],  # quettabyte -> bit
	]

	for t in translations:
		for suffix in t[1]:
			if value.endswith(suffix):
				return int(float(value[0: (0 - len(suffix))]) * t[0])

	return int(value)


def bytes_to_formatted_string(value: int, decimals: int = 2) -> str:
	"""
	Convert bytes to a formatted string
	"""

	if value >= 1125899906842624:
		value = value / 1125899906842624
		suffix = ' PiB'
	elif value >= 1099511627776:
		value = value / 1099511627776
		suffix = ' TiB'
	elif value >= 1073741824:
		value = value / 1073741824
		suffix = ' GiB'
	elif value >= 1048576:
		value = value / 1048576
		suffix = ' MiB'
	elif value >= 1024:
		value = value / 1024
		suffix = ' kiB'
	else:
		suffix = ' B'

	return str(round(value * pow(10, decimals)) / pow(10, decimals)) + suffix


def bps_to_formatted_string(value: int) -> str:
	if value < 1000:
		return str(value) + ' b/s'
	elif value < 1000000:
		return str(round(value / 1000, 0)) + ' kb/s'
	elif value < 1000000000:
		return str(round(value / 1000000, 0)) + ' Mb/s'
	else:
		return str(round(value / 1000000000, 0)) + ' Gb/s'
