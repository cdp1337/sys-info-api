<!-- markdownlint-disable -->

<a href="../src/sys_info_api/collectors/etc/version.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module:</kbd> `sys_info_api.collectors.etc.version`






---

<a href="../src/sys_info_api/collectors/etc/version.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `Version`




<a href="../src/sys_info_api/collectors/etc/version.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```








---

<a href="../src/sys_info_api/collectors/etc/version.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_name`

```python
get_name() → str
```

Get the appliance name from /etc/version 

When viewing managed appliances, the base OS is rarely wanted, so this will retrieve the appliance name instead 

:return: 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/etc/version.py#L54"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_version`

```python
get_version() → str
```

Get the appliance version from /etc/version 

When viewing managed appliances, the base OS is rarely wanted, so this will retrieve the appliance name instead 

:return: 

:raises MetricNotAvailable: 


---

<a href="../src/sys_info_api/collectors/etc/version.py#L75"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `VersionTest`







---

<a href="../src/sys_info_api/collectors/etc/version.py#L76"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
