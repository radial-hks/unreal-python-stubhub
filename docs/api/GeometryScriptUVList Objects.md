## GeometryScriptUVList Objects

```python
class GeometryScriptUVList(StructBase)
```

Geometry Script UVList

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: GeometryScriptTypes.h

<a id="unreal.GeometryScriptUVList.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.GeometryScriptUVList.set_uv_list_item"></a>

#### set_uv_list_item

```python
def set_uv_list_item(index: int, new_uv: Vector2D) -> bool
```

x.set_uv_list_item(index, new_uv) -> bool
Updates the value of the FVector2D stored in the UV List at the specified location.
If the Index is invalid, the operation will fail and bValidIndex will be set to false on return.

Args:
    index (int32): 
    new_uv (Vector2D): 

Returns:
    bool: 

    is_valid_index (bool):

<a id="unreal.GeometryScriptUVList.get_uv_list_length"></a>

#### get_uv_list_length

```python
def get_uv_list_length() -> int
```

x.get_uv_list_length() -> int32
Returns the number of items in the UV List.

Returns:
    int32:

<a id="unreal.GeometryScriptUVList.get_uv_list_last_index"></a>

#### get_uv_list_last_index

```python
def get_uv_list_last_index() -> int
```

x.get_uv_list_last_index() -> int32
Returns the index of the last item in the UV List.
If UV List is empty or invalid, the value -1 will be returned.

Returns:
    int32:

<a id="unreal.GeometryScriptUVList.get_uv_list_item"></a>

#### get_uv_list_item

```python
def get_uv_list_item(index: int) -> Tuple[Vector2D, bool]
```

x.get_uv_list_item(index) -> (Vector2D, is_valid_index=bool)
Returns the FVector2D stored in the UV List at the specified location.
If the Index is not valid for this UV List, the Zero Vector will be returned and bIsValidIndex set to false.

Args:
    index (int32): 

Returns:
    bool: 

    is_valid_index (bool):

<a id="unreal.GeometryScriptUVList.duplicate_uv_list"></a>

#### duplicate_uv_list

```python
def duplicate_uv_list() -> GeometryScriptUVList
```

x.duplicate_uv_list() -> GeometryScriptUVList
Duplicates the contents of UV List into Duplicate List.

Returns:
    GeometryScriptUVList: 

    duplicate_list (GeometryScriptUVList):

<a id="unreal.GeometryScriptUVList.convert_uv_list_to_array"></a>

#### convert_uv_list_to_array

```python
def convert_uv_list_to_array() -> Array[Vector2D]
```

x.convert_uv_list_to_array() -> Array[Vector2D]
Converts a UV List to an array of FVector2Ds (UV Array).

Returns:
    Array[Vector2D]: 

    uv_array (Array[Vector2D]):

<a id="unreal.GeometryScriptUVList.clear_uv_list"></a>

#### clear_uv_list

```python
def clear_uv_list(clear_uv: Vector2D) -> None
```

x.clear_uv_list(clear_uv) -> None
Resets all the items in the Vector List to the given Clear UV value.

Args:
    clear_uv (Vector2D):

<a id="unreal.GeometryScriptColorList"></a>