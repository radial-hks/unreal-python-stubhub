## SkeletalMeshBuildSettings Objects

```python
class SkeletalMeshBuildSettings(StructBase)
```

Settings applied when building a mesh.

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_influence_limit`` (int32):  [Read-Write] The maximum number of bone influences to allow each vertex in this mesh to use.

  If set higher than the limit determined by the project settings, it has no effect.

  If set to 0, the value is taken from the DefaultBoneInfluenceLimit project setting.
- ``compute_weighted_normals`` (bool):  [Read-Write] If true, we will use the surface area and the corner angle of the triangle as a ratio when computing the normals.
- ``morph_threshold_position`` (float):  [Read-Write] Threshold to compare vertex position equality when computing morph target deltas.
- ``recompute_normals`` (bool):  [Read-Write] If true, normals in the raw mesh are ignored and recomputed.
- ``recompute_tangents`` (bool):  [Read-Write] If true, tangents in the raw mesh are ignored and recomputed.
- ``remove_degenerates`` (bool):  [Read-Write] If true, degenerate triangles will be removed.
- ``threshold_position`` (float):  [Read-Write] Threshold use to decide if two vertex position are equal.
- ``threshold_tangent_normal`` (float):  [Read-Write] Threshold use to decide if two normal, tangents or bi-normals are equal.
- ``threshold_uv`` (float):  [Read-Write] Threshold use to decide if two UVs are equal.
- ``use_backwards_compatible_f16_trunc_u_vs`` (bool):  [Read-Write] If true, UVs will use backwards-compatible F16 conversion with truncation for legacy meshes.
- ``use_full_precision_u_vs`` (bool):  [Read-Write] If true, UVs will be stored at full floating point precision.
- ``use_high_precision_skin_weights`` (bool):  [Read-Write] Use 16-bit precision for rendering skin weights, instead of 8-bit precision.
- ``use_high_precision_tangent_basis`` (bool):  [Read-Write] If true, Tangents will be stored at 16 bit vs 8 bit precision.
- ``use_mikk_t_space`` (bool):  [Read-Write] If true, degenerate triangles will be removed.

<a id="unreal.SkeletalMeshBuildSettings.__init__"></a>

#### __init__

```python
def __init__(recompute_normals: bool = False,
             recompute_tangents: bool = False,
             use_mikk_t_space: bool = False,
             compute_weighted_normals: bool = False,
             remove_degenerates: bool = False,
             use_high_precision_tangent_basis: bool = False,
             use_high_precision_skin_weights: bool = False,
             use_full_precision_u_vs: bool = False,
             use_backwards_compatible_f16_trunc_u_vs: bool = False,
             threshold_position: float = 0.000000,
             threshold_tangent_normal: float = 0.000000,
             threshold_uv: float = 0.000000,
             morph_threshold_position: float = 0.000000,
             bone_influence_limit: int = 0) -> None
```

<a id="unreal.SkeletalMeshBuildSettings.recompute_normals"></a>

#### recompute_normals

```python
@property
def recompute_normals() -> bool
```

(bool):  [Read-Write] If true, normals in the raw mesh are ignored and recomputed.

<a id="unreal.SkeletalMeshBuildSettings.recompute_normals"></a>

#### recompute_normals

```python
@recompute_normals.setter
def recompute_normals(value: bool) -> None
```

<a id="unreal.SkeletalMeshBuildSettings.recompute_tangents"></a>

#### recompute_tangents

```python
@property
def recompute_tangents() -> bool
```

(bool):  [Read-Write] If true, tangents in the raw mesh are ignored and recomputed.

<a id="unreal.SkeletalMeshBuildSettings.recompute_tangents"></a>

#### recompute_tangents

```python
@recompute_tangents.setter
def recompute_tangents(value: bool) -> None
```

<a id="unreal.SkeletalMeshBuildSettings.use_mikk_t_space"></a>

#### use_mikk_t_space

```python
@property
def use_mikk_t_space() -> bool
```

(bool):  [Read-Write] If true, degenerate triangles will be removed.

<a id="unreal.SkeletalMeshBuildSettings.use_mikk_t_space"></a>

#### use_mikk_t_space

```python
@use_mikk_t_space.setter
def use_mikk_t_space(value: bool) -> None
```

<a id="unreal.SkeletalMeshBuildSettings.compute_weighted_normals"></a>

#### compute_weighted_normals

```python
@property
def compute_weighted_normals() -> bool
```

(bool):  [Read-Write] If true, we will use the surface area and the corner angle of the triangle as a ratio when computing the normals.

<a id="unreal.SkeletalMeshBuildSettings.compute_weighted_normals"></a>

#### compute_weighted_normals

```python
@compute_weighted_normals.setter
def compute_weighted_normals(value: bool) -> None
```

<a id="unreal.SkeletalMeshBuildSettings.remove_degenerates"></a>

#### remove_degenerates

```python
@property
def remove_degenerates() -> bool
```

(bool):  [Read-Write] If true, degenerate triangles will be removed.

