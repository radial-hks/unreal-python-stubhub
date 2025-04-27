## InterchangeGenericCommonMeshesProperties Objects

```python
class InterchangeGenericCommonMeshesProperties(InterchangePipelineBase)
```

Interchange Generic Common Meshes Properties

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangePipelines
- **File**: InterchangeGenericAssetsPipelineSharedSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_detect_mesh_type`` (bool):  [Read-Write] If enabled, and some static mesh transforms are animated, the pipeline will convert the static mesh into a rigid skeletal mesh.
  This setting is only used if the Force All Meshes As Type setting is set to "None".
- ``bake_meshes`` (bool):  [Read-Write] If enabled, meshes are baked with the scene instance hierarchy transform.
- ``bake_pivot_meshes`` (bool):  [Read-Write] If enabled, the inverse node rotation pivot will be apply to the mesh vertices. The pivot from the DCC will then be the origin of the mesh.
- ``compute_weighted_normals`` (bool):  [Read-Write] If enabled, normals are computed using the surface area and the corner angle of the triangle as a ratio.
- ``force_all_mesh_as_type`` (InterchangeForceMeshType):  [Read-Write] If set, imports all meshes in the source as either static meshes or skeletal meshes.
  For skeletal meshes the conversion will happen only if there is no skinned meshes.
  Mixing rigid skeletal mesh with skinned mesh is not good and will result in multiple skeletal meshes.
- ``import_lods`` (bool):  [Read-Write] If enabled, any existing LODs for meshes are imported. This setting is only used if the Bake Meshes setting is also enabled.
- ``keep_sections_separate`` (bool):  [Read-Write] If checked, sections with matching materials are kept separate and will not get combined.
- ``recompute_normals`` (bool):  [Read-Write] If enabled, normals in the imported mesh are ignored and recomputed.
- ``recompute_tangents`` (bool):  [Read-Write] If enabled, tangents in the imported mesh are ignored and recomputed.
- ``remove_degenerates`` (bool):  [Read-Write] If true, degenerate triangles are removed.
- ``use_backwards_compatible_f16_trunc_u_vs`` (bool):  [Read-Write] If enabled, UVs are converted to 16-bit by a legacy truncation process instead of the default rounding process. This may avoid differences when reimporting older content.
- ``use_full_precision_u_vs`` (bool):  [Read-Write] If true, UVs are stored at full floating-point precision.
- ``use_high_precision_tangent_basis`` (bool):  [Read-Write] If true, tangents are stored at 16-bit vs 8-bit precision.
- ``use_mikk_t_space`` (bool):  [Read-Write] If enabled, tangents are recomputed using MikkTSpace.
- ``vertex_color_import_option`` (InterchangeVertexColorImportOption):  [Read-Write] Specify how vertex colors should be imported.
- ``vertex_override_color`` (Color):  [Read-Write] Specify an override color for use when the Vertex Color Import Option setting is set to Override.

<a id="unreal.InterchangeGenericCommonMeshesProperties.force_all_mesh_as_type"></a>

#### force_all_mesh_as_type

```python
@property
def force_all_mesh_as_type() -> InterchangeForceMeshType
```

(InterchangeForceMeshType):  [Read-Write] If set, imports all meshes in the source as either static meshes or skeletal meshes.
For skeletal meshes the conversion will happen only if there is no skinned meshes.
Mixing rigid skeletal mesh with skinned mesh is not good and will result in multiple skeletal meshes.

<a id="unreal.InterchangeGenericCommonMeshesProperties.force_all_mesh_as_type"></a>

#### force_all_mesh_as_type

```python
@force_all_mesh_as_type.setter
def force_all_mesh_as_type(value: InterchangeForceMeshType) -> None
```

<a id="unreal.InterchangeGenericCommonMeshesProperties.auto_detect_mesh_type"></a>

#### auto_detect_mesh_type

```python
@property
def auto_detect_mesh_type() -> bool
```

