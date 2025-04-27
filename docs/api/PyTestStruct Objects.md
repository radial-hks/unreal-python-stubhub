## PyTestStruct Objects

```python
class PyTestStruct(StructBase)
```

Struct to allow testing of the various UStruct features that are exposed to Python wrapped types.

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

<a id="unreal.PyTestStruct.__init__"></a>

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

<a id="unreal.PyTestStruct.bool"></a>

#### bool

```python
@property
def bool() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PyTestStruct.bool"></a>

#### bool

```python
@bool.setter
def bool(value: bool) -> None
```

<a id="unreal.PyTestStruct.int"></a>

#### int

```python
@property
def int() -> int
```

(int32):  [Read-Write]

<a id="unreal.PyTestStruct.int"></a>

#### int

```python
@int.setter
def int(value: int) -> None
```

<a id="unreal.PyTestStruct.float"></a>

#### float

```python
@property
def float() -> float
```

(float):  [Read-Write]

<a id="unreal.PyTestStruct.float"></a>

#### float

```python
@float.setter
def float(value: float) -> None
```

<a id="unreal.PyTestStruct.enum"></a>

#### enum

```python
@property
def enum() -> PyTestEnum
```

(PyTestEnum):  [Read-Write]

<a id="unreal.PyTestStruct.enum"></a>

#### enum

```python
@enum.setter
def enum(value: PyTestEnum) -> None
```

<a id="unreal.PyTestStruct.string"></a>

#### string

```python
@property
def string() -> str
```

(str):  [Read-Write]

<a id="unreal.PyTestStruct.string"></a>

#### string

```python
@string.setter
def string(value: str) -> None
```

<a id="unreal.PyTestStruct.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PyTestStruct.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.PyTestStruct.text"></a>

#### text

```python
@property
def text() -> Text
```

(Text):  [Read-Write]

<a id="unreal.PyTestStruct.text"></a>

#### text

```python
@text.setter
def text(value: Text) -> None
```

<a id="unreal.PyTestStruct.field_path"></a>

#### field_path

```python
@property
def field_path() -> FieldPath
```

(FieldPath):  [Read-Write]

<a id="unreal.PyTestStruct.field_path"></a>

#### field_path

```python
@field_path.setter
def field_path(value: FieldPath) -> None
```

<a id="unreal.PyTestStruct.struct_field_path"></a>

#### struct_field_path

```python
@property
def struct_field_path() -> FieldPath
```

(FieldPath):  [Read-Write]

<a id="unreal.PyTestStruct.struct_field_path"></a>

#### struct_field_path

```python
@struct_field_path.setter
def struct_field_path(value: FieldPath) -> None
```

<a id="unreal.PyTestStruct.string_array"></a>

#### string_array

```python
@property
def string_array() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.PyTestStruct.string_array"></a>

#### string_array

```python
@string_array.setter
def string_array(value: Array[str]) -> None
```

<a id="unreal.PyTestStruct.string_set"></a>

#### string_set

```python
@property
def string_set() -> Set[str]
```

(Set[str]):  [Read-Write]

<a id="unreal.PyTestStruct.string_set"></a>

#### string_set

```python
@string_set.setter
def string_set(value: Set[str]) -> None
```

<a id="unreal.PyTestStruct.string_int_map"></a>

#### string_int_map

```python
@property
def string_int_map() -> Map[str, int]
```

(Map[str, int32]):  [Read-Write]

<a id="unreal.PyTestStruct.string_int_map"></a>

#### string_int_map

```python
@string_int_map.setter
def string_int_map(value: Map[str, int]) -> None
```

<a id="unreal.PyTestStruct.legacy_int"></a>

#### legacy_int

```python
@property
def legacy_int() -> int
```

(int32):  [Read-Write]
deprecated: LegacyInt is deprecated. Please use Int instead.

<a id="unreal.PyTestStruct.legacy_int"></a>

#### legacy_int

```python
@legacy_int.setter
def legacy_int(value: int) -> None
```

<a id="unreal.PyTestStruct.bool_mutable"></a>

#### bool_mutable

```python
@property
def bool_mutable() -> bool
```

(bool):  [Read-Only]

<a id="unreal.PyTestStruct.set_bool_mutable_via_ref"></a>

#### set_bool_mutable_via_ref

```python
def set_bool_mutable_via_ref() -> None
```

x.set_bool_mutable_via_ref() -> None
Set Bool Mutable Via Ref

<a id="unreal.PyTestStruct.set_bool_mutable"></a>

#### set_bool_mutable

```python
def set_bool_mutable() -> None
```

x.set_bool_mutable() -> None
Set Bool Mutable

<a id="unreal.PyTestStruct.legacy_is_bool_set"></a>

#### legacy_is_bool_set

```python
def legacy_is_bool_set() -> bool
```

x.legacy_is_bool_set() -> bool
Legacy Is Bool Set
deprecated: LegacyIsBoolSet is deprecated. Please use IsBoolSet instead.

Returns:
    bool:

<a id="unreal.PyTestStruct.is_bool_set"></a>

#### is_bool_set

```python
def is_bool_set() -> bool
```

x.is_bool_set() -> bool
Is Bool Set

Returns:
    bool:

<a id="unreal.PyTestStruct.is_bool_set_old"></a>

#### is_bool_set_old

```python
def is_bool_set_old() -> bool
```

deprecated: 'is_bool_set_old' was renamed to 'is_bool_set'.

<a id="unreal.PyTestStruct.clear_bool_mutable_via_ref"></a>

#### clear_bool_mutable_via_ref

```python
def clear_bool_mutable_via_ref() -> None
```

x.clear_bool_mutable_via_ref() -> None
Clear Bool Mutable Via Ref

<a id="unreal.PyTestStruct.clear_bool_mutable"></a>

#### clear_bool_mutable

```python
def clear_bool_mutable() -> None
```

x.clear_bool_mutable() -> None
Clear Bool Mutable

<a id="unreal.PyTestStruct.add_str"></a>

#### add_str

```python
def add_str(value: str) -> None
```

x.add_str(value) -> None
Add Str

Args:
    value (str): 

Returns:
    PyTestStruct:

<a id="unreal.PyTestStruct.add_int"></a>

#### add_int

```python
def add_int(value: int) -> None
```

x.add_int(value) -> None
Add Int

Args:
    value (int32): 

Returns:
    PyTestStruct:

<a id="unreal.PyTestStruct.add_float"></a>

#### add_float

```python
def add_float(value: float) -> None
```

x.add_float(value) -> None
Add Float

Args:
    value (float): 

Returns:
    PyTestStruct:

<a id="unreal.PyTestStruct.__add__"></a>

#### __add__

```python
def __add__(other: PyTestStruct) -> None
```

**Overloads:**

- ``str`` Add Str
- ``int32`` Add Int
- ``float`` Add Float

<a id="unreal.PyTestStruct.__iadd__"></a>

#### __iadd__

```python
def __iadd__(other: PyTestStruct) -> None
```

**Overloads:**

- ``str`` Add Str
- ``int32`` Add Int
- ``float`` Add Float

<a id="unreal.PyTestStruct.CONSTANT_VALUE"></a>

#### CONSTANT_VALUE

(int32): Get Constant Value

<a id="unreal.PythonLogOutputEntry"></a>