## GeometryScriptIndexList Objects

```python
class GeometryScriptIndexList(StructBase)
```

Geometry Script Index List

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: GeometryScriptTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``index_type`` (GeometryScriptIndexType):  [Read-Write]

<a id="unreal.GeometryScriptIndexList.__init__"></a>

#### __init__

```python
def __init__(
        index_type: GeometryScriptIndexType = GeometryScriptIndexType.ANY
) -> None
```

<a id="unreal.GeometryScriptIndexList.index_type"></a>

#### index_type

```python
@property
def index_type() -> GeometryScriptIndexType
```

(GeometryScriptIndexType):  [Read-Write]

<a id="unreal.GeometryScriptIndexList.index_type"></a>

#### index_type

```python
@index_type.setter
def index_type(value: GeometryScriptIndexType) -> None
```

<a id="unreal.GeometryScriptIndexList.set_index_list_item"></a>

#### set_index_list_item

```python
def set_index_list_item(index: int, new_value: int) -> bool
```

x.set_index_list_item(index, new_value) -> bool
Updates the value associated with Index in the Index List.
If the Index is invalid, the operation will fail and in this case bValidIndex will be set to false on return.

Args:
    index (int32): 
    new_value (int32): 

Returns:
    bool: 

    is_valid_index (bool):

<a id="unreal.GeometryScriptIndexList.get_index_list_length"></a>

#### get_index_list_length

```python
def get_index_list_length() -> int
```

x.get_index_list_length() -> int32
Returns the number of Items in Index List.

Returns:
    int32:

<a id="unreal.GeometryScriptIndexList.get_index_list_last_index"></a>

#### get_index_list_last_index

```python
def get_index_list_last_index() -> int
```

x.get_index_list_last_index() -> int32
Returns the index of the last element in the Index List.
Note, the value -1 will be returned if the list is empty or invalid.

Returns:
    int32:

<a id="unreal.GeometryScriptIndexList.get_index_list_item"></a>

#### get_index_list_item

```python
def get_index_list_item(index: int) -> Tuple[int, bool]
```

x.get_index_list_item(index) -> (int32, is_valid_index=bool)
Returns the item associated with Index in the Index List.
If Index is not valid for this Index List the value -1 will be returned and bIsValidIndex will be set to false.

Args:
    index (int32): 

Returns:
    bool: 

    is_valid_index (bool):

<a id="unreal.GeometryScriptIndexList.duplicate_index_list"></a>

#### duplicate_index_list

```python
def duplicate_index_list() -> GeometryScriptIndexList
```

x.duplicate_index_list() -> GeometryScriptIndexList
Updates Duplicate List to be identical to Index List.

Returns:
    GeometryScriptIndexList: 

    duplicate_list (GeometryScriptIndexList):

<a id="unreal.GeometryScriptIndexList.convert_index_list_to_array"></a>

#### convert_index_list_to_array

```python
def convert_index_list_to_array() -> Array[int]
```

x.convert_index_list_to_array() -> Array[int32]
Populates Index Array with the integer values stored in the Index List.

Returns:
    Array[int32]: 

    index_array (Array[int32]):

<a id="unreal.GeometryScriptIndexList.clear_index_list"></a>

#### clear_index_list

```python
def clear_index_list(clear_value: int = 0) -> None
```

x.clear_index_list(clear_value=0) -> None
Set each value in Index List to the given Clear Value.

Args:
    clear_value (int32):

<a id="unreal.GeometryScriptTriangleList"></a>