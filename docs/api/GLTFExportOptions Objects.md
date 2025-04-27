## GLTFExportOptions Objects

```python
class GLTFExportOptions(Object)
```

GLTFExport Options

**C++ Source:**

- **Plugin**: GLTFExporter
- **Module**: GLTFExporter
- **File**: GLTFExportOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``adjust_normalmaps`` (bool):  [Read-Write] If enabled, exported normalmaps will be adjusted from Unreal to glTF convention (i.e. the green channel is flipped).
- ``bake_material_inputs`` (GLTFMaterialBakeMode):  [Read-Write] Bake mode determining if and how a material input is baked out to a texture. Baking is only used for non-trivial material inputs (i.e. not simple texture or constant expressions).
- ``default_input_bake_settings`` (Map[GLTFMaterialPropertyGroup, GLTFOverrideMaterialBakeSettings]):  [Read-Write] Input-specific default bake settings that override the general defaults above.
- ``default_level_of_detail`` (int32):  [Read-Write] Default LOD level used for exporting a mesh. Can be overridden by component or asset settings (e.g. minimum or forced LOD level).
- ``default_material_bake_filter`` (TextureFilter):  [Read-Write] Default filtering mode used when sampling the baked out texture. Can be overridden by material- and input-specific bake settings, see GLTFMaterialExportOptions.
- ``default_material_bake_size`` (GLTFMaterialBakeSize):  [Read-Write] Default size of the baked out texture (containing the material input). Can be overridden by material- and input-specific bake settings, see GLTFMaterialExportOptions.
- ``default_material_bake_tiling`` (TextureAddress):  [Read-Write] Default addressing mode used when sampling the baked out texture. Can be overridden by material- and input-specific bake settings, see GLTFMaterialExportOptions.
- ``export_animation_sequences`` (bool):  [Read-Write] If enabled, export single animation asset used by a skeletal mesh component. Export of vertex skin weights must be enabled.
- ``export_cameras`` (bool):  [Read-Write] If enabled, export camera components.
- ``export_clear_coat_materials`` (bool):  [Read-Write] If enabled, materials with shading model clear coat will be properly exported. Uses extension KHR_materials_clearcoat.
- ``export_cloth_materials`` (bool):  [Read-Write] If enabled, materials with shading model cloth will be properly exported. Uses extension KHR_materials_sheen.
- ``export_emissive_strength`` (bool):  [Read-Write] If enabled, allows materials to have an emissive factor that exceeds the standard range [0.0, 1.0]. Uses extension KHR_materials_emissive_strength.
- ``export_hidden_in_game`` (bool):  [Read-Write] If enabled, export actors and components that are flagged as hidden in-game.
- ``export_level_sequences`` (bool):  [Read-Write] If enabled, export level sequences. Only transform tracks are currently supported. The level sequence will be played at the assigned display rate.
- ``export_lights`` (bool):  [Read-Write] If enabled, export directional, point, and spot light components. Uses extension KHR_lights_punctual.
- ``export_material_variants`` (GLTFMaterialVariantMode):  [Read-Write] Mode determining if and how to export material variants that change the materials property on a static or skeletal mesh component.
- ``export_preview_mesh`` (bool):  [Read-Write] If enabled, the preview mesh for a standalone animation or material asset will also be exported.
- ``export_proxy_materials`` (bool):  [Read-Write] If enabled, materials that have a proxy defined in their user data, will be exported using that proxy instead. This setting won't affect proxy materials exported or referenced directly.
- ``export_source_model`` (bool):  [Read-Write] If enabled, exports the SourceModel. If false, exports the Render Data.
- ``export_specular_glossiness_materials`` (bool):  [Read-Write] If enabled, materials using the Importer's SpecularGlossiness material function will be exported. Uses extension KHR_materials_pbrSpecularGlossiness.
- ``export_texture_transforms`` (bool):  [Read-Write] If enabled, export UV offset and scale/tiling used in materials. Uses extension KHR_texture_transform.
- ``export_thin_translucent_materials`` (bool):  [Read-Write] If enabled, materials with shading model thin translucency will be exported. Export is only partial. Uses extension KHR_materials_transmission.
- ``export_uniform_scale`` (float):  [Read-Write] Scale factor used for exporting all assets (0.01 by default) for conversion from centimeters (Unreal default) to meters (glTF).
- ``export_unlit_materials`` (bool):  [Read-Write] If enabled, materials with shading model unlit will be properly exported. Uses extension KHR_materials_unlit.
- ``export_vertex_colors`` (bool):  [Read-Write] If enabled, export vertex color. Not recommended due to vertex colors always being used as a base color multiplier in glTF, regardless of material. Often producing undesirable results.
- ``export_vertex_skin_weights`` (bool):  [Read-Write] If enabled, export vertex bone weights and indices in skeletal meshes. Necessary for animation sequences.
- ``include_copyright_notice`` (bool):  [Read-Write] If enabled, the copyright notice from project settings will be included as metadata in the glTF asset.
- ``make_skinned_meshes_root`` (bool):  [Read-Write] If enabled, make skeletal meshes into root nodes to strictly comply with the glTF specification. Final bone transforms remain the same and visual results are unaffected.
- ``skip_near_default_values`` (bool):  [Read-Write] If enabled, floating-point-based JSON properties that are nearly equal to their default value will not be exported and thus regarded as exactly default, reducing JSON size.
- ``texture_image_format`` (GLTFTextureImageFormat):  [Read-Write] Desired image format used for exported textures.
- ``texture_image_quality`` (int32):  [Read-Write] Level of compression used for textures exported with lossy image formats, 0 (default) or value between 1 (worst quality, best compression) and 100 (best quality, worst compression).
- ``use_importer_material_mapping`` (bool):  [Read-Write] If enabled, materials imported with the Interchange-glTF importer will be directly mapped for the Exporter. bExport material options below will be ignored.
- ``use_mesh_quantization`` (bool):  [Read-Write] If enabled, use quantization for vertex tangents and normals, reducing size. Requires extension KHR_mesh_quantization, which may result in the mesh not loading in some glTF viewers.

