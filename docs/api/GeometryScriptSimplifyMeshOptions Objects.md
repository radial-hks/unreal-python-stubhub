## GeometryScriptSimplifyMeshOptions Objects

```python
class GeometryScriptSimplifyMeshOptions(StructBase)
```

Geometry Script Simplify Mesh Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshSimplifyFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_seam_collapse`` (bool):  [Read-Write]
- ``allow_seam_smoothing`` (bool):  [Read-Write]
- ``allow_seam_splits`` (bool):  [Read-Write]
- ``auto_compact`` (bool):  [Read-Write] If enabled, the simplified mesh is automatically compacted to remove gaps in the index space. This is expensive and can be disabled by advanced users.
- ``method`` (GeometryScriptRemoveMeshSimplificationType):  [Read-Write]
- ``preserve_vertex_positions`` (bool):  [Read-Write]
- ``retain_quadric_memory`` (bool):  [Read-Write]

<a id="unreal.GeometryScriptSimplifyMeshOptions.__init__"></a>

#### __init__

```python
def __init__(
        method:
    GeometryScriptRemoveMeshSimplificationType = GeometryScriptRemoveMeshSimplificationType
    .STANDARD_QEM,
        allow_seam_collapse: bool = False,
        allow_seam_smoothing: bool = False,
        allow_seam_splits: bool = False,
        preserve_vertex_positions: bool = False,
        retain_quadric_memory: bool = False,
        auto_compact: bool = False) -> None
```

<a id="unreal.GeometryScriptSimplifyMeshOptions.method"></a>

#### method

```python
@property
def method() -> GeometryScriptRemoveMeshSimplificationType
```

(GeometryScriptRemoveMeshSimplificationType):  [Read-Write]

<a id="unreal.GeometryScriptSimplifyMeshOptions.method"></a>

#### method

```python
@method.setter
def method(value: GeometryScriptRemoveMeshSimplificationType) -> None
```

<a id="unreal.GeometryScriptSimplifyMeshOptions.allow_seam_collapse"></a>

#### allow_seam_collapse

```python
@property
def allow_seam_collapse() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptSimplifyMeshOptions.allow_seam_collapse"></a>

#### allow_seam_collapse

```python
@allow_seam_collapse.setter
def allow_seam_collapse(value: bool) -> None
```

<a id="unreal.GeometryScriptSimplifyMeshOptions.allow_seam_smoothing"></a>

#### allow_seam_smoothing

```python
@property
def allow_seam_smoothing() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptSimplifyMeshOptions.allow_seam_smoothing"></a>

#### allow_seam_smoothing

```python
@allow_seam_smoothing.setter
def allow_seam_smoothing(value: bool) -> None
```

<a id="unreal.GeometryScriptSimplifyMeshOptions.allow_seam_splits"></a>

#### allow_seam_splits

```python
@property
def allow_seam_splits() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptSimplifyMeshOptions.allow_seam_splits"></a>

#### allow_seam_splits

```python
@allow_seam_splits.setter
def allow_seam_splits(value: bool) -> None
```

<a id="unreal.GeometryScriptSimplifyMeshOptions.preserve_vertex_positions"></a>

#### preserve_vertex_positions

```python
@property
def preserve_vertex_positions() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptSimplifyMeshOptions.preserve_vertex_positions"></a>

#### preserve_vertex_positions

```python
@preserve_vertex_positions.setter
def preserve_vertex_positions(value: bool) -> None
```

<a id="unreal.GeometryScriptSimplifyMeshOptions.retain_quadric_memory"></a>

#### retain_quadric_memory

```python
@property
def retain_quadric_memory() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptSimplifyMeshOptions.retain_quadric_memory"></a>

#### retain_quadric_memory

```python
@retain_quadric_memory.setter
def retain_quadric_memory(value: bool) -> None
```

<a id="unreal.GeometryScriptSimplifyMeshOptions.auto_compact"></a>

#### auto_compact

```python
@property
def auto_compact() -> bool
```

(bool):  [Read-Write] If enabled, the simplified mesh is automatically compacted to remove gaps in the index space. This is expensive and can be disabled by advanced users.

<a id="unreal.GeometryScriptSimplifyMeshOptions.auto_compact"></a>

#### auto_compact

```python
@auto_compact.setter
def auto_compact(value: bool) -> None
```

<a id="unreal.GeometryScriptSpatialQueryOptions"></a>