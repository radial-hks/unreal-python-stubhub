## GeometryScript_List Objects

```python
class GeometryScript_List(BlueprintFunctionLibrary)
```

Geometry Script Library List Utility Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: ListUtilityFunctions.h

<a id="unreal.GeometryScript_List.set_vector_list_item"></a>

#### set_vector_list_item

```python
@classmethod
def set_vector_list_item(
        cls, vector_list: GeometryScriptVectorList, index: int,
        new_value: Vector) -> Tuple[GeometryScriptVectorList, bool]
```

X.set_vector_list_item(vector_list, index, new_value) -> (vector_list=GeometryScriptVectorList, is_valid_index=bool)
Updates the value of the FVector stored in the Vector List at the specified location.
If the Index is invalid, the operation will fail and bValidIndex will be set to false.

Args:
    vector_list (GeometryScriptVectorList): 
    index (int32): 
    new_value (Vector): 

Returns:
    tuple: 

    vector_list (GeometryScriptVectorList): 

    is_valid_index (bool):

<a id="unreal.GeometryScript_List.set_uv_list_item"></a>

#### set_uv_list_item

```python
@classmethod
def set_uv_list_item(cls, uv_list: GeometryScriptUVList, index: int,
                     new_uv: Vector2D) -> Tuple[GeometryScriptUVList, bool]
```

X.set_uv_list_item(uv_list, index, new_uv) -> (uv_list=GeometryScriptUVList, is_valid_index=bool)
Updates the value of the FVector2D stored in the UV List at the specified location.
If the Index is invalid, the operation will fail and bValidIndex will be set to false on return.

Args:
    uv_list (GeometryScriptUVList): 
    index (int32): 
    new_uv (Vector2D): 

Returns:
    tuple: 

    uv_list (GeometryScriptUVList): 

    is_valid_index (bool):

<a id="unreal.GeometryScript_List.set_scalar_list_item"></a>

#### set_scalar_list_item

```python
@classmethod
def set_scalar_list_item(
        cls, scalar_list: GeometryScriptScalarList, index: int,
        new_value: float) -> Tuple[GeometryScriptScalarList, bool]
```

X.set_scalar_list_item(scalar_list, index, new_value) -> (scalar_list=GeometryScriptScalarList, is_valid_index=bool)
Updates the value associated with Index in the Scalar List.
If the Index is invalid, the operation will fail and bValidIndex will be set to false.

Args:
    scalar_list (GeometryScriptScalarList): 
    index (int32): 
    new_value (double): 

Returns:
    tuple: 

    scalar_list (GeometryScriptScalarList): 

    is_valid_index (bool):

<a id="unreal.GeometryScript_List.set_index_list_item"></a>

#### set_index_list_item

```python
@classmethod
def set_index_list_item(
        cls, index_list: GeometryScriptIndexList, index: int,
        new_value: int) -> Tuple[GeometryScriptIndexList, bool]
```

X.set_index_list_item(index_list, index, new_value) -> (index_list=GeometryScriptIndexList, is_valid_index=bool)
Updates the value associated with Index in the Index List.
If the Index is invalid, the operation will fail and in this case bValidIndex will be set to false on return.

Args:
    index_list (GeometryScriptIndexList): 
    index (int32): 
    new_value (int32): 

Returns:
    tuple: 

    index_list (GeometryScriptIndexList): 

    is_valid_index (bool):

<a id="unreal.GeometryScript_List.set_color_list_item"></a>

#### set_color_list_item

```python
@classmethod
def set_color_list_item(
        cls, color_list: GeometryScriptColorList, index: int,
        new_color: LinearColor) -> Tuple[GeometryScriptColorList, bool]
```

X.set_color_list_item(color_list, index, new_color) -> (color_list=GeometryScriptColorList, is_valid_index=bool)
Updates the value of the FLinearColor stored in the Color List at the specified location.
If the Index is invalid, the operation will fail and bValidIndex will be set to false.

