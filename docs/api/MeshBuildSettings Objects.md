## MeshBuildSettings Objects

```python
class MeshBuildSettings(StructBase)
```

Settings applied when building a mesh.

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``build_reversed_index_buffer`` (bool):  [Read-Write] Required to optimize mesh in mirrored transform. Double index buffer size.
- ``build_scale3d`` (Vector):  [Read-Write] The local scale applied when building the mesh
- ``compute_weighted_normals`` (bool):  [Read-Write] If true, we will use the surface area and the corner angle of the triangle as a ratio when computing the normals.
- ``distance_field_replacement_mesh`` (StaticMesh):  [Read-Write]
- ``distance_field_resolution_scale`` (float):  [Read-Write] Scale to apply to the mesh when allocating the distance field volume texture.
  The default scale is 1, which is assuming that the mesh will be placed unscaled in the world.
- ``dst_lightmap_index`` (int32):  [Read-Write]
- ``generate_distance_field_as_if_two_sided`` (bool):  [Read-Write] Whether to generate the distance field treating every triangle hit as a front face.
  When enabled prevents the distance field from being discarded due to the mesh being open, but also lowers Distance Field AO quality.
- ``generate_lightmap_u_vs`` (bool):  [Read-Write]
- ``max_lumen_mesh_cards`` (int32):  [Read-Write] Max Lumen mesh cards to generate for this mesh.
  More cards means that surface will have better coverage, but will result in increased runtime overhead.
  Set to 0 in order to disable mesh card generation for this mesh.
  Default is 12.
- ``min_lightmap_resolution`` (int32):  [Read-Write]
- ``recompute_normals`` (bool):  [Read-Write] If true, normals in the raw mesh are ignored and recomputed.
- ``recompute_tangents`` (bool):  [Read-Write] If true, tangents in the raw mesh are ignored and recomputed.
- ``remove_degenerates`` (bool):  [Read-Write] If true, degenerate triangles will be removed.
- ``src_lightmap_index`` (int32):  [Read-Write]
- ``support_face_remap`` (bool):  [Read-Write]
- ``use_backwards_compatible_f16_trunc_u_vs`` (bool):  [Read-Write] If true, UVs will use backwards-compatible F16 conversion with truncation for legacy meshes.
- ``use_full_precision_u_vs`` (bool):  [Read-Write] If true, UVs will be stored at full floating point precision.
- ``use_high_precision_tangent_basis`` (bool):  [Read-Write] If true, Tangents will be stored at 16 bit vs 8 bit precision.
- ``use_mikk_t_space`` (bool):  [Read-Write] If true, degenerate triangles will be removed.

<a id="unreal.MeshBuildSettings.__init__"></a>

#### __init__

```python
def __init__(use_mikk_t_space: bool = False,
             recompute_normals: bool = False,
             recompute_tangents: bool = False,
             compute_weighted_normals: bool = False,
             remove_degenerates: bool = False,
             build_reversed_index_buffer: bool = False,
             use_high_precision_tangent_basis: bool = False,
             use_full_precision_u_vs: bool = False,
             use_backwards_compatible_f16_trunc_u_vs: bool = False,
             generate_lightmap_u_vs: bool = False,
             generate_distance_field_as_if_two_sided: bool = False,
             support_face_remap: bool = False,
             min_lightmap_resolution: int = 0,
             src_lightmap_index: int = 0,
             dst_lightmap_index: int = 0,
             build_scale3d: Vector = [0.000000, 0.000000, 0.000000],
             distance_field_resolution_scale: float = 0.000000,
             distance_field_replacement_mesh: StaticMesh = None,
             max_lumen_mesh_cards: int = 0) -> None
```

<a id="unreal.MeshBuildSettings.use_mikk_t_space"></a>

#### use_mikk_t_space

```python
@property
def use_mikk_t_space() -> bool
```

(bool):  [Read-Write] If true, degenerate triangles will be removed.

<a id="unreal.MeshBuildSettings.use_mikk_t_space"></a>

#### use_mikk_t_space

```python
@use_mikk_t_space.setter
def use_mikk_t_space(value: bool) -> None
```

<a id="unreal.MeshBuildSettings.recompute_normals"></a>

#### recompute_normals

```python
@property
def recompute_normals() -> bool
```

(bool):  [Read-Write] If true, normals in the raw mesh are ignored and recomputed.

