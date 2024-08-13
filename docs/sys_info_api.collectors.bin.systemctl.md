<!-- markdownlint-disable -->

<a href="../src/sys_info_api/collectors/bin/systemctl.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module:</kbd> `sys_info_api.collectors.bin.systemctl`






---

<a href="../src/sys_info_api/collectors/bin/systemctl.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `SystemCtlListServices`




<a href="../src/sys_info_api/collectors/bin/systemctl.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```








---

<a href="../src/sys_info_api/collectors/bin/systemctl.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_data`

```python
get_data() → list
```

Get the list of units and their statuses 

---

<a href="../src/sys_info_api/collectors/bin/systemctl.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/systemctl.py#L53"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `SystemCtlService`




<a href="../src/sys_info_api/collectors/bin/systemctl.py#L54"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__(service: str)
```








---

<a href="../src/sys_info_api/collectors/bin/systemctl.py#L77"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `disable`

```python
disable()
```

Disable the service 

---

<a href="../src/sys_info_api/collectors/bin/systemctl.py#L71"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `enable`

```python
enable()
```

Enable the service 

---

<a href="../src/sys_info_api/collectors/bin/systemctl.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_data`

```python
get_data() → dict
```

Get the status of a specific service 

---

<a href="../src/sys_info_api/collectors/bin/systemctl.py#L95"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `restart`

```python
restart()
```

Restart the service 

---

<a href="../src/sys_info_api/collectors/bin/systemctl.py#L83"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `start`

```python
start()
```

Start the service 

---

<a href="../src/sys_info_api/collectors/bin/systemctl.py#L89"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `stop`

```python
stop()
```

Stop the service 


---

<a href="../src/sys_info_api/collectors/bin/systemctl.py#L102"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `SystemCtlListServicesTest`







---

<a href="../src/sys_info_api/collectors/bin/systemctl.py#L103"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