<a id="unreal.SkeletalMeshBuildSettings.remove_degenerates"></a>

#### remove_degenerates

```python
@remove_degenerates.setter
def remove_degenerates(value: bool) -> None
```

<a id="unreal.SkeletalMeshBuildSettings.use_high_precision_tangent_basis"></a>

#### use_high_precision_tangent_basis

```python
@property
def use_high_precision_tangent_basis() -> bool
```

(bool):  [Read-Write] If true, Tangents will be stored at 16 bit vs 8 bit precision.

<a id="unreal.SkeletalMeshBuildSettings.use_high_precision_tangent_basis"></a>

#### use_high_precision_tangent_basis

```python
@use_high_precision_tangent_basis.setter
def use_high_precision_tangent_basis(value: bool) -> None
```

<a id="unreal.SkeletalMeshBuildSettings.use_high_precision_skin_weights"></a>

#### use_high_precision_skin_weights

```python
@property
def use_high_precision_skin_weights() -> bool
```

(bool):  [Read-Write] Use 16-bit precision for rendering skin weights, instead of 8-bit precision.

<a id="unreal.SkeletalMeshBuildSettings.use_high_precision_skin_weights"></a>

#### use_high_precision_skin_weights

```python
@use_high_precision_skin_weights.setter
def use_high_precision_skin_weights(value: bool) -> None
```

<a id="unreal.SkeletalMeshBuildSettings.use_full_precision_u_vs"></a>

#### use_full_precision_u_vs

```python
@property
def use_full_precision_u_vs() -> bool
```

(bool):  [Read-Write] If true, UVs will be stored at full floating point precision.

<a id="unreal.SkeletalMeshBuildSettings.use_full_precision_u_vs"></a>

#### use_full_precision_u_vs

```python
@use_full_precision_u_vs.setter
def use_full_precision_u_vs(value: bool) -> None
```

<a id="unreal.SkeletalMeshBuildSettings.use_backwards_compatible_f16_trunc_u_vs"></a>

#### use_backwards_compatible_f16_trunc_u_vs

```python
@property
def use_backwards_compatible_f16_trunc_u_vs() -> bool
```

(bool):  [Read-Write] If true, UVs will use backwards-compatible F16 conversion with truncation for legacy meshes.

<a id="unreal.SkeletalMeshBuildSettings.use_backwards_compatible_f16_trunc_u_vs"></a>

#### use_backwards_compatible_f16_trunc_u_vs

```python
@use_backwards_compatible_f16_trunc_u_vs.setter
def use_backwards_compatible_f16_trunc_u_vs(value: bool) -> None
```

<a id="unreal.SkeletalMeshBuildSettings.threshold_position"></a>

#### threshold_position

```python
@property
def threshold_position() -> float
```

(float):  [Read-Write] Threshold use to decide if two vertex position are equal.

<a id="unreal.SkeletalMeshBuildSettings.threshold_position"></a>

#### threshold_position

```python
@threshold_position.setter
def threshold_position(value: float) -> None
```

<a id="unreal.SkeletalMeshBuildSettings.threshold_tangent_normal"></a>

#### threshold_tangent_normal

```python
@property
def threshold_tangent_normal() -> float
```

(float):  [Read-Write] Threshold use to decide if two normal, tangents or bi-normals are equal.

<a id="unreal.SkeletalMeshBuildSettings.threshold_tangent_normal"></a>

#### threshold_tangent_normal

```python
@threshold_tangent_normal.setter
def threshold_tangent_normal(value: float) -> None
```

<a id="unreal.SkeletalMeshBuildSettings.threshold_uv"></a>

#### threshold_uv

```python
@property
def threshold_uv() -> float
```

(float):  [Read-Write] Threshold use to decide if two UVs are equal.

<a id="unreal.SkeletalMeshBuildSettings.threshold_uv"></a>

#### threshold_uv

```python
@threshold_uv.setter
def threshold_uv(value: float) -> None
```

<a id="unreal.SkeletalMeshBuildSettings.morph_threshold_position"></a>

#### morph_threshold_position

```python
@property
def morph_threshold_position() -> float
```

(float):  [Read-Write] Threshold to compare vertex position equality when computing morph target deltas.

<a id="unreal.SkeletalMeshBuildSettings.morph_threshold_position"></a>

#### morph_threshold_position

```python
@morph_threshold_position.setter
def morph_threshold_position(value: float) -> None
```

<a id="unreal.SkeletalMeshBuildSettings.bone_influence_limit"></a>

#### bone_influence_limit

```python
@property
def bone_influence_limit() -> int
```

(int32):  [Read-Write] The maximum number of bone influences to allow each vertex in this mesh to use.

If set higher than the limit determined by the project settings, it has no effect.

If set to 0, the value is taken from the DefaultBoneInfluenceLimit project setting.

<a id="unreal.SkeletalMeshBuildSettings.bone_influence_limit"></a>

#### bone_influence_limit

```python
@bone_influence_limit.setter
def bone_influence_limit(value: int) -> None
```

<a id="unreal.MeshDisplacementMap"></a>