## GeometryScriptPolyPath Objects

```python
class GeometryScriptPolyPath(StructBase)
```

Geometry Script Poly Path

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: GeometryScriptTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``closed_loop`` (bool):  [Read-Write]

<a id="unreal.GeometryScriptPolyPath.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.GeometryScriptPolyPath.get_poly_path_vertex"></a>

#### get_poly_path_vertex

```python
def get_poly_path_vertex(index: int) -> Tuple[Vector, bool]
```

x.get_poly_path_vertex(index) -> (Vector, is_valid_index=bool)
Returns the 3D position of the requested vertex in the PolyPath.
If the Index does not correspond to a vertex in the PolyPath, a Zero Vector (0,0,0) will be returned.

Args:
    index (int32): specifies a vertex in the PolyPath.

Returns:
    bool: 

    is_valid_index (bool): will be false on return if the Index is not included in the PolyPath.

<a id="unreal.GeometryScriptPolyPath.get_poly_path_tangent"></a>

#### get_poly_path_tangent

```python
def get_poly_path_tangent(index: int) -> Tuple[Vector, bool]
```

x.get_poly_path_tangent(index) -> (Vector, is_valid_index=bool)
Returns the local tangent vector of the PolyPath at the specified vertex index.
If the Index does not correspond to a vertex in the PolyPath, a Zero Vector (0,0,0) will be returned.

Args:
    index (int32): specifies a vertex in the PolyPath

Returns:
    bool: 

    is_valid_index (bool): will be false on return if the Index is not included in the PolyPath

<a id="unreal.GeometryScriptPolyPath.get_poly_path_num_vertices"></a>

#### get_poly_path_num_vertices

```python
def get_poly_path_num_vertices() -> int
```

x.get_poly_path_num_vertices() -> int32
Returns the number of vertices in the the PolyPath.

Returns:
    int32:

<a id="unreal.GeometryScriptPolyPath.get_poly_path_last_index"></a>

#### get_poly_path_last_index

```python
def get_poly_path_last_index() -> int
```

x.get_poly_path_last_index() -> int32
Returns the index of the last vertex in the PolyPath.

Returns:
    int32:

<a id="unreal.GeometryScriptPolyPath.get_poly_path_arc_length"></a>

#### get_poly_path_arc_length

```python
def get_poly_path_arc_length() -> float
```

x.get_poly_path_arc_length() -> double
Returns the length of the PolyPath.

Returns:
    double:

<a id="unreal.GeometryScriptPolyPath.get_nearest_vertex_index"></a>

#### get_nearest_vertex_index

```python
def get_nearest_vertex_index(point: Vector) -> int
```

x.get_nearest_vertex_index(point) -> int32
Find the index of the vertex closest to a given point.  Returns -1 if the PolyPath has no vertices.

Args:
    point (Vector): 

Returns:
    int32:

<a id="unreal.GeometryScriptPolyPath.flatten_to2d_on_axis"></a>

#### flatten_to2d_on_axis

```python
def flatten_to2d_on_axis(
    drop_axis: GeometryScriptAxis = GeometryScriptAxis.Z
) -> GeometryScriptPolyPath
```

x.flatten_to2d_on_axis(drop_axis=GeometryScriptAxis.Z) -> GeometryScriptPolyPath
Create a 2D, flattened copy of the path by dropping the given axis, and using the other two coordinates as the new X, Y coordinates.

Args:
    drop_axis (GeometryScriptAxis): 

Returns:
    GeometryScriptPolyPath:

<a id="unreal.GeometryScriptPolyPath.convert_poly_path_to_array_of_vector2d"></a>

#### convert_poly_path_to_array_of_vector2d

```python
def convert_poly_path_to_array_of_vector2d() -> Array[Vector2D]
```

x.convert_poly_path_to_array_of_vector2d() -> Array[Vector2D]
Creates an array of 2D Vectors with the PolyPath vertex locations projected onto the XY plane.

Returns:
    Array[Vector2D]: 

    vertex_array (Array[Vector2D]):

<a id="unreal.GeometryScriptPolyPath.convert_poly_path_to_array"></a>

#### convert_poly_path_to_array

```python
def convert_poly_path_to_array() -> Array[Vector]
```

x.convert_poly_path_to_array() -> Array[Vector]
Populates an array of 3D vectors with the PolyPath vertex locations.

Returns:
    Array[Vector]: 

    vertex_array (Array[Vector]):

<a id="unreal.GeometryScriptSimplePolygon"></a>