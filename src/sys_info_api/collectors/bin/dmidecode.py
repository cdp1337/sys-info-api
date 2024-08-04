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

import re
from datetime import datetime

from sys_info_api.common import formatted_string_to_bytes
from sys_info_api.common.bin_collector import BinCollector
from sys_info_api.common.bin_collector_test import BinCollectorTest
from sys_info_api.common.exceptions import MetricNotAvailable


class DmiSection(BinCollector):
	def __init__(self, type: str):
		super().__init__()
		self.bin = 'dmidecode'
		self.arguments = ['-q', '--type', type]
		self.parser = self.PARSER_LINES

	def parse(self):
		super().parse()
		groups = {}
		section = None
		last_key = None

		for line in self.data:
			if line == '':
				# Skip blank lines
				continue

			if re.match('^[a-zA-Z].*', line) is not None:
				# Header line, indicates a new section
				section = {}
				try:
					# Check if the group already exists
					# if it does, we want to convert it to a list.
					groups[line].append(section)
				except KeyError:
					# Group does not exist yet
					groups[line] = [section]
			elif re.match('^\t[a-zA-Z].*', line) is not None and section is not None:
				# Section header (may also be a self-contained value)
				line = line.strip()
				last_key = line[0: line.index(':')]
				line_value = line[line.index(':') + 2:].strip()

				if line_value == '':
					# Empty value, should contain either
					# a nested value set or legitimately an empty value.
					section[last_key] = None
				else:
					section[last_key] = line_value
			elif re.match('^\t\t[a-zA-Z].*', line) is not None and last_key is not None:
				# Nested key value for keys with multiple.
				line = line.strip()
				if section[last_key] is None:
					section[last_key] = []
				if not isinstance(section[last_key], list):
					section[last_key] = [section[last_key]]
				section[last_key].append(line)

		self.data = groups

	@classmethod
	def _check_string_unset(cls, value: str) -> str:
		"""
		Check if a given string is "unset" by the vendor

		Checks for common strings
		:param value: Value to check

		:raises MetricNotAvailable:
		"""
		empty_values = (
			'',
			'0123456789',
			'Default string',
			'N/A',
			'None',
			'No Asset Tag',
			'Not Applicable',
			'Not Specified',
			'System Product Name',
			'System Serial Number',
			'System Version',
			'System manufacturer',
			'Tag 12345',
			'To Be Filled By O.E.M.',
			'Unknown'
		)
		if value in empty_values:
			raise MetricNotAvailable

		return value

	@classmethod
	def _frequency_to_mhz(cls, value: str) -> int:
		if value.endswith(' MHz'):
			return int(value[:-4])
		elif value.endswith(' GHz'):
			return int(value[:-4]) * 1000
		else:
			raise MetricNotAvailable

	@classmethod
	def _transfers_to_mtps(cls, value: str) -> int:
		if value.endswith(' MT/s'):
			return int(value[:-5])
		elif value.endswith(' GT/s'):
			return int(value[:-5]) * 1000
		else:
			raise MetricNotAvailable

	@classmethod
	def _voltage_to_v(cls, value: str) -> float:
		if value.endswith(' V'):
			# This lookup will almost always return '#.# V'
			return float(value[:-2])
		else:
			raise MetricNotAvailable


class DmiBaseboard(DmiSection):

	def __init__(self):
		super().__init__('baseboard')

	def get_manufacturer(self) -> str:
		"""
		Retrieve the baseboard-manufacturer from DMI

		:raises MetricNotAvailable:
		"""
		return self._get(['Base Board Information', 0, 'Manufacturer'])

	def get_product_name(self) -> str:
		"""
		Retrieve the baseboard-product-name from DMI

		:raises MetricNotAvailable:
		"""
		return self._get(['Base Board Information', 0, 'Product Name'])

	def get_version(self) -> str:
		"""
		Retrieve the baseboard-version from DMI

		:raises MetricNotAvailable:
		"""
		return self._get(['Base Board Information', 0, 'Version'])

	def get_serial_number(self) -> str:
		"""
		Retrieve the baseboard-serial-number from DMI

		:raises MetricNotAvailable:
		"""
		return self._check_string_unset(self._get(['Base Board Information', 0, 'Serial Number']))

	def get_asset_tag(self) -> str:
		"""
		Retrieve the baseboard-asset-tag from DMI

		:raises MetricNotAvailable:
		"""
		return self._check_string_unset(self._get(['Base Board Information', 0, 'Asset Tag']))


