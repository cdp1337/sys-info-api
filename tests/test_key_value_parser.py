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
from sys_info_api.common.key_value_parser import KeyValueParser


class KeyValueParserTest(TestCase):
	def test_to_dict_defaults(self):
		parser = KeyValueParser()
		data = parser.to_dict("key1:value1\nkey2:value2\n# this is a comment\nkey3:'some value 3'")
		self.assertEqual({
			'key1': 'value1',
			'key2': 'value2',
			'key3': 'some value 3'
		}, data)

		# str_data = parser.to_str(data)
		# self.assertEqual("key1:value1\nkey2:value2\nkey3:some value 3", str_data)

	def test_string_continuation(self):
		test_string = '''Package: firefox-esr
Version: 115.12.0esr-1~deb12u1
Description-en: Mozilla Firefox web browser - Extended Support Release (ESR)
 Firefox ESR is a powerful, extensible web:browser with support for modern
 web application technologies.
Description-md5: 88ee196fd829d9218a763b4d498a6f6a
'''  # noqa: E101
		parser = KeyValueParser()
		parser.quotes = 'none'
		parser.sep = ':'
		parser.continuation = ' '
		data = parser.to_dict(test_string)
		self.assertEqual({
			'Package': 'firefox-esr',
			'Version': '115.12.0esr-1~deb12u1',
			'Description-en': '''Mozilla Firefox web browser - Extended Support Release (ESR)
Firefox ESR is a powerful, extensible web:browser with support for modern
web application technologies.''',
			'Description-md5': '88ee196fd829d9218a763b4d498a6f6a'
		}, data)
