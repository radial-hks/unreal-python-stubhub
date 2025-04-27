## DisplayClusterWarpGeometryOBJ Objects

```python
class DisplayClusterWarpGeometryOBJ(StructBase)
```

3D geometry that can be used for warping, in an OBJ-like format

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterWarp
- **File**: DisplayClusterWarpGeometry.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``normal`` (Array[Vector]):  [Read-Write] Normal of the vertices of the mesh.
- ``triangles`` (Array[int32]):  [Read-Write] Triangles with mesh vertex indices.
- ``uv`` (Array[Vector2D]):  [Read-Write] UV of the vertices of the mesh.
- ``vertices`` (Array[Vector]):  [Read-Write] Vertices of the mesh.

<a id="unreal.DisplayClusterWarpGeometryOBJ.__init__"></a>

#### __init__

```python
def __init__(vertices: Array[Vector] = [],
             normal: Array[Vector] = [],
             uv: Array[Vector2D] = [],
             triangles: Array[int] = []) -> None
```

<a id="unreal.DisplayClusterWarpGeometryOBJ.vertices"></a>

#### vertices

```python
@property
def vertices() -> Array[Vector]
```

(Array[Vector]):  [Read-Write] Vertices of the mesh.

<a id="unreal.DisplayClusterWarpGeometryOBJ.vertices"></a>

#### vertices

```python
@vertices.setter
def vertices(value: Array[Vector]) -> None
```

<a id="unreal.DisplayClusterWarpGeometryOBJ.normal"></a>

#### normal

```python
@property
def normal() -> Array[Vector]
```

(Array[Vector]):  [Read-Write] Normal of the vertices of the mesh.

<a id="unreal.DisplayClusterWarpGeometryOBJ.normal"></a>

#### normal

```python
@normal.setter
def normal(value: Array[Vector]) -> None
```

<a id="unreal.DisplayClusterWarpGeometryOBJ.uv"></a>

#### uv

```python
@property
def uv() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write] UV of the vertices of the mesh.

<a id="unreal.DisplayClusterWarpGeometryOBJ.uv"></a>

#### uv

```python
@uv.setter
def uv(value: Array[Vector2D]) -> None
```

<a id="unreal.DisplayClusterWarpGeometryOBJ.triangles"></a>

#### triangles

```python
@property
def triangles() -> Array[int]
```

(Array[int32]):  [Read-Write] Triangles with mesh vertex indices.

<a id="unreal.DisplayClusterWarpGeometryOBJ.triangles"></a>

#### triangles

```python
@triangles.setter
def triangles(value: Array[int]) -> None
```

<a id="unreal.DisplayClusterMoviePipelineConfiguration"></a>