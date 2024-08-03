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

from unittest import TestCase
from sys_info_api import common
import time
import datetime


class TestStrToUTC(TestCase):
	def test_simple(self):
		"""
		Dynamically create a UTC time of 'now' and use the built-in timezone handling to convert it
		to a simple string to ensure it is converted back to UTC correctly.
		:return:
		"""
		utc_date = datetime.datetime.now(datetime.timezone.utc)
		# Strip microseconds, they are not included in the string conversion
		utc_date = utc_date.replace(microsecond=0)

		# Local date will be the same time, but without any timezone data and converted to the local timezone.
		# This is typical for command output that doesn't include timezone data.
		local_date = (utc_date + datetime.timedelta(seconds=time.localtime().tm_gmtoff)).strftime('%Y-%m-%d %H:%M:%S')
		self.assertEqual(utc_date, common.str_to_utc(local_date, '%Y-%m-%d %H:%M:%S'))

	def test_with_timezone(self):
		"""
		Test with a string with built-in timezone data
		:return:
		"""
		utc_date = datetime.datetime.now(datetime.timezone.utc)
		# Strip microseconds, they are not included in the string conversion
		utc_date = utc_date.replace(microsecond=0)

		# Local date will be the same time, but without any timezone data and converted to the local timezone.
		# This is typical for command output that doesn't include timezone data.
		local_date = (utc_date + datetime.timedelta(seconds=-36000)).strftime('%Y-%m-%d %H:%M:%S')
		self.assertEqual(utc_date, common.str_to_utc(local_date + ' -1000', '%Y-%m-%d %H:%M:%S %z'))


class TestDateToEpoch(TestCase):
	def test_simple(self):
		"""
		Test converting a UTC date to epoch
		:return:
		"""
		utc_date = datetime.datetime.now(datetime.timezone.utc)
		self.assertEqual(int(time.time()), common.date_to_epoch(utc_date))

	def test_no_timezone(self):
		"""
		Test converting a UTC date with no timezone data to epoch
		:return:
		"""
		utc_date = datetime.datetime.now(tz=datetime.timezone.utc)

		# Convert to local timezone and strip the timezone data
		local_date = (utc_date + datetime.timedelta(seconds=time.localtime().tm_gmtoff)).replace(tzinfo=None)
		self.assertEqual(int(time.time()), common.date_to_epoch(local_date))


class TestCommon(TestCase):
	def test_formatted_string_to_bytes(self):
		self.assertEqual(common.formatted_string_to_bytes('1 PB'), 1125899906842624)
		self.assertEqual(common.formatted_string_to_bytes('1 TB'), 1099511627776)
		self.assertEqual(common.formatted_string_to_bytes('1 GB'), 1073741824)
		self.assertEqual(common.formatted_string_to_bytes('1 MB'), 1048576)
		self.assertEqual(common.formatted_string_to_bytes('1 kB'), 1024)

		self.assertEqual(common.formatted_string_to_bytes('1P'), 1125899906842624)
		self.assertEqual(common.formatted_string_to_bytes('1T'), 1099511627776)
		self.assertEqual(common.formatted_string_to_bytes('1G'), 1073741824)
		self.assertEqual(common.formatted_string_to_bytes('1M'), 1048576)
		self.assertEqual(common.formatted_string_to_bytes('1k'), 1024)

		self.assertEqual(common.formatted_string_to_bytes('1 PB/s'), 1e15)
		self.assertEqual(common.formatted_string_to_bytes('1 TB/s'), 1e12)
		self.assertEqual(common.formatted_string_to_bytes('1 GB/s'), 1e9)
		self.assertEqual(common.formatted_string_to_bytes('1 MB/s'), 1e6)
		self.assertEqual(common.formatted_string_to_bytes('1 kB/s'), 1000)

		self.assertEqual(common.formatted_string_to_bytes('1 Pb/s'), 1.25e14)
		self.assertEqual(common.formatted_string_to_bytes('1 Tb/s'), 1.25e11)
		self.assertEqual(common.formatted_string_to_bytes('1 Gb/s'), 1.25e8)
		self.assertEqual(common.formatted_string_to_bytes('1 Mb/s'), 1.25e5)
		self.assertEqual(common.formatted_string_to_bytes('1 kb/s'), 125)

	def test_formatted_string_to_bits(self):
		# 10kB == 80k bits
		self.assertEqual(common.formatted_string_to_bits('10 KB/s'), 80000)
