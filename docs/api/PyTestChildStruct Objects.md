## PyTestChildStruct Objects

```python
class PyTestChildStruct(PyTestStruct)
```

Struct to allow testing of inheritance on Python wrapped types.

**C++ Source:**

- **Plugin**: PythonScriptPlugin
- **Module**: PythonScriptPlugin
- **File**: PyTest.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bool`` (bool):  [Read-Write]
- ``bool_defaults_only`` (bool):  [Read-Write]
- ``bool_instance_only`` (bool):  [Read-Write]
- ``bool_mutable`` (bool):  [Read-Only]
- ``enum`` (PyTestEnum):  [Read-Write]
- ``field_path`` (FieldPath):  [Read-Write]
- ``float`` (float):  [Read-Write]
- ``int`` (int32):  [Read-Write]
- ``legacy_int`` (int32):  [Read-Write]
  deprecated: LegacyInt is deprecated. Please use Int instead.
- ``name`` (Name):  [Read-Write]
- ``string`` (str):  [Read-Write]
- ``string_array`` (Array[str]):  [Read-Write]
- ``string_int_map`` (Map[str, int32]):  [Read-Write]
- ``string_set`` (Set[str]):  [Read-Write]
- ``struct_field_path`` (FieldPath):  [Read-Write]
- ``text`` (Text):  [Read-Write]

<a id="unreal.PyTestChildStruct.__init__"></a>

#### __init__

```python
def __init__(bool: bool = False,
             int: int = 0,
             float: float = 0.000000,
             enum: PyTestEnum = PyTestEnum.ONE,
             string: str = "",
             name: Name = "None",
             text: Text = "",
             field_path: FieldPath = FieldPath(),
             struct_field_path: FieldPath = FieldPath(),
             string_array: Array[str] = [],
             string_set: Set[str] = [],
             string_int_map: Map[str, int] = {},
             bool_mutable: bool = False) -> None
```

<a id="unreal.PyTestClassSparseData"></a>