Args:
    color_list (GeometryScriptColorList): 
    index (int32): 
    new_color (LinearColor): 

Returns:
    tuple: 

    color_list (GeometryScriptColorList): 

    is_valid_index (bool):

<a id="unreal.GeometryScript_List.get_vector_list_length"></a>

#### get_vector_list_length

```python
@classmethod
def get_vector_list_length(cls, vector_list: GeometryScriptVectorList) -> int
```

X.get_vector_list_length(vector_list) -> int32
Returns the number of items in the Vector List.

Args:
    vector_list (GeometryScriptVectorList): 

Returns:
    int32:

<a id="unreal.GeometryScript_List.get_vector_list_last_index"></a>

#### get_vector_list_last_index

```python
@classmethod
def get_vector_list_last_index(cls,
                               vector_list: GeometryScriptVectorList) -> int
```

X.get_vector_list_last_index(vector_list) -> int32
Returns the index of the last item in the Vector List.
If Vector List is empty or invalid, the value -1 will be returned.

Args:
    vector_list (GeometryScriptVectorList): 

Returns:
    int32:

<a id="unreal.GeometryScript_List.get_vector_list_item"></a>

#### get_vector_list_item

```python
@classmethod
def get_vector_list_item(cls, vector_list: GeometryScriptVectorList,
                         index: int) -> Tuple[Vector, bool]
```

X.get_vector_list_item(vector_list, index) -> (Vector, is_valid_index=bool)
Returns the FVector stored in the VectorList at the specified location.
if the Index is not valid for this Vector List, the Zero Vector will be returned and bIsValidIndex set to false.

Args:
    vector_list (GeometryScriptVectorList): 
    index (int32): 

Returns:
    bool: 

    is_valid_index (bool):

<a id="unreal.GeometryScript_List.get_uv_list_length"></a>

#### get_uv_list_length

```python
@classmethod
def get_uv_list_length(cls, uv_list: GeometryScriptUVList) -> int
```

X.get_uv_list_length(uv_list) -> int32
Returns the number of items in the UV List.

Args:
    uv_list (GeometryScriptUVList): 

Returns:
    int32:

<a id="unreal.GeometryScript_List.get_uv_list_last_index"></a>

#### get_uv_list_last_index

```python
@classmethod
def get_uv_list_last_index(cls, uv_list: GeometryScriptUVList) -> int
```

X.get_uv_list_last_index(uv_list) -> int32
Returns the index of the last item in the UV List.
If UV List is empty or invalid, the value -1 will be returned.

Args:
    uv_list (GeometryScriptUVList): 

Returns:
    int32:

<a id="unreal.GeometryScript_List.get_uv_list_item"></a>

#### get_uv_list_item

```python
@classmethod
def get_uv_list_item(cls, uv_list: GeometryScriptUVList,
                     index: int) -> Tuple[Vector2D, bool]
```

X.get_uv_list_item(uv_list, index) -> (Vector2D, is_valid_index=bool)
Returns the FVector2D stored in the UV List at the specified location.
If the Index is not valid for this UV List, the Zero Vector will be returned and bIsValidIndex set to false.

Args:
    uv_list (GeometryScriptUVList): 
    index (int32): 

Returns:
    bool: 

    is_valid_index (bool):

<a id="unreal.GeometryScript_List.get_triangle_list_length"></a>

#### get_triangle_list_length

```python
@classmethod
def get_triangle_list_length(cls,
                             triangle_list: GeometryScriptTriangleList) -> int
```

X.get_triangle_list_length(triangle_list) -> int32
Returns the number of Triangles in the  Triangle list.

Args:
    triangle_list (GeometryScriptTriangleList): 

Returns:
    int32:

<a id="unreal.GeometryScript_List.get_triangle_list_last_triangle"></a>

#### get_triangle_list_last_triangle

```python
@classmethod
def get_triangle_list_last_triangle(
        cls, triangle_list: GeometryScriptTriangleList) -> int
```

