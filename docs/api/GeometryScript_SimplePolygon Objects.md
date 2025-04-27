## GeometryScript_SimplePolygon Objects

```python
class GeometryScript_SimplePolygon(BlueprintFunctionLibrary)
```

Geometry Script Library Simple Polygon Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: PolygonFunctions.h

<a id="unreal.GeometryScript_SimplePolygon.set_polygon_vertex"></a>

#### set_polygon_vertex

```python
@classmethod
def set_polygon_vertex(
        cls, polygon: GeometryScriptSimplePolygon, vertex_index: int,
        position: Vector2D) -> Tuple[GeometryScriptSimplePolygon, bool]
```

X.set_polygon_vertex(polygon, vertex_index, position) -> (polygon=GeometryScriptSimplePolygon, polygon_is_empty=bool)
Set the specified vertex of a Simple Polygon. VertexIndex loops around, so e.g., -1 gives the last vertex in the polygon.
Does nothing if Polygon has no vertices.

Args:
    polygon (GeometryScriptSimplePolygon): 
    vertex_index (int32): 
    position (Vector2D): 

Returns:
    tuple: 

    polygon (GeometryScriptSimplePolygon): 

    polygon_is_empty (bool):

<a id="unreal.GeometryScript_SimplePolygon.get_polygon_vertex_count"></a>

#### get_polygon_vertex_count

```python
@classmethod
def get_polygon_vertex_count(cls, polygon: GeometryScriptSimplePolygon) -> int
```

X.get_polygon_vertex_count(polygon) -> int32
Returns the number of vertices in a Simple Polygon

Args:
    polygon (GeometryScriptSimplePolygon): 

Returns:
    int32:

<a id="unreal.GeometryScript_SimplePolygon.get_polygon_vertex"></a>

#### get_polygon_vertex

```python
@classmethod
def get_polygon_vertex(cls, polygon: GeometryScriptSimplePolygon,
                       vertex_index: int) -> Tuple[Vector2D, bool]
```

X.get_polygon_vertex(polygon, vertex_index) -> (Vector2D, polygon_is_empty=bool)
Returns the specified vertex of a Simple Polygon. VertexIndex loops around, so e.g., -1 gives the last vertex in the polygon.
If Polygon has no vertices, returns the zero vector.

Args:
    polygon (GeometryScriptSimplePolygon): 
    vertex_index (int32): 

Returns:
    bool: 

    polygon_is_empty (bool):

<a id="unreal.GeometryScript_SimplePolygon.get_polygon_tangent"></a>

#### get_polygon_tangent

```python
@classmethod
def get_polygon_tangent(cls, polygon: GeometryScriptSimplePolygon,
                        vertex_index: int) -> Tuple[Vector2D, bool]
```

X.get_polygon_tangent(polygon, vertex_index) -> (Vector2D, polygon_is_empty=bool)
Returns a vertex's tangent of a Simple Polygon. VertexIndex loops around, so e.g., -1 gives the tangent of the last vertex in the polygon.
If Polygon has no vertices, returns the zero vector.

Args:
    polygon (GeometryScriptSimplePolygon): 
    vertex_index (int32): 

Returns:
    bool: 

    polygon_is_empty (bool):

<a id="unreal.GeometryScript_SimplePolygon.get_polygon_bounds"></a>

#### get_polygon_bounds

```python
@classmethod
def get_polygon_bounds(cls, polygon: GeometryScriptSimplePolygon) -> Box2D
```

X.get_polygon_bounds(polygon) -> Box2D
Returns the bounding box of a Simple Polygon

Args:
    polygon (GeometryScriptSimplePolygon): 

Returns:
    Box2D:

<a id="unreal.GeometryScript_SimplePolygon.get_polygon_area"></a>

#### get_polygon_area

```python
@classmethod
def get_polygon_area(cls, polygon: GeometryScriptSimplePolygon) -> float
```

X.get_polygon_area(polygon) -> double
Returns the area enclosed by a Simple Polygon

Args:
    polygon (GeometryScriptSimplePolygon): 

Returns:
    double:

<a id="unreal.GeometryScript_SimplePolygon.get_polygon_arc_length"></a>

#### get_polygon_arc_length

```python
@classmethod
def get_polygon_arc_length(cls, polygon: GeometryScriptSimplePolygon) -> float
```

X.get_polygon_arc_length(polygon) -> double
Returns the arc length of a Simple Polygon

Args:
    polygon (GeometryScriptSimplePolygon): 

