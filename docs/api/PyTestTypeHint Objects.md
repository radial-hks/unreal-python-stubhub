## PyTestTypeHint Objects

```python
class PyTestTypeHint(Object)
```

Used to verify if the generated Python stub is correctly type-hinted (if type hint is enabled). The stub is generated
* in the project intermediate folder when the Python developer mode is enabled (Editor preferences). The type hints can
* be checked in the stub itself or PythonScriptPlugin/Content/Python/test_type_hints.py can be loaded in a Python IDE that
* supports type checking and look at the code to verify that there is not problems with the types.

**C++ Source:**

- **Plugin**: PythonScriptPlugin
- **Module**: PythonScriptPlugin
- **File**: PyTest.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bool_prop`` (bool):  [Read-Write] Check type hinted properties (setter/getter)
- ``delegate_prop`` (PyTestDelegate):  [Read-Write]
- ``enum_prop`` (PyTestEnum):  [Read-Write]
- ``field_path_prop`` (FieldPath):  [Read-Write]
- ``float_prop`` (float):  [Read-Write]
- ``int_prop`` (int32):  [Read-Write]
- ``map_prop`` (Map[int32, str]):  [Read-Write]
- ``multicast_delegate_prop`` (PyTestMulticastDelegate):  [Read-Write]
- ``name_array_prop`` (Array[Name]):  [Read-Write]
- ``name_prop`` (Name):  [Read-Write]
- ``object_array_prop`` (Array[Object]):  [Read-Write]
- ``object_prop`` (PyTestObject):  [Read-Write]
- ``set_prop`` (Set[str]):  [Read-Write]
- ``slate_tick_delegate`` (PyTestSlateTickDelegate):  [Read-Write] Members to facilitate testing particular Python API.
- ``str_array_prop`` (Array[str]):  [Read-Write]
- ``string_prop`` (str):  [Read-Write]
- ``struct_prop`` (PyTestStruct):  [Read-Write]
- ``text_array_prop`` (Array[Text]):  [Read-Write]
- ``text_prop`` (Text):  [Read-Write]

<a id="unreal.PyTestTypeHint.bool_prop"></a>

#### bool_prop

```python
@property
def bool_prop() -> bool
```

(bool):  [Read-Write] Check type hinted properties (setter/getter)

<a id="unreal.PyTestTypeHint.bool_prop"></a>

#### bool_prop

```python
@bool_prop.setter
def bool_prop(value: bool) -> None
```

<a id="unreal.PyTestTypeHint.int_prop"></a>

#### int_prop

```python
@property
def int_prop() -> int
```

(int32):  [Read-Write]

<a id="unreal.PyTestTypeHint.int_prop"></a>

#### int_prop

```python
@int_prop.setter
def int_prop(value: int) -> None
```

<a id="unreal.PyTestTypeHint.float_prop"></a>

#### float_prop

```python
@property
def float_prop() -> float
```

(float):  [Read-Write]

<a id="unreal.PyTestTypeHint.float_prop"></a>

#### float_prop

```python
@float_prop.setter
def float_prop(value: float) -> None
```

<a id="unreal.PyTestTypeHint.enum_prop"></a>

#### enum_prop

```python
@property
def enum_prop() -> PyTestEnum
```

(PyTestEnum):  [Read-Write]

<a id="unreal.PyTestTypeHint.enum_prop"></a>

#### enum_prop

```python
@enum_prop.setter
def enum_prop(value: PyTestEnum) -> None
```

<a id="unreal.PyTestTypeHint.string_prop"></a>

#### string_prop

```python
@property
def string_prop() -> str
```

(str):  [Read-Write]

<a id="unreal.PyTestTypeHint.string_prop"></a>

#### string_prop

```python
@string_prop.setter
def string_prop(value: str) -> None
```

<a id="unreal.PyTestTypeHint.name_prop"></a>

#### name_prop

