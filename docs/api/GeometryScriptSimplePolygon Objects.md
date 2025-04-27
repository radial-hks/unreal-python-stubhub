## GeometryScriptSimplePolygon Objects

```python
class GeometryScriptSimplePolygon(StructBase)
```

A simple 2D Polygon with no holes

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: GeometryScriptTypes.h

<a id="unreal.GeometryScriptSimplePolygon.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.GeometryScriptSimplePolygon.set_polygon_vertex"></a>

#### set_polygon_vertex

```python
def set_polygon_vertex(vertex_index: int, position: Vector2D) -> bool
```

x.set_polygon_vertex(vertex_index, position) -> bool
Set the specified vertex of a Simple Polygon. VertexIndex loops around, so e.g., -1 gives the last vertex in the polygon.
Does nothing if Polygon has no vertices.

Args:
    vertex_index (int32): 
    position (Vector2D): 

Returns:
    bool: 

    polygon_is_empty (bool):

<a id="unreal.GeometryScriptSimplePolygon.get_polygon_vertex_count"></a>

#### get_polygon_vertex_count

```python
def get_polygon_vertex_count() -> int
```

x.get_polygon_vertex_count() -> int32
Returns the number of vertices in a Simple Polygon

Returns:
    int32:

<a id="unreal.GeometryScriptSimplePolygon.get_polygon_vertex"></a>

#### get_polygon_vertex

```python
def get_polygon_vertex(vertex_index: int) -> Tuple[Vector2D, bool]
```

x.get_polygon_vertex(vertex_index) -> (Vector2D, polygon_is_empty=bool)
Returns the specified vertex of a Simple Polygon. VertexIndex loops around, so e.g., -1 gives the last vertex in the polygon.
If Polygon has no vertices, returns the zero vector.

Args:
    vertex_index (int32): 

Returns:
    bool: 

    polygon_is_empty (bool):

<a id="unreal.GeometryScriptSimplePolygon.get_polygon_tangent"></a>

#### get_polygon_tangent

```python
def get_polygon_tangent(vertex_index: int) -> Tuple[Vector2D, bool]
```

x.get_polygon_tangent(vertex_index) -> (Vector2D, polygon_is_empty=bool)
Returns a vertex's tangent of a Simple Polygon. VertexIndex loops around, so e.g., -1 gives the tangent of the last vertex in the polygon.
If Polygon has no vertices, returns the zero vector.

Args:
    vertex_index (int32): 

Returns:
    bool: 

    polygon_is_empty (bool):

<a id="unreal.GeometryScriptSimplePolygon.get_polygon_bounds"></a>

#### get_polygon_bounds

```python
def get_polygon_bounds() -> Box2D
```

x.get_polygon_bounds() -> Box2D
Returns the bounding box of a Simple Polygon

Returns:
    Box2D:

<a id="unreal.GeometryScriptSimplePolygon.get_polygon_area"></a>

#### get_polygon_area

```python
def get_polygon_area() -> float
```

x.get_polygon_area() -> double
Returns the area enclosed by a Simple Polygon

Returns:
    double:

<a id="unreal.GeometryScriptSimplePolygon.get_polygon_arc_length"></a>

#### get_polygon_arc_length

```python
def get_polygon_arc_length() -> float
```

x.get_polygon_arc_length() -> double
Returns the arc length of a Simple Polygon

Returns:
    double:

<a id="unreal.GeometryScriptSimplePolygon.add_polygon_vertex"></a>

#### add_polygon_vertex

```python
def add_polygon_vertex(position: Vector2D) -> int
```

x.add_polygon_vertex(position) -> int32
Set the specified vertex of a Simple Polygon. Returns the index of the added vertex.

Args:
    position (Vector2D): 

Returns:
    int32:

<a id="unreal.GeometryScriptSimplePolygon.create_polygon_list_from_single_polygon"></a>

#### create_polygon_list_from_single_polygon

```python
def create_polygon_list_from_single_polygon(
        hole_polygons: Array[GeometryScriptSimplePolygon],
        fix_hole_orientations: bool = True
) -> GeometryScriptGeneralPolygonList
```

x.create_polygon_list_from_single_polygon(hole_polygons, fix_hole_orientations=True) -> GeometryScriptGeneralPolygonList
Create a Polygon List of a single Polygon, with optional holes

Args:
    hole_polygons (Array[GeometryScriptSimplePolygon]): 
    fix_hole_orientations (bool): 

Returns:
    GeometryScriptGeneralPolygonList:

<a id="unreal.GeometryScriptGeneralPolygonList"></a>