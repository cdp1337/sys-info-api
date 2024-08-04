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

from sys_info_api.common.bin_collector import BinCollector
from sys_info_api.common.bin_collector_test import BinCollectorTest
from sys_info_api.common.exceptions import MetricNotAvailable


class LldpStatus(BinCollector):
	STATUS_RX = 'RX'
	STATUS_TX = 'TX'
	STATUS_RXTX = 'RXTX'
	STATUS_DISABLED = 'DISABLED'

	def __init__(self, iface: str):
		super().__init__()
		self.iface = iface
		self.bin = 'lldptool'
		self.arguments = ['-l', '-i', self.iface, 'adminStatus']
		self.parser = None
		self.keys = {
			'status': self.get_admin_status
		}

	def parse(self):
		super().parse()

		# Parse the output
		# adminStatus=rx
		if self.raw == '':
			raise MetricNotAvailable

		status = self.raw.split('=')[1].strip()
		if status == 'rx':
			self.data = {'status': self.STATUS_RX}
		elif status == 'tx':
			self.data = {'status': self.STATUS_TX}
		elif status == 'rxtx':
			self.data = {'status': self.STATUS_RXTX}
		else:
			self.data = {'status': self.STATUS_DISABLED}

	def get_admin_status(self) -> str:
		"""
		Get the administrative status of LLDP on the given interface, or throws a MetricNotAvailable if unable to get status

		Returns "RX", "TX", "RXTX", or "DISABLED"
		:return:
		:raises MetricNotAvailable:
		"""
		return self._get('status')

	def enable_rx(self):
		"""
		Enable receive for LLDP data on this interface
		:raises MetricNotAvailable:
		"""
		status = self.get_admin_status()

		if status == self.STATUS_TX:
			new_status = self.STATUS_RXTX
		elif status == self.STATUS_DISABLED:
			new_status = self.STATUS_RX
		else:
			new_status = None

		if new_status is not None:
			self.run(['-L', '-i', self.iface, 'adminStatus=' + new_status])

	def enable_tx(self):
		"""
		Enable transmit for LLDP data on this interface
		:raises MetricNotAvailable:
		"""
		status = self.get_admin_status()

		if status == self.STATUS_RX:
			new_status = self.STATUS_RXTX
		elif status == self.STATUS_DISABLED:
			new_status = self.STATUS_TX
		else:
			new_status = None

		if new_status is not None:
			self.run(['-L', '-i', self.iface, 'adminStatus=' + new_status])


class LldpNeighborScan(BinCollector):

	def __init__(self, iface: str):
		"""
		Execute lldptool and scan for a neighboring interface
		:param iface:
		"""
		super().__init__()
		self.bin = 'lldptool'
		self.arguments = ['-t', '-n', '-i', iface]
		self.parser = self.PARSER_LINES

	def parse(self):
		super().parse()

		data = {
			'chassis_id': None,
			'mac': None,
			'port_id': None,
			'port_name': None,
			'system_name': None,
			'system_description': None,
		}

		'''
		Chassis ID TLV
			MAC: f0:9f:c2:18:4c:27
		Port ID TLV
			Local: 0/4
		Time to Live TLV
			120
		Port Description TLV
			Port 4
		System Name TLV
			UBNT
		System Description TLV
			USW-8P-60, 4.0.54.10625, Linux 3.6.5
		System Capabilities TLV
			System capabilities:  Bridge
			Enabled capabilities: Bridge
		End of LLDPDU TLV
		'''
		last_key = None
		for line in self.data:
			if not line.startswith('\t'):
				last_key = line
			else:
				line_value = line.strip()
				if last_key == 'Chassis ID TLV':
					# chassisID
					data['chassis_id'] = line_value

				elif last_key == 'Port ID TLV':
					# portID
					if line_value.startswith('Local: '):
						data['port_id'] = line_value[7:]
					elif line_value.startswith('Ifname: '):
						data['port_id'] = line_value[8:]
					else:
						data['port_id'] = line_value

				elif last_key == 'Port Description TLV':
					# portDesc
					data['port_name'] = line_value

				elif last_key == 'System Name TLV':
					# sysName
					data['system_name'] = line_value

				elif last_key == 'System Description TLV':
					# sysDesc
					data['system_description'] = line_value

		if data['chassis_id'] is not None and data['chassis_id'].startswith('MAC: '):
			data['mac'] = data['chassis_id'][5:]

		self.data = data

	def get_mac(self):
		"""
		Get the MAC address of the neighboring device
		:raises MetricNotAvailable:
		"""
		return self._get('mac')

	def get_port_id(self):
		"""
		Get the port ID of the neighboring device
		:raises MetricNotAvailable:
		"""
		return self._get('port_id')

	def get_port_name(self):
		"""
		Get the port name of the neighboring device
		:raises MetricNotAvailable:
		"""
		return self._get('port_name')

	def get_system_name(self):
		"""
		Get the system name of the neighboring device
		:raises MetricNotAvailable:
		"""
		return self._get('system_name')

	def get_system_description(self):
		"""
		Get the system description of the neighboring device
		:raises MetricNotAvailable:
		"""
		return self._get('system_description')

	def get_chassis_id(self):
		"""
		Get the chassis ID of the neighboring device
		:raises MetricNotAvailable:
		"""
		return self._get('chassis_id')


class LldpStatusTest(BinCollectorTest):
	def setUp(self, iface='TEST'):
		self.collector = LldpStatus(iface)

	def get_test_keys(self) -> dict:
		return {
			'status': self.collector.get_admin_status,
		}


class LldpNeighborScanTest(BinCollectorTest):
	def setUp(self, iface='TEST'):
		self.collector = LldpNeighborScan(iface)

		self.keys = {
			'chassis_id': self.collector.get_chassis_id,
			'mac': self.collector.get_mac,
			'port_id': self.collector.get_port_id,
			'port_name': self.collector.get_port_name,
			'system_name': self.collector.get_system_name,
			'system_description': self.collector.get_system_description,
		}
