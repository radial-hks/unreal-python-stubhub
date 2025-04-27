## GeometryScript_PolygonList Objects

```python
class GeometryScript_PolygonList(BlueprintFunctionLibrary)
```

Geometry Script Library Polygon List Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: PolygonFunctions.h

<a id="unreal.GeometryScript_PolygonList.polygons_union"></a>

#### polygons_union

```python
@classmethod
def polygons_union(
        cls,
        polygon_list: GeometryScriptGeneralPolygonList,
        copy_input_on_failure: bool = True
) -> GeometryScriptGeneralPolygonList
```

X.polygons_union(polygon_list, copy_input_on_failure=True) -> GeometryScriptGeneralPolygonList
Compute union of all polygons in Polygon List. Also resolves self-intersections within each polygon.

Args:
    polygon_list (GeometryScriptGeneralPolygonList): 
    copy_input_on_failure (bool): 

Returns:
    GeometryScriptGeneralPolygonList:

<a id="unreal.GeometryScript_PolygonList.polygons_offsets"></a>

#### polygons_offsets

```python
@classmethod
def polygons_offsets(
    cls,
    polygon_list: GeometryScriptGeneralPolygonList,
    offset_options: GeometryScriptPolygonOffsetOptions,
    first_offset: float,
    second_offset: float,
    copy_input_on_failure: bool = True
) -> Tuple[GeometryScriptGeneralPolygonList, bool]
```

X.polygons_offsets(polygon_list, offset_options, first_offset, second_offset, copy_input_on_failure=True) -> (GeometryScriptGeneralPolygonList, operation_success=bool)
Apply two offsets in sequence to a list of closed polygons

Args:
    polygon_list (GeometryScriptGeneralPolygonList): 
    offset_options (GeometryScriptPolygonOffsetOptions): 
    first_offset (double): 
    second_offset (double): 
    copy_input_on_failure (bool): 

Returns:
    bool: 

    operation_success (bool):

<a id="unreal.GeometryScript_PolygonList.polygons_offset"></a>

#### polygons_offset

```python
@classmethod
def polygons_offset(
    cls,
    polygon_list: GeometryScriptGeneralPolygonList,
    offset_options: GeometryScriptPolygonOffsetOptions,
    offset: float,
    copy_input_on_failure: bool = True
) -> Tuple[GeometryScriptGeneralPolygonList, bool]
```

X.polygons_offset(polygon_list, offset_options, offset, copy_input_on_failure=True) -> (GeometryScriptGeneralPolygonList, operation_success=bool)
Apply a single offset to a list of closed polygons

Args:
    polygon_list (GeometryScriptGeneralPolygonList): 
    offset_options (GeometryScriptPolygonOffsetOptions): 
    offset (double): 
    copy_input_on_failure (bool): 

Returns:
    bool: 

    operation_success (bool):

<a id="unreal.GeometryScript_PolygonList.polygons_morphology_open"></a>

#### polygons_morphology_open

```python
@classmethod
def polygons_morphology_open(
    cls,
    polygon_list: GeometryScriptGeneralPolygonList,
    offset_options: GeometryScriptPolygonOffsetOptions,
    offset: float,
    copy_input_on_failure: bool = True
) -> Tuple[GeometryScriptGeneralPolygonList, bool]
```

X.polygons_morphology_open(polygon_list, offset_options, offset, copy_input_on_failure=True) -> (GeometryScriptGeneralPolygonList, operation_success=bool)
Apply a morphological "open" operator to a list of closed polygons -- first offsetting by -Offset, then by +Offset. If Offset is negative, this will instead function as a 'Close' operation

Args:
    polygon_list (GeometryScriptGeneralPolygonList): 
    offset_options (GeometryScriptPolygonOffsetOptions): 
    offset (double): 
    copy_input_on_failure (bool): 

Returns:
    bool: 

    operation_success (bool):

<a id="unreal.GeometryScript_PolygonList.polygons_morphology_close"></a>