<a id="unreal.GLTFExportOptions.export_uniform_scale"></a>

#### export_uniform_scale

```python
@property
def export_uniform_scale() -> float
```

(float):  [Read-Write] Scale factor used for exporting all assets (0.01 by default) for conversion from centimeters (Unreal default) to meters (glTF).

<a id="unreal.GLTFExportOptions.export_uniform_scale"></a>

#### export_uniform_scale

```python
@export_uniform_scale.setter
def export_uniform_scale(value: float) -> None
```

<a id="unreal.GLTFExportOptions.export_preview_mesh"></a>

#### export_preview_mesh

```python
@property
def export_preview_mesh() -> bool
```

(bool):  [Read-Write] If enabled, the preview mesh for a standalone animation or material asset will also be exported.

<a id="unreal.GLTFExportOptions.export_preview_mesh"></a>

#### export_preview_mesh

```python
@export_preview_mesh.setter
def export_preview_mesh(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.skip_near_default_values"></a>

#### skip_near_default_values

```python
@property
def skip_near_default_values() -> bool
```

(bool):  [Read-Write] If enabled, floating-point-based JSON properties that are nearly equal to their default value will not be exported and thus regarded as exactly default, reducing JSON size.

<a id="unreal.GLTFExportOptions.skip_near_default_values"></a>

#### skip_near_default_values

```python
@skip_near_default_values.setter
def skip_near_default_values(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.include_copyright_notice"></a>

#### include_copyright_notice

```python
@property
def include_copyright_notice() -> bool
```

(bool):  [Read-Write] If enabled, the copyright notice from project settings will be included as metadata in the glTF asset.

<a id="unreal.GLTFExportOptions.include_copyright_notice"></a>

#### include_copyright_notice

```python
@include_copyright_notice.setter
def include_copyright_notice(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.export_proxy_materials"></a>

#### export_proxy_materials

```python
@property
def export_proxy_materials() -> bool
```

(bool):  [Read-Write] If enabled, materials that have a proxy defined in their user data, will be exported using that proxy instead. This setting won't affect proxy materials exported or referenced directly.

<a id="unreal.GLTFExportOptions.export_proxy_materials"></a>

#### export_proxy_materials

```python
@export_proxy_materials.setter
def export_proxy_materials(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.use_importer_material_mapping"></a>

#### use_importer_material_mapping

```python
@property
def use_importer_material_mapping() -> bool
```

(bool):  [Read-Write] If enabled, materials imported with the Interchange-glTF importer will be directly mapped for the Exporter. bExport material options below will be ignored.

<a id="unreal.GLTFExportOptions.use_importer_material_mapping"></a>

#### use_importer_material_mapping

```python
@use_importer_material_mapping.setter
def use_importer_material_mapping(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.export_unlit_materials"></a>

#### export_unlit_materials

```python
@property
def export_unlit_materials() -> bool
```

(bool):  [Read-Write] If enabled, materials with shading model unlit will be properly exported. Uses extension KHR_materials_unlit.

<a id="unreal.GLTFExportOptions.export_unlit_materials"></a>

#### export_unlit_materials

```python
@export_unlit_materials.setter
def export_unlit_materials(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.export_clear_coat_materials"></a>

#### export_clear_coat_materials

```python
@property
def export_clear_coat_materials() -> bool
```

(bool):  [Read-Write] If enabled, materials with shading model clear coat will be properly exported. Uses extension KHR_materials_clearcoat.

<a id="unreal.GLTFExportOptions.export_clear_coat_materials"></a>

#### export_clear_coat_materials

```python
@export_clear_coat_materials.setter
def export_clear_coat_materials(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.export_cloth_materials"></a>

#### export_cloth_materials

```python
@property
def export_cloth_materials() -> bool
```

(bool):  [Read-Write] If enabled, materials with shading model cloth will be properly exported. Uses extension KHR_materials_sheen.

<a id="unreal.GLTFExportOptions.export_cloth_materials"></a>

#### export_cloth_materials

```python
@export_cloth_materials.setter
def export_cloth_materials(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.export_thin_translucent_materials"></a>

#### export_thin_translucent_materials

```python
@property
def export_thin_translucent_materials() -> bool
```

(bool):  [Read-Write] If enabled, materials with shading model thin translucency will be exported. Export is only partial. Uses extension KHR_materials_transmission.

<a id="unreal.GLTFExportOptions.export_thin_translucent_materials"></a>

#### export_thin_translucent_materials

```python
@export_thin_translucent_materials.setter
def export_thin_translucent_materials(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.export_specular_glossiness_materials"></a>

#### export_specular_glossiness_materials

```python
@property
def export_specular_glossiness_materials() -> bool
```

(bool):  [Read-Write] If enabled, materials using the Importer's SpecularGlossiness material function will be exported. Uses extension KHR_materials_pbrSpecularGlossiness.

<a id="unreal.GLTFExportOptions.export_specular_glossiness_materials"></a>

#### export_specular_glossiness_materials

```python
@export_specular_glossiness_materials.setter
def export_specular_glossiness_materials(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.export_emissive_strength"></a>

#### export_emissive_strength

```python
@property
def export_emissive_strength() -> bool
```

(bool):  [Read-Write] If enabled, allows materials to have an emissive factor that exceeds the standard range [0.0, 1.0]. Uses extension KHR_materials_emissive_strength.

<a id="unreal.GLTFExportOptions.export_emissive_strength"></a>

#### export_emissive_strength

```python
@export_emissive_strength.setter
def export_emissive_strength(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.bake_material_inputs"></a>

#### bake_material_inputs

```python
@property
def bake_material_inputs() -> GLTFMaterialBakeMode
```

(GLTFMaterialBakeMode):  [Read-Write] Bake mode determining if and how a material input is baked out to a texture. Baking is only used for non-trivial material inputs (i.e. not simple texture or constant expressions).

<a id="unreal.GLTFExportOptions.bake_material_inputs"></a>

#### bake_material_inputs

```python
@bake_material_inputs.setter
def bake_material_inputs(value: GLTFMaterialBakeMode) -> None
```

<a id="unreal.GLTFExportOptions.default_material_bake_size"></a>

#### default_material_bake_size

```python
@property
def default_material_bake_size() -> GLTFMaterialBakeSize
```

(GLTFMaterialBakeSize):  [Read-Write] Default size of the baked out texture (containing the material input). Can be overridden by material- and input-specific bake settings, see GLTFMaterialExportOptions.

<a id="unreal.GLTFExportOptions.default_material_bake_size"></a>

#### default_material_bake_size

```python
@default_material_bake_size.setter
def default_material_bake_size(value: GLTFMaterialBakeSize) -> None
```

<a id="unreal.GLTFExportOptions.default_material_bake_filter"></a>

#### default_material_bake_filter

```python
@property
def default_material_bake_filter() -> TextureFilter
```

(TextureFilter):  [Read-Write] Default filtering mode used when sampling the baked out texture. Can be overridden by material- and input-specific bake settings, see GLTFMaterialExportOptions.

<a id="unreal.GLTFExportOptions.default_material_bake_filter"></a>

#### default_material_bake_filter

```python
@default_material_bake_filter.setter
def default_material_bake_filter(value: TextureFilter) -> None
```

<a id="unreal.GLTFExportOptions.default_material_bake_tiling"></a>

#### default_material_bake_tiling

```python
@property
def default_material_bake_tiling() -> TextureAddress
```

(TextureAddress):  [Read-Write] Default addressing mode used when sampling the baked out texture. Can be overridden by material- and input-specific bake settings, see GLTFMaterialExportOptions.

<a id="unreal.GLTFExportOptions.default_material_bake_tiling"></a>

#### default_material_bake_tiling

```python
@default_material_bake_tiling.setter
def default_material_bake_tiling(value: TextureAddress) -> None
```

<a id="unreal.GLTFExportOptions.default_input_bake_settings"></a>

#### default_input_bake_settings

```python
@property
def default_input_bake_settings(
) -> Map[GLTFMaterialPropertyGroup, GLTFOverrideMaterialBakeSettings]
```

(Map[GLTFMaterialPropertyGroup, GLTFOverrideMaterialBakeSettings]):  [Read-Write] Input-specific default bake settings that override the general defaults above.

<a id="unreal.GLTFExportOptions.default_input_bake_settings"></a>

#### default_input_bake_settings

```python
@default_input_bake_settings.setter
def default_input_bake_settings(
    value: Map[GLTFMaterialPropertyGroup, GLTFOverrideMaterialBakeSettings]
) -> None
```

<a id="unreal.GLTFExportOptions.default_level_of_detail"></a>

#### default_level_of_detail

```python
@property
def default_level_of_detail() -> int
```

(int32):  [Read-Write] Default LOD level used for exporting a mesh. Can be overridden by component or asset settings (e.g. minimum or forced LOD level).

<a id="unreal.GLTFExportOptions.default_level_of_detail"></a>

#### default_level_of_detail

```python
@default_level_of_detail.setter
def default_level_of_detail(value: int) -> None
```

<a id="unreal.GLTFExportOptions.export_source_model"></a>

#### export_source_model

```python
@property
def export_source_model() -> bool
```

(bool):  [Read-Write] If enabled, exports the SourceModel. If false, exports the Render Data.

<a id="unreal.GLTFExportOptions.export_source_model"></a>

#### export_source_model

```python
@export_source_model.setter
def export_source_model(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.export_vertex_colors"></a>

#### export_vertex_colors

```python
@property
def export_vertex_colors() -> bool
```

(bool):  [Read-Write] If enabled, export vertex color. Not recommended due to vertex colors always being used as a base color multiplier in glTF, regardless of material. Often producing undesirable results.

<a id="unreal.GLTFExportOptions.export_vertex_colors"></a>

#### export_vertex_colors

```python
@export_vertex_colors.setter
def export_vertex_colors(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.export_vertex_skin_weights"></a>

#### export_vertex_skin_weights

```python
@property
def export_vertex_skin_weights() -> bool
```

(bool):  [Read-Write] If enabled, export vertex bone weights and indices in skeletal meshes. Necessary for animation sequences.

<a id="unreal.GLTFExportOptions.export_vertex_skin_weights"></a>

#### export_vertex_skin_weights

```python
@export_vertex_skin_weights.setter
def export_vertex_skin_weights(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.make_skinned_meshes_root"></a>

#### make_skinned_meshes_root

```python
@property
def make_skinned_meshes_root() -> bool
```

(bool):  [Read-Write] If enabled, make skeletal meshes into root nodes to strictly comply with the glTF specification. Final bone transforms remain the same and visual results are unaffected.

<a id="unreal.GLTFExportOptions.make_skinned_meshes_root"></a>

#### make_skinned_meshes_root

```python
@make_skinned_meshes_root.setter
def make_skinned_meshes_root(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.use_mesh_quantization"></a>

#### use_mesh_quantization

```python
@property
def use_mesh_quantization() -> bool
```

(bool):  [Read-Write] If enabled, use quantization for vertex tangents and normals, reducing size. Requires extension KHR_mesh_quantization, which may result in the mesh not loading in some glTF viewers.

<a id="unreal.GLTFExportOptions.use_mesh_quantization"></a>

#### use_mesh_quantization

```python
@use_mesh_quantization.setter
def use_mesh_quantization(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.export_level_sequences"></a>

#### export_level_sequences

```python
@property
def export_level_sequences() -> bool
```

(bool):  [Read-Write] If enabled, export level sequences. Only transform tracks are currently supported. The level sequence will be played at the assigned display rate.

<a id="unreal.GLTFExportOptions.export_level_sequences"></a>

#### export_level_sequences

```python
@export_level_sequences.setter
def export_level_sequences(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.export_animation_sequences"></a>

#### export_animation_sequences

```python
@property
def export_animation_sequences() -> bool
```

(bool):  [Read-Write] If enabled, export single animation asset used by a skeletal mesh component. Export of vertex skin weights must be enabled.

<a id="unreal.GLTFExportOptions.export_animation_sequences"></a>

#### export_animation_sequences

```python
@export_animation_sequences.setter
def export_animation_sequences(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.texture_image_format"></a>

#### texture_image_format

```python
@property
def texture_image_format() -> GLTFTextureImageFormat
```

(GLTFTextureImageFormat):  [Read-Write] Desired image format used for exported textures.

<a id="unreal.GLTFExportOptions.texture_image_format"></a>

#### texture_image_format

```python
@texture_image_format.setter
def texture_image_format(value: GLTFTextureImageFormat) -> None
```

<a id="unreal.GLTFExportOptions.texture_image_quality"></a>

#### texture_image_quality

```python
@property
def texture_image_quality() -> int
```

(int32):  [Read-Write] Level of compression used for textures exported with lossy image formats, 0 (default) or value between 1 (worst quality, best compression) and 100 (best quality, worst compression).

<a id="unreal.GLTFExportOptions.texture_image_quality"></a>

#### texture_image_quality

```python
@texture_image_quality.setter
def texture_image_quality(value: int) -> None
```

<a id="unreal.GLTFExportOptions.export_texture_transforms"></a>

#### export_texture_transforms

```python
@property
def export_texture_transforms() -> bool
```

(bool):  [Read-Write] If enabled, export UV offset and scale/tiling used in materials. Uses extension KHR_texture_transform.

<a id="unreal.GLTFExportOptions.export_texture_transforms"></a>

#### export_texture_transforms

```python
@export_texture_transforms.setter
def export_texture_transforms(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.adjust_normalmaps"></a>

#### adjust_normalmaps

```python
@property
def adjust_normalmaps() -> bool
```

(bool):  [Read-Write] If enabled, exported normalmaps will be adjusted from Unreal to glTF convention (i.e. the green channel is flipped).

<a id="unreal.GLTFExportOptions.adjust_normalmaps"></a>

#### adjust_normalmaps

```python
@adjust_normalmaps.setter
def adjust_normalmaps(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.export_hidden_in_game"></a>

#### export_hidden_in_game

```python
@property
def export_hidden_in_game() -> bool
```

(bool):  [Read-Write] If enabled, export actors and components that are flagged as hidden in-game.

<a id="unreal.GLTFExportOptions.export_hidden_in_game"></a>

#### export_hidden_in_game

```python
@export_hidden_in_game.setter
def export_hidden_in_game(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.export_lights"></a>

#### export_lights

```python
@property
def export_lights() -> bool
```

(bool):  [Read-Write] If enabled, export directional, point, and spot light components. Uses extension KHR_lights_punctual.

<a id="unreal.GLTFExportOptions.export_lights"></a>

#### export_lights

```python
@export_lights.setter
def export_lights(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.export_cameras"></a>

#### export_cameras

```python
@property
def export_cameras() -> bool
```

(bool):  [Read-Write] If enabled, export camera components.

<a id="unreal.GLTFExportOptions.export_cameras"></a>

#### export_cameras

```python
@export_cameras.setter
def export_cameras(value: bool) -> None
```

<a id="unreal.GLTFExportOptions.export_material_variants"></a>

#### export_material_variants

```python
@property
def export_material_variants() -> GLTFMaterialVariantMode
```

(GLTFMaterialVariantMode):  [Read-Write] Mode determining if and how to export material variants that change the materials property on a static or skeletal mesh component.

<a id="unreal.GLTFExportOptions.export_material_variants"></a>

#### export_material_variants

```python
@export_material_variants.setter
def export_material_variants(value: GLTFMaterialVariantMode) -> None
```

<a id="unreal.GLTFExportOptions.reset_to_default"></a>

#### reset_to_default

```python
def reset_to_default() -> None
```

x.reset_to_default() -> None
Reset to Default

<a id="unreal.GLTFExporter"></a>