```python
@property
def name_prop() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PyTestTypeHint.name_prop"></a>

#### name_prop

```python
@name_prop.setter
def name_prop(value: Name) -> None
```

<a id="unreal.PyTestTypeHint.text_prop"></a>

#### text_prop

```python
@property
def text_prop() -> Text
```

(Text):  [Read-Write]

<a id="unreal.PyTestTypeHint.text_prop"></a>

#### text_prop

```python
@text_prop.setter
def text_prop(value: Text) -> None
```

<a id="unreal.PyTestTypeHint.field_path_prop"></a>

#### field_path_prop

```python
@property
def field_path_prop() -> FieldPath
```

(FieldPath):  [Read-Write]

<a id="unreal.PyTestTypeHint.field_path_prop"></a>

#### field_path_prop

```python
@field_path_prop.setter
def field_path_prop(value: FieldPath) -> None
```

<a id="unreal.PyTestTypeHint.struct_prop"></a>

#### struct_prop

```python
@property
def struct_prop() -> PyTestStruct
```

(PyTestStruct):  [Read-Write]

<a id="unreal.PyTestTypeHint.struct_prop"></a>

#### struct_prop

```python
@struct_prop.setter
def struct_prop(value: PyTestStruct) -> None
```

<a id="unreal.PyTestTypeHint.object_prop"></a>

#### object_prop

```python
@property
def object_prop() -> PyTestObject
```

(PyTestObject):  [Read-Write]

<a id="unreal.PyTestTypeHint.object_prop"></a>

#### object_prop

```python
@object_prop.setter
def object_prop(value: PyTestObject) -> None
```

<a id="unreal.PyTestTypeHint.str_array_prop"></a>

#### str_array_prop

```python
@property
def str_array_prop() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.PyTestTypeHint.str_array_prop"></a>

#### str_array_prop

```python
@str_array_prop.setter
def str_array_prop(value: Array[str]) -> None
```

<a id="unreal.PyTestTypeHint.name_array_prop"></a>

#### name_array_prop

```python
@property
def name_array_prop() -> Array[Name]
```

(Array[Name]):  [Read-Write]

<a id="unreal.PyTestTypeHint.name_array_prop"></a>

#### name_array_prop

```python
@name_array_prop.setter
def name_array_prop(value: Array[Name]) -> None
```

<a id="unreal.PyTestTypeHint.text_array_prop"></a>

#### text_array_prop

```python
@property
def text_array_prop() -> Array[Text]
```

(Array[Text]):  [Read-Write]

<a id="unreal.PyTestTypeHint.text_array_prop"></a>

#### text_array_prop

```python
@text_array_prop.setter
def text_array_prop(value: Array[Text]) -> None
```

<a id="unreal.PyTestTypeHint.object_array_prop"></a>

#### object_array_prop

```python
@property
def object_array_prop() -> Array[Object]
```

(Array[Object]):  [Read-Write]

<a id="unreal.PyTestTypeHint.object_array_prop"></a>

#### object_array_prop

```python
@object_array_prop.setter
def object_array_prop(value: Array[Object]) -> None
```

<a id="unreal.PyTestTypeHint.set_prop"></a>

#### set_prop

```python
@property
def set_prop() -> Set[str]
```

(Set[str]):  [Read-Write]

<a id="unreal.PyTestTypeHint.set_prop"></a>

#### set_prop

```python
@set_prop.setter
def set_prop(value: Set[str]) -> None
```

<a id="unreal.PyTestTypeHint.map_prop"></a>

#### map_prop

```python
@property
def map_prop() -> Map[int, str]
```

(Map[int32, str]):  [Read-Write]

<a id="unreal.PyTestTypeHint.map_prop"></a>

#### map_prop

```python
@map_prop.setter
def map_prop(value: Map[int, str]) -> None
```

<a id="unreal.PyTestTypeHint.delegate_prop"></a>

#### delegate_prop

```python
@property
def delegate_prop() -> PyTestDelegate
```

(PyTestDelegate):  [Read-Write]

<a id="unreal.PyTestTypeHint.delegate_prop"></a>

#### delegate_prop

```python
@delegate_prop.setter
def delegate_prop(value: PyTestDelegate) -> None
```

<a id="unreal.PyTestTypeHint.multicast_delegate_prop"></a>

#### multicast_delegate_prop

```python
@property
def multicast_delegate_prop() -> PyTestMulticastDelegate
```

(PyTestMulticastDelegate):  [Read-Write]

<a id="unreal.PyTestTypeHint.multicast_delegate_prop"></a>

#### multicast_delegate_prop

