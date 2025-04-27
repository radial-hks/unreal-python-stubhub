## GeometryScriptGeneralPolygonList Objects

```python
class GeometryScriptGeneralPolygonList(StructBase)
```

A list of general polygons, which may have holes.

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: GeometryScriptTypes.h

<a id="unreal.GeometryScriptGeneralPolygonList.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.GeometryScriptGeneralPolygonList.polygons_union"></a>

#### polygons_union

```python
def polygons_union(
        copy_input_on_failure: bool = True
) -> GeometryScriptGeneralPolygonList
```

x.polygons_union(copy_input_on_failure=True) -> GeometryScriptGeneralPolygonList
Compute union of all polygons in Polygon List. Also resolves self-intersections within each polygon.

Args:
    copy_input_on_failure (bool): 

Returns:
    GeometryScriptGeneralPolygonList:

<a id="unreal.GeometryScriptGeneralPolygonList.polygons_offsets"></a>

#### polygons_offsets

```python
def polygons_offsets(
    offset_options: GeometryScriptPolygonOffsetOptions,
    first_offset: float,
    second_offset: float,
    copy_input_on_failure: bool = True
) -> Tuple[GeometryScriptGeneralPolygonList, bool]
```

x.polygons_offsets(offset_options, first_offset, second_offset, copy_input_on_failure=True) -> (GeometryScriptGeneralPolygonList, operation_success=bool)
Apply two offsets in sequence to a list of closed polygons

Args:
    offset_options (GeometryScriptPolygonOffsetOptions): 
    first_offset (double): 
    second_offset (double): 
    copy_input_on_failure (bool): 

Returns:
    bool: 

    operation_success (bool):

<a id="unreal.GeometryScriptGeneralPolygonList.polygons_offset"></a>

#### polygons_offset

```python
def polygons_offset(
    offset_options: GeometryScriptPolygonOffsetOptions,
    offset: float,
    copy_input_on_failure: bool = True
) -> Tuple[GeometryScriptGeneralPolygonList, bool]
```

x.polygons_offset(offset_options, offset, copy_input_on_failure=True) -> (GeometryScriptGeneralPolygonList, operation_success=bool)
Apply a single offset to a list of closed polygons

Args:
    offset_options (GeometryScriptPolygonOffsetOptions): 
    offset (double): 
    copy_input_on_failure (bool): 

Returns:
    bool: 

    operation_success (bool):

<a id="unreal.GeometryScriptGeneralPolygonList.polygons_morphology_open"></a>

#### polygons_morphology_open

```python
def polygons_morphology_open(
    offset_options: GeometryScriptPolygonOffsetOptions,
    offset: float,
    copy_input_on_failure: bool = True
) -> Tuple[GeometryScriptGeneralPolygonList, bool]
```

x.polygons_morphology_open(offset_options, offset, copy_input_on_failure=True) -> (GeometryScriptGeneralPolygonList, operation_success=bool)
Apply a morphological "open" operator to a list of closed polygons -- first offsetting by -Offset, then by +Offset. If Offset is negative, this will instead function as a 'Close' operation

Args:
    offset_options (GeometryScriptPolygonOffsetOptions): 
    offset (double): 
    copy_input_on_failure (bool): 

Returns:
    bool: 

    operation_success (bool):

<a id="unreal.GeometryScriptGeneralPolygonList.polygons_morphology_close"></a>

#### polygons_morphology_close

```python
def polygons_morphology_close(
    offset_options: GeometryScriptPolygonOffsetOptions,
    offset: float,
    copy_input_on_failure: bool = True
) -> Tuple[GeometryScriptGeneralPolygonList, bool]
```

x.polygons_morphology_close(offset_options, offset, copy_input_on_failure=True) -> (GeometryScriptGeneralPolygonList, operation_success=bool)
Apply a morphological "close" operator to a list of closed polygons -- first offsetting by +Offset, then by -Offset. If Offset is negative, this will instead function as an 'Open' operation

Args:
    offset_options (GeometryScriptPolygonOffsetOptions): 
    offset (double): 
    copy_input_on_failure (bool): 

Returns:
    bool: 

    operation_success (bool):