<a id="unreal.MeshBuildSettings.recompute_normals"></a>

#### recompute_normals

```python
@recompute_normals.setter
def recompute_normals(value: bool) -> None
```

<a id="unreal.MeshBuildSettings.recompute_tangents"></a>

#### recompute_tangents

```python
@property
def recompute_tangents() -> bool
```

(bool):  [Read-Write] If true, tangents in the raw mesh are ignored and recomputed.

<a id="unreal.MeshBuildSettings.recompute_tangents"></a>

#### recompute_tangents

```python
@recompute_tangents.setter
def recompute_tangents(value: bool) -> None
```

<a id="unreal.MeshBuildSettings.compute_weighted_normals"></a>

#### compute_weighted_normals

```python
@property
def compute_weighted_normals() -> bool
```

(bool):  [Read-Write] If true, we will use the surface area and the corner angle of the triangle as a ratio when computing the normals.

<a id="unreal.MeshBuildSettings.compute_weighted_normals"></a>

#### compute_weighted_normals

```python
@compute_weighted_normals.setter
def compute_weighted_normals(value: bool) -> None
```

<a id="unreal.MeshBuildSettings.remove_degenerates"></a>

#### remove_degenerates

```python
@property
def remove_degenerates() -> bool
```

(bool):  [Read-Write] If true, degenerate triangles will be removed.

<a id="unreal.MeshBuildSettings.remove_degenerates"></a>

#### remove_degenerates

```python
@remove_degenerates.setter
def remove_degenerates(value: bool) -> None
```

<a id="unreal.MeshBuildSettings.build_reversed_index_buffer"></a>

#### build_reversed_index_buffer

```python
@property
def build_reversed_index_buffer() -> bool
```

(bool):  [Read-Write] Required to optimize mesh in mirrored transform. Double index buffer size.

<a id="unreal.MeshBuildSettings.build_reversed_index_buffer"></a>

#### build_reversed_index_buffer

```python
@build_reversed_index_buffer.setter
def build_reversed_index_buffer(value: bool) -> None
```

<a id="unreal.MeshBuildSettings.use_high_precision_tangent_basis"></a>

#### use_high_precision_tangent_basis

```python
@property
def use_high_precision_tangent_basis() -> bool
```

(bool):  [Read-Write] If true, Tangents will be stored at 16 bit vs 8 bit precision.

<a id="unreal.MeshBuildSettings.use_high_precision_tangent_basis"></a>

#### use_high_precision_tangent_basis

```python
@use_high_precision_tangent_basis.setter
def use_high_precision_tangent_basis(value: bool) -> None
```

<a id="unreal.MeshBuildSettings.use_full_precision_u_vs"></a>

#### use_full_precision_u_vs

```python
@property
def use_full_precision_u_vs() -> bool
```

(bool):  [Read-Write] If true, UVs will be stored at full floating point precision.

<a id="unreal.MeshBuildSettings.use_full_precision_u_vs"></a>

#### use_full_precision_u_vs

```python
@use_full_precision_u_vs.setter
def use_full_precision_u_vs(value: bool) -> None
```

<a id="unreal.MeshBuildSettings.use_backwards_compatible_f16_trunc_u_vs"></a>

#### use_backwards_compatible_f16_trunc_u_vs

```python
@property
def use_backwards_compatible_f16_trunc_u_vs() -> bool
```

(bool):  [Read-Write] If true, UVs will use backwards-compatible F16 conversion with truncation for legacy meshes.

<a id="unreal.MeshBuildSettings.use_backwards_compatible_f16_trunc_u_vs"></a>

#### use_backwards_compatible_f16_trunc_u_vs

```python
@use_backwards_compatible_f16_trunc_u_vs.setter
def use_backwards_compatible_f16_trunc_u_vs(value: bool) -> None
```

<a id="unreal.MeshBuildSettings.generate_lightmap_u_vs"></a>

#### generate_lightmap_u_vs