#### polygons_morphology_close

```python
@classmethod
def polygons_morphology_close(
    cls,
    polygon_list: GeometryScriptGeneralPolygonList,
    offset_options: GeometryScriptPolygonOffsetOptions,
    offset: float,
    copy_input_on_failure: bool = True
) -> Tuple[GeometryScriptGeneralPolygonList, bool]
```

X.polygons_morphology_close(polygon_list, offset_options, offset, copy_input_on_failure=True) -> (GeometryScriptGeneralPolygonList, operation_success=bool)
Apply a morphological "close" operator to a list of closed polygons -- first offsetting by +Offset, then by -Offset. If Offset is negative, this will instead function as an 'Open' operation

Args:
    polygon_list (GeometryScriptGeneralPolygonList): 
    offset_options (GeometryScriptPolygonOffsetOptions): 
    offset (double): 
    copy_input_on_failure (bool): 

Returns:
    bool: 

    operation_success (bool):

<a id="unreal.GeometryScript_PolygonList.polygons_intersection"></a>

#### polygons_intersection

```python
@classmethod
def polygons_intersection(
    cls, polygon_list: GeometryScriptGeneralPolygonList,
    polygons_to_intersect: GeometryScriptGeneralPolygonList
) -> GeometryScriptGeneralPolygonList
```

X.polygons_intersection(polygon_list, polygons_to_intersect) -> GeometryScriptGeneralPolygonList
Compute intersection of Polygon List and Polygons to Intersect

Args:
    polygon_list (GeometryScriptGeneralPolygonList): 
    polygons_to_intersect (GeometryScriptGeneralPolygonList): 

Returns:
    GeometryScriptGeneralPolygonList:

<a id="unreal.GeometryScript_PolygonList.polygons_exclusive_or"></a>

#### polygons_exclusive_or

```python
@classmethod
def polygons_exclusive_or(
    cls, polygon_list: GeometryScriptGeneralPolygonList,
    polygons_to_exclusive_or: GeometryScriptGeneralPolygonList
) -> GeometryScriptGeneralPolygonList
```

X.polygons_exclusive_or(polygon_list, polygons_to_exclusive_or) -> GeometryScriptGeneralPolygonList
Compute exclusive or of Polygon List and Polygons to Exclusive Or

Args:
    polygon_list (GeometryScriptGeneralPolygonList): 
    polygons_to_exclusive_or (GeometryScriptGeneralPolygonList): 

Returns:
    GeometryScriptGeneralPolygonList:

<a id="unreal.GeometryScript_PolygonList.polygons_difference"></a>

#### polygons_difference

```python
@classmethod
def polygons_difference(
    cls, polygon_list: GeometryScriptGeneralPolygonList,
    polygons_to_subtract: GeometryScriptGeneralPolygonList
) -> GeometryScriptGeneralPolygonList
```

X.polygons_difference(polygon_list, polygons_to_subtract) -> GeometryScriptGeneralPolygonList
Compute difference of Polygon List and Polygons to Subtract

Args:
    polygon_list (GeometryScriptGeneralPolygonList): 
    polygons_to_subtract (GeometryScriptGeneralPolygonList): 

Returns:
    GeometryScriptGeneralPolygonList:

<a id="unreal.GeometryScript_PolygonList.get_simple_polygon"></a>

#### get_simple_polygon

```python
@classmethod
def get_simple_polygon(
        cls,
        polygon_list: GeometryScriptGeneralPolygonList,
        polygon_index: int,
        hole_index: int = -1) -> Tuple[GeometryScriptSimplePolygon, bool]
```

X.get_simple_polygon(polygon_list, polygon_index, hole_index=-1) -> (GeometryScriptSimplePolygon, valid_indices=bool)
Returns a specified Simple Polygon from a Polygon List -- either the outer polygon, if HoleIndex is -1, or specified inner hole.
Polygon will be empty for invalid Polygon or Hole indices.

