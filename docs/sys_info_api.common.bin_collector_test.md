<!-- markdownlint-disable -->

<a href="../src/sys_info_api/common/bin_collector_test.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `sys_info_api.common.bin_collector_test`






---

<a href="../src/sys_info_api/common/bin_collector_test.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `BinCollectorTest`
Base class for collector tests for binary commands. 




---

<a href="../src/sys_info_api/common/bin_collector_test.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `generate_raw_data`

```python
generate_raw_data() → str
```

Dump the raw data pulled from the underlying collector :return: 

---

<a href="../src/sys_info_api/common/bin_collector_test.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `generate_test_data`

```python
generate_test_data() → dict
```

Dump the test data generated based on the underlying collector :return: 

---

<a href="../src/sys_info_api/common/bin_collector_test.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_test_keys`

```python
get_test_keys() → dict
```

Get the keys in the data of this collector that are testable :return: 

---

<a href="../src/sys_info_api/common/bin_collector_test.py#L77"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `load_raw_data`

```python
load_raw_data(data: str)
```

Load raw data into this collector (useful for testing) :param data: :return: 

---

<a href="../src/sys_info_api/common/bin_collector_test.py#L27"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `setUp`

```python
setUp()
```





---

<a href="../src/sys_info_api/common/bin_collector_test.py#L122"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `verify_test_data`

```python
verify_test_data(data: dict)
```

Verify test data against the underlying collector :param data: :return: 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
