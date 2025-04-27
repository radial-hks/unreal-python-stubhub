## GeometryScriptRemeshOptions Objects

```python
class GeometryScriptRemeshOptions(StructBase)
```

Standard Remeshing Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshRemeshFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_collapses`` (bool):  [Read-Write] Enable/Disable Edge Collapses during Remeshing. Disabling Collapses will prevent the mesh density from decreasing.
- ``allow_flips`` (bool):  [Read-Write] Enable/Disable Edge Flips during Remeshing. Disabling flips will significantly reduce the output mesh quality
- ``allow_splits`` (bool):  [Read-Write] Enable/Disable Edge Splits during Remeshing. Disabling Splits will prevent the mesh density from increasing.
- ``auto_compact`` (bool):  [Read-Write] If enabled, the output mesh is automatically compacted to remove gaps in the index space. This is expensive and can be disabled by advanced users.
- ``discard_attributes`` (bool):  [Read-Write] When enabled, all mesh attributes are discarded, so UV and Normal Seams can be ignored. New per-vertex normals are computed.
- ``group_boundary_constraint`` (GeometryScriptRemeshEdgeConstraintType):  [Read-Write] Constraints on the mesh boundary/border edges between different PolyGroups of the Mesh
- ``material_boundary_constraint`` (GeometryScriptRemeshEdgeConstraintType):  [Read-Write] Constraints on the mesh boundary/border edges between different Material Results of the Mesh
- ``mesh_boundary_constraint`` (GeometryScriptRemeshEdgeConstraintType):  [Read-Write] Constraints on the open mesh boundary/border edges
- ``prevent_normal_flips`` (bool):  [Read-Write] When Enabled, Flips and Collapses will be skipped if they would flip any triangle face normals
- ``prevent_tiny_triangles`` (bool):  [Read-Write] When Enabled, Flips and Collapses will be skipped if they would create tiny degenerate triangles
- ``remesh_iterations`` (int32):  [Read-Write] Maximum Number of iterations of the Remeshing Strategy to apply to the Mesh. More iterations are generally more expensive (much moreso with bUseFullRemeshPasses = true)
- ``reproject_to_input_mesh`` (bool):  [Read-Write] When enabled, mesh vertices are projected back onto the input mesh surface during Remeshing, preserving the shape
- ``smoothing_rate`` (float):  [Read-Write] Smoothing Rate/Speed. Faster Smoothing results in a more regular mesh, but also more potential for undesirable 3D shape change and UV distortion
- ``smoothing_type`` (GeometryScriptRemeshSmoothingType):  [Read-Write] Type of 3D Mesh Smoothing to apply during Remeshing. Disable by setting SmoothingRate = 0
- ``use_full_remesh_passes`` (bool):  [Read-Write] By default, remeshing is accelerated by tracking a queue of edges that need to be processed. This is signficantly faster but can produce a lower quality output. Enable this option to use a more expensive strategy that guarantees maximum quality.

<a id="unreal.GeometryScriptRemeshOptions.__init__"></a>

#### __init__

```python
def __init__(
        discard_attributes: bool = False,
        reproject_to_input_mesh: bool = False,
        smoothing_type:
    GeometryScriptRemeshSmoothingType = GeometryScriptRemeshSmoothingType.
    UNIFORM,
        smoothing_rate: float = 0.000000,
        mesh_boundary_constraint:
    GeometryScriptRemeshEdgeConstraintType = GeometryScriptRemeshEdgeConstraintType
    .FIXED,
        group_boundary_constraint:
    GeometryScriptRemeshEdgeConstraintType = GeometryScriptRemeshEdgeConstraintType
    .FIXED,
        material_boundary_constraint:
    GeometryScriptRemeshEdgeConstraintType = GeometryScriptRemeshEdgeConstraintType
    .FIXED,
        allow_flips: bool = False,
        allow_splits: bool = False,
        allow_collapses: bool = False,
        prevent_normal_flips: bool = False,
        prevent_tiny_triangles: bool = False,
        use_full_remesh_passes: bool = False,
        remesh_iterations: int = 0,
        auto_compact: bool = False) -> None
```

<a id="unreal.GeometryScriptRemeshOptions.discard_attributes"></a>

