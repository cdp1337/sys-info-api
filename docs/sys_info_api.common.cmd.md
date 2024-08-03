<!-- markdownlint-disable -->

<a href="../src/sys_info_api/common/cmd.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `sys_info_api.common.cmd`





---

<a href="../src/sys_info_api/common/cmd.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `run_passthru`

```python
run_passthru(cmd: list, input=None, env=None)
```

Run a command and pass stdout and stderr directly to appropriate streams 

Throws CmdExecException 

:param cmd: The parameters of the call to execute 

:raises CmdExecExitCodeException: If the process returns an exit code other than 0 :raises CmdExecNotFoundException: If the binary was not found on the system 


---

<a href="../src/sys_info_api/common/cmd.py#L67"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `run_output`

```python
run_output(cmd: list) → str
```

Run a command and pass stderr to the log, while capturing stdout 

Throws all exceptions from command 

Will encode the output to UTF-8 and trim any newlines and whitespace 

:param cmd: The parameters of the call to execute :returns: The output from the command 

:raises CmdExecExitCodeException: If the process returns an exit code other than 0 :raises CmdExecNotFoundException: If the binary was not found on the system 


---

<a href="../src/sys_info_api/common/cmd.py#L93"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `run_binary`

```python
run_binary(cmd: list) → bytes
```

Run a command and pass stderr to the log, while capturing stdout as its raw binary output 

Throws all exceptions from command 

:param cmd: The parameters of the call to execute :returns: The output from the command 

:raises CmdExecExitCodeException: If the process returns an exit code other than 0 :raises CmdExecNotFoundException: If the binary was not found on the system 


---

<a href="../src/sys_info_api/common/cmd.py#L118"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `run_returncode`

```python
run_returncode(cmd: list) → int
```

Run a command and pass stderr to the log, ignoring output, and return the returncode 

Throws command not found exceptions 

:param cmd: The parameters of the call to execute :returns: The exit returncode from the command 

:raises CmdExecNotFoundException: If the binary was not found on the system 


---

<a href="../src/sys_info_api/common/cmd.py#L137"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `check_binary_exists`

```python
check_binary_exists(cmd: str) → bool
```

Check if a binary exists in the path 

:param cmd: :return: 


---

<a href="../src/sys_info_api/common/cmd.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CmdExecException`
Base command execution exception 





---

<a href="../src/sys_info_api/common/cmd.py#L27"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CmdExecExitCodeException`
Thrown if the command exit code wasn't good 

<a href="../src/sys_info_api/common/cmd.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(returncode, stdout)
```









---

<a href="../src/sys_info_api/common/cmd.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CmdExecNotFoundException`
Thrown if the command could not be located 







---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