class DmiBios(DmiSection):
	def __init__(self):
		super().__init__('bios')

	def get_vendor(self) -> str:
		"""
		:returns str: BIOS/UEFI vendor name

		:raises MetricNotAvailable:
		"""
		return self._check_string_unset(self._get(['BIOS Information', 0, 'Vendor']))

	def get_version(self) -> str:
		"""
		:returns str: BIOS/UEFI version

		:raises MetricNotAvailable:
		"""
		return self._get(['BIOS Information', 0, 'Version'])

	def get_release_date(self) -> datetime.date:
		"""
		:returns str: BIOS/UEFI release date

		:raises MetricNotAvailable:
		"""
		val = self._get(['BIOS Information', 0, 'Release Date'])
		return datetime.strptime(val, '%m/%d/%Y').date()


class DmiCache(DmiSection):
	def __init__(self):
		super().__init__('cache')

	def get_l1_size(self) -> int:
		"""
		:returns int: L1 cache size in bytes

		:raises MetricNotAvailable:
		"""
		vals = self._get(['Cache Information'])
		for val in vals:
			if 'Socket Designation' in val and val['Socket Designation'] == 'L1 - Cache':
				return formatted_string_to_bytes(val['Installed Size'])
		raise MetricNotAvailable

	def get_l2_size(self) -> int:
		"""
		:returns int: L1 cache size in bytes

		:raises MetricNotAvailable:
		"""
		vals = self._get(['Cache Information'])
		for val in vals:
			if 'Socket Designation' in val and val['Socket Designation'] == 'L2 - Cache':
				return formatted_string_to_bytes(val['Installed Size'])
		raise MetricNotAvailable

	def get_l3_size(self) -> int:
		"""
		:returns int: L1 cache size in bytes

		:raises MetricNotAvailable:
		"""
		vals = self._get(['Cache Information'])
		for val in vals:
			if 'Socket Designation' in val and val['Socket Designation'] == 'L3 - Cache':
				return formatted_string_to_bytes(val['Installed Size'])
		raise MetricNotAvailable


class DmiChassis(DmiSection):
	def __init__(self):
		super().__init__('chassis')

	def get_manufacturer(self) -> str:
		"""
		Retrieve the chassis-manufacturer from DMI

		:raises MetricNotAvailable:
		"""
		return self._check_string_unset(self._get(['Chassis Information', 0, 'Manufacturer']))

	def get_type(self) -> str:
		"""
		Retrieve the chassis-type from DMI

		:raises MetricNotAvailable:
		"""
		return self._check_string_unset(self._get(['Chassis Information', 0, 'Type']))

	def get_version(self) -> str:
		"""
		Retrieve the chassis-version from DMI

		:raises MetricNotAvailable:
		"""
		return self._check_string_unset(self._get(['Chassis Information', 0, 'Version']))

	def get_serial_number(self) -> str:
		"""
		Retrieve the chassis-serial-number from DMI

		:raises MetricNotAvailable:
		"""
		return self._check_string_unset(self._get(['Chassis Information', 0, 'Serial Number']))

	def get_asset_tag(self) -> str:
		"""
		Retrieve the chassis-asset-tag from DMI

		:raises MetricNotAvailable:
		"""
		return self._check_string_unset(self._get(['Chassis Information', 0, 'Asset Tag']))


'''
class Connector(DmiSection):

	def __init__(self):
		"""
		:raises MetricNotAvailable:
		"""
		self.groups = {}
		self._scan('connector')
'''


