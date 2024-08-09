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
from typing import Union

from sys_info_api.common.bin_collector import BinCollector
from sys_info_api.common.bin_collector_test import BinCollectorTest


class Lsusb(BinCollector):
	def __init__(self):
		super().__init__()
		self.bin = 'lsusb'
		self.arguments = ['-v']
		self.parser = self.PARSER_LINES

	def parse(self):
		"""
		Run lsusb and retrieve the results as an array of dict objects
		"""
		super().parse()

		mappings = {
			'bcdUSB ': ['usb_version', _line_val],
			'idVendor ': ['id_vendor', _line_hex_and_string],
			'idProduct ': ['id_product', _line_hex_and_string],
			'iManufacturer ': ['manufacturer', _line_val_and_string_string_only],
			'iProduct ': ['product', _line_val_and_string_string_only],
			'iSerial ': ['serial', _line_val_and_string_string_only],
			'MaxPower ': ['max_power', _line_val_amps],
			'bDeviceClass ': ['device_class', _line_val_and_string_string_only],
			'bDeviceSubClass ': ['device_sub_class', _line_val_and_string_string_only],
			'bDeviceProtocol ': ['device_protocol', _line_val_and_string_string_only],
			'bInterfaceClass ': ['interface_class', _line_val_and_string_string_only],
			'bInterfaceSubClass ': ['interface_sub_class', _line_val_and_string_string_only],
			'bInterfaceProtocol ': ['interface_sub_class', _line_val_and_string_string_only],
			'nNbrPorts ': ['number_ports', _line_val_int],
		}

		mapping_keys = list(mappings.keys())

		devices = []
		entry = {}

		for line in self.data:
			"""
			Parse the output from lsusb line-by-line to sort them into a dictionary
			"""

			if line.startswith("Bus"):
				# The "Bus" line indicates a new device and contains the bus and device ID.
				# Reset the current to a new object and start tracking
				entry = {
					'bus': re.sub('Bus ([0-9]*) .*', '\\1', line),
					'device': re.sub('.*Device ([0-9]*):.*', '\\1', line)
				}
				devices.append(entry)
				continue

			# Determine the nesting level of the current line prior to trimming.
			# May be useful in determining some values.
			# level = (len(line) - len(line.lstrip(' '))) / 2 + 1
			trimmed_line = line.strip()

			for key in mapping_keys:
				if trimmed_line.startswith(key):
					entry[mappings[key][0]] = mappings[key][1](trimmed_line)
					break

		self.data = devices

	def get_data(self):
		self.ensure_ready()
		return self.data


def _line_hex_and_string(line: str) -> dict:
	"""
	ex: 0x0bda Realtek Semiconductor Corp.

	:param line:
	:return:
	"""
	value = line[line.index(' '):].strip()
	return {'code': int(value[0:6], 16), 'value': value[7:]}


def _line_val_and_string_string_only(line: str) -> Union[str, None]:
	"""
	ex: 2 USB 10/100/1000 LAN

	:param line:
	:return:
	"""
	value = line[line.index(' '):].strip()
	try:
		value = value[value.index(' '):].strip()
		return value
	except ValueError:
		return None


def _line_val(line: str) -> str:
	"""
	ex: bcdUSB               3.00

	:param line:
	:return:
	"""
	return line[line.index(' '):].strip()


def _line_val_amps(line: str) -> int:
	"""
	ex: MaxPower              288mA
	:param line:
	:return:
	"""
	return int(line[line.index(' '):].strip()[0:-2])


def _line_val_int(line: str) -> int:
	return int(line[line.index(' '):].strip())


class LsusbTest(BinCollectorTest):
	def setUp(self):
		self.collector = Lsusb()
		self.keys = {
			'data': self.collector.get_data,
		}
