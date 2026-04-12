## PythonEnumLib Objects

```python
class PythonEnumLib(BlueprintFunctionLibrary)
```

Python Enum Lib

**C++ Source:**

- **Plugin**: TAPython
- **Module**: TAPython
- **File**: PythonEnumLib.h

<a id="unreal.PythonEnumLib.set_enum_items"></a>

#### set\_enum\_items

```python
@classmethod
def set_enum_items(cls, enum: UserDefinedEnum,
                   display_names: Array[str]) -> None
```

X.set_enum_items(enum, display_names) -> None
Set the items of the given User Define Enum.

Args:
    enum (UserDefinedEnum): The User Define Enum you want to modify.
    display_names (Array[str]): The display names of the enum's items. The Raw Enum Name will generated automaticly.

<a id="unreal.PythonEnumLib.set_display_name"></a>

#### set\_display\_name

```python
@classmethod
def set_display_name(cls, enum: UserDefinedEnum, index: int,
                     new_display_name: str) -> bool
```

X.set_display_name(enum, index, new_display_name) -> bool
Get the display name of the given User Define Enum

Args:
    enum (UserDefinedEnum): The User Define Enum you want to query.
    index (int32): The index of the enum item, 0-based.
    new_display_name (str): The new display name

Returns:
    bool: True if the new name set.

<a id="unreal.PythonEnumLib.set_description_by_index"></a>

#### set\_description\_by\_index

```python
@classmethod
def set_description_by_index(cls, enum: UserDefinedEnum, index: int,
                             description: str) -> bool
```

X.set_description_by_index(enum, index, description) -> bool
Set the Description of the given User Define Enum Item

Args:
    enum (UserDefinedEnum): The User Define Enum you want to query.
    index (int32): The index of the enum item, 0-based.
    description (str): The description of the enum item.

Returns:
    bool: True if the description set.

<a id="unreal.PythonEnumLib.set_bitflags_type"></a>

#### set\_bitflags\_type

```python
@classmethod
def set_bitflags_type(cls, enum: UserDefinedEnum, bitflags_type: bool) -> None
```

X.set_bitflags_type(enum, bitflags_type) -> None
Set the state of the bitflags of the given User Define Enum

Args:
    enum (UserDefinedEnum): The User Define Enum you want to query.
    bitflags_type (bool): Bitflags Value

<a id="unreal.PythonEnumLib.move_enum_item"></a>

#### move\_enum\_item

```python
@classmethod
def move_enum_item(cls, enum: UserDefinedEnum, initial_index: int,
                   target_index: int) -> None
```

X.move_enum_item(enum, initial_index, target_index) -> None
Moves the enumerator at the given initial index to a new target index, shifting other enumerators as needed.
E.g. with enum [A, B, C, D, E], moving index 1 to index 3 results in [A, C, D, B, E].

Args:
    enum (UserDefinedEnum): The User Define Enum you want to modify.
    initial_index (int32): The initial index of the enum item
    target_index (int32): The target index of the enum item

<a id="unreal.PythonEnumLib.is_bitflags_type"></a>

#### is\_bitflags\_type

```python
@classmethod
def is_bitflags_type(cls, enum: UserDefinedEnum) -> bool
```

X.is_bitflags_type(enum) -> bool
Check if the enumerator-as-bitflags meta data is set

Args:
    enum (UserDefinedEnum): The User Define Enum you want to query.

Returns:
    bool: Whether has Bitflags or not.

<a id="unreal.PythonEnumLib.get_name_by_index"></a>

#### get\_name\_by\_index

```python
@classmethod
def get_name_by_index(cls, enum: UserDefinedEnum, index: int) -> str
```

X.get_name_by_index(enum, index) -> str
Get the raw name of the given User Define Enum

Args:
    enum (UserDefinedEnum): The User Define Enum you want to query.
    index (int32): The index of the enum item, 0-based.

Returns:
    str: The raw name of the enum item

<a id="unreal.PythonEnumLib.get_enum_len"></a>

#### get\_enum\_len

```python
@classmethod
def get_enum_len(cls, enum: UserDefinedEnum) -> int
```

X.get_enum_len(enum) -> int32
Get the number of the given User Define Enum's items.

Args:
    enum (UserDefinedEnum): The User Define Enum you want to query.

Returns:
    int32: Number of User Define Enum

<a id="unreal.PythonEnumLib.get_display_name_map"></a>

#### get\_display\_name\_map

```python
@classmethod
def get_display_name_map(cls, enum: UserDefinedEnum) -> Map[Name, Text]
```

X.get_display_name_map(enum) -> Map[Name, Text]
Get the DiaplayNameMap of the given User Define Enum. Key: Raw Enum Num, Value：Display Name
note: Return value is a map, unordered.

Args:
    enum (UserDefinedEnum): The User Define Enum you want to query.

Returns:
    Map[Name, Text]: The DisplayNameMap in enum. (type: <class 'Map'>)

<a id="unreal.PythonEnumLib.get_display_name_by_index"></a>

#### get\_display\_name\_by\_index

```python
@classmethod
def get_display_name_by_index(cls, enum: UserDefinedEnum, index: int) -> str
```

X.get_display_name_by_index(enum, index) -> str
Get the display name of the given User Define Enum

Args:
    enum (UserDefinedEnum): The User Define Enum you want to query.
    index (int32): The index of the enum item, 0-based.

Returns:
    str: The display name of the enum item

<a id="unreal.PythonEnumLib.get_description_by_index"></a>

#### get\_description\_by\_index

```python
@classmethod
def get_description_by_index(cls, enum: UserDefinedEnum, index: int) -> str
```

X.get_description_by_index(enum, index) -> str
Get the Description of the given User Define Enum Item

Args:
    enum (UserDefinedEnum): The User Define Enum you want to query.
    index (int32): The index of the enum item, 0-based.

Returns:
    str: The description name of the enum item

<a id="unreal.PythonEnumLib.get_cpp_form"></a>

#### get\_cpp\_form

```python
@classmethod
def get_cpp_form(cls, enum: UserDefinedEnum) -> int
```

X.get_cpp_form(enum) -> int32
Get the CppForm value as int of the given User Define Enum

Args:
    enum (UserDefinedEnum): The User Define Enum you want to query.

Returns:
    int32: ECppForm value as int.          0: Regular, 1: Namespaced, 2EnumClass

<a id="unreal.PythonLandscapeLib"></a>