class DmiMemory(DmiSection):
	def __init__(self):
		super().__init__('memory')

	def get_total_banks(self) -> int:
		"""
		Get total number of memory banks on the system

		Will return both empty and occupied slots

		:return:
		"""
		return len(self._get('Memory Device'))

	def get_system_ecc(self) -> bool:
		"""
		Get if ECC is supported by the controller
		:return:
		"""
		value = self._get(['Physical Memory Array', 0, 'Error Correction Type'])
		return True if value != 'None' else False

	def get_system_maximum_capacity(self) -> int:
		"""
		Get the maximum memory capacity, in bytes
		:return:
		"""
		capacity = 0
		# Iterate over all the physical memory arrays and add up their capacities.
		# This is particularly required for multi-socket systems with multiple memory controllers.
		for i in range(len(self._get('Physical Memory Array'))):
			capacity += formatted_string_to_bytes(self._get(['Physical Memory Array', i, 'Maximum Capacity']))
		return capacity

	def get_width(self, module: int) -> int:
		"""
		Get memory width, in units of number of bits
		:param module:
		:return:
		"""
		value = self._get(['Memory Device', module, 'Total Width'])
		if value.endswith(' bits'):
			return int(value[:-4])
		else:
			return int(value)

	def is_installed(self, module: int) -> bool:
		"""
		Check if memory is installed in a given bank
		:param module:
		:return:
		"""
		return self._get(['Memory Device', module, 'Size']) != 'No Module Installed'

	def get_size(self, module: int) -> int:
		"""
		Get memory size, in bytes
		:param module:
		:return:
		"""
		return formatted_string_to_bytes(self._get(['Memory Device', module, 'Size']))

	def get_form_factor(self, module: int) -> str:
		"""
		Get memory form factor
		:param module:
		:return:
		"""
		return self._get(['Memory Device', module, 'Form Factor'])

	def get_locator(self, module: int) -> str:
		"""
		Get memory socket / location
		:param module:
		:return:
		"""
		return self._get(['Memory Device', module, 'Locator'])

	def get_type(self, module: int) -> str:
		"""
		Get memory type
		:param module:
		:return:
		"""
		return self._get(['Memory Device', module, 'Type'])

	def get_speed(self, module: int) -> int:
		"""
		Get memory speed, usually with MT/s units
		:param module:
		:return:
		"""
		return self._transfers_to_mtps(self._get(['Memory Device', module, 'Configured Memory Speed']))

	def get_max_speed(self, module: int) -> int:
		"""
		Get memory speed, usually with MT/s units
		:param module:
		:return:
		"""
		return self._transfers_to_mtps(self._get(['Memory Device', module, 'Speed']))

	def get_manufacturer(self, module: int) -> str:
		"""
		Get memory manufacturer
		:param module:
		:return:
		"""
		return self._check_string_unset(self._get(['Memory Device', module, 'Manufacturer']))

	def get_serial(self, module: int) -> str:
		"""
		Get memory serial number
		:param module:
		:return:
		"""
		return self._check_string_unset(self._get(['Memory Device', module, 'Serial Number']))

	def get_asset(self, module: int) -> str:
		"""
		Get memory asset tag
		:param module:
		:return:
		"""
		return self._check_string_unset(self._get(['Memory Device', module, 'Asset Tag']))

	def get_part(self, module: int) -> str:
		"""
		Get memory part number
		:param module:
		:return:
		"""
		return self._check_string_unset(self._get(['Memory Device', module, 'Part Number']))

	def get_voltage(self, module: int) -> float:
		"""
		Get memory voltage, will pull from system is individual memory voltage not available
		:param module:
		:return:
		"""
		return self._voltage_to_v(self._get(['Memory Device', module, 'Configured Voltage']))


