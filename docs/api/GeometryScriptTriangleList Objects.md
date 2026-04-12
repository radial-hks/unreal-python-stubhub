## GeometryScriptTriangleList Objects

```python
class GeometryScriptTriangleList(StructBase)
```

Geometry Script Triangle List

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: GeometryScriptTypes.h

<a id="unreal.GeometryScriptTriangleList.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.GeometryScriptTriangleList.get_triangle_list_length"></a>

#### get\_triangle\_list\_length

```python
def get_triangle_list_length() -> int
```

x.get_triangle_list_length() -> int32
Returns the number of Triangles in the  Triangle list.

Returns:
    int32:

<a id="unreal.GeometryScriptTriangleList.get_triangle_list_last_triangle"></a>

#### get\_triangle\_list\_last\_triangle

```python
def get_triangle_list_last_triangle() -> int
```

x.get_triangle_list_last_triangle() -> int32
Returns the index of the last element in the Triangle List.
If the Triangle List is empty or invalid, the value 0 will be returned.

Returns:
    int32:

<a id="unreal.GeometryScriptTriangleList.get_triangle_list_item"></a>

#### get\_triangle\_list\_item

```python
def get_triangle_list_item(triangle: int) -> Tuple[IntVector, bool]
```

x.get_triangle_list_item(triangle) -> (IntVector, is_valid_triangle=bool)
Returns the integer triplet associated with the index Triangle in the Triangle  List.
If Triangle is not valid for this Triangle List, the triplet (-1, -1, -1) will be returned and bIsValidIndex set to false.

Args:
    triangle (int32): 

Returns:
    bool: 

    is_valid_triangle (bool):

<a id="unreal.GeometryScriptTriangleList.convert_triangle_list_to_array"></a>

#### convert\_triangle\_list\_to\_array

```python
def convert_triangle_list_to_array() -> Array[IntVector]
```

x.convert_triangle_list_to_array() -> Array[IntVector]
Converts Triangle List to Triangle Array by populating with the appropriate integer triplets.

Returns:
    Array[IntVector]: 

    triangle_array (Array[IntVector]):

<a id="unreal.GeometryScriptScalarList"></a>