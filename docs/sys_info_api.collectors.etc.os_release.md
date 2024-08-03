<!-- markdownlint-disable -->

<a href="../src/sys_info_api/collectors/etc/os_release.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module:</kbd> `sys_info_api.collectors.etc.os_release`






---

<a href="../src/sys_info_api/collectors/etc/os_release.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `OsRelease`
Provides a simple API to read /etc/os-release data 

Compatibility: 

![Debian](images/icons/debian.svg) ![Fedora](images/icons/fedora.svg) ![Redhat](images/icons/redhat.svg) ![Rocky](images/icons/rocky.svg) ![Ubuntu](images/icons/ubuntu.svg) ![FreeBSD](images/icons/freebsd.svg) ![Ubuntu](images/icons/proxmox.svg) ![Ubuntu](images/icons/truenas.svg) 

@see https://www.man7.org/linux/man-pages/man5/os-release.5.html 

<a href="../src/sys_info_api/collectors/etc/os_release.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```

:raises MetricNotAvailable: 




---

<a href="../src/sys_info_api/collectors/etc/os_release.py#L139"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_id`

```python
get_id() → str
```





---

<a href="../src/sys_info_api/collectors/etc/os_release.py#L142"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_like`

```python
get_like() → list[str]
```

Get a list of "like" operating systems 

A lower-case string (no spaces or other characters outside of 0-9, a-z, ".", "_" and "-") identifying the operating system, excluding any version information and suitable for processing by scripts or usage in generated filenames. If not set, defaults to "ID=linux". Example: "ID=fedora" or "ID=debian". :return: 

---

<a href="../src/sys_info_api/collectors/etc/os_release.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_name`

```python
get_name() → str
```

A string identifying the operating system, without a version component, and suitable for presentation to the user. 

:return: :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/etc/os_release.py#L62"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_version`

```python
get_version() → dict
```

Get the version as a dictionary of values 

A string identifying the operating system version, excluding any OS name information, possibly including a release code name, and suitable for presentation to the user. 

:return dict: 'major', 'minor', 'point', 'modifier', 'release', 'codename' :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/etc/os_release.py#L131"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_version_codename`

```python
get_version_codename() → str
```

Get the codename of this OS version :return: str :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/etc/os_release.py#L108"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_version_string`

```python
get_version_string() → str
```

Get the full version string of this OS 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/etc/os_release.py#L164"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `like_os`

```python
like_os(name: str) → bool
```

Check if this OS is "like" the requested OS. 

This checks if it is a derivative, but also checks if the OS itself is what's being checked 

:param name: OS name to check, lowercase :return: If this appears to be the matching OS 


---

<a href="../src/sys_info_api/collectors/etc/os_release.py#L177"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `OsReleaseTest`







---

<a href="../src/sys_info_api/collectors/etc/os_release.py#L178"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
