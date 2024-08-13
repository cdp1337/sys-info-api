<!-- markdownlint-disable -->

<a href="../src/sys_info_api/collectors/etc/lsb_release.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module:</kbd> `sys_info_api.collectors.etc.lsb_release`






---

<a href="../src/sys_info_api/collectors/etc/lsb_release.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `LsbRelease`
Provides a simple API to read /etc/lsb-release or /etc/upstream-release/lsb-release data 

Compatibility: 

![Ubuntu](images/icons/ubuntu.svg) 

<a href="../src/sys_info_api/collectors/etc/lsb_release.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__(upstream=False)
```

:raises MetricNotAvailable: 




---

<a href="../src/sys_info_api/collectors/etc/lsb_release.py#L54"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_id`

```python
get_id() → str
```

A string identifying the operating system, without a version component, and suitable for presentation to the user. 

:return: :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/etc/lsb_release.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_version`

```python
get_version() → dict
```

Get the version as a dictionary of values 

A string identifying the operating system version, excluding any OS name information, possibly including a release code name, and suitable for presentation to the user. 

:return dict: 'major', 'minor' :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/etc/lsb_release.py#L107"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_version_codename`

```python
get_version_codename() → str
```

Get the codename of this OS version :return: str :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/etc/lsb_release.py#L90"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_version_string`

```python
get_version_string() → str
```

Get the full version string of this OS 

:raises MetricNotAvailable: 


---

<a href="../src/sys_info_api/collectors/etc/lsb_release.py#L116"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `LsbReleaseTest`







---

<a href="../src/sys_info_api/collectors/etc/lsb_release.py#L117"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
