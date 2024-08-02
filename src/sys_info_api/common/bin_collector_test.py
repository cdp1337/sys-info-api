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

from enum import Enum
from unittest import TestCase

from sys_info_api.common import BinCollector, MetricNotAvailable


class BinCollectorTest(TestCase):
	"""
	Base class for collector tests for binary commands.
	"""

	def __init__(self):
		super().__init__()
		self.collector = BinCollector()

		self.keys = {}
		"""
		List of value keys and their associated functions to retrieve the value
		Useful for automated test generation of collectors
		:type: dict[str, callable]
		"""

	def get_test_keys(self) -> dict[str, callable]:
		"""
		Get the keys in the data of this collector that are testable
		:return:
		"""
		return self.keys

	def generate_raw_data(self) -> str:
		"""
		Dump the raw data pulled from the underlying collector
		:return:
		"""
		self.collector.ensure_ready()
		return self.collector.raw

	def generate_test_data(self) -> dict:
		"""
		Dump the test data generated based on the underlying collector
		:return:
		"""
		# return self.collector.data

		data = {}
		keys = self.get_test_keys()
		for key in keys:
			try:
				if isinstance(keys[key], list):
					# Complex call which requires arguments
					val = keys[key][0](*keys[key][1:])
				else:
					val = keys[key]()

				if isinstance(val, Enum):
					# Simplify ENUM values to their underlying value.
					val = val.value
				data[key] = val
			except MetricNotAvailable:
				data[key] = None
		return data

	def load_raw_data(self, data: str):
		"""
		Load raw data into this collector (useful for testing)
		:param data:
		:return:
		"""
		self.collector.raw = data
		self.collector.parse()

	def _verify_test_key(self, key: str, keys: dict, data: dict):
		"""
		Verify test data against the underlying collector
		:param key: Key to verify
		:param keys: List of keys from test collector
		:param data: Data to verify against
		:return:
		"""
		if key in data and data[key] is not None:
			if isinstance(keys[key], list):
				calculated_value = keys[key][0](*keys[key][1:])
			else:
				calculated_value = keys[key]()
			expected_value = data[key]

			# Allow ENUMs to be simplified to their underlying value
			if isinstance(calculated_value, Enum):
				calculated_value = calculated_value.value

			self.assertEqual(
				data[key],
				calculated_value,
				'Key {} expected {} but {} calculated from data'.format(key, expected_value, calculated_value)
			)
		else:
			try:
				# This is supposed to fail, but if it succeeds, notify the dev of the value
				if isinstance(keys[key], list):
					calculated_value = keys[key][0](*keys[key][1:])
				else:
					calculated_value = keys[key]()

				self.fail('Key "{}" expected to be not available but "{}" calculated from data'.format(key, calculated_value))
			except MetricNotAvailable:
				calculated_value = None

	def verify_test_data(self, data: dict):
		"""
		Verify test data against the underlying collector
		:param data:
		:return:
		"""
		keys = self.get_test_keys()
		for key in keys:
			self._verify_test_key(key, keys, data)
