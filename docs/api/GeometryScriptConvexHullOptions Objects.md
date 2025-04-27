## GeometryScriptConvexHullOptions Objects

```python
class GeometryScriptConvexHullOptions(StructBase)
```

Geometry Script Convex Hull Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: ContainmentFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``prefilter_grid_resolution`` (int32):  [Read-Write]
- ``prefilter_vertices`` (bool):  [Read-Write]
- ``simplify_to_face_count`` (int32):  [Read-Write] Try to simplify each convex hull to this triangle count. If 0, no simplification

<a id="unreal.GeometryScriptConvexHullOptions.__init__"></a>

#### __init__

```python
def __init__(prefilter_vertices: bool = False,
             prefilter_grid_resolution: int = 0,
             simplify_to_face_count: int = 0) -> None
```

<a id="unreal.GeometryScriptConvexHullOptions.prefilter_vertices"></a>

#### prefilter_vertices

```python
@property
def prefilter_vertices() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptConvexHullOptions.prefilter_vertices"></a>

#### prefilter_vertices

```python
@prefilter_vertices.setter
def prefilter_vertices(value: bool) -> None
```

<a id="unreal.GeometryScriptConvexHullOptions.prefilter_grid_resolution"></a>

#### prefilter_grid_resolution

```python
@property
def prefilter_grid_resolution() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptConvexHullOptions.prefilter_grid_resolution"></a>

#### prefilter_grid_resolution

```python
@prefilter_grid_resolution.setter
def prefilter_grid_resolution(value: int) -> None
```

<a id="unreal.GeometryScriptConvexHullOptions.simplify_to_face_count"></a>

#### simplify_to_face_count

```python
@property
def simplify_to_face_count() -> int
```

(int32):  [Read-Write] Try to simplify each convex hull to this triangle count. If 0, no simplification

<a id="unreal.GeometryScriptConvexHullOptions.simplify_to_face_count"></a>

#### simplify_to_face_count

```python
@simplify_to_face_count.setter
def simplify_to_face_count(value: int) -> None
```

<a id="unreal.GeometryScriptSweptHullOptions"></a>