X.get_triangle_list_last_triangle(triangle_list) -> int32
Returns the index of the last element in the Triangle List.
If the Triangle List is empty or invalid, the value 0 will be returned.

Args:
    triangle_list (GeometryScriptTriangleList): 

Returns:
    int32:

<a id="unreal.GeometryScript_List.get_triangle_list_item"></a>

#### get_triangle_list_item

```python
@classmethod
def get_triangle_list_item(cls, triangle_list: GeometryScriptTriangleList,
                           triangle: int) -> Tuple[IntVector, bool]
```

X.get_triangle_list_item(triangle_list, triangle) -> (IntVector, is_valid_triangle=bool)
Returns the integer triplet associated with the index Triangle in the Triangle  List.
If Triangle is not valid for this Triangle List, the triplet (-1, -1, -1) will be returned and bIsValidIndex set to false.

Args:
    triangle_list (GeometryScriptTriangleList): 
    triangle (int32): 

Returns:
    bool: 

    is_valid_triangle (bool):

<a id="unreal.GeometryScript_List.get_scalar_list_length"></a>

#### get_scalar_list_length

```python
@classmethod
def get_scalar_list_length(cls, scalar_list: GeometryScriptScalarList) -> int
```

X.get_scalar_list_length(scalar_list) -> int32
Returns the number of items in the Scalar List.

Args:
    scalar_list (GeometryScriptScalarList): 

Returns:
    int32:

<a id="unreal.GeometryScript_List.get_scalar_list_last_index"></a>

#### get_scalar_list_last_index

```python
@classmethod
def get_scalar_list_last_index(cls,
                               scalar_list: GeometryScriptScalarList) -> int
```

X.get_scalar_list_last_index(scalar_list) -> int32
Returns the index of the last Scalar in Scalar List.
If Scalar List is empty or invalid, the value -1 will be returned

Args:
    scalar_list (GeometryScriptScalarList): 

Returns:
    int32:

<a id="unreal.GeometryScript_List.get_scalar_list_item"></a>

#### get_scalar_list_item

```python
@classmethod
def get_scalar_list_item(cls, scalar_list: GeometryScriptScalarList,
                         index: int) -> Tuple[float, bool]
```

X.get_scalar_list_item(scalar_list, index) -> (double, is_valid_index=bool)
Returns the Scalar value associated with Index in Scalar List.
If the Index is not valid for this Scalar List, the value 0.0 will be returned and bIsValidIndex set to false.

Args:
    scalar_list (GeometryScriptScalarList): 
    index (int32): 

Returns:
    bool: 

    is_valid_index (bool):

<a id="unreal.GeometryScript_List.get_index_list_length"></a>

#### get_index_list_length

```python
@classmethod
def get_index_list_length(cls, index_list: GeometryScriptIndexList) -> int
```

X.get_index_list_length(index_list) -> int32
Returns the number of Items in Index List.

Args:
    index_list (GeometryScriptIndexList): 

Returns:
    int32:

<a id="unreal.GeometryScript_List.get_index_list_last_index"></a>

#### get_index_list_last_index

```python
@classmethod
def get_index_list_last_index(cls, index_list: GeometryScriptIndexList) -> int
```

X.get_index_list_last_index(index_list) -> int32
Returns the index of the last element in the Index List.
Note, the value -1 will be returned if the list is empty or invalid.

Args:
    index_list (GeometryScriptIndexList): 

Returns:
    int32:

<a id="unreal.GeometryScript_List.get_index_list_item"></a>

#### get_index_list_item

```python
@classmethod
def get_index_list_item(cls, index_list: GeometryScriptIndexList,
                        index: int) -> Tuple[int, bool]
```

X.get_index_list_item(index_list, index) -> (int32, is_valid_index=bool)
Returns the item associated with Index in the Index List.
If Index is not valid for this Index List the value -1 will be returned and bIsValidIndex will be set to false.