```python
@multicast_delegate_prop.setter
def multicast_delegate_prop(value: PyTestMulticastDelegate) -> None
```

<a id="unreal.PyTestTypeHint.slate_tick_delegate"></a>

#### slate_tick_delegate

```python
@property
def slate_tick_delegate() -> PyTestSlateTickDelegate
```

(PyTestSlateTickDelegate):  [Read-Write] Members to facilitate testing particular Python API.

<a id="unreal.PyTestTypeHint.slate_tick_delegate"></a>

#### slate_tick_delegate

```python
@slate_tick_delegate.setter
def slate_tick_delegate(value: PyTestSlateTickDelegate) -> None
```

<a id="unreal.PyTestTypeHint.check_tuple_return_type"></a>

#### check_tuple_return_type

```python
@classmethod
def check_tuple_return_type(cls, out_string: str) -> Tuple[int, str]
```

X.check_tuple_return_type(out_string) -> (int32, out_string=str)
Check Tuple Return Type

Args:
    out_string (str): 

Returns:
    str: 

    out_string (str):

<a id="unreal.PyTestTypeHint.check_text_type_hints"></a>

#### check_text_type_hints

```python
def check_text_type_hints(param1: Text, param2: Text = "Hi") -> Text
```

x.check_text_type_hints(param1, param2="Hi") -> Text
Check Text Type Hints

Args:
    param1 (Text): 
    param2 (Text): 

Returns:
    Text:

<a id="unreal.PyTestTypeHint.check_struct_type_hints"></a>

#### check_struct_type_hints

```python
def check_struct_type_hints(
    param1: PyTestStruct,
    param2: PyTestStruct = [
        False, 0, 0.000000, PyTestEnum.ONE, "", "None", "",
        FieldPath(),
        FieldPath(), [], [], {}, False
    ]
) -> PyTestStruct
```

x.check_struct_type_hints(param1, param2=[False, 0, 0.000000, PyTestEnum.ONE, "", "None", "", FieldPath(), FieldPath(), [], [], {}, False]) -> PyTestStruct
Check Struct Type Hints

Args:
    param1 (PyTestStruct): 
    param2 (PyTestStruct): 

Returns:
    PyTestStruct:

<a id="unreal.PyTestTypeHint.check_string_type_hints"></a>

#### check_string_type_hints

```python
def check_string_type_hints(param1: str, param2: str = "Hi") -> str
```

x.check_string_type_hints(param1, param2="Hi") -> str
Check String Type Hints

Args:
    param1 (str): 
    param2 (str): 

Returns:
    str:

<a id="unreal.PyTestTypeHint.check_static_function"></a>

#### check_static_function

```python
@classmethod
def check_static_function(cls, param1: bool, param2: int, param3: float,
                          param4: str) -> bool
```

X.check_static_function(param1, param2, param3, param4) -> bool
Check Static Function

Args:
    param1 (bool): 
    param2 (int32): 
    param3 (double): 
    param4 (str): 

Returns:
    bool:

<a id="unreal.PyTestTypeHint.check_set_type_hints"></a>

#### check_set_type_hints

```python
def check_set_type_hints(param1: Set[str], param2: Set[Name],
                         param3: Set[Object]) -> Set[Name]
```

x.check_set_type_hints(param1, param2, param3) -> Set[Name]
Check Set Type Hints

Args:
    param1 (Set[str]): 
    param2 (Set[Name]): 
    param3 (Set[Object]): 

Returns:
    Set[Name]:

<a id="unreal.PyTestTypeHint.check_object_type_hints"></a>

#### check_object_type_hints

```python
def check_object_type_hints(param1: PyTestObject,
                            param4: PyTestObject = None) -> PyTestObject
```

x.check_object_type_hints(param1, param4=None) -> PyTestObject
Check Object Type Hints

Args:
    param1 (PyTestObject): 
    param4 (PyTestObject): 

Returns:
    PyTestObject:

<a id="unreal.PyTestTypeHint.check_name_type_hints"></a>

#### check_name_type_hints

```python
def check_name_type_hints(param1: Name, param2: Name = "Hi") -> Name
```

x.check_name_type_hints(param1, param2="Hi") -> Name
Check Name Type Hints

Args:
    param1 (Name): 
    param2 (Name): 

