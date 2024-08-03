<!-- markdownlint-disable -->

<a href="../src/sys_info_api/collectors/bin/arp.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `sys_info_api.collectors.bin.arp`






---

<a href="../src/sys_info_api/collectors/bin/arp.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Arp`
Execute `arp` to get the list of neighbors on the network. 

Compatibility: 

![Debian](images/icons/debian.svg) ![Fedora](images/icons/fedora.svg) ![Redhat](images/icons/redhat.svg) ![Rocky](images/icons/rocky.svg) ![Ubuntu](images/icons/ubuntu.svg) ![FreeBSD](images/icons/freebsd.svg) ![Ubuntu](images/icons/proxmox.svg) ![Ubuntu](images/icons/truenas.svg) 

<a href="../src/sys_info_api/collectors/bin/arp.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__()
```

:raises MetricNotAvailable: 




---

<a href="../src/sys_info_api/collectors/bin/arp.py#L84"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_data`

```python
get_data() → List[dict]
```

Get the neighbors as a list of dictionaries 



**Example:**
 

```yaml

- interface: enp6s0
ip: 10.200.0.115
mac: 9e:db:c1:43:4d:d3

- interface: enp6s0
ip: 10.200.0.204
mac: 50:5a:65:85:05:a9
``` 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/arp.py#L104"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_ips`

```python
get_ips() → List[str]
```

Get the list of IP addresses 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/arp.py#L113"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_ips_on`

```python
get_ips_on(iface: str) → List[str]
```

Get the list of IP addresses on a specific interface 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/arp.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/arp.py#L123"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ArpTest`







---

<a href="../src/sys_info_api/collectors/bin/arp.py#L127"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_test_keys`

```python
get_test_keys() → dict
```





---

<a href="../src/sys_info_api/collectors/bin/arp.py#L124"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `setUp`

```python
setUp()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
