## GeometryScriptColorList Objects

```python
class GeometryScriptColorList(StructBase)
```

Geometry Script Color List

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: GeometryScriptTypes.h

<a id="unreal.GeometryScriptColorList.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.GeometryScriptColorList.set_color_list_item"></a>

#### set_color_list_item

```python
def set_color_list_item(index: int, new_color: LinearColor) -> bool
```

x.set_color_list_item(index, new_color) -> bool
Updates the value of the FLinearColor stored in the Color List at the specified location.
If the Index is invalid, the operation will fail and bValidIndex will be set to false.

Args:
    index (int32): 
    new_color (LinearColor): 

Returns:
    bool: 

    is_valid_index (bool):

<a id="unreal.GeometryScriptColorList.get_color_list_length"></a>

#### get_color_list_length

```python
def get_color_list_length() -> int
```

x.get_color_list_length() -> int32
Returns the number of items in the Color List.

Returns:
    int32:

<a id="unreal.GeometryScriptColorList.get_color_list_last_index"></a>

#### get_color_list_last_index

```python
def get_color_list_last_index() -> int
```

x.get_color_list_last_index() -> int32
Returns the index of the last item in the Color List.
If Color List is empty or invalid, the value -1 will be returned.

Returns:
    int32:

<a id="unreal.GeometryScriptColorList.get_color_list_item"></a>

#### get_color_list_item

```python
def get_color_list_item(index: int) -> Tuple[LinearColor, bool]
```

x.get_color_list_item(index) -> (LinearColor, is_valid_index=bool)
Returns the FLinearColor stored in the Color List at the specified location.
If the Index is not valid for this Color List, FLinearColor::White will be returned and bIsValidIndex set to false.

Args:
    index (int32): 

Returns:
    bool: 

    is_valid_index (bool):

<a id="unreal.GeometryScriptColorList.extract_color_list_channels"></a>

#### extract_color_list_channels

```python
def extract_color_list_channels(
        x_channel_index: int = 0,
        y_channel_index: int = 1,
        z_channel_index: int = 2) -> GeometryScriptVectorList
```

x.extract_color_list_channels(x_channel_index=0, y_channel_index=1, z_channel_index=2) -> GeometryScriptVectorList
Populates a Vector List from a Color List. The channels in the Color List are mapped to vector components by means of X Channel Index, Y Channel Index, and Z Channel Index.

Args:
    x_channel_index (int32): 
    y_channel_index (int32): 
    z_channel_index (int32): 

Returns:
    GeometryScriptVectorList: 

    vector_list (GeometryScriptVectorList):

<a id="unreal.GeometryScriptColorList.extract_color_list_channel"></a>

#### extract_color_list_channel

```python
def extract_color_list_channel(
        channel_index: int = 0) -> GeometryScriptScalarList
```

x.extract_color_list_channel(channel_index=0) -> GeometryScriptScalarList
Populates a Scalar List with values that corresponds to the 0, 1, 2, or 3 channel of a Color List.

Args:
    channel_index (int32): 

Returns:
    GeometryScriptScalarList: 

    scalar_list (GeometryScriptScalarList):

<a id="unreal.GeometryScriptColorList.duplicate_color_list"></a>

#### duplicate_color_list

```python
def duplicate_color_list() -> GeometryScriptColorList
```

x.duplicate_color_list() -> GeometryScriptColorList
Duplicates the contents of Color List into Duplicate List.

Returns:
    GeometryScriptColorList: 

    duplicate_list (GeometryScriptColorList):

<a id="unreal.GeometryScriptColorList.convert_color_list_to_array"></a>

#### convert_color_list_to_array

```python
def convert_color_list_to_array() -> Array[LinearColor]
```

x.convert_color_list_to_array() -> Array[LinearColor]
Converts the Color List to an array of FLinearColor (Color Array).

Returns:
    Array[LinearColor]: 

    color_array (Array[LinearColor]):

<a id="unreal.GeometryScriptColorList.clear_color_list"></a>

#### clear_color_list

```python
def clear_color_list(clear_color: LinearColor) -> None
```

x.clear_color_list(clear_color) -> None
Resets all the items in the Color List to the specified Clear Color.

Args:
    clear_color (LinearColor):

<a id="unreal.GeometryScriptPolyPath"></a>