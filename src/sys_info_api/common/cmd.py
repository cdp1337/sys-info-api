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

import subprocess
import os
import logging


class CmdExecException(BaseException):
	"""
	Base command execution exception
	"""
	pass


class CmdExecExitCodeException(CmdExecException):
	"""
	Thrown if the command exit code wasn't good
	"""

	def __init__(self, returncode, stdout):
		self.returncode = returncode
		self.stdout = stdout


class CmdExecNotFoundException(CmdExecException):
	"""
	Thrown if the command could not be located
	"""
	pass


def run_passthru(cmd: list, input=None, env=None):
	"""
	Run a command and pass stdout and stderr directly to appropriate streams

	Throws CmdExecException

	:param cmd: The parameters of the call to execute

	:raises CmdExecExitCodeException: If the process returns an exit code other than 0
	:raises CmdExecNotFoundException: If the binary was not found on the system
	"""

	try:
		subprocess.run(cmd, stdout=None, stderr=None, check=True, input=input, env=env)

	except subprocess.CalledProcessError as e:
		logging.info('Exception [ReturnCode] from cmd.run_passthru([' + ', '.join(cmd) + '])')
		raise CmdExecExitCodeException(e.returncode, e.stdout)
	except FileNotFoundError:
		logging.info('Exception [BinaryNotFound] from cmd.run_passthru([' + ', '.join(cmd) + '])')
		raise CmdExecNotFoundException


def run_output(cmd: list) -> str:
	"""
	Run a command and pass stderr to the log, while capturing stdout

	Throws all exceptions from command

	Will encode the output to UTF-8 and trim any newlines and whitespace

	:param cmd: The parameters of the call to execute
	:returns: The output from the command

	:raises CmdExecExitCodeException: If the process returns an exit code other than 0
	:raises CmdExecNotFoundException: If the binary was not found on the system
	"""

	try:
		return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, encoding='utf-8').stdout.strip()
	except subprocess.CalledProcessError as e:
		logging.info('Exception [ReturnCode ' + str(e.returncode) + '] from cmd.run_output([' + ', '.join(cmd) + '])')
		logging.info(e.stderr)
		raise CmdExecExitCodeException(e.returncode, e.stdout)
	except FileNotFoundError:
		logging.info('Exception [BinaryNotFound] from cmd.run_output([' + ', '.join(cmd) + '])')
		raise CmdExecNotFoundException


def run_binary(cmd: list) -> bytes:
	"""
	Run a command and pass stderr to the log, while capturing stdout as its raw binary output

	Throws all exceptions from command

	:param cmd: The parameters of the call to execute
	:returns: The output from the command

	:raises CmdExecExitCodeException: If the process returns an exit code other than 0
	:raises CmdExecNotFoundException: If the binary was not found on the system
	"""

	try:
		# We're not doing any encoding work here, so raw output can be provided.
		return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True).stdout
	except subprocess.CalledProcessError as e:
		logging.info('Exception [ReturnCode ' + str(e.returncode) + '] from cmd.run_binary([' + ', '.join(cmd) + '])')
		logging.info(e.stderr)
		raise CmdExecExitCodeException(e.returncode, e.stdout)
	except FileNotFoundError:
		logging.info('Exception [BinaryNotFound] from cmd.run_binary([' + ', '.join(cmd) + '])')
		raise CmdExecNotFoundException


def run_returncode(cmd: list) -> int:
	"""
	Run a command and pass stderr to the log, ignoring output, and return the returncode

	Throws command not found exceptions

	:param cmd: The parameters of the call to execute
	:returns: The exit returncode from the command

	:raises CmdExecNotFoundException: If the binary was not found on the system
	"""

	try:
		return subprocess.run(cmd, stdout=open(os.devnull, "w"), stderr=None).returncode
	except FileNotFoundError:
		logging.info('Exception [BinaryNotFound] from cmd.run_returncode([' + ', '.join(cmd) + '])')
		raise CmdExecNotFoundException


def check_binary_exists(cmd: str) -> bool:
	"""
	Check if a binary exists in the path

	:param cmd:
	:return:
	"""
	return run_returncode(['which', cmd]) == 0
