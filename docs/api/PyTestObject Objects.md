## PyTestObject Objects

```python
class PyTestObject(Object)
```

Object to allow testing of the various UObject features that are exposed to Python wrapped types.

**C++ Source:**

- **Plugin**: PythonScriptPlugin
- **Module**: PythonScriptPlugin
- **File**: PyTest.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bool`` (bool):  [Read-Write]
- ``bool_defaults_only`` (bool):  [Read-Write]
- ``bool_instance_only`` (bool):  [Read-Write]
- ``child_struct`` (PyTestChildStruct):  [Read-Write]
- ``delegate`` (PyTestDelegate):  [Read-Write]
- ``enum`` (PyTestEnum):  [Read-Write]
- ``field_path`` (FieldPath):  [Read-Write]
- ``float`` (float):  [Read-Write]
- ``int`` (int32):  [Read-Write]
- ``multicast_delegate`` (PyTestMulticastDelegate):  [Read-Write]
- ``name`` (Name):  [Read-Write]
- ``string`` (str):  [Read-Write]
- ``string_array`` (Array[str]):  [Read-Write]
- ``string_int_map`` (Map[str, int32]):  [Read-Write]
- ``string_set`` (Set[str]):  [Read-Write]
- ``struct`` (PyTestStruct):  [Read-Write]
- ``struct_array`` (Array[PyTestStruct]):  [Read-Write]
- ``struct_field_path`` (FieldPath):  [Read-Write]
- ``text`` (Text):  [Read-Write]

<a id="unreal.PyTestObject.bool"></a>

#### bool

```python
@property
def bool() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PyTestObject.bool"></a>

#### bool

```python
@bool.setter
def bool(value: bool) -> None
```

<a id="unreal.PyTestObject.int"></a>

#### int

```python
@property
def int() -> int
```

(int32):  [Read-Write]

<a id="unreal.PyTestObject.int"></a>

#### int

```python
@int.setter
def int(value: int) -> None
```

<a id="unreal.PyTestObject.float"></a>

#### float

```python
@property
def float() -> float
```

(float):  [Read-Write]

<a id="unreal.PyTestObject.float"></a>

#### float

```python
@float.setter
def float(value: float) -> None
```

<a id="unreal.PyTestObject.enum"></a>

#### enum

```python
@property
def enum() -> PyTestEnum
```

(PyTestEnum):  [Read-Write]

<a id="unreal.PyTestObject.enum"></a>

#### enum

```python
@enum.setter
def enum(value: PyTestEnum) -> None
```

<a id="unreal.PyTestObject.string"></a>

#### string

```python
@property
def string() -> str
```

(str):  [Read-Write]

<a id="unreal.PyTestObject.string"></a>

#### string

```python
@string.setter
def string(value: str) -> None
```

<a id="unreal.PyTestObject.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PyTestObject.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.PyTestObject.text"></a>

#### text

```python
@property
def text() -> Text
```

(Text):  [Read-Write]

<a id="unreal.PyTestObject.text"></a>

#### text

```python
@text.setter
def text(value: Text) -> None
```

<a id="unreal.PyTestObject.field_path"></a>

#### field_path

```python
@property
def field_path() -> FieldPath
```

(FieldPath):  [Read-Write]

<a id="unreal.PyTestObject.field_path"></a>

#### field_path

```python
@field_path.setter
def field_path(value: FieldPath) -> None
```

<a id="unreal.PyTestObject.struct_field_path"></a>

#### struct_field_path

```python
@property
def struct_field_path() -> FieldPath
```

(FieldPath):  [Read-Write]

<a id="unreal.PyTestObject.struct_field_path"></a>

#### struct_field_path

```python
@struct_field_path.setter
def struct_field_path(value: FieldPath) -> None
```

<a id="unreal.PyTestObject.string_array"></a>

#### string_array

```python
@property
def string_array() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.PyTestObject.string_array"></a>

#### string_array

```python
@string_array.setter
def string_array(value: Array[str]) -> None
```

<a id="unreal.PyTestObject.string_set"></a>

#### string_set

```python
@property
def string_set() -> Set[str]
```

(Set[str]):  [Read-Write]

<a id="unreal.PyTestObject.string_set"></a>

#### string_set

```python
@string_set.setter
def string_set(value: Set[str]) -> None
```

<a id="unreal.PyTestObject.string_int_map"></a>

#### string_int_map

```python
@property
def string_int_map() -> Map[str, int]
```

(Map[str, int32]):  [Read-Write]

<a id="unreal.PyTestObject.string_int_map"></a>

#### string_int_map

```python
@string_int_map.setter
def string_int_map(value: Map[str, int]) -> None
```

<a id="unreal.PyTestObject.delegate"></a>

#### delegate

```python
@property
def delegate() -> PyTestDelegate
```

(PyTestDelegate):  [Read-Write]

<a id="unreal.PyTestObject.delegate"></a>

#### delegate

```python
@delegate.setter
def delegate(value: PyTestDelegate) -> None
```

<a id="unreal.PyTestObject.multicast_delegate"></a>

#### multicast_delegate