Args:
    index_list (GeometryScriptIndexList): 
    index (int32): 

Returns:
    bool: 

    is_valid_index (bool):

<a id="unreal.GeometryScript_List.get_color_list_length"></a>

#### get_color_list_length

```python
@classmethod
def get_color_list_length(cls, color_list: GeometryScriptColorList) -> int
```

X.get_color_list_length(color_list) -> int32
Returns the number of items in the Color List.

Args:
    color_list (GeometryScriptColorList): 

Returns:
    int32:

<a id="unreal.GeometryScript_List.get_color_list_last_index"></a>

#### get_color_list_last_index

```python
@classmethod
def get_color_list_last_index(cls, color_list: GeometryScriptColorList) -> int
```

X.get_color_list_last_index(color_list) -> int32
Returns the index of the last item in the Color List.
If Color List is empty or invalid, the value -1 will be returned.

Args:
    color_list (GeometryScriptColorList): 

Returns:
    int32:

<a id="unreal.GeometryScript_List.get_color_list_item"></a>

#### get_color_list_item

```python
@classmethod
def get_color_list_item(cls, color_list: GeometryScriptColorList,
                        index: int) -> Tuple[LinearColor, bool]
```

X.get_color_list_item(color_list, index) -> (LinearColor, is_valid_index=bool)
Returns the FLinearColor stored in the Color List at the specified location.
If the Index is not valid for this Color List, FLinearColor::White will be returned and bIsValidIndex set to false.

Args:
    color_list (GeometryScriptColorList): 
    index (int32): 

Returns:
    bool: 

    is_valid_index (bool):

<a id="unreal.GeometryScript_List.extract_color_list_channels"></a>

#### extract_color_list_channels

```python
@classmethod
def extract_color_list_channels(
        cls,
        color_list: GeometryScriptColorList,
        x_channel_index: int = 0,
        y_channel_index: int = 1,
        z_channel_index: int = 2) -> GeometryScriptVectorList
```

X.extract_color_list_channels(color_list, x_channel_index=0, y_channel_index=1, z_channel_index=2) -> GeometryScriptVectorList
Populates a Vector List from a Color List. The channels in the Color List are mapped to vector components by means of X Channel Index, Y Channel Index, and Z Channel Index.

Args:
    color_list (GeometryScriptColorList): 
    x_channel_index (int32): 
    y_channel_index (int32): 
    z_channel_index (int32): 

Returns:
    GeometryScriptVectorList: 

    vector_list (GeometryScriptVectorList):

<a id="unreal.GeometryScript_List.extract_color_list_channel"></a>

#### extract_color_list_channel

```python
@classmethod
def extract_color_list_channel(
        cls,
        color_list: GeometryScriptColorList,
        channel_index: int = 0) -> GeometryScriptScalarList
```

X.extract_color_list_channel(color_list, channel_index=0) -> GeometryScriptScalarList
Populates a Scalar List with values that corresponds to the 0, 1, 2, or 3 channel of a Color List.

Args:
    color_list (GeometryScriptColorList): 
    channel_index (int32): 

Returns:
    GeometryScriptScalarList: 

    scalar_list (GeometryScriptScalarList):

<a id="unreal.GeometryScript_List.duplicate_vector_list"></a>

#### duplicate_vector_list

```python
@classmethod
def duplicate_vector_list(
        cls,
        vector_list: GeometryScriptVectorList) -> GeometryScriptVectorList
```

X.duplicate_vector_list(vector_list) -> GeometryScriptVectorList
Copies the contents of Vector List into Duplicate Vector List.

Args:
    vector_list (GeometryScriptVectorList): 

Returns:
    GeometryScriptVectorList: 

    duplicate_list (GeometryScriptVectorList):

<a id="unreal.GeometryScript_List.duplicate_uv_list"></a>

#### duplicate_uv_list

```python
@classmethod
def duplicate_uv_list(cls,
                      uv_list: GeometryScriptUVList) -> GeometryScriptUVList
```