```python
@property
def generate_lightmap_u_vs() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MeshBuildSettings.generate_lightmap_u_vs"></a>

#### generate_lightmap_u_vs

```python
@generate_lightmap_u_vs.setter
def generate_lightmap_u_vs(value: bool) -> None
```

<a id="unreal.MeshBuildSettings.generate_distance_field_as_if_two_sided"></a>

#### generate_distance_field_as_if_two_sided

```python
@property
def generate_distance_field_as_if_two_sided() -> bool
```

(bool):  [Read-Write] Whether to generate the distance field treating every triangle hit as a front face.
When enabled prevents the distance field from being discarded due to the mesh being open, but also lowers Distance Field AO quality.

<a id="unreal.MeshBuildSettings.generate_distance_field_as_if_two_sided"></a>

#### generate_distance_field_as_if_two_sided

```python
@generate_distance_field_as_if_two_sided.setter
def generate_distance_field_as_if_two_sided(value: bool) -> None
```

<a id="unreal.MeshBuildSettings.support_face_remap"></a>

#### support_face_remap

```python
@property
def support_face_remap() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MeshBuildSettings.support_face_remap"></a>

#### support_face_remap

```python
@support_face_remap.setter
def support_face_remap(value: bool) -> None
```

<a id="unreal.MeshBuildSettings.min_lightmap_resolution"></a>

#### min_lightmap_resolution

```python
@property
def min_lightmap_resolution() -> int
```

(int32):  [Read-Write]

<a id="unreal.MeshBuildSettings.min_lightmap_resolution"></a>

#### min_lightmap_resolution

```python
@min_lightmap_resolution.setter
def min_lightmap_resolution(value: int) -> None
```

<a id="unreal.MeshBuildSettings.src_lightmap_index"></a>

#### src_lightmap_index

```python
@property
def src_lightmap_index() -> int
```

(int32):  [Read-Write]

<a id="unreal.MeshBuildSettings.src_lightmap_index"></a>

#### src_lightmap_index

```python
@src_lightmap_index.setter
def src_lightmap_index(value: int) -> None
```

<a id="unreal.MeshBuildSettings.dst_lightmap_index"></a>

#### dst_lightmap_index

```python
@property
def dst_lightmap_index() -> int
```

(int32):  [Read-Write]

<a id="unreal.MeshBuildSettings.dst_lightmap_index"></a>

#### dst_lightmap_index

```python
@dst_lightmap_index.setter
def dst_lightmap_index(value: int) -> None
```

<a id="unreal.MeshBuildSettings.build_scale3d"></a>

#### build_scale3d

```python
@property
def build_scale3d() -> Vector
```

(Vector):  [Read-Write] The local scale applied when building the mesh

<a id="unreal.MeshBuildSettings.build_scale3d"></a>

#### build_scale3d

```python
@build_scale3d.setter
def build_scale3d(value: Vector) -> None
```

<a id="unreal.MeshBuildSettings.distance_field_resolution_scale"></a>

#### distance_field_resolution_scale

```python
@property
def distance_field_resolution_scale() -> float
```

(float):  [Read-Write] Scale to apply to the mesh when allocating the distance field volume texture.
The default scale is 1, which is assuming that the mesh will be placed unscaled in the world.

<a id="unreal.MeshBuildSettings.distance_field_resolution_scale"></a>

#### distance_field_resolution_scale

```python
@distance_field_resolution_scale.setter
def distance_field_resolution_scale(value: float) -> None
```

<a id="unreal.MeshBuildSettings.distance_field_replacement_mesh"></a>

#### distance_field_replacement_mesh

```python
@property
def distance_field_replacement_mesh() -> StaticMesh
```

(StaticMesh):  [Read-Write]

<a id="unreal.MeshBuildSettings.distance_field_replacement_mesh"></a>

#### distance_field_replacement_mesh

```python
@distance_field_replacement_mesh.setter
def distance_field_replacement_mesh(value: StaticMesh) -> None
```

<a id="unreal.MeshBuildSettings.max_lumen_mesh_cards"></a>

#### max_lumen_mesh_cards

```python
@property
def max_lumen_mesh_cards() -> int
```

(int32):  [Read-Write] Max Lumen mesh cards to generate for this mesh.
More cards means that surface will have better coverage, but will result in increased runtime overhead.
Set to 0 in order to disable mesh card generation for this mesh.
Default is 12.

<a id="unreal.MeshBuildSettings.max_lumen_mesh_cards"></a>

#### max_lumen_mesh_cards

```python
@max_lumen_mesh_cards.setter
def max_lumen_mesh_cards(value: int) -> None
```

<a id="unreal.SkeletalMeshBuildSettings"></a>