Args:
    polygon_list (GeometryScriptGeneralPolygonList): 
    polygon_index (int32): 
    hole_index (int32): 

Returns:
    bool: 

    valid_indices (bool):

<a id="unreal.GeometryScript_PolygonList.get_polygon_vertices"></a>

#### get_polygon_vertices

```python
@classmethod
def get_polygon_vertices(cls,
                         polygon_list: GeometryScriptGeneralPolygonList,
                         polygon_index: int,
                         hole_index: int = -1) -> Tuple[Array[Vector2D], bool]
```

X.get_polygon_vertices(polygon_list, polygon_index, hole_index=-1) -> (out_vertices=Array[Vector2D], valid_indices=bool)
Returns the vertices of a Polygon -- either of the outer polygon, if HoleIndex is -1, or specified inner hole.
OutVertices will be empty for invalid Polygon or Hole indices.

Args:
    polygon_list (GeometryScriptGeneralPolygonList): 
    polygon_index (int32): 
    hole_index (int32): 

Returns:
    tuple: 

    out_vertices (Array[Vector2D]): 

    valid_indices (bool):

<a id="unreal.GeometryScript_PolygonList.get_polygon_vertex_count"></a>

#### get_polygon_vertex_count

```python
@classmethod
def get_polygon_vertex_count(cls,
                             polygon_list: GeometryScriptGeneralPolygonList,
                             polygon_index: int,
                             hole_index: int = -1) -> Tuple[int, bool]
```

X.get_polygon_vertex_count(polygon_list, polygon_index, hole_index=-1) -> (int32, valid_indices=bool)
Returns the number of vertices in a Polygon's outer shape, if HoleIndex is -1, or in the specified inner hole.
Returns 0 for invalid Polygon or Hole indices.

Args:
    polygon_list (GeometryScriptGeneralPolygonList): 
    polygon_index (int32): 
    hole_index (int32): 

Returns:
    bool: 

    valid_indices (bool):

<a id="unreal.GeometryScript_PolygonList.get_polygon_vertex"></a>

#### get_polygon_vertex

```python
@classmethod
def get_polygon_vertex(cls,
                       polygon_list: GeometryScriptGeneralPolygonList,
                       vertex_index: int,
                       polygon_index: int,
                       hole_index: int = -1) -> Tuple[Vector2D, bool]
```

X.get_polygon_vertex(polygon_list, vertex_index, polygon_index, hole_index=-1) -> (Vector2D, is_valid_vertex=bool)
Returns the specified vertex of a Polygon -- either of the outer polygon, if HoleIndex is -1, or specified inner hole.
Vertex will be the zero vector for invalid Polygon or Hole indices, or if the polygon is empty. VertexIndex will loop.

Args:
    polygon_list (GeometryScriptGeneralPolygonList): 
    vertex_index (int32): 
    polygon_index (int32): 
    hole_index (int32): 

Returns:
    bool: 

    is_valid_vertex (bool):

<a id="unreal.GeometryScript_PolygonList.get_polygon_list_bounds"></a>

#### get_polygon_list_bounds

```python
@classmethod
def get_polygon_list_bounds(
        cls, polygon_list: GeometryScriptGeneralPolygonList) -> Box2D
```

X.get_polygon_list_bounds(polygon_list) -> Box2D
Returns the bounding box of a Polygon

Args:
    polygon_list (GeometryScriptGeneralPolygonList): 

Returns:
    Box2D:

<a id="unreal.GeometryScript_PolygonList.get_polygon_list_area"></a>

#### get_polygon_list_area

```python
@classmethod
def get_polygon_list_area(
        cls, polygon_list: GeometryScriptGeneralPolygonList) -> float
```

X.get_polygon_list_area(polygon_list) -> double
Returns the area enclosed by a Polygon

Args:
    polygon_list (GeometryScriptGeneralPolygonList): 

Returns:
    double:

<a id="unreal.GeometryScript_PolygonList.get_polygon_hole_count"></a>

