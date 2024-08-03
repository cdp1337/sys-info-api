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
from sys_info_api.common import cmd


class TestRunPassthru(TestCase):
	"""
	Test the passthru command executor

	Since this def doesn't return anything, just test basic execution
	"""
	def test_good_exec(self):
		cmd.run_passthru(['true'])

	def test_bad_return_code(self):
		self.assertRaises(cmd.CmdExecExitCodeException, cmd.run_passthru, ['false'])

	def test_not_found(self):
		self.assertRaises(cmd.CmdExecNotFoundException, cmd.run_passthru, ['notfound'])


class TestRunOutput(TestCase):
	"""
	Test the command executor for retrieving output (as a string)
	"""
	def test_good_exec(self):
		self.assertEqual(cmd.run_output(['true']), '')

		root_listing = cmd.run_output(['ls', '/'])
		# This particular command should have at least 2 newlines
		self.assertGreater(root_listing.count("\n"), 1)

	def test_bad_return_code(self):
		self.assertRaises(cmd.CmdExecExitCodeException, cmd.run_output, ['false'])

	def test_not_found(self):
		self.assertRaises(cmd.CmdExecNotFoundException, cmd.run_output, ['notfound'])


class TestRunBinary(TestCase):
	"""
	Test the command executor for retrieving output (as binary data)
	"""
	def test_good_exec(self):
		self.assertEqual(cmd.run_binary(['true']), b'')

	def test_bad_return_code(self):
		self.assertRaises(cmd.CmdExecExitCodeException, cmd.run_binary, ['false'])

	def test_not_found(self):
		self.assertRaises(cmd.CmdExecNotFoundException, cmd.run_binary, ['notfound'])


class TestRunReturncode(TestCase):
	"""
	Test the command executor for retrieving the return code of processes
	"""
	def test_good_exec(self):
		self.assertEqual(cmd.run_returncode(['true']), 0)

	def test_bad_return_code(self):
		self.assertEqual(cmd.run_returncode(['false']), 1)

	def test_not_found(self):
		# Not found binaries still throw an exception.
		self.assertRaises(cmd.CmdExecNotFoundException, cmd.run_returncode, ['notfound'])


class TestCheckBinaryExists(TestCase):
	"""
	Test the command helper for checking if a given binary is available
	"""
	def test_found(self):
		self.assertTrue(cmd.check_binary_exists('true'))

	def test_not_found(self):
		self.assertFalse(cmd.check_binary_exists('notfound'))
