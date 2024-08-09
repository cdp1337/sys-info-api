<!-- markdownlint-disable -->

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module:</kbd> `sys_info_api.collectors.bin.lsblk`






---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `Lsblk`




<a href="../src/sys_info_api/collectors/bin/lsblk.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```








---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L120"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_disk_hotplug`

```python
get_disk_hotplug(disk: str) → bool
```

:param disk: Disk name to lookup :return: :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L128"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_disk_model`

```python
get_disk_model(disk: str) → str
```

:param disk: Disk name to lookup :return: :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L80"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_disk_names`

```python
get_disk_names() → List[str]
```

:return list: List of disk names detected 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L117"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_disk_partitioning`

```python
get_disk_partitioning(disk: str) → str
```





---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_disk_path`

```python
get_disk_path(disk: str) → str
```

:param disk: Disk name to lookup :return: :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L176"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_disk_rev`

```python
get_disk_rev(disk: str) → str
```

:param disk: Disk name to lookup :return: :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L160"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_disk_rotational`

```python
get_disk_rotational(disk: str) → bool
```

:param disk: Disk name to lookup :return: :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L136"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_disk_serial`

```python
get_disk_serial(disk: str) → str
```

:param disk: Disk name to lookup :return: :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L144"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_disk_size`

```python
get_disk_size(disk: str) → int
```

:param disk: Disk name to lookup :return: :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L152"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_disk_state`

```python
get_disk_state(disk: str) → str
```

:param disk: Disk name to lookup :return: :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L168"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_disk_transport`

```python
get_disk_transport(disk: str) → str
```

:param disk: Disk name to lookup :return: :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L106"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_disk_uuid`

```python
get_disk_uuid(disk: str) → str
```

:param disk: Disk name to lookup :return: :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L184"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_disk_vendor`

```python
get_disk_vendor(disk: str) → str
```

:param disk: Disk name to lookup :return: :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L241"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_filesystem_label`

```python
get_filesystem_label(filesystem: str) → str
```





---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L248"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_filesystem_mount`

```python
get_filesystem_mount(filesystem: str) → str
```





---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L94"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_filesystem_names`

```python
get_filesystem_names() → List[str]
```





---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L227"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_filesystem_size`

```python
get_filesystem_size(filesystem: str) → int
```





---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L213"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_filesystem_type`

```python
get_filesystem_type(filesystem: str) → str
```





---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L234"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_filesystem_used`

```python
get_filesystem_used(filesystem: str) → int
```





---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L220"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_filesystem_version`

```python
get_filesystem_version(filesystem: str) → str
```





---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L90"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_partition_names`

```python
get_partition_names() → List[str]
```





---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L201"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_partition_path`

```python
get_partition_path(partition: str) → str
```





---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L209"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_partition_size`

```python
get_partition_size(partition: str) → int
```





---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L197"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_partition_type`

```python
get_partition_type(partition: str) → str
```





---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L205"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_partition_uuid`

```python
get_partition_uuid(partition: str) → str
```





---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L256"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `LsblkTest`







---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L260"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_test_keys`

```python
get_test_keys() → dict
```





---

<a href="../src/sys_info_api/collectors/bin/lsblk.py#L257"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