```python
@property
def multicast_delegate() -> PyTestMulticastDelegate
```

(PyTestMulticastDelegate):  [Read-Write]

<a id="unreal.PyTestObject.multicast_delegate"></a>

#### multicast_delegate

```python
@multicast_delegate.setter
def multicast_delegate(value: PyTestMulticastDelegate) -> None
```

<a id="unreal.PyTestObject.struct"></a>

#### struct

```python
@property
def struct() -> PyTestStruct
```

(PyTestStruct):  [Read-Write]

<a id="unreal.PyTestObject.struct"></a>

#### struct

```python
@struct.setter
def struct(value: PyTestStruct) -> None
```

<a id="unreal.PyTestObject.struct_array"></a>

#### struct_array

```python
@property
def struct_array() -> Array[PyTestStruct]
```

(Array[PyTestStruct]):  [Read-Write]

<a id="unreal.PyTestObject.struct_array"></a>

#### struct_array

```python
@struct_array.setter
def struct_array(value: Array[PyTestStruct]) -> None
```

<a id="unreal.PyTestObject.child_struct"></a>

#### child_struct

```python
@property
def child_struct() -> PyTestChildStruct
```

(PyTestChildStruct):  [Read-Write]

<a id="unreal.PyTestObject.child_struct"></a>

#### child_struct

```python
@child_struct.setter
def child_struct(value: PyTestChildStruct) -> None
```

<a id="unreal.PyTestObject.return_set"></a>

#### return_set

```python
@classmethod
def return_set(cls) -> Set[int]
```

X.return_set() -> Set[int32]
Return Set

Returns:
    Set[int32]:

<a id="unreal.PyTestObject.return_map"></a>

#### return_map

```python
@classmethod
def return_map(cls) -> Map[int, bool]
```

X.return_map() -> Map[int32, bool]
Return Map

Returns:
    Map[int32, bool]:

<a id="unreal.PyTestObject.return_field_path"></a>

#### return_field_path

```python
@classmethod
def return_field_path(cls) -> FieldPath
```

X.return_field_path() -> FieldPath
Return Field Path

Returns:
    FieldPath:

<a id="unreal.PyTestObject.return_array"></a>

#### return_array

```python
@classmethod
def return_array(cls) -> Array[int]
```

X.return_array() -> Array[int32]
Return Array

Returns:
    Array[int32]:

<a id="unreal.PyTestObject.multicast_delegate_property_callback"></a>

#### multicast_delegate_property_callback

```python
def multicast_delegate_property_callback(str: str) -> None
```

x.multicast_delegate_property_callback(str) -> None
Multicast Delegate Property Callback

Args:
    str (str):

<a id="unreal.PyTestObject.legacy_func_taking_py_test_struct"></a>

#### legacy_func_taking_py_test_struct

```python
def legacy_func_taking_py_test_struct(struct: PyTestStruct) -> None
```

x.legacy_func_taking_py_test_struct(struct) -> None
Legacy Func Taking Py Test Struct
deprecated: LegacyFuncTakingPyTestStruct is deprecated. Please use FuncTakingPyTestStruct instead.

Args:
    struct (PyTestStruct):

<a id="unreal.PyTestObject.func_taking_py_test_struct_default"></a>

#### func_taking_py_test_struct_default

```python
def func_taking_py_test_struct_default(
    struct: PyTestStruct = [
        False, 0, 0.000000, PyTestEnum.ONE, "", "None", "",
        FieldPath(),
        FieldPath(), [], [], {}, False
    ]
) -> None
```

x.func_taking_py_test_struct_default(struct=[False, 0, 0.000000, PyTestEnum.ONE, "", "None", "", FieldPath(), FieldPath(), [], [], {}, False]) -> None
Func Taking Py Test Struct Default

Args:
    struct (PyTestStruct):

<a id="unreal.PyTestObject.func_taking_py_test_struct"></a>

#### func_taking_py_test_struct

```python
def func_taking_py_test_struct(struct: PyTestStruct) -> None
```

x.func_taking_py_test_struct(struct) -> None
Func Taking Py Test Struct

Args:
    struct (PyTestStruct):

<a id="unreal.PyTestObject.func_taking_py_test_delegate"></a>

#### func_taking_py_test_delegate

```python
def func_taking_py_test_delegate(delegate: PyTestDelegate, value: int) -> int
```

x.func_taking_py_test_delegate(delegate, value) -> int32
Func Taking Py Test Delegate

Args:
    delegate (PyTestDelegate): 
    value (int32): 

Returns:
    int32:

<a id="unreal.PyTestObject.func_taking_py_test_child_struct"></a>

#### func_taking_py_test_child_struct

```python
def func_taking_py_test_child_struct(struct: PyTestChildStruct) -> None
```

x.func_taking_py_test_child_struct(struct) -> None
Func Taking Py Test Child Struct

Args:
    struct (PyTestChildStruct):

<a id="unreal.PyTestObject.func_taking_field_path"></a>

#### func_taking_field_path

```python
def func_taking_field_path(field_path: FieldPath) -> None
```

