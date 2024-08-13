<!-- markdownlint-disable -->

<a href="../src/sys_info_api/collectors/bin/apt.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module:</kbd> `sys_info_api.collectors.bin.apt`






---

<a href="../src/sys_info_api/collectors/bin/apt.py#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `AptUpdates`




<a href="../src/sys_info_api/collectors/bin/apt.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```








---

<a href="../src/sys_info_api/collectors/bin/apt.py#L55"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `fetch`

```python
fetch()
```





---

<a href="../src/sys_info_api/collectors/bin/apt.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_data`

```python
get_data() → list
```





---

<a href="../src/sys_info_api/collectors/bin/apt.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_package_by_name`

```python
get_package_by_name(name: str) → dict
```





---

<a href="../src/sys_info_api/collectors/bin/apt.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_package_names`

```python
get_package_names() → List[str]
```





---

<a href="../src/sys_info_api/collectors/bin/apt.py#L60"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/apt.py#L100"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `AptShow`




<a href="../src/sys_info_api/collectors/bin/apt.py#L101"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__(package: str)
```








---

<a href="../src/sys_info_api/collectors/bin/apt.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_data`

```python
get_data() → list
```





---

<a href="../src/sys_info_api/collectors/bin/apt.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_package_by_name`

```python
get_package_by_name(name: str) → dict
```





---

<a href="../src/sys_info_api/collectors/bin/apt.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_package_names`

```python
get_package_names() → List[str]
```





---

<a href="../src/sys_info_api/collectors/bin/apt.py#L107"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/apt.py#L136"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `AptInstall`
Install packages using apt-get 

Compatibility: 

![Debian](images/icons/debian.svg) ![Ubuntu](images/icons/ubuntu.svg) 

<a href="../src/sys_info_api/collectors/bin/apt.py#L145"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```








---

<a href="../src/sys_info_api/collectors/bin/apt.py#L178"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `install_package`

```python
install_package(package: str)
```

Install a package using apt-get :param package: The package to install 

Usage: 

```python
from sys_info_api.collectors.bin.apt import AptInstall
AptInstall().install_package('package1')
``` 

Package string formats: 

* 'name-of-package' -- Installs the latest version, guessing architecture * 'name-of-package=version' -- Install a specific version, guessing architecture * 'name-of-package:arch=version' -- Install a specific version and architecture 

---

<a href="../src/sys_info_api/collectors/bin/apt.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `install_packages`

```python
install_packages(packages: [<class 'str'>])
```

Install a set of packages using apt-get :param packages: The packages to install 

Usage: 

```python
from sys_info_api.collectors.bin.apt import AptInstall
AptInstall().install_packages(['package1', 'package2'])
``` 

Package string formats: 

* 'name-of-package' -- Installs the latest version, guessing architecture * 'name-of-package=version' -- Install a specific version, guessing architecture * 'name-of-package:arch=version' -- Install a specific version and architecture 


---

<a href="../src/sys_info_api/collectors/bin/apt.py#L199"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `AptUpdatesTest`







---

<a href="../src/sys_info_api/collectors/bin/apt.py#L200"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```






---

<a href="../src/sys_info_api/collectors/bin/apt.py#L207"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `AptShowTest`







---

<a href="../src/sys_info_api/collectors/bin/apt.py#L208"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp(package: str)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
