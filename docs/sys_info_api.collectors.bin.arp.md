<!-- markdownlint-disable -->

<a href="../src/sys_info_api/collectors/bin/arp.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `sys_info_api.collectors.bin.arp`






---

<a href="../src/sys_info_api/collectors/bin/arp.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Arp`




<a href="../src/sys_info_api/collectors/bin/arp.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__()
```

:raises MetricNotAvailable: 




---

<a href="../src/sys_info_api/collectors/bin/arp.py#L76"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_data`

```python
get_data() → List[dict]
```

Get the neighbors as a list of dictionaries 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/arp.py#L85"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_ips`

```python
get_ips() → List[str]
```

Get the list of IP addresses 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/arp.py#L94"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_ips_on`

```python
get_ips_on(iface: str) → List[str]
```

Get the list of IP addresses on a specific interface 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/arp.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/arp.py#L104"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ArpTest`







---

<a href="../src/sys_info_api/collectors/bin/arp.py#L108"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_test_keys`

```python
get_test_keys() → dict
```





---

<a href="../src/sys_info_api/collectors/bin/arp.py#L105"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `setUp`

```python
setUp()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