Returns:
    double:

<a id="unreal.GeometryScript_SimplePolygon.convert_spline_to_polygon"></a>

#### convert_spline_to_polygon

```python
@classmethod
def convert_spline_to_polygon(
    cls,
    spline: SplineComponent,
    sampling_options: GeometryScriptSplineSamplingOptions,
    drop_axis: GeometryScriptAxis = GeometryScriptAxis.Z
) -> GeometryScriptSimplePolygon
```

X.convert_spline_to_polygon(spline, sampling_options, drop_axis=GeometryScriptAxis.Z) -> GeometryScriptSimplePolygon
Sample positions from a USplineComponent into a Simple Polyon, based on the given SamplingOptions

Args:
    spline (SplineComponent): 
    sampling_options (GeometryScriptSplineSamplingOptions): 
    drop_axis (GeometryScriptAxis): 

Returns:
    GeometryScriptSimplePolygon: 

    polygon (GeometryScriptSimplePolygon):

<a id="unreal.GeometryScript_SimplePolygon.conv_geometry_script_simple_polygon_to_array_of_vector2d"></a>

#### conv_geometry_script_simple_polygon_to_array_of_vector2d

```python
@classmethod
def conv_geometry_script_simple_polygon_to_array_of_vector2d(
        cls, polygon: GeometryScriptSimplePolygon) -> Array[Vector2D]
```

X.conv_geometry_script_simple_polygon_to_array_of_vector2d(polygon) -> Array[Vector2D]
Returns an array of 2D Vectors with the Polygon vertex locations.

Args:
    polygon (GeometryScriptSimplePolygon): 

Returns:
    Array[Vector2D]:

<a id="unreal.GeometryScript_SimplePolygon.conv_geometry_script_simple_polygon_to_array"></a>

#### conv_geometry_script_simple_polygon_to_array

```python
@classmethod
def conv_geometry_script_simple_polygon_to_array(
        cls, polygon: GeometryScriptSimplePolygon) -> Array[Vector]
```

X.conv_geometry_script_simple_polygon_to_array(polygon) -> Array[Vector]
Returns an array of 3D vectors with the Polygon vertex locations, with Z coordinate set to zero.

Args:
    polygon (GeometryScriptSimplePolygon): 

Returns:
    Array[Vector]:

<a id="unreal.GeometryScript_SimplePolygon.conv_array_to_geometry_script_simple_polygon"></a>

#### conv_array_to_geometry_script_simple_polygon

```python
@classmethod
def conv_array_to_geometry_script_simple_polygon(
        cls, path_vertices: Array[Vector]) -> GeometryScriptSimplePolygon
```

X.conv_array_to_geometry_script_simple_polygon(path_vertices) -> GeometryScriptSimplePolygon
Returns a Polygon created from an array of 3D position vectors, ignoring the Z coordinate.

Args:
    path_vertices (Array[Vector]): 

Returns:
    GeometryScriptSimplePolygon:

<a id="unreal.GeometryScript_SimplePolygon.conv_array_of_vector2d_to_geometry_script_simple_polygon"></a>

#### conv_array_of_vector2d_to_geometry_script_simple_polygon

```python
@classmethod
def conv_array_of_vector2d_to_geometry_script_simple_polygon(
        cls, path_vertices: Array[Vector2D]) -> GeometryScriptSimplePolygon
```

X.conv_array_of_vector2d_to_geometry_script_simple_polygon(path_vertices) -> GeometryScriptSimplePolygon
Returns a Polygon created from an array of 2D position vectors.

Args:
    path_vertices (Array[Vector2D]): 

Returns:
    GeometryScriptSimplePolygon:

<a id="unreal.GeometryScript_SimplePolygon.add_polygon_vertex"></a>

#### add_polygon_vertex

```python
@classmethod
def add_polygon_vertex(
        cls, polygon: GeometryScriptSimplePolygon,
        position: Vector2D) -> Tuple[int, GeometryScriptSimplePolygon]
```

X.add_polygon_vertex(polygon, position) -> (int32, polygon=GeometryScriptSimplePolygon)
Set the specified vertex of a Simple Polygon. Returns the index of the added vertex.

Args:
    polygon (GeometryScriptSimplePolygon): 
    position (Vector2D): 

Returns:
    GeometryScriptSimplePolygon: 

    polygon (GeometryScriptSimplePolygon):

<a id="unreal.GeometryScript_PolygonList"></a>