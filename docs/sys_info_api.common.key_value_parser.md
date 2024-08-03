<!-- markdownlint-disable -->

<a href="../src/sys_info_api/common/key_value_parser.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module:</kbd> `sys_info_api.common.key_value_parser`






---

<a href="../src/sys_info_api/common/key_value_parser.py#L15"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class:</kbd> `KeyValueParser`
A simple key/value parser for parsing key/value pairs from a string. 

<a href="../src/sys_info_api/common/key_value_parser.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `__init__`

```python
__init__(sep=':', linebreak='\n', comment=None, quotes='auto')
```

:raises ValueError: 




---

<a href="../src/sys_info_api/common/key_value_parser.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `set_opts`

```python
set_opts(options: dict)
```

Set the options for the parser. 

:param options: The options to set :type options: dict 

---

<a href="../src/sys_info_api/common/key_value_parser.py#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method:</kbd> `to_dict`

```python
to_dict(raw: str) → dict
```

Parse the raw string into a dictionary of key/value pairs. 

:param raw: The raw string to parse :type raw: str :return: A dictionary of key/value pairs :rtype: dict 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
