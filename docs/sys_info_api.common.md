<!-- markdownlint-disable -->

<a href="../src/sys_info_api/common/__init__.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `sys_info_api.common`





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

:param date_value: :param format: :return: 


---

<a href="../src/sys_info_api/common/__init__.py#L62"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `date_to_epoch`

```python
date_to_epoch(date: datetime) → int
```

Retrieve the time in UTC epoch of a given date. 

This will return an int representing the number of seconds since Jan 1, 1970 UTC. 


---

<a href="../src/sys_info_api/common/__init__.py#L76"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `formatted_string_to_bytes`

```python
formatted_string_to_bytes(value: str) → int
```

Convert a string of bytes to the actual number of bytes included. 

Supports suffixes for "k/K/M/G/T/P/E/Z/Y/R/Q" 

Assume that byte values are Gibi/Tebi/etc and not actually Giga/Tera/etc. Technically "1 PB" is different than "1 PiB", but most output of PB lazily just means PiB. These values are calculated in Base2. 

Assume that speed values are actually Giga/Tera/etc, and thus calculated in Base10. 


---

<a href="../src/sys_info_api/common/__init__.py#L131"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `formatted_string_to_bits`

```python
formatted_string_to_bits(value: str) → int
```

Convert a string of bits to the actual number of bits included. 

Supports suffixes for "k/K/M/G/T/P/E/Z/Y/R/Q" 

Assume that bit values are Gibi/Tebi/etc and not actually Giga/Tera/etc. Technically "1 Pb" is different than "1 Pib", but most output of Pb lazily just means Pib. These values are calculated in Base2. 

Assume that speed values are actually Giga/Tera/etc, and thus calculated in Base10. 


---

<a href="../src/sys_info_api/common/__init__.py#L197"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `bytes_to_formatted_string`

```python
bytes_to_formatted_string(value: int, decimals: int = 2) → str
```

Convert bytes to a formatted string 


---

<a href="../src/sys_info_api/common/__init__.py#L223"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `bps_to_formatted_string`

```python
bps_to_formatted_string(value: int) → str
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
