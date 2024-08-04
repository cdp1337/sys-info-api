<!-- markdownlint-disable -->

<a href="../src/sys_info_api/collectors/bin/lldptool.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module:</kbd> `sys_info_api.collectors.bin.lldptool`






---

<a href="../src/sys_info_api/collectors/bin/lldptool.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `LldpStatus`




<a href="../src/sys_info_api/collectors/bin/lldptool.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__(iface: str)
```








---

<a href="../src/sys_info_api/collectors/bin/lldptool.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `enable_rx`

```python
enable_rx()
```

Enable receive for LLDP data on this interface :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/lldptool.py#L81"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `enable_tx`

```python
enable_tx()
```

Enable transmit for LLDP data on this interface :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/lldptool.py#L54"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_admin_status`

```python
get_admin_status() → str
```

Get the administrative status of LLDP on the given interface, or throws a MetricNotAvailable if unable to get status 

Returns "RX", "TX", "RXTX", or "DISABLED" :return: :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/lldptool.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/lldptool.py#L99"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `LldpNeighborScan`




<a href="../src/sys_info_api/collectors/bin/lldptool.py#L101"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__(iface: str)
```

Execute lldptool and scan for a neighboring interface :param iface: 




---

<a href="../src/sys_info_api/collectors/bin/lldptool.py#L212"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_chassis_id`

```python
get_chassis_id()
```

Get the chassis ID of the neighboring device :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/lldptool.py#L177"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_mac`

```python
get_mac()
```

Get the MAC address of the neighboring device :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/lldptool.py#L184"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_port_id`

```python
get_port_id()
```

Get the port ID of the neighboring device :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/lldptool.py#L191"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_port_name`

```python
get_port_name()
```

Get the port name of the neighboring device :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/lldptool.py#L205"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_system_description`

```python
get_system_description()
```

Get the system description of the neighboring device :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/lldptool.py#L198"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_system_name`

```python
get_system_name()
```

Get the system name of the neighboring device :raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/lldptool.py#L111"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/lldptool.py#L220"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `LldpStatusTest`







---

<a href="../src/sys_info_api/collectors/bin/lldptool.py#L224"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_test_keys`

```python
get_test_keys() → dict
```





---

<a href="../src/sys_info_api/collectors/bin/lldptool.py#L221"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp(iface='TEST')
```






---

<a href="../src/sys_info_api/collectors/bin/lldptool.py#L230"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `LldpNeighborScanTest`







---

<a href="../src/sys_info_api/collectors/bin/lldptool.py#L231"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp(iface='TEST')
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
