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

class KeyValueParser:
	"""
	A simple key/value parser for parsing key/value pairs from a string.
	"""

	def __init__(self, sep=":", linebreak="\n"):
		"""
		:raises ValueError:
		"""
		if sep is None or linebreak is None:
			raise ValueError("sep and linebreak cannot be None")

		self.sep = sep
		self.linebreak = linebreak
		self.comment = None
		self.quotes = 'auto'
		self.continuation = None

	def set_opts(self, options: dict):
		"""
		Set the options for the parser.

		:param options: The options to set
		:type options: dict
		"""
		if 'sep' in options:
			self.sep = options['sep']
		if 'linebreak' in options:
			self.linebreak = options['linebreak']
		if 'comment' in options:
			self.comment = options['comment']
		if 'quotes' in options:
			self.quotes = options['quotes']
		if 'continuation' in options:
			self.continuation = options['continuation']

	def to_dict(self, raw: str) -> dict:
		"""
		Parse the raw string into a dictionary of key/value pairs.

		:param raw: The raw string to parse
		:type raw: str
		:return: A dictionary of key/value pairs
		:rtype: dict
		"""

		data = {}
		key = None
		contents = raw.split(self.linebreak)
		for line in contents:
			if line.strip() == "":
				# Skip blank lines.
				continue

			if self.comment is not None and line.startswith(self.comment):
				# Skip comments if set
				continue

			if self.continuation and line.startswith(self.continuation) and key is not None:
				# Continuation line, (allows long multi-line descriptions)
				data[key] += "\n" + line[len(self.continuation):]
				continue

			# Use "index" to grab the first index of the sep; otherwise a string such as
			# key = cn=powell,ou=users,dc=example,dc=org
			# would really not work well.
			try:
				pos = line.index(self.sep)
			except ValueError:
				# Seperator not present on this line...?
				continue

			key = line[0:pos].strip()
			val = line[pos + 1:].strip()

			# Remove quotes if present and enabled
			if (self.quotes == 'auto' or self.quotes == '"') and val.startswith('"') and val.endswith('"'):
				val = val[1:-1]
			elif (self.quotes == 'auto' or self.quotes == "'") and val.startswith("'") and val.endswith("'"):
				val = val[1:-1]

			try:
				if type(data[key]) is str:
					data[key] = [data[key]]
					data[key].append(val)
				else:
					data[key].append(val)
			except KeyError:
				# Simple drop-in!
				data[key] = val

		return data

	'''
	Disabled until needed.  (No spec for this functionality, so nothing to build against)
	def to_str(self, data: dict) -> str:
		"""
		Convert a dictionary of key/value pairs back into a string.

		:param data: The dictionary of key/value pairs
		:type data: dict
		:return: The string representation of the key/value pairs
		:rtype: str
		"""

		lines = []
		for key, val in data.items():
			if type(val) is list:
				for v in val:
					lines.append(f"{key}{self.sep}{v}")
			else:
				lines.append(f"{key}{self.sep}{val}")

		return self.linebreak.join(lines)
	'''
