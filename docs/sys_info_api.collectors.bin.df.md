<!-- markdownlint-disable -->

<a href="../src/sys_info_api/collectors/bin/df.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module:</kbd> `sys_info_api.collectors.bin.df`






---

<a href="../src/sys_info_api/collectors/bin/df.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `Df`
Execute `df` to get the list of filesystems. 

Compatibility: 

![Debian](images/icons/debian.svg) ![Fedora](images/icons/fedora.svg) ![Redhat](images/icons/redhat.svg) ![Rocky](images/icons/rocky.svg) ![Ubuntu](images/icons/ubuntu.svg) ![FreeBSD](images/icons/freebsd.svg) ![Ubuntu](images/icons/proxmox.svg) ![Ubuntu](images/icons/truenas.svg) 

<a href="../src/sys_info_api/collectors/bin/df.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```

:raises MetricNotAvailable: 




---

<a href="../src/sys_info_api/collectors/bin/df.py#L71"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_data`

```python
get_data() → List[dict]
```

Get the filesystems as a list of dictionaries 

Example Response: 

```yaml

- device: nvme0n1p2
format: ext4
free: 199701401600
label: /
total: 1869023645696
used: 1574305480704

- device: nvme0n1p1
format: vfat
free: 4982681600
label: /boot/efi
total: 4988796928
used: 6115328
``` 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/df.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/df.py#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DfTest`







---

<a href="../src/sys_info_api/collectors/bin/df.py#L99"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