X.duplicate_uv_list(uv_list) -> GeometryScriptUVList
Duplicates the contents of UV List into Duplicate List.

Args:
    uv_list (GeometryScriptUVList): 

Returns:
    GeometryScriptUVList: 

    duplicate_list (GeometryScriptUVList):

<a id="unreal.GeometryScript_List.duplicate_scalar_list"></a>

#### duplicate_scalar_list

```python
@classmethod
def duplicate_scalar_list(
        cls,
        scalar_list: GeometryScriptScalarList) -> GeometryScriptScalarList
```

X.duplicate_scalar_list(scalar_list) -> GeometryScriptScalarList
Copies the contents of Scalar List into Duplicate List.

Args:
    scalar_list (GeometryScriptScalarList): 

Returns:
    GeometryScriptScalarList: 

    duplicate_list (GeometryScriptScalarList):

<a id="unreal.GeometryScript_List.duplicate_index_list"></a>

#### duplicate_index_list

```python
@classmethod
def duplicate_index_list(
        cls, index_list: GeometryScriptIndexList) -> GeometryScriptIndexList
```

X.duplicate_index_list(index_list) -> GeometryScriptIndexList
Updates Duplicate List to be identical to Index List.

Args:
    index_list (GeometryScriptIndexList): 

Returns:
    GeometryScriptIndexList: 

    duplicate_list (GeometryScriptIndexList):

<a id="unreal.GeometryScript_List.duplicate_color_list"></a>

#### duplicate_color_list

```python
@classmethod
def duplicate_color_list(
        cls, color_list: GeometryScriptColorList) -> GeometryScriptColorList
```

X.duplicate_color_list(color_list) -> GeometryScriptColorList
Duplicates the contents of Color List into Duplicate List.

Args:
    color_list (GeometryScriptColorList): 

Returns:
    GeometryScriptColorList: 

    duplicate_list (GeometryScriptColorList):

<a id="unreal.GeometryScript_List.convert_vector_list_to_array"></a>

#### convert_vector_list_to_array

```python
@classmethod
def convert_vector_list_to_array(
        cls, vector_list: GeometryScriptVectorList) -> Array[Vector]
```

X.convert_vector_list_to_array(vector_list) -> Array[Vector]
Converts Vector List to an array of FVectors (Vector Array).

Args:
    vector_list (GeometryScriptVectorList): 

Returns:
    Array[Vector]: 

    vector_array (Array[Vector]):

<a id="unreal.GeometryScript_List.convert_uv_list_to_array"></a>

#### convert_uv_list_to_array

```python
@classmethod
def convert_uv_list_to_array(cls,
                             uv_list: GeometryScriptUVList) -> Array[Vector2D]
```

X.convert_uv_list_to_array(uv_list) -> Array[Vector2D]
Converts a UV List to an array of FVector2Ds (UV Array).

Args:
    uv_list (GeometryScriptUVList): 

Returns:
    Array[Vector2D]: 

    uv_array (Array[Vector2D]):

<a id="unreal.GeometryScript_List.convert_triangle_list_to_array"></a>

#### convert_triangle_list_to_array

```python
@classmethod
def convert_triangle_list_to_array(
        cls, triangle_list: GeometryScriptTriangleList) -> Array[IntVector]
```

X.convert_triangle_list_to_array(triangle_list) -> Array[IntVector]
Converts Triangle List to Triangle Array by populating with the appropriate integer triplets.

Args:
    triangle_list (GeometryScriptTriangleList): 

Returns:
    Array[IntVector]: 

    triangle_array (Array[IntVector]):

<a id="unreal.GeometryScript_List.convert_scalar_list_to_array"></a>

#### convert_scalar_list_to_array

```python
@classmethod
def convert_scalar_list_to_array(
        cls, scalar_list: GeometryScriptScalarList) -> Array[float]
```

X.convert_scalar_list_to_array(scalar_list) -> Array[double]
Converts a Scalar List to an Scalar Array (an array of doubles).