#### get_polygon_hole_count

```python
@classmethod
def get_polygon_hole_count(cls, polygon_list: GeometryScriptGeneralPolygonList,
                           polygon_index: int) -> Tuple[int, bool]
```

X.get_polygon_hole_count(polygon_list, polygon_index) -> (int32, valid_index=bool)
Returns the number of holes in a Polygon. Returns zero for an invalid PolygonIndex.

Args:
    polygon_list (GeometryScriptGeneralPolygonList): 
    polygon_index (int32): 

Returns:
    bool: 

    valid_index (bool):

<a id="unreal.GeometryScript_PolygonList.get_polygon_count"></a>

#### get_polygon_count

```python
@classmethod
def get_polygon_count(cls,
                      polygon_list: GeometryScriptGeneralPolygonList) -> int
```

X.get_polygon_count(polygon_list) -> int32
Returns the number of polygons in the Polygon List

Args:
    polygon_list (GeometryScriptGeneralPolygonList): 

Returns:
    int32:

<a id="unreal.GeometryScript_PolygonList.get_polygon_bounds"></a>

#### get_polygon_bounds

```python
@classmethod
def get_polygon_bounds(cls, polygon_list: GeometryScriptGeneralPolygonList,
                       polygon_index: int) -> Tuple[Box2D, bool]
```

X.get_polygon_bounds(polygon_list, polygon_index) -> (Box2D, valid_index=bool)
Returns the bounding box of a Polygon. Returns an empty, invalid box for an invalid PolygonIndex.

Args:
    polygon_list (GeometryScriptGeneralPolygonList): 
    polygon_index (int32): 

Returns:
    bool: 

    valid_index (bool):

<a id="unreal.GeometryScript_PolygonList.get_polygon_area"></a>

#### get_polygon_area

```python
@classmethod
def get_polygon_area(cls, polygon_list: GeometryScriptGeneralPolygonList,
                     polygon_index: int) -> Tuple[float, bool]
```

X.get_polygon_area(polygon_list, polygon_index) -> (double, valid_index=bool)
Returns the area enclosed by a Polygon. Returns zero for an invalid PolygonIndex.

Args:
    polygon_list (GeometryScriptGeneralPolygonList): 
    polygon_index (int32): 

Returns:
    bool: 

    valid_index (bool):

<a id="unreal.GeometryScript_PolygonList.create_polygons_from_path_offset"></a>

#### create_polygons_from_path_offset

```python
@classmethod
def create_polygons_from_path_offset(
    cls,
    path: Array[Vector2D],
    offset_options: GeometryScriptOpenPathOffsetOptions,
    offset: float,
    copy_input_on_failure: bool = True
) -> Tuple[GeometryScriptGeneralPolygonList, bool]
```

X.create_polygons_from_path_offset(path, offset_options, offset, copy_input_on_failure=True) -> (GeometryScriptGeneralPolygonList, operation_success=bool)
Apply an offset to a single open 2D path, generating closed polygons as a result

Args:
    path (Array[Vector2D]): 
    offset_options (GeometryScriptOpenPathOffsetOptions): 
    offset (double): 
    copy_input_on_failure (bool): 

Returns:
    bool: 

    operation_success (bool):

<a id="unreal.GeometryScript_PolygonList.create_polygons_from_open_poly_paths_offset"></a>

#### create_polygons_from_open_poly_paths_offset

```python
@classmethod
def create_polygons_from_open_poly_paths_offset(
    cls,
    poly_paths: Array[GeometryScriptPolyPath],
    offset_options: GeometryScriptOpenPathOffsetOptions,
    offset: float,
    copy_input_on_failure: bool = True
) -> Tuple[GeometryScriptGeneralPolygonList, bool]
```

X.create_polygons_from_open_poly_paths_offset(poly_paths, offset_options, offset, copy_input_on_failure=True) -> (GeometryScriptGeneralPolygonList, operation_success=bool)
Apply an offset to a set of open 2D PolyPaths, generating closed polygons as a result

