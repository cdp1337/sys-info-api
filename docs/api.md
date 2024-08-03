# Table of Contents

* [sys\_info\_api](#sys_info_api)
* [sys\_info\_api.bin.generate\_test\_data](#sys_info_api.bin.generate_test_data)
* [sys\_info\_api.common.bin\_collector](#sys_info_api.common.bin_collector)
  * [BinCollector](#sys_info_api.common.bin_collector.BinCollector)
    * [PARSER\_JSON](#sys_info_api.common.bin_collector.BinCollector.PARSER_JSON)
    * [PARSER\_RAW](#sys_info_api.common.bin_collector.BinCollector.PARSER_RAW)
    * [PARSER\_LINES](#sys_info_api.common.bin_collector.BinCollector.PARSER_LINES)
    * [PARSER\_LINES\_KEY\_VALUE](#sys_info_api.common.bin_collector.BinCollector.PARSER_LINES_KEY_VALUE)
    * [\_\_init\_\_](#sys_info_api.common.bin_collector.BinCollector.__init__)
    * [fetch](#sys_info_api.common.bin_collector.BinCollector.fetch)
    * [run](#sys_info_api.common.bin_collector.BinCollector.run)
    * [parse](#sys_info_api.common.bin_collector.BinCollector.parse)
    * [clear](#sys_info_api.common.bin_collector.BinCollector.clear)
    * [ensure\_ready](#sys_info_api.common.bin_collector.BinCollector.ensure_ready)
* [sys\_info\_api.common.cmd](#sys_info_api.common.cmd)
  * [CmdExecException](#sys_info_api.common.cmd.CmdExecException)
  * [CmdExecExitCodeException](#sys_info_api.common.cmd.CmdExecExitCodeException)
  * [CmdExecNotFoundException](#sys_info_api.common.cmd.CmdExecNotFoundException)
  * [run\_passthru](#sys_info_api.common.cmd.run_passthru)
  * [run\_output](#sys_info_api.common.cmd.run_output)
  * [run\_binary](#sys_info_api.common.cmd.run_binary)
  * [run\_returncode](#sys_info_api.common.cmd.run_returncode)
  * [check\_binary\_exists](#sys_info_api.common.cmd.check_binary_exists)
* [sys\_info\_api.common.exceptions](#sys_info_api.common.exceptions)
  * [MetricNotAvailable](#sys_info_api.common.exceptions.MetricNotAvailable)
* [sys\_info\_api.common.local\_timezone](#sys_info_api.common.local_timezone)
* [sys\_info\_api.common](#sys_info_api.common)
  * [print\_error](#sys_info_api.common.print_error)
  * [print\_warning](#sys_info_api.common.print_warning)
  * [str\_to\_utc](#sys_info_api.common.str_to_utc)
  * [date\_to\_epoch](#sys_info_api.common.date_to_epoch)
  * [formatted\_string\_to\_bytes](#sys_info_api.common.formatted_string_to_bytes)
  * [formatted\_string\_to\_bits](#sys_info_api.common.formatted_string_to_bits)
  * [bytes\_to\_formatted\_string](#sys_info_api.common.bytes_to_formatted_string)
* [sys\_info\_api.common.enums](#sys_info_api.common.enums)
* [sys\_info\_api.common.bin\_collector\_test](#sys_info_api.common.bin_collector_test)
  * [BinCollectorTest](#sys_info_api.common.bin_collector_test.BinCollectorTest)
    * [get\_test\_keys](#sys_info_api.common.bin_collector_test.BinCollectorTest.get_test_keys)
    * [generate\_raw\_data](#sys_info_api.common.bin_collector_test.BinCollectorTest.generate_raw_data)
    * [generate\_test\_data](#sys_info_api.common.bin_collector_test.BinCollectorTest.generate_test_data)
    * [load\_raw\_data](#sys_info_api.common.bin_collector_test.BinCollectorTest.load_raw_data)
    * [verify\_test\_data](#sys_info_api.common.bin_collector_test.BinCollectorTest.verify_test_data)
* [sys\_info\_api.common.key\_value\_parser](#sys_info_api.common.key_value_parser)
  * [KeyValueParser](#sys_info_api.common.key_value_parser.KeyValueParser)
    * [\_\_init\_\_](#sys_info_api.common.key_value_parser.KeyValueParser.__init__)
    * [set\_opts](#sys_info_api.common.key_value_parser.KeyValueParser.set_opts)
    * [to\_dict](#sys_info_api.common.key_value_parser.KeyValueParser.to_dict)
* [sys\_info\_api.collectors.bin.arp](#sys_info_api.collectors.bin.arp)
  * [Arp](#sys_info_api.collectors.bin.arp.Arp)
    * [\_\_init\_\_](#sys_info_api.collectors.bin.arp.Arp.__init__)
    * [get\_data](#sys_info_api.collectors.bin.arp.Arp.get_data)
    * [get\_ips](#sys_info_api.collectors.bin.arp.Arp.get_ips)
    * [get\_ips\_on](#sys_info_api.collectors.bin.arp.Arp.get_ips_on)

<a id="sys_info_api"></a>

# sys\_info\_api

<a id="sys_info_api.bin.generate_test_data"></a>

# sys\_info\_api.bin.generate\_test\_data

<a id="sys_info_api.common.bin_collector"></a>

# sys\_info\_api.common.bin\_collector

<a id="sys_info_api.common.bin_collector.BinCollector"></a>

## BinCollector Objects

```python
class BinCollector()
```

Base class for collectors that run a binary command and parse the output.

<a id="sys_info_api.common.bin_collector.BinCollector.PARSER_JSON"></a>

#### PARSER\_JSON

Use JSON to parse the output

<a id="sys_info_api.common.bin_collector.BinCollector.PARSER_RAW"></a>

#### PARSER\_RAW

Do not parse the output at all, just directly use from raw output

<a id="sys_info_api.common.bin_collector.BinCollector.PARSER_LINES"></a>

#### PARSER\_LINES

Split lines from the output

<a id="sys_info_api.common.bin_collector.BinCollector.PARSER_LINES_KEY_VALUE"></a>

#### PARSER\_LINES\_KEY\_VALUE

Split lines from output and convert to a dictionary via key/value pairs

<a id="sys_info_api.common.bin_collector.BinCollector.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

When initializing a new binary collector, set the following arguments:

- self.bin: The binary to run
- self.arguments: A list of arguments to pass to the binary
- self.parser: The parser to use for handling the output

<a id="sys_info_api.common.bin_collector.BinCollector.fetch"></a>

#### fetch

```python
def fetch()
```

Run the binary and store the output
:throws MetricNotAvailable:

<a id="sys_info_api.common.bin_collector.BinCollector.run"></a>

#### run

```python
def run(arguments: [str]) -> str
```

Run the binary with the given arguments and return the output

Does NOT store the output, (useful for one-off commands)

**Arguments**:

- `arguments`: 

**Raises**:

- `MetricNotAvailable`: 

<a id="sys_info_api.common.bin_collector.BinCollector.parse"></a>

#### parse

```python
def parse()
```

Parse the raw output into a usable format
:throws MetricNotAvailable:

<a id="sys_info_api.common.bin_collector.BinCollector.clear"></a>

#### clear

```python
def clear()
```

Clear the raw and parsed data, allowing for multiple functions on the same binary
or manual re-fetching of data.

<a id="sys_info_api.common.bin_collector.BinCollector.ensure_ready"></a>

#### ensure\_ready

```python
def ensure_ready()
```

Ensure that the data is ready for use, (safe to call multiple times)

<a id="sys_info_api.common.cmd"></a>

# sys\_info\_api.common.cmd

<a id="sys_info_api.common.cmd.CmdExecException"></a>

## CmdExecException Objects

```python
class CmdExecException(BaseException)
```

Base command execution exception

<a id="sys_info_api.common.cmd.CmdExecExitCodeException"></a>

## CmdExecExitCodeException Objects

```python
class CmdExecExitCodeException(CmdExecException)
```

Thrown if the command exit code wasn't good

<a id="sys_info_api.common.cmd.CmdExecNotFoundException"></a>

## CmdExecNotFoundException Objects

```python
class CmdExecNotFoundException(CmdExecException)
```

Thrown if the command could not be located

<a id="sys_info_api.common.cmd.run_passthru"></a>

#### run\_passthru

```python
def run_passthru(cmd: list, input=None, env=None)
```

Run a command and pass stdout and stderr directly to appropriate streams

Throws CmdExecException

**Arguments**:

- `cmd`: The parameters of the call to execute

**Raises**:

- `CmdExecExitCodeException`: If the process returns an exit code other than 0
- `CmdExecNotFoundException`: If the binary was not found on the system

<a id="sys_info_api.common.cmd.run_output"></a>

#### run\_output

```python
def run_output(cmd: list) -> str
```

Run a command and pass stderr to the log, while capturing stdout

Throws all exceptions from command

Will encode the output to UTF-8 and trim any newlines and whitespace

**Arguments**:

- `cmd`: The parameters of the call to execute

**Raises**:

- `CmdExecExitCodeException`: If the process returns an exit code other than 0
- `CmdExecNotFoundException`: If the binary was not found on the system

**Returns**:

The output from the command

<a id="sys_info_api.common.cmd.run_binary"></a>

#### run\_binary

```python
def run_binary(cmd: list) -> bytes
```

Run a command and pass stderr to the log, while capturing stdout as its raw binary output

Throws all exceptions from command

**Arguments**:

- `cmd`: The parameters of the call to execute

**Raises**:

- `CmdExecExitCodeException`: If the process returns an exit code other than 0
- `CmdExecNotFoundException`: If the binary was not found on the system

**Returns**:

The output from the command

<a id="sys_info_api.common.cmd.run_returncode"></a>

#### run\_returncode

```python
def run_returncode(cmd: list) -> int
```

Run a command and pass stderr to the log, ignoring output, and return the returncode

Throws command not found exceptions

**Arguments**:

- `cmd`: The parameters of the call to execute

**Raises**:

- `CmdExecNotFoundException`: If the binary was not found on the system

**Returns**:

The exit returncode from the command

<a id="sys_info_api.common.cmd.check_binary_exists"></a>

#### check\_binary\_exists

```python
def check_binary_exists(cmd: str) -> bool
```

Check if a binary exists in the path

**Arguments**:

- `cmd`: 

<a id="sys_info_api.common.exceptions"></a>

# sys\_info\_api.common.exceptions

<a id="sys_info_api.common.exceptions.MetricNotAvailable"></a>

## MetricNotAvailable Objects

```python
class MetricNotAvailable(BaseException)
```

General exception thrown when a metric is not available

Usually used to encompass various things like FileNotFound or cmd exceptions.

<a id="sys_info_api.common.local_timezone"></a>

# sys\_info\_api.common.local\_timezone

<a id="sys_info_api.common"></a>

# sys\_info\_api.common

<a id="sys_info_api.common.print_error"></a>

#### print\_error

```python
def print_error(string)
```

Simple method to write out an error message to STDERR.

This will be available to the retrieving server but will not interfere with the standard output!

<a id="sys_info_api.common.print_warning"></a>

#### print\_warning

```python
def print_warning(string)
```

Simple method to write out a warning message to STDERR.

This will be available to the retrieving server but will not interfere with the standard output!

<a id="sys_info_api.common.str_to_utc"></a>

#### str\_to\_utc

```python
def str_to_utc(date_value: str, format: str) -> datetime.datetime
```

Similar to datetime.strptime, but will auto convert to UTC.

**Arguments**:

- `date_value`: 
- `format`: 

<a id="sys_info_api.common.date_to_epoch"></a>

#### date\_to\_epoch

```python
def date_to_epoch(date: datetime.datetime) -> int
```

Retrieve the time in UTC epoch of a given date.

This will return an int representing the number of seconds since Jan 1, 1970 UTC.

<a id="sys_info_api.common.formatted_string_to_bytes"></a>

#### formatted\_string\_to\_bytes

```python
def formatted_string_to_bytes(value: str) -> int
```

Convert a string of bytes to the actual number of bytes included.

Supports suffixes for "k/K/M/G/T/P/E/Z/Y/R/Q"

Assume that byte values are Gibi/Tebi/etc and not actually Giga/Tera/etc.
Technically "1 PB" is different than "1 PiB", but most output of PB lazily just means PiB.
These values are calculated in Base2.

Assume that speed values are actually Giga/Tera/etc, and thus calculated in Base10.

<a id="sys_info_api.common.formatted_string_to_bits"></a>

#### formatted\_string\_to\_bits

```python
def formatted_string_to_bits(value: str) -> int
```

Convert a string of bits to the actual number of bits included.

Supports suffixes for "k/K/M/G/T/P/E/Z/Y/R/Q"

Assume that bit values are Gibi/Tebi/etc and not actually Giga/Tera/etc.
Technically "1 Pb" is different than "1 Pib", but most output of Pb lazily just means Pib.
These values are calculated in Base2.

Assume that speed values are actually Giga/Tera/etc, and thus calculated in Base10.

<a id="sys_info_api.common.bytes_to_formatted_string"></a>

#### bytes\_to\_formatted\_string

```python
def bytes_to_formatted_string(value: int, decimals: int = 2) -> str
```

Convert bytes to a formatted string

<a id="sys_info_api.common.enums"></a>

# sys\_info\_api.common.enums

<a id="sys_info_api.common.bin_collector_test"></a>

# sys\_info\_api.common.bin\_collector\_test

<a id="sys_info_api.common.bin_collector_test.BinCollectorTest"></a>

## BinCollectorTest Objects

```python
class BinCollectorTest(TestCase)
```

Base class for collector tests for binary commands.

<a id="sys_info_api.common.bin_collector_test.BinCollectorTest.get_test_keys"></a>

#### get\_test\_keys

```python
def get_test_keys() -> dict
```

Get the keys in the data of this collector that are testable


<a id="sys_info_api.common.bin_collector_test.BinCollectorTest.generate_raw_data"></a>

#### generate\_raw\_data

```python
def generate_raw_data() -> str
```

Dump the raw data pulled from the underlying collector


<a id="sys_info_api.common.bin_collector_test.BinCollectorTest.generate_test_data"></a>

#### generate\_test\_data

```python
def generate_test_data() -> dict
```

Dump the test data generated based on the underlying collector


<a id="sys_info_api.common.bin_collector_test.BinCollectorTest.load_raw_data"></a>

#### load\_raw\_data

```python
def load_raw_data(data: str)
```

Load raw data into this collector (useful for testing)

**Arguments**:

- `data`: 

<a id="sys_info_api.common.bin_collector_test.BinCollectorTest.verify_test_data"></a>

#### verify\_test\_data

```python
def verify_test_data(data: dict)
```

Verify test data against the underlying collector

**Arguments**:

- `data`: 

<a id="sys_info_api.common.key_value_parser"></a>

# sys\_info\_api.common.key\_value\_parser

<a id="sys_info_api.common.key_value_parser.KeyValueParser"></a>

## KeyValueParser Objects

```python
class KeyValueParser()
```

A simple key/value parser for parsing key/value pairs from a string.

<a id="sys_info_api.common.key_value_parser.KeyValueParser.__init__"></a>

#### \_\_init\_\_

```python
def __init__(sep=":", linebreak="\n", comment=None, quotes='auto')
```

**Raises**:

- `ValueError`: 

<a id="sys_info_api.common.key_value_parser.KeyValueParser.set_opts"></a>

#### set\_opts

```python
def set_opts(options: dict)
```

Set the options for the parser.

**Arguments**:

- `options` (`dict`): The options to set

<a id="sys_info_api.common.key_value_parser.KeyValueParser.to_dict"></a>

#### to\_dict

```python
def to_dict(raw: str) -> dict
```

Parse the raw string into a dictionary of key/value pairs.

**Arguments**:

- `raw` (`str`): The raw string to parse

**Returns**:

`dict`: A dictionary of key/value pairs

<a id="sys_info_api.collectors.bin.arp"></a>

# sys\_info\_api.collectors.bin.arp

<a id="sys_info_api.collectors.bin.arp.Arp"></a>

## Arp Objects

```python
class Arp(BinCollector)
```

<a id="sys_info_api.collectors.bin.arp.Arp.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

**Raises**:

- `MetricNotAvailable`: 

<a id="sys_info_api.collectors.bin.arp.Arp.get_data"></a>

#### get\_data

```python
def get_data() -> List[dict]
```

Get the neighbors as a list of dictionaries

**Raises**:

- `MetricNotAvailable`: 

<a id="sys_info_api.collectors.bin.arp.Arp.get_ips"></a>

#### get\_ips

```python
def get_ips() -> List[str]
```

Get the list of IP addresses

**Raises**:

- `MetricNotAvailable`: 

<a id="sys_info_api.collectors.bin.arp.Arp.get_ips_on"></a>

#### get\_ips\_on

```python
def get_ips_on(iface: str) -> List[str]
```

Get the list of IP addresses on a specific interface

**Raises**:

- `MetricNotAvailable`: 

