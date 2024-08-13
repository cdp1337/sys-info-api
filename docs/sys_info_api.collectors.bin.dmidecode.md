<!-- markdownlint-disable -->

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module:</kbd> `sys_info_api.collectors.bin.dmidecode`






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiSection`




<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__(type: str)
```








---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L134"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiBaseboard`




<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L136"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```








---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L171"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_asset_tag`

```python
get_asset_tag() → str
```

Retrieve the baseboard-asset-tag from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L139"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_manufacturer`

```python
get_manufacturer() → str
```

Retrieve the baseboard-manufacturer from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L147"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_product_name`

```python
get_product_name() → str
```

Retrieve the baseboard-product-name from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L163"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_serial_number`

```python
get_serial_number() → str
```

Retrieve the baseboard-serial-number from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L155"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_version`

```python
get_version() → str
```

Retrieve the baseboard-version from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L180"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiBios`




<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L181"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```








---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L200"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_release_date`

```python
get_release_date() → <method 'date' of 'datetime' objects>
```

:returns str: BIOS/UEFI release date 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L184"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_vendor`

```python
get_vendor() → str
```

:returns str: BIOS/UEFI vendor name 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L192"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_version`

```python
get_version() → str
```

:returns str: BIOS/UEFI version 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L210"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiCache`




<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L211"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```








---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L214"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_l1_size`

```python
get_l1_size() → int
```

:returns int: L1 cache size in bytes 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L226"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_l2_size`

```python
get_l2_size() → int
```

:returns int: L1 cache size in bytes 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L238"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_l3_size`

```python
get_l3_size() → int
```

:returns int: L1 cache size in bytes 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L251"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiChassis`




<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L252"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```








---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L287"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_asset_tag`

```python
get_asset_tag() → str
```

Retrieve the chassis-asset-tag from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L255"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_manufacturer`

```python
get_manufacturer() → str
```

Retrieve the chassis-manufacturer from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L279"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_serial_number`

```python
get_serial_number() → str
```

Retrieve the chassis-serial-number from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L263"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_type`

```python
get_type() → str
```

Retrieve the chassis-type from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L271"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_version`

```python
get_version() → str
```

Retrieve the chassis-version from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L308"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiMemory`




<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L309"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```








---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L428"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_asset`

```python
get_asset(module: int) → str
```

Get memory asset tag :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L372"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_form_factor`

```python
get_form_factor(module: int) → str
```

Get memory form factor :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L380"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_locator`

```python
get_locator(module: int) → str
```

Get memory socket / location :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L412"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_manufacturer`

```python
get_manufacturer(module: int) → str
```

Get memory manufacturer :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L404"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_max_speed`

```python
get_max_speed(module: int) → int
```

Get memory speed, usually with MT/s units :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L436"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_part`

```python
get_part(module: int) → str
```

Get memory part number :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L420"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_serial`

```python
get_serial(module: int) → str
```

Get memory serial number :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L364"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_size`

```python
get_size(module: int) → int
```

Get memory size, in bytes :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L396"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_speed`

```python
get_speed(module: int) → int
```

Get memory speed, usually with MT/s units :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L322"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_system_ecc`

```python
get_system_ecc() → bool
```

Get if ECC is supported by the controller :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L330"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_system_maximum_capacity`

```python
get_system_maximum_capacity() → int
```

Get the maximum memory capacity, in bytes :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L312"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_total_banks`

```python
get_total_banks() → int
```

Get total number of memory banks on the system 

Will return both empty and occupied slots 

:return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L388"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_type`

```python
get_type(module: int) → str
```

Get memory type :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L444"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_voltage`

```python
get_voltage(module: int) → float
```

Get memory voltage, will pull from system is individual memory voltage not available :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L342"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_width`

```python
get_width(module: int) → int
```

Get memory width, in units of number of bits :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L356"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `is_installed`

```python
is_installed(module: int) → bool
```