Args:
    poly_paths (Array[GeometryScriptPolyPath]): 
    offset_options (GeometryScriptOpenPathOffsetOptions): 
    offset (double): 
    copy_input_on_failure (bool): 

Returns:
    bool: 

    operation_success (bool):

<a id="unreal.GeometryScript_PolygonList.create_polygon_list_from_single_polygon"></a>

#### create_polygon_list_from_single_polygon

```python
@classmethod
def create_polygon_list_from_single_polygon(
        cls,
        outer_polygon: GeometryScriptSimplePolygon,
        hole_polygons: Array[GeometryScriptSimplePolygon],
        fix_hole_orientations: bool = True
) -> GeometryScriptGeneralPolygonList
```

X.create_polygon_list_from_single_polygon(outer_polygon, hole_polygons, fix_hole_orientations=True) -> GeometryScriptGeneralPolygonList
Create a Polygon List of a single Polygon, with optional holes

Args:
    outer_polygon (GeometryScriptSimplePolygon): 
    hole_polygons (Array[GeometryScriptSimplePolygon]): 
    fix_hole_orientations (bool): 

Returns:
    GeometryScriptGeneralPolygonList:

<a id="unreal.GeometryScript_PolygonList.create_polygon_list_from_simple_polygons"></a>

#### create_polygon_list_from_simple_polygons

```python
@classmethod
def create_polygon_list_from_simple_polygons(
    cls, outer_polygons: Array[GeometryScriptSimplePolygon]
) -> GeometryScriptGeneralPolygonList
```

X.create_polygon_list_from_simple_polygons(outer_polygons) -> GeometryScriptGeneralPolygonList
Create a Polygon List from an array of Simple Polygons

Args:
    outer_polygons (Array[GeometryScriptSimplePolygon]): 

Returns:
    GeometryScriptGeneralPolygonList:

<a id="unreal.GeometryScript_PolygonList.append_polygon_list"></a>

#### append_polygon_list

```python
@classmethod
def append_polygon_list(
    cls, polygon_list: GeometryScriptGeneralPolygonList,
    polygons_to_append: GeometryScriptGeneralPolygonList
) -> GeometryScriptGeneralPolygonList
```

X.append_polygon_list(polygon_list, polygons_to_append) -> GeometryScriptGeneralPolygonList
Append the polygons in 'Polygons to Append' to Polygon List

Args:
    polygon_list (GeometryScriptGeneralPolygonList): 
    polygons_to_append (GeometryScriptGeneralPolygonList): 

Returns:
    GeometryScriptGeneralPolygonList: 

    polygon_list (GeometryScriptGeneralPolygonList):

<a id="unreal.GeometryScript_PolygonList.add_polygon_to_list"></a>

#### add_polygon_to_list

```python
@classmethod
def add_polygon_to_list(
    cls,
    polygon_list: GeometryScriptGeneralPolygonList,
    outer_polygon: GeometryScriptSimplePolygon,
    hole_polygons: Array[GeometryScriptSimplePolygon],
    fix_hole_orientations: bool = True
) -> Tuple[int, GeometryScriptGeneralPolygonList]
```

X.add_polygon_to_list(polygon_list, outer_polygon, hole_polygons, fix_hole_orientations=True) -> (int32, polygon_list=GeometryScriptGeneralPolygonList)
Add Polygon to a Polygon List, with optional holes. Returns index of the added polygon.

Args:
    polygon_list (GeometryScriptGeneralPolygonList): 
    outer_polygon (GeometryScriptSimplePolygon): 
    hole_polygons (Array[GeometryScriptSimplePolygon]): 
    fix_hole_orientations (bool): 

Returns:
    GeometryScriptGeneralPolygonList: 

    polygon_list (GeometryScriptGeneralPolygonList):

<a id="unreal.GeometryScript_PolyPath"></a>