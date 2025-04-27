## GeometryScriptBakeVertexOptions Objects

```python
class GeometryScriptBakeVertexOptions(StructBase)
```

Geometry Script Bake Vertex Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBakeFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``projection_distance`` (float):  [Read-Write] Maximum allowed distance for the projection from target mesh to source mesh for the sample to be considered valid.
  This is only relevant if a separate source mesh is provided.
- ``projection_in_world_space`` (bool):  [Read-Write] If true, uses the world space positions for the projection from target mesh to source mesh, otherwise it uses their object space positions.
  This is only relevant if a separate source mesh is provided.
- ``split_at_normal_seams`` (bool):  [Read-Write] If true, compute a separate vertex color for each unique normal on a vertex
- ``split_at_uv_seams`` (bool):  [Read-Write] If true, compute a separate vertex color for each unique UV on a vertex.

<a id="unreal.GeometryScriptBakeVertexOptions.__init__"></a>

#### __init__

```python
def __init__(split_at_normal_seams: bool = False,
             split_at_uv_seams: bool = False,
             projection_distance: float = 0.000000,
             projection_in_world_space: bool = False) -> None
```

<a id="unreal.GeometryScriptBakeVertexOptions.split_at_normal_seams"></a>

#### split_at_normal_seams

```python
@property
def split_at_normal_seams() -> bool
```

(bool):  [Read-Write] If true, compute a separate vertex color for each unique normal on a vertex

<a id="unreal.GeometryScriptBakeVertexOptions.split_at_normal_seams"></a>

#### split_at_normal_seams

```python
@split_at_normal_seams.setter
def split_at_normal_seams(value: bool) -> None
```

<a id="unreal.GeometryScriptBakeVertexOptions.split_at_uv_seams"></a>

#### split_at_uv_seams

```python
@property
def split_at_uv_seams() -> bool
```

(bool):  [Read-Write] If true, compute a separate vertex color for each unique UV on a vertex.

<a id="unreal.GeometryScriptBakeVertexOptions.split_at_uv_seams"></a>

#### split_at_uv_seams

```python
@split_at_uv_seams.setter
def split_at_uv_seams(value: bool) -> None
```

<a id="unreal.GeometryScriptBakeVertexOptions.projection_distance"></a>

#### projection_distance

```python
@property
def projection_distance() -> float
```

(float):  [Read-Write] Maximum allowed distance for the projection from target mesh to source mesh for the sample to be considered valid.
This is only relevant if a separate source mesh is provided.

<a id="unreal.GeometryScriptBakeVertexOptions.projection_distance"></a>

#### projection_distance

```python
@projection_distance.setter
def projection_distance(value: float) -> None
```

<a id="unreal.GeometryScriptBakeVertexOptions.projection_in_world_space"></a>

#### projection_in_world_space

```python
@property
def projection_in_world_space() -> bool
```

(bool):  [Read-Write] If true, uses the world space positions for the projection from target mesh to source mesh, otherwise it uses their object space positions.
This is only relevant if a separate source mesh is provided.

<a id="unreal.GeometryScriptBakeVertexOptions.projection_in_world_space"></a>

#### projection_in_world_space

```python
@projection_in_world_space.setter
def projection_in_world_space(value: bool) -> None
```

<a id="unreal.GeometryScriptBakeOutputType"></a>