<a id="unreal.GeometryScriptGeneralPolygonList.polygons_intersection"></a>

#### polygons_intersection

```python
def polygons_intersection(
    polygons_to_intersect: GeometryScriptGeneralPolygonList
) -> GeometryScriptGeneralPolygonList
```

x.polygons_intersection(polygons_to_intersect) -> GeometryScriptGeneralPolygonList
Compute intersection of Polygon List and Polygons to Intersect

Args:
    polygons_to_intersect (GeometryScriptGeneralPolygonList): 

Returns:
    GeometryScriptGeneralPolygonList:

<a id="unreal.GeometryScriptGeneralPolygonList.polygons_exclusive_or"></a>

#### polygons_exclusive_or

```python
def polygons_exclusive_or(
    polygons_to_exclusive_or: GeometryScriptGeneralPolygonList
) -> GeometryScriptGeneralPolygonList
```

x.polygons_exclusive_or(polygons_to_exclusive_or) -> GeometryScriptGeneralPolygonList
Compute exclusive or of Polygon List and Polygons to Exclusive Or

Args:
    polygons_to_exclusive_or (GeometryScriptGeneralPolygonList): 

Returns:
    GeometryScriptGeneralPolygonList:

<a id="unreal.GeometryScriptGeneralPolygonList.polygons_difference"></a>

#### polygons_difference

```python
def polygons_difference(
    polygons_to_subtract: GeometryScriptGeneralPolygonList
) -> GeometryScriptGeneralPolygonList
```

x.polygons_difference(polygons_to_subtract) -> GeometryScriptGeneralPolygonList
Compute difference of Polygon List and Polygons to Subtract

Args:
    polygons_to_subtract (GeometryScriptGeneralPolygonList): 

Returns:
    GeometryScriptGeneralPolygonList:

<a id="unreal.GeometryScriptGeneralPolygonList.get_simple_polygon"></a>

#### get_simple_polygon

```python
def get_simple_polygon(
        polygon_index: int,
        hole_index: int = -1) -> Tuple[GeometryScriptSimplePolygon, bool]
```

x.get_simple_polygon(polygon_index, hole_index=-1) -> (GeometryScriptSimplePolygon, valid_indices=bool)
Returns a specified Simple Polygon from a Polygon List -- either the outer polygon, if HoleIndex is -1, or specified inner hole.
Polygon will be empty for invalid Polygon or Hole indices.

Args:
    polygon_index (int32): 
    hole_index (int32): 

Returns:
    bool: 

    valid_indices (bool):

<a id="unreal.GeometryScriptGeneralPolygonList.get_polygon_vertices"></a>

#### get_polygon_vertices

```python
def get_polygon_vertices(polygon_index: int,
                         hole_index: int = -1) -> Tuple[Array[Vector2D], bool]
```

x.get_polygon_vertices(polygon_index, hole_index=-1) -> (out_vertices=Array[Vector2D], valid_indices=bool)
Returns the vertices of a Polygon -- either of the outer polygon, if HoleIndex is -1, or specified inner hole.
OutVertices will be empty for invalid Polygon or Hole indices.

Args:
    polygon_index (int32): 
    hole_index (int32): 

Returns:
    tuple: 

    out_vertices (Array[Vector2D]): 

    valid_indices (bool):

<a id="unreal.GeometryScriptGeneralPolygonList.get_polygon_vertex_count"></a>

#### get_polygon_vertex_count

```python
def get_polygon_vertex_count(polygon_index: int,
                             hole_index: int = -1) -> Tuple[int, bool]
```

x.get_polygon_vertex_count(polygon_index, hole_index=-1) -> (int32, valid_indices=bool)
Returns the number of vertices in a Polygon's outer shape, if HoleIndex is -1, or in the specified inner hole.
Returns 0 for invalid Polygon or Hole indices.

Args:
    polygon_index (int32): 
    hole_index (int32): 

Returns:
    bool: 

    valid_indices (bool):

<a id="unreal.GeometryScriptGeneralPolygonList.get_polygon_vertex"></a>

#### get_polygon_vertex

```python
def get_polygon_vertex(vertex_index: int,
                       polygon_index: int,
                       hole_index: int = -1) -> Tuple[Vector2D, bool]
```

