## GeometryScriptConstrainedDelaunayTriangulationOptions Objects

```python
class GeometryScriptConstrainedDelaunayTriangulationOptions(StructBase)
```

Geometry Script Constrained Delaunay Triangulation Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshPrimitiveFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``constrained_edges_fill_mode`` (GeometryScriptPolygonFillMode):  [Read-Write] How to decide which parts of the shape defined by constrained edges should be filled with triangles
- ``remove_duplicate_vertices`` (bool):  [Read-Write] Whether to remove duplicate vertices from the output.  If false, duplicate vertices will not be used in any triangles, but will remain in the output mesh.
- ``validate_edges_in_result`` (bool):  [Read-Write] Whether the triangulation should be considered a failure if it doesn't include the requested Constrained Edges.
  (Edges may be missing e.g. due to intersecting edges in the input.)

<a id="unreal.GeometryScriptConstrainedDelaunayTriangulationOptions.__init__"></a>

#### \_\_init\_\_

```python
def __init__(constrained_edges_fill_mode:
             GeometryScriptPolygonFillMode = GeometryScriptPolygonFillMode.ALL,
             validate_edges_in_result: bool = False,
             remove_duplicate_vertices: bool = False) -> None
```

<a id="unreal.GeometryScriptConstrainedDelaunayTriangulationOptions.constrained_edges_fill_mode"></a>

#### constrained\_edges\_fill\_mode

```python
@property
def constrained_edges_fill_mode() -> GeometryScriptPolygonFillMode
```

(GeometryScriptPolygonFillMode):  [Read-Write] How to decide which parts of the shape defined by constrained edges should be filled with triangles

<a id="unreal.GeometryScriptConstrainedDelaunayTriangulationOptions.constrained_edges_fill_mode"></a>

#### constrained\_edges\_fill\_mode

```python
@constrained_edges_fill_mode.setter
def constrained_edges_fill_mode(value: GeometryScriptPolygonFillMode) -> None
```

<a id="unreal.GeometryScriptConstrainedDelaunayTriangulationOptions.validate_edges_in_result"></a>

#### validate\_edges\_in\_result

```python
@property
def validate_edges_in_result() -> bool
```

(bool):  [Read-Write] Whether the triangulation should be considered a failure if it doesn't include the requested Constrained Edges.
(Edges may be missing e.g. due to intersecting edges in the input.)

<a id="unreal.GeometryScriptConstrainedDelaunayTriangulationOptions.validate_edges_in_result"></a>

#### validate\_edges\_in\_result

```python
@validate_edges_in_result.setter
def validate_edges_in_result(value: bool) -> None
```

<a id="unreal.GeometryScriptConstrainedDelaunayTriangulationOptions.remove_duplicate_vertices"></a>

#### remove\_duplicate\_vertices

```python
@property
def remove_duplicate_vertices() -> bool
```

(bool):  [Read-Write] Whether to remove duplicate vertices from the output.  If false, duplicate vertices will not be used in any triangles, but will remain in the output mesh.

<a id="unreal.GeometryScriptConstrainedDelaunayTriangulationOptions.remove_duplicate_vertices"></a>

#### remove\_duplicate\_vertices

```python
@remove_duplicate_vertices.setter
def remove_duplicate_vertices(value: bool) -> None
```

<a id="unreal.GeometryScriptPolygonsTriangulationOptions"></a>