Returns:
    Name:

<a id="unreal.PyTestTypeHint.check_map_type_hints"></a>

#### check_map_type_hints

```python
def check_map_type_hints(param1: Map[int, str], param2: Map[int, Name],
                         param3: Map[int, Text],
                         param4: Map[int, Object]) -> Map[str, Object]
```

x.check_map_type_hints(param1, param2, param3, param4) -> Map[str, Object]
Check Map Type Hints

Args:
    param1 (Map[int32, str]): 
    param2 (Map[int32, Name]): 
    param3 (Map[int32, Text]): 
    param4 (Map[int32, Object]): 

Returns:
    Map[str, Object]:

<a id="unreal.PyTestTypeHint.check_integer_type_hints"></a>

#### check_integer_type_hints

```python
def check_integer_type_hints(param1: int,
                             param2: int = 4,
                             param3: int = 5) -> int
```

x.check_integer_type_hints(param1, param2=4, param3=5) -> int32
Check Integer Type Hints

Args:
    param1 (uint8): 
    param2 (int32): 
    param3 (int64): 

Returns:
    int32:

<a id="unreal.PyTestTypeHint.check_float_type_hints"></a>

#### check_float_type_hints

```python
def check_float_type_hints(param1: float,
                           param2: float,
                           param3: float = -3.300000,
                           param4: float = 4.400000) -> float
```

x.check_float_type_hints(param1, param2, param3=-3.300000, param4=4.400000) -> double
Check Float Type Hints

Args:
    param1 (float): 
    param2 (double): 
    param3 (float): 
    param4 (double): 

Returns:
    double:

<a id="unreal.PyTestTypeHint.check_field_path_type_hints"></a>

#### check_field_path_type_hints

```python
def check_field_path_type_hints(param1: FieldPath) -> FieldPath
```

x.check_field_path_type_hints(param1) -> FieldPath
Check Field Path Type Hints

Args:
    param1 (FieldPath): 

Returns:
    FieldPath:

<a id="unreal.PyTestTypeHint.check_enum_type_hints"></a>

#### check_enum_type_hints

```python
def check_enum_type_hints(param1: PyTestEnum,
                          param2: PyTestEnum = PyTestEnum.ONE) -> PyTestEnum
```

x.check_enum_type_hints(param1, param2=PyTestEnum.ONE) -> PyTestEnum
Check Enum Type Hints

Args:
    param1 (PyTestEnum): 
    param2 (PyTestEnum): 

Returns:
    PyTestEnum:

<a id="unreal.PyTestTypeHint.check_delegate_type_hints"></a>

#### check_delegate_type_hints

```python
def check_delegate_type_hints(param1: PyTestDelegate) -> PyTestDelegate
```

x.check_delegate_type_hints(param1) -> PyTestDelegate
Check Delegate Type Hints

Args:
    param1 (PyTestDelegate): 

Returns:
    PyTestDelegate:

<a id="unreal.PyTestTypeHint.check_bool_type_hints"></a>

#### check_bool_type_hints

```python
def check_bool_type_hints(param1: bool,
                          param2: bool = True,
                          param3: bool = False) -> bool
```

x.check_bool_type_hints(param1, param2=True, param3=False) -> bool
Check type hinted methods.

Args:
    param1 (bool): 
    param2 (bool): 
    param3 (bool): 

Returns:
    bool:

<a id="unreal.PyTestTypeHint.check_array_type_hints"></a>

#### check_array_type_hints

```python
def check_array_type_hints(param1: Array[str], param2: Array[Name],
                           param3: Array[Text],
                           param4: Array[Object]) -> Array[Text]
```

x.check_array_type_hints(param1, param2, param3, param4) -> Array[Text]
Check Array Type Hints

Args:
    param1 (Array[str]): 
    param2 (Array[Name]): 
    param3 (Array[Text]): 
    param4 (Array[Object]): 

Returns:
    Array[Text]:

<a id="unreal.PyTestTypeHint.STR_CONST"></a>

#### STR_CONST

(str): Check type hinted constants

<a id="unreal.PyTestTypeHint.INT_CONST"></a>

#### INT_CONST

(int32): Get Int Const

<a id="unreal.PythonScriptLibrary"></a>