class DmiProcessor(DmiSection):
	def __init__(self):
		super().__init__('processor')

	def get_total_count(self) -> int:
		"""
		:return int: The total number of processors detected

		:raises MetricNotAvailable:
		"""
		return len(self._get('Processor Information'))

	def get_total_cores(self) -> int:
		"""
		:return int: The total number of cores detected across all processors

		:raises MetricNotAvailable:
		"""
		value = 0
		for i in range(self.get_total_count()):
			value += self.get_cores(i)
		return value

	def get_total_threads(self) -> int:
		"""
		:return int: The total number of threads detected across all processors

		:raises MetricNotAvailable:
		"""
		value = 0
		for i in range(self.get_total_count()):
			value += self.get_threads(i)
		return value

	def get_socket(self, processor: int = 0) -> str:
		"""
		:raises MetricNotAvailable:
		"""
		return self._check_string_unset(self._get(['Processor Information', processor, 'Socket Designation']))

	def get_family(self, processor: int = 0) -> str:
		"""
		Retrieve the processor-family from DMI

		:raises MetricNotAvailable:
		"""
		return self._check_string_unset(self._get(['Processor Information', processor, 'Family']))

	def get_manufacturer(self, processor: int = 0) -> str:
		"""
		Retrieve the processor-manufacturer from DMI

		:raises MetricNotAvailable:
		"""
		return self._check_string_unset(self._get(['Processor Information', processor, 'Manufacturer']))

	def get_flags(self, processor: int = 0) -> list:
		"""
		:param processor:
		:return list:

		:raises MetricNotAvailable:
		"""
		flags = []
		for flag in self._get(['Processor Information', processor, 'Flags']):
			if flag.find('('):
				flags.append((flag[0: flag.find('(')]).strip())
			else:
				flags.append(flag)
		return flags

	def get_model(self, processor: int = 0) -> str:
		"""
		Retrieve the processor-version from DMI

		:raises KeyError:
		"""
		return self._check_string_unset(self._get(['Processor Information', processor, 'Version']))

	def get_voltage(self, processor: int = 0) -> float:
		"""
		:param processor:
		:return:

		:raises KeyError:
		"""
		return self._voltage_to_v(self._get(['Processor Information', processor, 'Voltage']))

	def get_frequency(self, processor: int = 0) -> int:
		"""
		Retrieve the processor-frequency from DMI

		:return int: Current speed of the processor in MHz

		:raises MetricNotAvailable:
		"""

		return self._frequency_to_mhz(self._get(['Processor Information', processor, 'Current Speed']))

	def get_max_frequency(self, processor: int = 0) -> int:
		"""
		Retrieve the processor-frequency from DMI

		:return int: Maximum speed of the processor in MHz

		:raises MetricNotAvailable:
		"""
		return self._frequency_to_mhz(self._get(['Processor Information', processor, 'Max Speed']))

	def get_status(self, processor: int = 0) -> str:
		"""

		:param processor:
		:return:

		:raises MetricNotAvailable:
		"""
		return self._get(['Processor Information', processor, 'Status'])

	def get_socket_type(self, processor: int = 0) -> str:
		"""

		:param processor:
		:return:

		:raises KeyError:
		"""
		return self._get(['Processor Information', processor, 'Upgrade'])

	def get_serial_number(self, processor: int = 0) -> str:
		"""

		:param processor:
		:return:

		:raises MetricNotAvailable:
		"""
		return self._check_string_unset(self._get(['Processor Information', processor, 'Serial Number']))

	def get_asset_tag(self, processor: int = 0) -> str:
		"""

		:param processor:
		:return:

		:raises MetricNotAvailable:
		"""
		return self._check_string_unset(self._get(['Processor Information', processor, 'Asset Tag']))

	def get_part_number(self, processor: int = 0) -> str:
		"""

		:param processor:
		:return:

		:raises MetricNotAvailable:
		"""
		return self._check_string_unset(self._get(['Processor Information', processor, 'Part Number']))

	def get_cores(self, processor: int = 0) -> int:
		"""

		:param processor:
		:return:

		:raises MetricNotAvailable:
		"""
		return int(self._get(['Processor Information', processor, 'Core Count']))

	def get_threads(self, processor: int = 0) -> int:
		"""

		:param processor:
		:return:

		:raises MetricNotAvailable:
		"""
		return int(self._get(['Processor Information', processor, 'Thread Count']))


'''
class Slot(DmiSection):

	def __init__(self):
		"""
		:raises MetricNotAvailable:
		"""
		self.groups = {}
		self._scan('slot')
'''


class DmiSystem(DmiSection):
	def __init__(self):
		super().__init__('system')

	def get_manufacturer(self) -> str:
		"""
		Retrieve the system-manufacturer from DMI

		:raises MetricNotAvailable:
		"""
		return self._check_string_unset(self._get(['System Information', 0, 'Manufacturer']))

	def get_product_name(self) -> str:
		"""
		Retrieve the system-product-name from DMI

		:raises MetricNotAvailable:
		"""
		return self._check_string_unset(self._get(['System Information', 0, 'Product Name']))

	def get_version(self) -> str:
		"""
		Retrieve the system-version from DMI

		:raises MetricNotAvailable:
		"""
		return self._check_string_unset(self._get(['System Information', 0, 'Version']))

	def get_serial_number(self) -> str:
		"""
		Retrieve the system-serial-number from DMI

		:raises MetricNotAvailable:
		"""
		return self._check_string_unset(self._get(['System Information', 0, 'Serial Number']))

	def get_uuid(self) -> str:
		"""
		Retrieve the system-uuid from DMI

		:raises MetricNotAvailable:
		"""
		return self._check_string_unset(self._get(['System Information', 0, 'UUID']))

	def get_family(self) -> str:
		"""
		Retrieve the system-family from DMI

		:raises MetricNotAvailable:
		"""
		return self._check_string_unset(self._get(['System Information', 0, 'Family']))


class DmiBaseboardTest(BinCollectorTest):
	def setUp(self):
		self.collector = DmiBaseboard()

	def get_test_keys(self) -> dict:
		keys = {
			'manufacturer': self.collector.get_manufacturer,
			'product_name': self.collector.get_product_name,
			'version': self.collector.get_version,
			'serial_number': self.collector.get_serial_number,
			'asset_tag': self.collector.get_asset_tag
		}

		return keys