#### discard_attributes

```python
@property
def discard_attributes() -> bool
```

(bool):  [Read-Write] When enabled, all mesh attributes are discarded, so UV and Normal Seams can be ignored. New per-vertex normals are computed.

<a id="unreal.GeometryScriptRemeshOptions.discard_attributes"></a>

#### discard_attributes

```python
@discard_attributes.setter
def discard_attributes(value: bool) -> None
```

<a id="unreal.GeometryScriptRemeshOptions.reproject_to_input_mesh"></a>

#### reproject_to_input_mesh

```python
@property
def reproject_to_input_mesh() -> bool
```

(bool):  [Read-Write] When enabled, mesh vertices are projected back onto the input mesh surface during Remeshing, preserving the shape

<a id="unreal.GeometryScriptRemeshOptions.reproject_to_input_mesh"></a>

#### reproject_to_input_mesh

```python
@reproject_to_input_mesh.setter
def reproject_to_input_mesh(value: bool) -> None
```

<a id="unreal.GeometryScriptRemeshOptions.smoothing_type"></a>

#### smoothing_type

```python
@property
def smoothing_type() -> GeometryScriptRemeshSmoothingType
```

(GeometryScriptRemeshSmoothingType):  [Read-Write] Type of 3D Mesh Smoothing to apply during Remeshing. Disable by setting SmoothingRate = 0

<a id="unreal.GeometryScriptRemeshOptions.smoothing_type"></a>

#### smoothing_type

```python
@smoothing_type.setter
def smoothing_type(value: GeometryScriptRemeshSmoothingType) -> None
```

<a id="unreal.GeometryScriptRemeshOptions.smoothing_rate"></a>

#### smoothing_rate

```python
@property
def smoothing_rate() -> float
```

(float):  [Read-Write] Smoothing Rate/Speed. Faster Smoothing results in a more regular mesh, but also more potential for undesirable 3D shape change and UV distortion

<a id="unreal.GeometryScriptRemeshOptions.smoothing_rate"></a>

#### smoothing_rate

```python
@smoothing_rate.setter
def smoothing_rate(value: float) -> None
```

<a id="unreal.GeometryScriptRemeshOptions.mesh_boundary_constraint"></a>

#### mesh_boundary_constraint

```python
@property
def mesh_boundary_constraint() -> GeometryScriptRemeshEdgeConstraintType
```

(GeometryScriptRemeshEdgeConstraintType):  [Read-Write] Constraints on the open mesh boundary/border edges

<a id="unreal.GeometryScriptRemeshOptions.mesh_boundary_constraint"></a>

#### mesh_boundary_constraint

```python
@mesh_boundary_constraint.setter
def mesh_boundary_constraint(
        value: GeometryScriptRemeshEdgeConstraintType) -> None
```

<a id="unreal.GeometryScriptRemeshOptions.group_boundary_constraint"></a>

#### group_boundary_constraint

```python
@property
def group_boundary_constraint() -> GeometryScriptRemeshEdgeConstraintType
```

(GeometryScriptRemeshEdgeConstraintType):  [Read-Write] Constraints on the mesh boundary/border edges between different PolyGroups of the Mesh

<a id="unreal.GeometryScriptRemeshOptions.group_boundary_constraint"></a>

#### group_boundary_constraint

```python
@group_boundary_constraint.setter
def group_boundary_constraint(
        value: GeometryScriptRemeshEdgeConstraintType) -> None
```

<a id="unreal.GeometryScriptRemeshOptions.material_boundary_constraint"></a>

#### material_boundary_constraint

```python
@property
def material_boundary_constraint() -> GeometryScriptRemeshEdgeConstraintType
```

(GeometryScriptRemeshEdgeConstraintType):  [Read-Write] Constraints on the mesh boundary/border edges between different Material Results of the Mesh

<a id="unreal.GeometryScriptRemeshOptions.material_boundary_constraint"></a>

#### material_boundary_constraint

```python
@material_boundary_constraint.setter
def material_boundary_constraint(
        value: GeometryScriptRemeshEdgeConstraintType) -> None
```

<a id="unreal.GeometryScriptRemeshOptions.allow_flips"></a>