(bool):  [Read-Write] If enabled, and some static mesh transforms are animated, the pipeline will convert the static mesh into a rigid skeletal mesh.
This setting is only used if the Force All Meshes As Type setting is set to "None".

<a id="unreal.InterchangeGenericCommonMeshesProperties.auto_detect_mesh_type"></a>

#### auto_detect_mesh_type

```python
@auto_detect_mesh_type.setter
def auto_detect_mesh_type(value: bool) -> None
```

<a id="unreal.InterchangeGenericCommonMeshesProperties.import_lods"></a>

#### import_lods

```python
@property
def import_lods() -> bool
```

(bool):  [Read-Write] If enabled, any existing LODs for meshes are imported. This setting is only used if the Bake Meshes setting is also enabled.

<a id="unreal.InterchangeGenericCommonMeshesProperties.import_lods"></a>

#### import_lods

```python
@import_lods.setter
def import_lods(value: bool) -> None
```

<a id="unreal.InterchangeGenericCommonMeshesProperties.bake_meshes"></a>

#### bake_meshes

```python
@property
def bake_meshes() -> bool
```

(bool):  [Read-Write] If enabled, meshes are baked with the scene instance hierarchy transform.

<a id="unreal.InterchangeGenericCommonMeshesProperties.bake_meshes"></a>

#### bake_meshes

```python
@bake_meshes.setter
def bake_meshes(value: bool) -> None
```

<a id="unreal.InterchangeGenericCommonMeshesProperties.bake_pivot_meshes"></a>

#### bake_pivot_meshes

```python
@property
def bake_pivot_meshes() -> bool
```

(bool):  [Read-Write] If enabled, the inverse node rotation pivot will be apply to the mesh vertices. The pivot from the DCC will then be the origin of the mesh.

<a id="unreal.InterchangeGenericCommonMeshesProperties.bake_pivot_meshes"></a>

#### bake_pivot_meshes

```python
@bake_pivot_meshes.setter
def bake_pivot_meshes(value: bool) -> None
```

<a id="unreal.InterchangeGenericCommonMeshesProperties.keep_sections_separate"></a>

#### keep_sections_separate

```python
@property
def keep_sections_separate() -> bool
```

(bool):  [Read-Write] If checked, sections with matching materials are kept separate and will not get combined.

<a id="unreal.InterchangeGenericCommonMeshesProperties.keep_sections_separate"></a>

#### keep_sections_separate

```python
@keep_sections_separate.setter
def keep_sections_separate(value: bool) -> None
```

<a id="unreal.InterchangeGenericCommonMeshesProperties.vertex_color_import_option"></a>

#### vertex_color_import_option

```python
@property
def vertex_color_import_option() -> InterchangeVertexColorImportOption
```

(InterchangeVertexColorImportOption):  [Read-Write] Specify how vertex colors should be imported.

<a id="unreal.InterchangeGenericCommonMeshesProperties.vertex_color_import_option"></a>

#### vertex_color_import_option

```python
@vertex_color_import_option.setter
def vertex_color_import_option(
        value: InterchangeVertexColorImportOption) -> None
```

<a id="unreal.InterchangeGenericCommonMeshesProperties.vertex_override_color"></a>

#### vertex_override_color

```python
@property
def vertex_override_color() -> Color
```

(Color):  [Read-Write] Specify an override color for use when the Vertex Color Import Option setting is set to Override.

<a id="unreal.InterchangeGenericCommonMeshesProperties.vertex_override_color"></a>

#### vertex_override_color

```python
@vertex_override_color.setter
def vertex_override_color(value: Color) -> None
```

<a id="unreal.InterchangeGenericCommonMeshesProperties.recompute_normals"></a>

#### recompute_normals

```python
@property
def recompute_normals() -> bool
```

(bool):  [Read-Write] If enabled, normals in the imported mesh are ignored and recomputed.

<a id="unreal.InterchangeGenericCommonMeshesProperties.recompute_normals"></a>

#### recompute_normals

```python
@recompute_normals.setter
def recompute_normals(value: bool) -> None
```

