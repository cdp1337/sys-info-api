<!-- markdownlint-disable -->

<a href="../src/sys_info_api/common/bin_collector.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module:</kbd> `sys_info_api.common.bin_collector`






---

<a href="../src/sys_info_api/common/bin_collector.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `BinParser`
Parser layer for processing data, (usually from commands) 

<a href="../src/sys_info_api/common/bin_collector.py#L47"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```








---

<a href="../src/sys_info_api/common/bin_collector.py#L157"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `clear`

```python
clear()
```

Clear the raw and parsed data, allowing for multiple functions on the same binary or manual re-fetching of data. 

---

<a href="../src/sys_info_api/common/bin_collector.py#L165"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `ensure_ready`

```python
ensure_ready()
```

Ensure that the data is ready for use, (safe to call multiple times) 

---

<a href="../src/sys_info_api/common/bin_collector.py#L114"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```

Parse the raw output into a usable format :throws MetricNotAvailable: 


---

<a href="../src/sys_info_api/common/bin_collector.py#L173"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `BinCollector`
Base class for collectors that run a binary command and parse the output. 

<a href="../src/sys_info_api/common/bin_collector.py#L178"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```

When initializing a new binary collector, set the following arguments: 


- self.bin: The binary to run 
- self.arguments: A list of arguments to pass to the binary 
- self.parser: The parser to use for handling the output 




---

<a href="../src/sys_info_api/common/bin_collector.py#L157"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `clear`

```python
clear()
```

Clear the raw and parsed data, allowing for multiple functions on the same binary or manual re-fetching of data. 

---

<a href="../src/sys_info_api/common/bin_collector.py#L165"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `ensure_ready`

```python
ensure_ready()
```

Ensure that the data is ready for use, (safe to call multiple times) 

---

<a href="../src/sys_info_api/common/bin_collector.py#L206"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `fetch`

```python
fetch()
```

Run the binary and store the output :throws MetricNotAvailable: 

---

<a href="../src/sys_info_api/common/bin_collector.py#L239"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```

Parse the raw output into a usable format :throws MetricNotAvailable: 

---

<a href="../src/sys_info_api/common/bin_collector.py#L225"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `run`

```python
run(arguments: [<class 'str'>]) → str
```

Run the binary with the given arguments and return the output 

Does NOT store the output, (useful for one-off commands) :param arguments: :return: :raises MetricNotAvailable: 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
