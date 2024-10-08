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
import os

from sys_info_api.common.exceptions import MetricNotAvailable
from sys_info_api.common.key_value_parser import KeyValueParser
from sys_info_api.common import cmd


class BinParser:
	"""
	Parser layer for processing data, (usually from commands)
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

	def _gets(self, keys: [str]):
		"""
		Get one of multiple values from the data using the keys

		Will return the first located key, or throw an exception if none of the provided are found.

		:param keys:
		:return:
		"""
		for key in keys:
			try:
				return self._get(key)
			except MetricNotAvailable:
				pass

		# None matched
		raise MetricNotAvailable

	def parse(self):
		"""
		Parse the raw output into a usable format
		:throws MetricNotAvailable:
		"""
		if self.raw is None:
			# Parse cannot be called before the data is available!
			raise MetricNotAvailable

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


class BinCollector(BinParser):
	"""
	Base class for collectors that run a binary command and parse the output.
	"""

	BIN_FREAD = 'PYTHON_FILE_READ'

	def __init__(self):
		"""
		When initializing a new binary collector, set the following arguments:

		- self.bin: The binary to run
		- self.arguments: A list of arguments to pass to the binary
		- self.parser: The parser to use for handling the output
		"""
		super().__init__()

		self.bin = 'true'
		"""
		Binary to run, (either fully resolved or in the PATH)
		:type str
		"""

		self.filename = None
		"""
		When native read is requested, this is the filename to read
		:type str
		"""

		self.arguments = []
		"""
		List of arguments (as strings) to pass to the binary
		:type list[str]
		"""

		self.return_codes = None
		"""
		List of return codes to consider as successful, (default is none, only allow '0')
		:type list[int]
		"""

	def fetch(self):
		"""
		Run the binary and store the output
		:throws MetricNotAvailable:
		"""
		if self.bin == self.BIN_FREAD:
			# Special option to have Python handle the read natively
			if not os.path.exists(self.filename):
				self.raw = False
				raise MetricNotAvailable
			try:
				with open(self.filename, 'r') as f:
					self.raw = f.read()
			except OSError:
				self.raw = False
				raise MetricNotAvailable
		else:
			# Standard binary execution
			try:
				self.raw = cmd.run_output([self.bin] + self.arguments)
			except cmd.CmdExecExitCodeException as e:
				if self.return_codes is not None and e.returncode in self.return_codes:
					# A return code != 0 will trigger an exception to be raised,
					# but allow the developer to specify which return codes are acceptable
					self.raw = e.stdout.strip()
				else:
					self.raw = False
					raise MetricNotAvailable
			except cmd.CmdExecException:
				self.raw = False
				raise MetricNotAvailable

	def run(self, arguments: [str], input=None, env=None):
		"""
		Run the binary with the given arguments

		Does NOT store the output, (useful for one-off commands)
		:param env:
		:param input:
		:param arguments:
		:raises MetricNotAvailable:
		"""
		try:
			cmd.run_passthru([self.bin] + arguments, input=input, env=env)
		except cmd.CmdExecException:
			raise MetricNotAvailable

	def parse(self):
		"""
		Parse the raw output into a usable format
		:throws MetricNotAvailable:
		"""
		if self.raw is None:
			self.fetch()

		super().parse()