<a id="unreal.InterchangeGenericCommonMeshesProperties.recompute_tangents"></a>

#### recompute_tangents

```python
@property
def recompute_tangents() -> bool
```

(bool):  [Read-Write] If enabled, tangents in the imported mesh are ignored and recomputed.

<a id="unreal.InterchangeGenericCommonMeshesProperties.recompute_tangents"></a>

#### recompute_tangents

```python
@recompute_tangents.setter
def recompute_tangents(value: bool) -> None
```

<a id="unreal.InterchangeGenericCommonMeshesProperties.use_mikk_t_space"></a>

#### use_mikk_t_space

```python
@property
def use_mikk_t_space() -> bool
```

(bool):  [Read-Write] If enabled, tangents are recomputed using MikkTSpace.

<a id="unreal.InterchangeGenericCommonMeshesProperties.use_mikk_t_space"></a>

#### use_mikk_t_space

```python
@use_mikk_t_space.setter
def use_mikk_t_space(value: bool) -> None
```

<a id="unreal.InterchangeGenericCommonMeshesProperties.compute_weighted_normals"></a>

#### compute_weighted_normals

```python
@property
def compute_weighted_normals() -> bool
```

(bool):  [Read-Write] If enabled, normals are computed using the surface area and the corner angle of the triangle as a ratio.

<a id="unreal.InterchangeGenericCommonMeshesProperties.compute_weighted_normals"></a>

#### compute_weighted_normals

```python
@compute_weighted_normals.setter
def compute_weighted_normals(value: bool) -> None
```

<a id="unreal.InterchangeGenericCommonMeshesProperties.use_high_precision_tangent_basis"></a>

#### use_high_precision_tangent_basis

```python
@property
def use_high_precision_tangent_basis() -> bool
```

(bool):  [Read-Write] If true, tangents are stored at 16-bit vs 8-bit precision.

<a id="unreal.InterchangeGenericCommonMeshesProperties.use_high_precision_tangent_basis"></a>

#### use_high_precision_tangent_basis

```python
@use_high_precision_tangent_basis.setter
def use_high_precision_tangent_basis(value: bool) -> None
```

<a id="unreal.InterchangeGenericCommonMeshesProperties.use_full_precision_u_vs"></a>

#### use_full_precision_u_vs

```python
@property
def use_full_precision_u_vs() -> bool
```

(bool):  [Read-Write] If true, UVs are stored at full floating-point precision.

<a id="unreal.InterchangeGenericCommonMeshesProperties.use_full_precision_u_vs"></a>

#### use_full_precision_u_vs

```python
@use_full_precision_u_vs.setter
def use_full_precision_u_vs(value: bool) -> None
```

<a id="unreal.InterchangeGenericCommonMeshesProperties.use_backwards_compatible_f16_trunc_u_vs"></a>

#### use_backwards_compatible_f16_trunc_u_vs

```python
@property
def use_backwards_compatible_f16_trunc_u_vs() -> bool
```

(bool):  [Read-Write] If enabled, UVs are converted to 16-bit by a legacy truncation process instead of the default rounding process. This may avoid differences when reimporting older content.

<a id="unreal.InterchangeGenericCommonMeshesProperties.use_backwards_compatible_f16_trunc_u_vs"></a>

#### use_backwards_compatible_f16_trunc_u_vs

```python
@use_backwards_compatible_f16_trunc_u_vs.setter
def use_backwards_compatible_f16_trunc_u_vs(value: bool) -> None
```

<a id="unreal.InterchangeGenericCommonMeshesProperties.remove_degenerates"></a>

#### remove_degenerates

```python
@property
def remove_degenerates() -> bool
```

(bool):  [Read-Write] If true, degenerate triangles are removed.

<a id="unreal.InterchangeGenericCommonMeshesProperties.remove_degenerates"></a>

#### remove_degenerates

```python
@remove_degenerates.setter
def remove_degenerates(value: bool) -> None
```

<a id="unreal.InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties"></a>