Args:
    scalar_list (GeometryScriptScalarList): 

Returns:
    Array[double]: 

    scalar_array (Array[double]):

<a id="unreal.GeometryScript_List.convert_index_list_to_array"></a>

#### convert_index_list_to_array

```python
@classmethod
def convert_index_list_to_array(
        cls, index_list: GeometryScriptIndexList) -> Array[int]
```

X.convert_index_list_to_array(index_list) -> Array[int32]
Populates Index Array with the integer values stored in the Index List.

Args:
    index_list (GeometryScriptIndexList): 

Returns:
    Array[int32]: 

    index_array (Array[int32]):

<a id="unreal.GeometryScript_List.convert_color_list_to_array"></a>

#### convert_color_list_to_array

```python
@classmethod
def convert_color_list_to_array(
        cls, color_list: GeometryScriptColorList) -> Array[LinearColor]
```

X.convert_color_list_to_array(color_list) -> Array[LinearColor]
Converts the Color List to an array of FLinearColor (Color Array).

Args:
    color_list (GeometryScriptColorList): 

Returns:
    Array[LinearColor]: 

    color_array (Array[LinearColor]):

<a id="unreal.GeometryScript_List.convert_array_to_vector_list"></a>

#### convert_array_to_vector_list

```python
@classmethod
def convert_array_to_vector_list(
        cls, vector_array: Array[Vector]) -> GeometryScriptVectorList
```

X.convert_array_to_vector_list(vector_array) -> GeometryScriptVectorList
Converts an Array of FVectors (Vector Array) to Vector List.

Args:
    vector_array (Array[Vector]): 

Returns:
    GeometryScriptVectorList: 

    vector_list (GeometryScriptVectorList):

<a id="unreal.GeometryScript_List.convert_array_to_uv_list"></a>

#### convert_array_to_uv_list

```python
@classmethod
def convert_array_to_uv_list(
        cls, uv_array: Array[Vector2D]) -> GeometryScriptUVList
```

X.convert_array_to_uv_list(uv_array) -> GeometryScriptUVList
Converts an array of FVector2D (UV Array) to UV List.

Args:
    uv_array (Array[Vector2D]): 

Returns:
    GeometryScriptUVList: 

    uv_list (GeometryScriptUVList):

<a id="unreal.GeometryScript_List.convert_array_to_triangle_list"></a>

#### convert_array_to_triangle_list

```python
@classmethod
def convert_array_to_triangle_list(
        cls, triangle_array: Array[IntVector]) -> GeometryScriptTriangleList
```

X.convert_array_to_triangle_list(triangle_array) -> GeometryScriptTriangleList
Converts a Triangle Array of integer triplets to a Triangle List.

Args:
    triangle_array (Array[IntVector]): 

Returns:
    GeometryScriptTriangleList: 

    triangle_list (GeometryScriptTriangleList):

<a id="unreal.GeometryScript_List.convert_array_to_scalar_list"></a>

#### convert_array_to_scalar_list

```python
@classmethod
def convert_array_to_scalar_list(
        cls, vector_array: Array[float]) -> GeometryScriptScalarList
```

X.convert_array_to_scalar_list(vector_array) -> GeometryScriptScalarList
Converts an array of doubles (Scalar Array) to Scalar List.

Args:
    vector_array (Array[double]): 

Returns:
    GeometryScriptScalarList: 

    scalar_list (GeometryScriptScalarList):

<a id="unreal.GeometryScript_List.convert_array_to_index_list"></a>

#### convert_array_to_index_list

```python
@classmethod
def convert_array_to_index_list(
    cls,
    index_array: Array[int],
    index_type: GeometryScriptIndexType = GeometryScriptIndexType.ANY
) -> GeometryScriptIndexList
```

X.convert_array_to_index_list(index_array, index_type=GeometryScriptIndexType.ANY) -> GeometryScriptIndexList
Populates Index List of the specified Index Type from the integer values stored in the Index Array.

