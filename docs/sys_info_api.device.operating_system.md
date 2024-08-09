<!-- markdownlint-disable -->

<a href="../src/sys_info_api/device/operating_system.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module:</kbd> `sys_info_api.device.operating_system`





---

<a href="../src/sys_info_api/device/operating_system.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_name`

```python
get_name() → str
```

Try to get the name of the device OS based on hints in /etc 


---

<a href="../src/sys_info_api/device/operating_system.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_version`

```python
get_version() → str
```

Try to get the name of the device OS based on hints in /etc 


---

<a href="../src/sys_info_api/device/operating_system.py#L94"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_arch`

```python
get_arch() → str
```

Get the architecture of this OS 


---

<a href="../src/sys_info_api/device/operating_system.py#L102"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_boottime`

```python
get_boottime() → Optional[datetime]
```






---

<a href="../src/sys_info_api/device/operating_system.py#L127"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_installed_software`

```python
get_installed_software()
```

Call the underlying OS's package manager to handle detection of installed software 


---

<a href="../src/sys_info_api/device/operating_system.py#L143"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_updates`

```python
get_updates() → List[dict]
```

Get any updates that are available 


---

<a href="../src/sys_info_api/device/operating_system.py#L158"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `like_os`

```python
like_os(family: str) → bool
```

Check if this operating system is "like" another 

Useful to see if this OS is "like Debian" or "like Red Hat" 

:param family: :return: 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
