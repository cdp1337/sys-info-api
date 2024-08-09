<!-- markdownlint-disable -->

<a href="../src/sys_info_api/collectors/bin/ip.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module:</kbd> `sys_info_api.collectors.bin.ip`






---

<a href="../src/sys_info_api/collectors/bin/ip.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `IPLink`
Gathers interface names from ip 

<a href="../src/sys_info_api/collectors/bin/ip.py#L27"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```

:raises MetricNotAvailable: 




---

<a href="../src/sys_info_api/collectors/bin/ip.py#L70"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_admin_statuses`

```python
get_admin_statuses() → dict
```

Get the administrative status of the interfaces :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/ip.py#L100"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_mac_addresses`

```python
get_mac_addresses() → dict
```

Get the status of the interfaces :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/ip.py#L62"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_names`

```python
get_names() → List[str]
```

Get a list of network interfaces present :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/ip.py#L90"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_status`

```python
get_status(iface: str) → str
```

Get the status of the given interface :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/ip.py#L80"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_statuses`

```python
get_statuses() → dict
```

Get the status of the interfaces :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/ip.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/ip.py#L111"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `IPLinkTest`







---

<a href="../src/sys_info_api/collectors/bin/ip.py#L112"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