#### allow_flips

```python
@property
def allow_flips() -> bool
```

(bool):  [Read-Write] Enable/Disable Edge Flips during Remeshing. Disabling flips will significantly reduce the output mesh quality

<a id="unreal.GeometryScriptRemeshOptions.allow_flips"></a>

#### allow_flips

```python
@allow_flips.setter
def allow_flips(value: bool) -> None
```

<a id="unreal.GeometryScriptRemeshOptions.allow_splits"></a>

#### allow_splits

```python
@property
def allow_splits() -> bool
```

(bool):  [Read-Write] Enable/Disable Edge Splits during Remeshing. Disabling Splits will prevent the mesh density from increasing.

<a id="unreal.GeometryScriptRemeshOptions.allow_splits"></a>

#### allow_splits

```python
@allow_splits.setter
def allow_splits(value: bool) -> None
```

<a id="unreal.GeometryScriptRemeshOptions.allow_collapses"></a>

#### allow_collapses

```python
@property
def allow_collapses() -> bool
```

(bool):  [Read-Write] Enable/Disable Edge Collapses during Remeshing. Disabling Collapses will prevent the mesh density from decreasing.

<a id="unreal.GeometryScriptRemeshOptions.allow_collapses"></a>

#### allow_collapses

```python
@allow_collapses.setter
def allow_collapses(value: bool) -> None
```

<a id="unreal.GeometryScriptRemeshOptions.prevent_normal_flips"></a>

#### prevent_normal_flips

```python
@property
def prevent_normal_flips() -> bool
```

(bool):  [Read-Write] When Enabled, Flips and Collapses will be skipped if they would flip any triangle face normals

<a id="unreal.GeometryScriptRemeshOptions.prevent_normal_flips"></a>

#### prevent_normal_flips

```python
@prevent_normal_flips.setter
def prevent_normal_flips(value: bool) -> None
```

<a id="unreal.GeometryScriptRemeshOptions.prevent_tiny_triangles"></a>

#### prevent_tiny_triangles

```python
@property
def prevent_tiny_triangles() -> bool
```

(bool):  [Read-Write] When Enabled, Flips and Collapses will be skipped if they would create tiny degenerate triangles

<a id="unreal.GeometryScriptRemeshOptions.prevent_tiny_triangles"></a>

#### prevent_tiny_triangles

```python
@prevent_tiny_triangles.setter
def prevent_tiny_triangles(value: bool) -> None
```

<a id="unreal.GeometryScriptRemeshOptions.use_full_remesh_passes"></a>

#### use_full_remesh_passes

```python
@property
def use_full_remesh_passes() -> bool
```

(bool):  [Read-Write] By default, remeshing is accelerated by tracking a queue of edges that need to be processed. This is signficantly faster but can produce a lower quality output. Enable this option to use a more expensive strategy that guarantees maximum quality.

<a id="unreal.GeometryScriptRemeshOptions.use_full_remesh_passes"></a>

#### use_full_remesh_passes

```python
@use_full_remesh_passes.setter
def use_full_remesh_passes(value: bool) -> None
```

<a id="unreal.GeometryScriptRemeshOptions.remesh_iterations"></a>

#### remesh_iterations

```python
@property
def remesh_iterations() -> int
```

(int32):  [Read-Write] Maximum Number of iterations of the Remeshing Strategy to apply to the Mesh. More iterations are generally more expensive (much moreso with bUseFullRemeshPasses = true)

<a id="unreal.GeometryScriptRemeshOptions.remesh_iterations"></a>

#### remesh_iterations

```python
@remesh_iterations.setter
def remesh_iterations(value: int) -> None
```

<a id="unreal.GeometryScriptRemeshOptions.auto_compact"></a>

#### auto_compact

```python
@property
def auto_compact() -> bool
```

(bool):  [Read-Write] If enabled, the output mesh is automatically compacted to remove gaps in the index space. This is expensive and can be disabled by advanced users.

<a id="unreal.GeometryScriptRemeshOptions.auto_compact"></a>

#### auto_compact

```python
@auto_compact.setter
def auto_compact(value: bool) -> None
```

<a id="unreal.GeometryScriptUniformRemeshOptions"></a>