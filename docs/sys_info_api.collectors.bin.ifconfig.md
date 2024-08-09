<!-- markdownlint-disable -->

<a href="../src/sys_info_api/collectors/bin/ifconfig.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module:</kbd> `sys_info_api.collectors.bin.ifconfig`






---

<a href="../src/sys_info_api/collectors/bin/ifconfig.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `Ifconfig`
Collects information about network interfaces from the ifconfig command. 

<a href="../src/sys_info_api/collectors/bin/ifconfig.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```

:raises MetricNotAvailable: 




---

<a href="../src/sys_info_api/collectors/bin/ifconfig.py#L142"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_addresses`

```python
get_addresses(iface: str) → List[IP]
```





---

<a href="../src/sys_info_api/collectors/bin/ifconfig.py#L136"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_admin_status`

```python
get_admin_status(iface: str) → <enum 'NetStatus'>
```





---

<a href="../src/sys_info_api/collectors/bin/ifconfig.py#L130"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_mac`

```python
get_mac(iface: str) → str
```





---

<a href="../src/sys_info_api/collectors/bin/ifconfig.py#L127"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_mtu`

```python
get_mtu(iface: str) → int
```





---

<a href="../src/sys_info_api/collectors/bin/ifconfig.py#L116"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_names`

```python
get_names() → List[str]
```

Get a list of all interface names :return: 

---

<a href="../src/sys_info_api/collectors/bin/ifconfig.py#L124"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_slot`

```python
get_slot(iface: str) → str
```





---

<a href="../src/sys_info_api/collectors/bin/ifconfig.py#L133"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_status`

```python
get_status(iface: str) → <enum 'NetStatus'>
```





---

<a href="../src/sys_info_api/collectors/bin/ifconfig.py#L139"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_type`

```python
get_type(iface: str) → str
```





---

<a href="../src/sys_info_api/collectors/bin/ifconfig.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/ifconfig.py#L146"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `IfconfigTest`







---

<a href="../src/sys_info_api/collectors/bin/ifconfig.py#L167"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `generate_test_data`

```python
generate_test_data() → dict
```





---

<a href="../src/sys_info_api/collectors/bin/ifconfig.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_test_keys`

```python
get_test_keys() → dict
```





---

<a href="../src/sys_info_api/collectors/bin/ifconfig.py#L147"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
