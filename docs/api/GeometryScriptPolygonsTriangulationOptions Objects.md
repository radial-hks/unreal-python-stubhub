## GeometryScriptPolygonsTriangulationOptions Objects

```python
class GeometryScriptPolygonsTriangulationOptions(StructBase)
```

Geometry Script Polygons Triangulation Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshPrimitiveFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``still_append_on_triangulation_error`` (bool):  [Read-Write] Whether to still append the triangulation in error cases -- typically, cases where the input contained intersecting edges. Resulting triangulation likely will appear correct except at the intersecting edges.

<a id="unreal.GeometryScriptPolygonsTriangulationOptions.__init__"></a>

#### __init__

```python
def __init__(still_append_on_triangulation_error: bool = False) -> None
```

<a id="unreal.GeometryScriptPolygonsTriangulationOptions.still_append_on_triangulation_error"></a>

#### still_append_on_triangulation_error

```python
@property
def still_append_on_triangulation_error() -> bool
```

(bool):  [Read-Write] Whether to still append the triangulation in error cases -- typically, cases where the input contained intersecting edges. Resulting triangulation likely will appear correct except at the intersecting edges.

<a id="unreal.GeometryScriptPolygonsTriangulationOptions.still_append_on_triangulation_error"></a>

#### still_append_on_triangulation_error

```python
@still_append_on_triangulation_error.setter
def still_append_on_triangulation_error(value: bool) -> None
```

<a id="unreal.GeometryScriptRemeshOptions"></a>