class DmiBiosTest(BinCollectorTest):
	def setUp(self):
		self.collector = DmiBios()

	def get_test_keys(self) -> dict:
		keys = {
			'vendor': self.collector.get_vendor,
			'version': self.collector.get_version,
			'release_date': self.collector.get_release_date
		}

		return keys


class DmiCacheTest(BinCollectorTest):
	def setUp(self):
		self.collector = DmiCache()

	def get_test_keys(self) -> dict:
		keys = {
			'l1_size': self.collector.get_l1_size,
			'l2_size': self.collector.get_l2_size,
			'l3_size': self.collector.get_l3_size
		}

		return keys


class DmiChassisTest(BinCollectorTest):
	def setUp(self):
		self.collector = DmiChassis()

	def get_test_keys(self) -> dict:
		keys = {
			'manufacturer': self.collector.get_manufacturer,
			'type': self.collector.get_type,
			'version': self.collector.get_version,
			'serial_number': self.collector.get_serial_number,
			'asset_tag': self.collector.get_asset_tag
		}

		return keys


class DmiMemoryTest(BinCollectorTest):
	def setUp(self):
		self.collector = DmiMemory()

	def get_test_keys(self) -> dict:
		keys = {
			'total_banks': self.collector.get_total_banks,
			'system_ecc': self.collector.get_system_ecc,
			'system_maximum_capacity': self.collector.get_system_maximum_capacity,
		}

		banks = self.collector.get_total_banks()
		for bank in range(banks):
			keys[f'bank_{bank}_width'] = [self.collector.get_width, bank]
			keys[f'bank_{bank}_installed'] = [self.collector.is_installed, bank]
			keys[f'bank_{bank}_size'] = [self.collector.get_size, bank]
			keys[f'bank_{bank}_form_factor'] = [self.collector.get_form_factor, bank]
			keys[f'bank_{bank}_locator'] = [self.collector.get_locator, bank]
			keys[f'bank_{bank}_type'] = [self.collector.get_type, bank]
			keys[f'bank_{bank}_speed'] = [self.collector.get_speed, bank]
			keys[f'bank_{bank}_max_speed'] = [self.collector.get_max_speed, bank]

		return keys


class DmiProcessorTest(BinCollectorTest):
	def setUp(self):
		self.collector = DmiProcessor()

	def get_test_keys(self) -> dict:
		keys = {
			'total_count': self.collector.get_total_count,
			'total_cores': self.collector.get_total_cores,
			'total_threads': self.collector.get_total_threads,
		}

		# Dynamic keys
		for cpu in range(self.collector.get_total_count()):
			keys[f'cpu_{cpu}_socket'] = [self.collector.get_socket, cpu]
			keys[f'cpu_{cpu}_family'] = [self.collector.get_family, cpu]
			keys[f'cpu_{cpu}_manufacturer'] = [self.collector.get_manufacturer, cpu]
			keys[f'cpu_{cpu}_flags'] = [self.collector.get_flags, cpu]
			keys[f'cpu_{cpu}_model'] = [self.collector.get_model, cpu]
			keys[f'cpu_{cpu}_voltage'] = [self.collector.get_voltage, cpu]
			keys[f'cpu_{cpu}_frequency'] = [self.collector.get_frequency, cpu]
			keys[f'cpu_{cpu}_max_frequency'] = [self.collector.get_max_frequency, cpu]
			keys[f'cpu_{cpu}_status'] = [self.collector.get_status, cpu]
			keys[f'cpu_{cpu}_socket_type'] = [self.collector.get_socket_type, cpu]
			keys[f'cpu_{cpu}_serial_number'] = [self.collector.get_serial_number, cpu]
			keys[f'cpu_{cpu}_asset_tag'] = [self.collector.get_asset_tag, cpu]
			keys[f'cpu_{cpu}_part_number'] = [self.collector.get_part_number, cpu]
			keys[f'cpu_{cpu}_cores'] = [self.collector.get_cores, cpu]
			keys[f'cpu_{cpu}_threads'] = [self.collector.get_threads, cpu]

		return keys


class DmiSystemTest(BinCollectorTest):
	def setUp(self):
		self.collector = DmiSystem()

	def get_test_keys(self) -> dict:
		keys = {
			'manufacturer': self.collector.get_manufacturer,
			'product_name': self.collector.get_product_name,
			'version': self.collector.get_version,
			'serial_number': self.collector.get_serial_number,
			'uuid': self.collector.get_uuid,
			'family': self.collector.get_family
		}

		return keys
