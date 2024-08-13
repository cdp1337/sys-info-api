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


class SystemCtlListServices(BinCollector):
	def __init__(self):
		super().__init__()
		self.bin = 'systemctl'
		self.arguments = ['--type=service', '--all', '--no-pager', '--no-legend']
		self.parser = self.PARSER_LINES

	def parse(self):
		super().parse()

		out = []
		for line in self.data:
			parts = line.split()
			if len(parts) < 4:
				continue

			out.append({
				'service': parts[0],
				'load': parts[1],
				'active': parts[2],
				'sub': parts[3],
				'description': ' '.join(parts[4:])
			})

		self.data = out

	def get_data(self) -> list:
		"""
		Get the list of units and their statuses
		"""
		self.ensure_ready()
		return self.data


class SystemCtlService(BinCollector):
	def __init__(self, service: str):
		super().__init__()
		self.service = service
		self.bin = 'systemctl'
		self.arguments = ['show', self.service, '--no-pager']
		self.parser = self.PARSER_LINES_KEY_VALUE
		self.parser_options = {
			'separator': '='
		}

	def get_data(self) -> dict:
		"""
		Get the status of a specific service
		"""
		self.ensure_ready()
		return self.data

	def enable(self):
		"""
		Enable the service
		"""
		self.run(['enable', self.service])

	def disable(self):
		"""
		Disable the service
		"""
		self.run(['disable', self.service])

	def start(self):
		"""
		Start the service
		"""
		self.run(['start', self.service])

	def stop(self):
		"""
		Stop the service
		"""
		self.run(['stop', self.service])

	def restart(self):
		"""
		Restart the service
		"""
		self.run(['restart', self.service])


class SystemCtlListServicesTest(BinCollectorTest):
	def setUp(self):
		self.collector = SystemCtlListServices()
		self.keys = {
			'data': self.collector.get_data,
		}
