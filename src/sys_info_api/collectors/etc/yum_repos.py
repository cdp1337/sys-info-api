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

import os
from typing import List

from sys_info_api.common.bin_collector import BinCollector
from sys_info_api.common.bin_collector_test import BinCollectorTest
from sys_info_api.common.exceptions import MetricNotAvailable


class _YumRepo:
	def __init__(self):
		self.name = ''
		self.data = []

	def parse_line(self, line):
		if line.startswith('['):
			self.name = line[1:-1]
		elif line.startswith('# '):
			self.data.append({
				'type': 'comment',
				'value': line[2:]
			})
		else:
			enabled = True
			if line.startswith('#'):
				# Disabled line
				enabled = False
				line = line.strip('#').strip()

			key = line[0:line.index('=')].strip()
			value = line[line.index('=') + 1:].strip()

			self.data.append({
				'type': 'directive',
				'enabled': enabled,
				'key': key,
				'value': value
			})

	def get_content(self) -> str:
		content = '[' + self.name + ']\n'
		for line in self.data:
			if line['type'] == 'comment':
				content += '# ' + line['value'] + '\n'
			elif line['type'] == 'directive':
				if not line['enabled']:
					content += '#'
				content += line['key'] + '=' + line['value'] + '\n'

		return content

	def _get_line_idx(self, key: str) -> int:
		for idx, line in enumerate(self.data):
			if line['type'] == 'directive' and line['key'] == key:
				return idx
		return -1

	def key_enable(self, key: str):
		idx = self._get_line_idx(key)
		if idx == -1:
			# autocreate
			self.data.append({
				'type': 'directive',
				'enabled': True,
				'key': key,
				'value': ''
			})
		else:
			self.data[idx]['enabled'] = True

	def key_disable(self, key: str):
		idx = self._get_line_idx(key)
		if idx != -1:
			self.data[idx]['enabled'] = False

	def get_key_value(self, key: str):
		idx = self._get_line_idx(key)
		if idx == -1:
			return None
		return self.data[idx]['value']

	def set_key_value(self, key: str, value: str):
		idx = self._get_line_idx(key)
		if idx == -1:
			# autocreate
			self.data.append({
				'type': 'directive',
				'enabled': True,
				'key': key,
				'value': value
			})
		else:
			self.data[idx]['value'] = value

	def is_key_enabled(self, key: str) -> bool:
		idx = self._get_line_idx(key)
		if idx == -1:
			return False
		return self.data[idx]['enabled']

	def enable(self):
		self.set_key_value('enabled', '1')

	def disable(self):
		self.set_key_value('enabled', '0')

	def get_excluded_packages(self) -> List[str]:
		idx = self._get_line_idx('excludepkgs')
		if idx == -1:
			return []
		return self.data[idx]['value'].split()

	def add_excluded_package(self, package: str):
		excluded = self.get_excluded_packages()
		if package not in excluded:
			excluded.append(package)
		self.set_key_value('excludepkgs', ' '.join(excluded))


class YumRepos(BinCollector):
	def __init__(self, filename: str):
		super().__init__()

		self.path = os.path.join('/etc/yum.repos.d', filename + '.repo')
		self.bin = 'cat'

		if os.path.exists(self.path):
			self.arguments = [self.path]
		else:
			self.bin = 'false'

		self.parser = self.PARSER_RAW

	def fetch(self):
		if self.bin != 'false':
			# Allow this collector to run if the file does not exist, (it can generate a new file if save is called.)
			super().fetch()
		else:
			self.data = ''

	def parse(self):
		super().parse()

		self.data = {
			'comment': '',
			'repos': [],
		}

		# Grab the document header comment and iterate through handling each repo as it's found
		in_header = True
		repo = None
		for line in self.raw.split('\n'):
			if in_header:
				if line.startswith('# '):
					self.data['comment'] += line[2:] + '\n'
				elif line.startswith('#'):
					self.data['comment'] += '\n'
				else:
					# Strip the last newline from the comment, (otherwise it'll produce an extra '# ' at the end)
					self.data['comment'] = self.data['comment'].strip()
					in_header = False
			else:
				if line.strip() == '':
					continue

				if line.startswith('['):
					# Start of a new repo
					repo = _YumRepo()
					self.data['repos'].append(repo)

				repo.parse_line(line)

	def has_repo(self, name: str) -> bool:
		self.ensure_ready()

		for repo in self.data['repos']:
			if repo.name == name:
				return True

		return False

	def get_repo(self, name: str) -> _YumRepo:
		self.ensure_ready()

		for repo in self.data['repos']:
			if repo.name == name:
				return repo

		raise MetricNotAvailable

	def new_repo(self, name: str) -> _YumRepo:
		repo = _YumRepo()
		repo.name = name
		self.data['repos'].append(repo)
		return repo

	def get_content(self):
		self.ensure_ready()

		content = ''
		for comment in self.data['comment'].split('\n'):
			if comment == '':
				content += '#\n'
			else:
				content += '# ' + comment + '\n'

		for repo in self.data['repos']:
			content += '\n' + repo.get_content()

		return content

	def save(self):
		with open(self.path, 'w') as f:
			f.write(self.get_content())


class YumReposTest(BinCollectorTest):
	def setUp(self, filename: str):
		self.collector = YumRepos(filename)
		self.keys = {
			'content': self.collector.get_content,
		}
