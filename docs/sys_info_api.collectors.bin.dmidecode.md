<!-- markdownlint-disable -->

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module:</kbd> `sys_info_api.collectors.bin.dmidecode`






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiSection`




<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__(type: str)
```








---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L135"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiBaseboard`




<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L137"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```








---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L172"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_asset_tag`

```python
get_asset_tag() → str
```

Retrieve the baseboard-asset-tag from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L140"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_manufacturer`

```python
get_manufacturer() → str
```

Retrieve the baseboard-manufacturer from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L148"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_product_name`

```python
get_product_name() → str
```

Retrieve the baseboard-product-name from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L164"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_serial_number`

```python
get_serial_number() → str
```

Retrieve the baseboard-serial-number from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L156"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_version`

```python
get_version() → str
```

Retrieve the baseboard-version from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L181"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiBios`




<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L182"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```








---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L201"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_release_date`

```python
get_release_date() → <method 'date' of 'datetime' objects>
```

:returns str: BIOS/UEFI release date 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L185"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_vendor`

```python
get_vendor() → str
```

:returns str: BIOS/UEFI vendor name 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L193"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_version`

```python
get_version() → str
```

:returns str: BIOS/UEFI version 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L211"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiCache`




<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L212"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```








---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L215"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_l1_size`

```python
get_l1_size() → int
```

:returns int: L1 cache size in bytes 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L227"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_l2_size`

```python
get_l2_size() → int
```

:returns int: L1 cache size in bytes 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L239"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_l3_size`

```python
get_l3_size() → int
```

:returns int: L1 cache size in bytes 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L252"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiChassis`




<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L253"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```








---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L288"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_asset_tag`

```python
get_asset_tag() → str
```

Retrieve the chassis-asset-tag from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L256"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_manufacturer`

```python
get_manufacturer() → str
```

Retrieve the chassis-manufacturer from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L280"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_serial_number`

```python
get_serial_number() → str
```

Retrieve the chassis-serial-number from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L264"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_type`

```python
get_type() → str
```

Retrieve the chassis-type from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L272"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_version`

```python
get_version() → str
```

Retrieve the chassis-version from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L309"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiMemory`




<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L310"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```








---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L427"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_asset`

```python
get_asset(module: int) → str
```

Get memory asset tag :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L371"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_form_factor`

```python
get_form_factor(module: int) → str
```

Get memory form factor :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L379"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_locator`

```python
get_locator(module: int) → str
```

Get memory socket / location :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L411"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_manufacturer`

```python
get_manufacturer(module: int) → str
```

Get memory manufacturer :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L403"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_max_speed`

```python
get_max_speed(module: int) → int
```

Get memory speed, usually with MT/s units :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L435"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_part`

```python
get_part(module: int) → str
```

Get memory part number :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L419"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_serial`

```python
get_serial(module: int) → str
```

Get memory serial number :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L363"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_size`

```python
get_size(module: int) → int
```

Get memory size, in bytes :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L395"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_speed`

```python
get_speed(module: int) → int
```

Get memory speed, usually with MT/s units :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L323"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_system_ecc`

```python
get_system_ecc() → bool
```

Get if ECC is supported by the controller :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L331"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_system_maximum_capacity`

```python
get_system_maximum_capacity() → int
```

Get the maximum memory capacity, in bytes :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L313"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_total_banks`

```python
get_total_banks() → int
```

Get total number of memory banks on the system 

Will return both empty and occupied slots 

:return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L387"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_type`

```python
get_type(module: int) → str
```

Get memory type :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L443"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_voltage`

```python
get_voltage(module: int) → float
```

Get memory voltage, will pull from system is individual memory voltage not available :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L343"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_width`

```python
get_width(module: int) → int
```

Get memory width, in units of number of bits :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L355"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `is_installed`

```python
is_installed(module: int) → bool
```

Check if memory is installed in a given bank :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L452"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiProcessor`




<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L453"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```








---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L591"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_asset_tag`

```python
get_asset_tag(processor: int = 0) → str
```

:param processor: :return: 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L611"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_cores`

```python
get_cores(processor: int = 0) → int
```

:param processor: :return: 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L492"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_family`

```python
get_family(processor: int = 0) → str
```

Retrieve the processor-family from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L508"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_flags`

```python
get_flags(processor: int = 0) → list
```

:param processor: :return list: 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L540"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_frequency`

```python
get_frequency(processor: int = 0) → int
```

Retrieve the processor-frequency from DMI 

:return int: Current speed of the processor in MHz 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L500"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_manufacturer`

```python
get_manufacturer(processor: int = 0) → str
```

Retrieve the processor-manufacturer from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L551"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_max_frequency`

```python
get_max_frequency(processor: int = 0) → int
```

Retrieve the processor-frequency from DMI 

:return int: Maximum speed of the processor in MHz 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L523"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_model`

```python
get_model(processor: int = 0) → str
```

Retrieve the processor-version from DMI 

:raises KeyError: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L601"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_part_number`

```python
get_part_number(processor: int = 0) → str
```

:param processor: :return: 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L581"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_serial_number`

```python
get_serial_number(processor: int = 0) → str
```

:param processor: :return: 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L486"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_socket`

```python
get_socket(processor: int = 0) → str
```

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L571"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_socket_type`

```python
get_socket_type(processor: int = 0) → str
```

:param processor: :return: 

:raises KeyError: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L561"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_status`

```python
get_status(processor: int = 0) → str
```

:param processor: :return: 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L621"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_threads`

```python
get_threads(processor: int = 0) → int
```

:param processor: :return: 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L464"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_total_cores`

```python
get_total_cores() → int
```

:return int: The total number of cores detected across all processors 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L456"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_total_count`

```python
get_total_count() → int
```

:return int: The total number of processors detected 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L475"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_total_threads`

```python
get_total_threads() → int
```

:return int: The total number of threads detected across all processors 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L531"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_voltage`

```python
get_voltage(processor: int = 0) → float
```

:param processor: :return: 

:raises KeyError: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L644"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiSystem`




<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L645"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```








---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L688"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_family`

```python
get_family() → str
```

Retrieve the system-family from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L648"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_manufacturer`

```python
get_manufacturer() → str
```

Retrieve the system-manufacturer from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L656"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_product_name`

```python
get_product_name() → str
```

Retrieve the system-product-name from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L672"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_serial_number`

```python
get_serial_number() → str
```

Retrieve the system-serial-number from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L680"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_uuid`

```python
get_uuid() → str
```

Retrieve the system-uuid from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L664"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_version`

```python
get_version() → str
```

Retrieve the system-version from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L697"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiBaseboardTest`







---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L701"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_test_keys`

```python
get_test_keys() → dict
```





---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L698"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L713"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiBiosTest`







---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L717"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_test_keys`

```python
get_test_keys() → dict
```





---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L714"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L727"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiCacheTest`







---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L731"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_test_keys`

```python
get_test_keys() → dict
```





---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L728"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L741"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiChassisTest`







---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L745"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_test_keys`

```python
get_test_keys() → dict
```





---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L742"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L757"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiMemoryTest`







---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L761"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_test_keys`

```python
get_test_keys() → dict
```





---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L758"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L782"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiProcessorTest`







---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L786"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_test_keys`

```python
get_test_keys() → dict
```





---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L783"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L814"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiSystemTest`







---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L818"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_test_keys`

```python
get_test_keys() → dict
```





---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L815"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