Check if memory is installed in a given bank :param module: :return: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L453"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiProcessor`




<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L454"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```








---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L592"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_asset_tag`

```python
get_asset_tag(processor: int = 0) → str
```

:param processor: :return: 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L612"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_cores`

```python
get_cores(processor: int = 0) → int
```

:param processor: :return: 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L493"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_family`

```python
get_family(processor: int = 0) → str
```

Retrieve the processor-family from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L509"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_flags`

```python
get_flags(processor: int = 0) → list
```

:param processor: :return list: 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L541"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_frequency`

```python
get_frequency(processor: int = 0) → int
```

Retrieve the processor-frequency from DMI 

:return int: Current speed of the processor in MHz 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L501"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_manufacturer`

```python
get_manufacturer(processor: int = 0) → str
```

Retrieve the processor-manufacturer from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L552"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_max_frequency`

```python
get_max_frequency(processor: int = 0) → int
```

Retrieve the processor-frequency from DMI 

:return int: Maximum speed of the processor in MHz 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L524"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_model`

```python
get_model(processor: int = 0) → str
```

Retrieve the processor-version from DMI 

:raises KeyError: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L602"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_part_number`

```python
get_part_number(processor: int = 0) → str
```

:param processor: :return: 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L582"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_serial_number`

```python
get_serial_number(processor: int = 0) → str
```

:param processor: :return: 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L487"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_socket`

```python
get_socket(processor: int = 0) → str
```

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L572"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_socket_type`

```python
get_socket_type(processor: int = 0) → str
```

:param processor: :return: 

:raises KeyError: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L562"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_status`

```python
get_status(processor: int = 0) → str
```

:param processor: :return: 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L622"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_threads`

```python
get_threads(processor: int = 0) → int
```

:param processor: :return: 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L465"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_total_cores`

```python
get_total_cores() → int
```

:return int: The total number of cores detected across all processors 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L457"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_total_count`

```python
get_total_count() → int
```

:return int: The total number of processors detected 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L476"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_total_threads`

```python
get_total_threads() → int
```

:return int: The total number of threads detected across all processors 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L532"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_voltage`

```python
get_voltage(processor: int = 0) → float
```

:param processor: :return: 

:raises KeyError: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L645"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiSystem`




<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L646"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__()
```








---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L689"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_family`

```python
get_family() → str
```

Retrieve the system-family from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L649"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_manufacturer`

```python
get_manufacturer() → str
```

Retrieve the system-manufacturer from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L657"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_product_name`

```python
get_product_name() → str
```

Retrieve the system-product-name from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L673"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_serial_number`

```python
get_serial_number() → str
```

Retrieve the system-serial-number from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L681"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_uuid`

```python
get_uuid() → str
```

Retrieve the system-uuid from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L665"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_version`

```python
get_version() → str
```

Retrieve the system-version from DMI 

:raises MetricNotAvailable: 

---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `parse`

```python
parse()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L698"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiBaseboardTest`







---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L702"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_test_keys`

```python
get_test_keys() → dict
```





---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L699"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L714"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiBiosTest`







---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L718"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_test_keys`

```python
get_test_keys() → dict
```





---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L715"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L728"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiCacheTest`







---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L732"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_test_keys`

```python
get_test_keys() → dict
```





---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L729"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L742"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiChassisTest`







---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L746"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_test_keys`

```python
get_test_keys() → dict
```





---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L743"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L758"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiMemoryTest`







---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L762"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_test_keys`

```python
get_test_keys() → dict
```





---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L759"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L783"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiProcessorTest`







---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L787"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_test_keys`

```python
get_test_keys() → dict
```





---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L784"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```






---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L815"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `DmiSystemTest`







---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L819"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `get_test_keys`

```python
get_test_keys() → dict
```





---

<a href="../src/sys_info_api/collectors/bin/dmidecode.py#L816"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `setUp`

```python
setUp()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