x.func_taking_field_path(field_path) -> None
Func Taking Field Path

Args:
    field_path (FieldPath):

<a id="unreal.PyTestObject.func_blueprint_native_ref"></a>

#### func_blueprint_native_ref

```python
def func_blueprint_native_ref(out_struct: PyTestStruct) -> PyTestStruct
```

x.func_blueprint_native_ref(out_struct) -> PyTestStruct
Func Blueprint Native Ref

Args:
    out_struct (PyTestStruct): 

Returns:
    PyTestStruct: 

    out_struct (PyTestStruct):

<a id="unreal.PyTestObject.func_blueprint_native"></a>

#### func_blueprint_native

```python
def func_blueprint_native(value: int) -> int
```

x.func_blueprint_native(value) -> int32
Func Blueprint Native

Args:
    value (int32): 

Returns:
    int32:

<a id="unreal.PyTestObject.func_blueprint_implementable_packed_getter"></a>

#### func_blueprint_implementable_packed_getter

```python
def func_blueprint_implementable_packed_getter() -> Optional[int]
```

x.func_blueprint_implementable_packed_getter() -> int32 or None
Func Blueprint Implementable Packed Getter

Returns:
    int32 or None: 

    out_value (int32):

<a id="unreal.PyTestObject.func_blueprint_implementable"></a>

#### func_blueprint_implementable

```python
def func_blueprint_implementable(value: int) -> int
```

x.func_blueprint_implementable(value) -> int32
Func Blueprint Implementable

Args:
    value (int32): 

Returns:
    int32:

<a id="unreal.PyTestObject.emit_script_warning"></a>

#### emit_script_warning

```python
@classmethod
def emit_script_warning(cls) -> None
```

X.emit_script_warning() -> None
Emit Script Warning

<a id="unreal.PyTestObject.emit_script_error"></a>

#### emit_script_error

```python
@classmethod
def emit_script_error(cls) -> None
```

X.emit_script_error() -> None
Emit Script Error

<a id="unreal.PyTestObject.delegate_property_callback"></a>

#### delegate_property_callback

```python
def delegate_property_callback(value: int) -> int
```

x.delegate_property_callback(value) -> int32
UHT couldn't parse any default value for the FieldPath.

Args:
    value (int32): 

Returns:
    int32:

<a id="unreal.PyTestObject.call_func_blueprint_native_ref"></a>

#### call_func_blueprint_native_ref

```python
def call_func_blueprint_native_ref(out_struct: PyTestStruct) -> PyTestStruct
```

x.call_func_blueprint_native_ref(out_struct) -> PyTestStruct
Call Func Blueprint Native Ref

Args:
    out_struct (PyTestStruct): 

Returns:
    PyTestStruct: 

    out_struct (PyTestStruct):

<a id="unreal.PyTestObject.call_func_blueprint_native"></a>

#### call_func_blueprint_native

```python
def call_func_blueprint_native(value: int) -> int
```

x.call_func_blueprint_native(value) -> int32
Call Func Blueprint Native

Args:
    value (int32): 

Returns:
    int32:

<a id="unreal.PyTestObject.call_func_blueprint_implementable_packed_getter"></a>

#### call_func_blueprint_implementable_packed_getter

```python
def call_func_blueprint_implementable_packed_getter() -> Optional[int]
```

x.call_func_blueprint_implementable_packed_getter() -> int32 or None
Call Func Blueprint Implementable Packed Getter

Returns:
    int32 or None: 

    out_value (int32):

<a id="unreal.PyTestObject.call_func_blueprint_implementable"></a>

#### call_func_blueprint_implementable

```python
def call_func_blueprint_implementable(value: int) -> int
```

x.call_func_blueprint_implementable(value) -> int32
Call Func Blueprint Implementable

Args:
    value (int32): 

Returns:
    int32:

<a id="unreal.PyTestObject.func_interface_child"></a>

#### func_interface_child

```python
def func_interface_child(value: int) -> int
```

x.func_interface_child(value) -> int32
Func Interface Child

Args:
    value (int32): 

Returns:
    int32:

<a id="unreal.PyTestObject.func_interface"></a>

#### func_interface

```python
def func_interface(value: int) -> int
```

x.func_interface(value) -> int32
Func Interface

Args:
    value (int32): 

Returns:
    int32:

<a id="unreal.PyTestObject.func_interface_other"></a>

#### func_interface_other

```python
def func_interface_other(value: int) -> int
```

x.func_interface_other(value) -> int32
Func Interface Other

Args:
    value (int32): 

Returns:
    int32:

<a id="unreal.PyTestObject.is_bool_set"></a>

#### is_bool_set

```python
def is_bool_set() -> bool
```

x.is_bool_set() -> bool
Is Bool Set

Returns:
    bool:

<a id="unreal.PyTestObject.CONSTANT_VALUE"></a>

#### CONSTANT_VALUE

(int32): Get Constant Value

<a id="unreal.PyTestObject.OTHER_CONSTANT_VALUE"></a>

#### OTHER_CONSTANT_VALUE

(int32): Get Other Constant Value

<a id="unreal.PyTestChildObject"></a>