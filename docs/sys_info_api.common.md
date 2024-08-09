<!-- markdownlint-disable -->

<a href="../src/sys_info_api/common/__init__.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module:</kbd> `sys_info_api.common`




**Global Variables**
---------------
- **exceptions**
- **key_value_parser**: #  Copyright (c) 2024 Charlie Powell <cdp1337@veraciousnetwork.com>
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

- **cmd**: #  Copyright (c) 2024 Charlie Powell <cdp1337@veraciousnetwork.com>
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

- **bin_collector**: #  Copyright (c) 2024 Charlie Powell <cdp1337@veraciousnetwork.com>
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

- **bin_collector_test**: #  Copyright (c) 2024 Charlie Powell <cdp1337@veraciousnetwork.com>
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

- **enums**: #  Copyright (c) 2024 Charlie Powell <cdp1337@veraciousnetwork.com>
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


---

<a href="../src/sys_info_api/common/__init__.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `print_error`

```python
print_error(string)
```

Simple method to write out an error message to STDERR. 

This will be available to the retrieving server but will not interfere with the standard output! 


---

<a href="../src/sys_info_api/common/__init__.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `print_warning`

```python
print_warning(string)
```

Simple method to write out a warning message to STDERR. 

This will be available to the retrieving server but will not interfere with the standard output! 


---

<a href="../src/sys_info_api/common/__init__.py#L43"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `str_to_utc`

```python
str_to_utc(date_value: str, format: str) → datetime
```

Similar to datetime.strptime, but will auto convert to UTC. 

| Directive | Example                                               | Note                  | |-----------|-------------------------------------------------------|-----------------------| | %a        | Sun, Mon, …, Sat                                      | Day of week           | | %A        | Sunday, Monday, …, Saturday                           | Day of week           | | %w        | 0, 1, …, 6                                            | Day of week           | | %d        | 01, 02, …, 31                                         | Day of month          | | %b        | Jan, Feb, …, Dec                                      | Month                 | | %B        | January, February, …, December                        | Month                 | | %m        | 01, 02, …, 12                                         | Month                 | | %y        | 00, 01, …, 99                                         | Year                  | | %Y        | 0001, 0002, …, 2013, 2014, …, 9998, 9999              | Year                  | | %H        | 00, 01, …, 23                                         | Hour                  | | %I        | 01, 02, …, 12                                         | Hour (12-hour)        | | %p        | AM, PM                                                | AM/PM                 | | %M        | 00, 01, …, 59                                         | Minute                | | %S        | 00, 01, …, 59                                         | Seconds               | | %f        | 000000, 000001, …, 999999                             | Microseconds          | | %z        | (empty), +0000, -0400, +1030, +063415, -030712.345216 | Timezone Offset       | | %Z        | (empty), UTC, GMT                                     | Timezone Name         | | %j        | 001, 002, …, 366                                      | Day of year           | | %U        | 00, 01, …, 53                                         | Week of year (Sunday) | | %W        | 00, 01, …, 53                                         | Week of year (Monday) | | %c        | Tue Aug 16 21:30:00 1988                              | Locale date/time      | | %x        | 08/16/88                                              | Locale date           | | %X        | 21:30:00                                              | Locale time           | 

:param date_value: :param format: :return: 


---

<a href="../src/sys_info_api/common/__init__.py#L88"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `date_to_epoch`

```python
date_to_epoch(date: datetime) → int
```

Retrieve the time in UTC epoch of a given date. 

This will return an int representing the number of seconds since Jan 1, 1970 UTC. 


---

<a href="../src/sys_info_api/common/__init__.py#L102"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `formatted_string_to_bytes`

```python
formatted_string_to_bytes(value: str) → int
```

Convert a string of bytes to the actual number of bytes included. 

Supports suffixes for "k/K/M/G/T/P/E/Z/Y/R/Q" 

Assume that byte values are Gibi/Tebi/etc and not actually Giga/Tera/etc. Technically "1 PB" is different than "1 PiB", but most output of PB lazily just means PiB. These values are calculated in Base2. 

Assume that speed values are actually Giga/Tera/etc, and thus calculated in Base10. 


---

<a href="../src/sys_info_api/common/__init__.py#L157"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `formatted_string_to_bits`

```python
formatted_string_to_bits(value: str) → int
```

Convert a string of bits to the actual number of bits included. 

Supports suffixes for "k/K/M/G/T/P/E/Z/Y/R/Q" 

Assume that bit values are Gibi/Tebi/etc and not actually Giga/Tera/etc. Technically "1 Pb" is different than "1 Pib", but most output of Pb lazily just means Pib. These values are calculated in Base2. 

Assume that speed values are actually Giga/Tera/etc, and thus calculated in Base10. 


---

<a href="../src/sys_info_api/common/__init__.py#L223"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `bytes_to_formatted_string`

```python
bytes_to_formatted_string(value: int, decimals: int = 2) → str
```

Convert bytes to a formatted string 


---

<a href="../src/sys_info_api/common/__init__.py#L249"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `bps_to_formatted_string`

```python
bps_to_formatted_string(value: int) → str
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
