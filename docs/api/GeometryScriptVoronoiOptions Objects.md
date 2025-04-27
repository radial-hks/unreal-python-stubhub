## GeometryScriptVoronoiOptions Objects

```python
class GeometryScriptVoronoiOptions(StructBase)
```

Geometry Script Voronoi Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshPrimitiveFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bounds`` (Box):  [Read-Write]
- ``bounds_expand`` (float):  [Read-Write]
- ``create_cells`` (Array[int32]):  [Read-Write] Optional list of cells to create meshes for.  If empty, create all cells.
- ``include_boundary`` (bool):  [Read-Write] Whether to include the bordering Voronoi cells (which extend 'infinitely' to any boundary)

<a id="unreal.GeometryScriptVoronoiOptions.__init__"></a>

#### __init__

```python
def __init__(bounds_expand: float = 0.000000,
             bounds: Box = [[0.000000, 0.000000, 0.000000],
                            [0.000000, 0.000000, 0.000000], False],
             create_cells: Array[int] = [],
             include_boundary: bool = False) -> None
```

<a id="unreal.GeometryScriptVoronoiOptions.bounds_expand"></a>

#### bounds_expand

```python
@property
def bounds_expand() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptVoronoiOptions.bounds_expand"></a>

#### bounds_expand

```python
@bounds_expand.setter
def bounds_expand(value: float) -> None
```

<a id="unreal.GeometryScriptVoronoiOptions.bounds"></a>

#### bounds

```python
@property
def bounds() -> Box
```

(Box):  [Read-Write]

<a id="unreal.GeometryScriptVoronoiOptions.bounds"></a>

#### bounds

```python
@bounds.setter
def bounds(value: Box) -> None
```

<a id="unreal.GeometryScriptVoronoiOptions.create_cells"></a>

#### create_cells

```python
@property
def create_cells() -> Array[int]
```

(Array[int32]):  [Read-Write] Optional list of cells to create meshes for.  If empty, create all cells.

<a id="unreal.GeometryScriptVoronoiOptions.create_cells"></a>

#### create_cells

```python
@create_cells.setter
def create_cells(value: Array[int]) -> None
```

<a id="unreal.GeometryScriptVoronoiOptions.include_boundary"></a>

#### include_boundary

```python
@property
def include_boundary() -> bool
```

(bool):  [Read-Write] Whether to include the bordering Voronoi cells (which extend 'infinitely' to any boundary)

<a id="unreal.GeometryScriptVoronoiOptions.include_boundary"></a>

#### include_boundary

```python
@include_boundary.setter
def include_boundary(value: bool) -> None
```

<a id="unreal.GeometryScriptConstrainedDelaunayTriangulationOptions"></a>