Args:
    index_array (Array[int32]): 
    index_type (GeometryScriptIndexType): 

Returns:
    GeometryScriptIndexList: 

    index_list (GeometryScriptIndexList):

<a id="unreal.GeometryScript_List.convert_array_to_color_list"></a>

#### convert_array_to_color_list

```python
@classmethod
def convert_array_to_color_list(
        cls, color_array: Array[LinearColor]) -> GeometryScriptColorList
```

X.convert_array_to_color_list(color_array) -> GeometryScriptColorList
Converts an array of FLinearColor (Color Array) to a Color List.

Args:
    color_array (Array[LinearColor]): 

Returns:
    GeometryScriptColorList: 

    color_list (GeometryScriptColorList):

<a id="unreal.GeometryScript_List.clear_vector_list"></a>

#### clear_vector_list

```python
@classmethod
def clear_vector_list(
    cls,
    vector_list: GeometryScriptVectorList,
    clear_value: Vector = [0.000000, 0.000000, 0.000000]
) -> GeometryScriptVectorList
```

X.clear_vector_list(vector_list, clear_value=[0.000000, 0.000000, 0.000000]) -> GeometryScriptVectorList
Resets all the items in the Vector List to the Clear Value.

Args:
    vector_list (GeometryScriptVectorList): 
    clear_value (Vector): 

Returns:
    GeometryScriptVectorList: 

    vector_list (GeometryScriptVectorList):

<a id="unreal.GeometryScript_List.clear_uv_list"></a>

#### clear_uv_list

```python
@classmethod
def clear_uv_list(cls, uv_list: GeometryScriptUVList,
                  clear_uv: Vector2D) -> GeometryScriptUVList
```

X.clear_uv_list(uv_list, clear_uv) -> GeometryScriptUVList
Resets all the items in the Vector List to the given Clear UV value.

Args:
    uv_list (GeometryScriptUVList): 
    clear_uv (Vector2D): 

Returns:
    GeometryScriptUVList: 

    uv_list (GeometryScriptUVList):

<a id="unreal.GeometryScript_List.clear_scalar_list"></a>

#### clear_scalar_list

```python
@classmethod
def clear_scalar_list(
        cls,
        scalar_list: GeometryScriptScalarList,
        clear_value: float = 0.000000) -> GeometryScriptScalarList
```

X.clear_scalar_list(scalar_list, clear_value=0.000000) -> GeometryScriptScalarList
Resets all the items in the Scalar List to the Clear Value.

Args:
    scalar_list (GeometryScriptScalarList): 
    clear_value (double): 

Returns:
    GeometryScriptScalarList: 

    scalar_list (GeometryScriptScalarList):

<a id="unreal.GeometryScript_List.clear_index_list"></a>

#### clear_index_list

```python
@classmethod
def clear_index_list(cls,
                     index_list: GeometryScriptIndexList,
                     clear_value: int = 0) -> GeometryScriptIndexList
```

X.clear_index_list(index_list, clear_value=0) -> GeometryScriptIndexList
Set each value in Index List to the given Clear Value.

Args:
    index_list (GeometryScriptIndexList): 
    clear_value (int32): 

Returns:
    GeometryScriptIndexList: 

    index_list (GeometryScriptIndexList):

<a id="unreal.GeometryScript_List.clear_color_list"></a>

#### clear_color_list

```python
@classmethod
def clear_color_list(cls, color_list: GeometryScriptColorList,
                     clear_color: LinearColor) -> GeometryScriptColorList
```

X.clear_color_list(color_list, clear_color) -> GeometryScriptColorList
Resets all the items in the Color List to the specified Clear Color.

Args:
    color_list (GeometryScriptColorList): 
    clear_color (LinearColor): 

Returns:
    GeometryScriptColorList: 

    color_list (GeometryScriptColorList):

<a id="unreal.GeometryScript_AssetUtils"></a>