x.get_polygon_vertex(vertex_index, polygon_index, hole_index=-1) -> (Vector2D, is_valid_vertex=bool)
Returns the specified vertex of a Polygon -- either of the outer polygon, if HoleIndex is -1, or specified inner hole.
Vertex will be the zero vector for invalid Polygon or Hole indices, or if the polygon is empty. VertexIndex will loop.

Args:
    vertex_index (int32): 
    polygon_index (int32): 
    hole_index (int32): 

Returns:
    bool: 

    is_valid_vertex (bool):

<a id="unreal.GeometryScriptGeneralPolygonList.get_polygon_list_bounds"></a>

#### get_polygon_list_bounds

```python
def get_polygon_list_bounds() -> Box2D
```

x.get_polygon_list_bounds() -> Box2D
Returns the bounding box of a Polygon

Returns:
    Box2D:

<a id="unreal.GeometryScriptGeneralPolygonList.get_polygon_list_area"></a>

#### get_polygon_list_area

```python
def get_polygon_list_area() -> float
```

x.get_polygon_list_area() -> double
Returns the area enclosed by a Polygon

Returns:
    double:

<a id="unreal.GeometryScriptGeneralPolygonList.get_polygon_hole_count"></a>

#### get_polygon_hole_count

```python
def get_polygon_hole_count(polygon_index: int) -> Tuple[int, bool]
```

x.get_polygon_hole_count(polygon_index) -> (int32, valid_index=bool)
Returns the number of holes in a Polygon. Returns zero for an invalid PolygonIndex.

Args:
    polygon_index (int32): 

Returns:
    bool: 

    valid_index (bool):

<a id="unreal.GeometryScriptGeneralPolygonList.get_polygon_count"></a>

#### get_polygon_count

```python
def get_polygon_count() -> int
```

x.get_polygon_count() -> int32
Returns the number of polygons in the Polygon List

Returns:
    int32:

<a id="unreal.GeometryScriptGeneralPolygonList.get_polygon_bounds"></a>

#### get_polygon_bounds

```python
def get_polygon_bounds(polygon_index: int) -> Tuple[Box2D, bool]
```

x.get_polygon_bounds(polygon_index) -> (Box2D, valid_index=bool)
Returns the bounding box of a Polygon. Returns an empty, invalid box for an invalid PolygonIndex.

Args:
    polygon_index (int32): 

Returns:
    bool: 

    valid_index (bool):

<a id="unreal.GeometryScriptGeneralPolygonList.get_polygon_area"></a>

#### get_polygon_area

```python
def get_polygon_area(polygon_index: int) -> Tuple[float, bool]
```

x.get_polygon_area(polygon_index) -> (double, valid_index=bool)
Returns the area enclosed by a Polygon. Returns zero for an invalid PolygonIndex.

Args:
    polygon_index (int32): 

Returns:
    bool: 

    valid_index (bool):

<a id="unreal.GeometryScriptGeneralPolygonList.append_polygon_list"></a>

#### append_polygon_list

```python
def append_polygon_list(
        polygons_to_append: GeometryScriptGeneralPolygonList) -> None
```

x.append_polygon_list(polygons_to_append) -> None
Append the polygons in 'Polygons to Append' to Polygon List

Args:
    polygons_to_append (GeometryScriptGeneralPolygonList):

<a id="unreal.GeometryScriptGeneralPolygonList.add_polygon_to_list"></a>

#### add_polygon_to_list

```python
def add_polygon_to_list(outer_polygon: GeometryScriptSimplePolygon,
                        hole_polygons: Array[GeometryScriptSimplePolygon],
                        fix_hole_orientations: bool = True) -> int
```

x.add_polygon_to_list(outer_polygon, hole_polygons, fix_hole_orientations=True) -> int32
Add Polygon to a Polygon List, with optional holes. Returns index of the added polygon.

Args:
    outer_polygon (GeometryScriptSimplePolygon): 
    hole_polygons (Array[GeometryScriptSimplePolygon]): 
    fix_hole_orientations (bool): 

Returns:
    int32:

<a id="unreal.GeometryScriptDynamicMeshBVH"></a>