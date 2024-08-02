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

import json

from sys_info_api.common import MetricNotAvailable, KeyValueParser
from sys_info_api.common import cmd


class BinCollector:
	"""
	Base class for collectors that run a binary command and parse the output.
	"""

	PARSER_JSON = 'json'
	"""
	Use JSON to parse the output
	"""

	PARSER_RAW = 'raw'
	"""
	Do not parse the output at all, just directly use from raw output
	"""

	PARSER_LINES = 'lines'
	"""
	Split lines from the output
	"""

	PARSER_LINES_KEY_VALUE = 'lines_key_value'
	"""
	Split lines from output and convert to a dictionary via key/value pairs
	"""

	def __init__(self):
		"""
		When initializing a new binary collector, set the following arguments:

		- self.bin: The binary to run
		- self.arguments: A list of arguments to pass to the binary
		- self.parser: The parser to use for handling the output
		"""
		self.bin = 'true'
		"""
		Binary to run, (either fully resolved or in the PATH)
		:type str
		"""

		self.arguments = []
		"""
		List of arguments (as strings) to pass to the binary
		:type list[str]
		"""

		self.raw = None
		"""
		Raw output from binary
		"""

		self.data = None
		"""
		Parsed data from binary (to be manipulated as necessary by any custom parser)
		"""

		self.parser = None
		"""
		Type of parser to run automatically
		:type str|None
		"""

		self.parser_options = None
		"""
		Options to pass into the parser, see the corresponding parser for details.
		"""

	def fetch(self):
		"""
		Run the binary and store the output
		:throws MetricNotAvailable:
		"""
		try:
			self.raw = cmd.run_output([self.bin] + self.arguments)
		except cmd.CmdExecException:
			self.raw = False
			raise MetricNotAvailable

	def run(self, arguments: [str]) -> str:
		"""
		Run the binary with the given arguments and return the output

		Does NOT store the output, (useful for one-off commands)
		:param arguments:
		:return:
		:raises MetricNotAvailable:
		"""
		try:
			return cmd.run_output([self.bin] + arguments)
		except cmd.CmdExecException:
			raise MetricNotAvailable

	def _get(self, key):
		"""
		Get a value from the data using the key
		:param key:
		:return:
		"""
		self.ensure_ready()

		if isinstance(key, list):
			check = self.data
			for k in key:
				try:
					check = check[k]
				except KeyError:
					raise MetricNotAvailable
			if check is None:
				raise MetricNotAvailable

			return check
		else:
			try:
				if self.data[key] is None:
					raise MetricNotAvailable
				return self.data[key]
			except KeyError:
				raise MetricNotAvailable

	def parse(self):
		"""
		Parse the raw output into a usable format
		:throws MetricNotAvailable:
		"""
		if self.raw is None:
			self.fetch()

		if self.parser is None:
			# No parser requested, just skip.
			# Allows super.parse() to be called to setup data
			pass
		elif self.parser == self.PARSER_JSON:
			# Parse data using JSON parser
			if self.raw == '':
				raise MetricNotAvailable

			try:
				self.data = json.loads(self.raw)
			except (json.JSONDecodeError, TypeError):
				raise MetricNotAvailable
		elif self.parser == self.PARSER_RAW:
			# No parsing, just pass the raw data
			if self.raw == '':
				raise MetricNotAvailable

			self.data = self.raw
		elif self.parser == self.PARSER_LINES:
			# Extract lines from the output and set data as an array of lines
			if self.raw == '':
				raise MetricNotAvailable

			self.data = self.raw.split("\n")
		elif self.parser == self.PARSER_LINES_KEY_VALUE:
			# Use the KeyValueParser to parse the output into a dictionary
			parser = KeyValueParser()
			if self.parser_options is not None:
				parser.set_opts(self.parser_options)
			self.data = parser.to_dict(self.raw)
		else:
			raise MetricNotAvailable

	def clear(self):
		"""
		Clear the raw and parsed data, allowing for multiple functions on the same binary
		or manual re-fetching of data.
		"""
		self.raw = None
		self.data = None

	def ensure_ready(self):
		"""
		Ensure that the data is ready for use, (safe to call multiple times)
		"""
		if self.data is None:
			self.parse()
