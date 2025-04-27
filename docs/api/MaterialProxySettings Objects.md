## MaterialProxySettings Objects

```python
class MaterialProxySettings(StructBase)
```

Material Proxy Settings

**C++ Source:**

- **Module**: Engine
- **File**: MaterialMerging.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_two_sided_material`` (bool):  [Read-Write] Whether or not to allow the generated material can be two-sided
- ``ambient_occlusion_constant`` (float):  [Read-Write] Constant value to use for the Ambient Occlusion property
- ``ambient_occlusion_map`` (bool):  [Read-Write] Whether to generate a texture for the Ambient Occlusion property
- ``ambient_occlusion_texture_size`` (IntPoint):  [Read-Write] Override Ambient Occlusion texture size
- ``anisotropy_constant`` (float):  [Read-Write] Constant value to use for the Anisotropy property
- ``anisotropy_map`` (bool):  [Read-Write] Whether to generate a texture for the Anisotropy property
- ``anisotropy_texture_size`` (IntPoint):  [Read-Write] Override Anisotropy texture size
- ``blend_mode`` (BlendMode):  [Read-Write] Target blend mode for the generated material
- ``diffuse_texture_size`` (IntPoint):  [Read-Write] Override Diffuse texture size
- ``emissive_map`` (bool):  [Read-Write] Whether to generate a texture for the Emissive property
- ``emissive_texture_size`` (IntPoint):  [Read-Write] Override Emissive texture size
- ``gutter_space`` (float):  [Read-Write] Gutter space to take into account
- ``mesh_max_screen_size_percent`` (float):  [Read-Write] Expected maximum screen size for the mesh
- ``mesh_min_draw_distance`` (double):  [Read-Write] Expected minimum distance at which the mesh will be rendered
- ``metallic_constant`` (float):  [Read-Write] Constant value to use for the Metallic property
- ``metallic_map`` (bool):  [Read-Write] Whether to generate a texture for the Metallic property
- ``metallic_texture_size`` (IntPoint):  [Read-Write] Override Metallic texture size
- ``normal_map`` (bool):  [Read-Write] Whether to generate a texture for the Normal property
- ``normal_texture_size`` (IntPoint):  [Read-Write] Override Normal texture size
- ``opacity_constant`` (float):  [Read-Write] Constant value to use for the Opacity property
- ``opacity_map`` (bool):  [Read-Write] Whether to generate a texture for the Opacity property
- ``opacity_mask_constant`` (float):  [Read-Write] Constant value to use for the Opacity mask property
- ``opacity_mask_map`` (bool):  [Read-Write] Whether to generate a texture for the Opacity Mask property
- ``opacity_mask_texture_size`` (IntPoint):  [Read-Write] Override Opacity Mask texture size
- ``opacity_texture_size`` (IntPoint):  [Read-Write] Override Opacity texture size
- ``roughness_constant`` (float):  [Read-Write] Constant value to use for the Roughness property
- ``roughness_map`` (bool):  [Read-Write] Whether to generate a texture for the Roughness property
- ``roughness_texture_size`` (IntPoint):  [Read-Write] Override Roughness texture size
- ``specular_constant`` (float):  [Read-Write] Constant value to use for the Specular property
- ``specular_map`` (bool):  [Read-Write] Whether to generate a texture for the Specular property
- ``specular_texture_size`` (IntPoint):  [Read-Write] Override Specular texture size
- ``tangent_map`` (bool):  [Read-Write] Whether to generate a texture for the Tangent property
- ``tangent_texture_size`` (IntPoint):  [Read-Write] Override Tangent texture size
- ``target_texel_density_per_meter`` (float):  [Read-Write] Target texel density
- ``texture_size`` (IntPoint):  [Read-Write] Size of generated BaseColor map
- ``texture_sizing_type`` (TextureSizingType):  [Read-Write] Method that should be used to generate the sizes of the output textures

<a id="unreal.MaterialProxySettings.__init__"></a>

#### __init__

```python
def __init__(texture_sizing_type: TextureSizingType = TextureSizingType.
             TEXTURE_SIZING_TYPE_USE_SINGLE_TEXTURE_SIZE,
             target_texel_density_per_meter: float = 0.000000,
             mesh_max_screen_size_percent: float = 0.000000,
             mesh_min_draw_distance: float = 0.000000,
             gutter_space: float = 0.000000,
             metallic_constant: float = 0.000000,
             roughness_constant: float = 0.000000,
             anisotropy_constant: float = 0.000000,
             specular_constant: float = 0.000000,
             opacity_constant: float = 0.000000,
             opacity_mask_constant: float = 0.000000,
             ambient_occlusion_constant: float = 0.000000,
             blend_mode: BlendMode = BlendMode.BLEND_OPAQUE,
             allow_two_sided_material: bool = False,
             normal_map: bool = False,
             tangent_map: bool = False,
             metallic_map: bool = False,
             roughness_map: bool = False,
             anisotropy_map: bool = False,
             specular_map: bool = False,
             emissive_map: bool = False,
             opacity_map: bool = False,
             opacity_mask_map: bool = False,
             ambient_occlusion_map: bool = False,
             diffuse_texture_size: IntPoint = [0, 0],
             normal_texture_size: IntPoint = [0, 0],
             tangent_texture_size: IntPoint = [0, 0],
             metallic_texture_size: IntPoint = [0, 0],
             roughness_texture_size: IntPoint = [0, 0],
             anisotropy_texture_size: IntPoint = [0, 0],
             specular_texture_size: IntPoint = [0, 0],
             emissive_texture_size: IntPoint = [0, 0],
             opacity_texture_size: IntPoint = [0, 0],
             opacity_mask_texture_size: IntPoint = [0, 0],
             ambient_occlusion_texture_size: IntPoint = [0, 0]) -> None
```

<a id="unreal.MaterialProxySettings.texture_sizing_type"></a>

#### texture_sizing_type

```python
@property
def texture_sizing_type() -> TextureSizingType
```

(TextureSizingType):  [Read-Write] Method that should be used to generate the sizes of the output textures

<a id="unreal.MaterialProxySettings.texture_sizing_type"></a>

#### texture_sizing_type

```python
@texture_sizing_type.setter
def texture_sizing_type(value: TextureSizingType) -> None
```

<a id="unreal.MaterialProxySettings.target_texel_density_per_meter"></a>

#### target_texel_density_per_meter

```python
@property
def target_texel_density_per_meter() -> float
```

(float):  [Read-Write] Target texel density

<a id="unreal.MaterialProxySettings.target_texel_density_per_meter"></a>

#### target_texel_density_per_meter

```python
@target_texel_density_per_meter.setter
def target_texel_density_per_meter(value: float) -> None
```

<a id="unreal.MaterialProxySettings.mesh_max_screen_size_percent"></a>

#### mesh_max_screen_size_percent

```python
@property
def mesh_max_screen_size_percent() -> float
```

(float):  [Read-Write] Expected maximum screen size for the mesh

<a id="unreal.MaterialProxySettings.mesh_max_screen_size_percent"></a>

#### mesh_max_screen_size_percent

```python
@mesh_max_screen_size_percent.setter
def mesh_max_screen_size_percent(value: float) -> None
```

<a id="unreal.MaterialProxySettings.mesh_min_draw_distance"></a>

#### mesh_min_draw_distance

```python
@property
def mesh_min_draw_distance() -> float
```

(double):  [Read-Write] Expected minimum distance at which the mesh will be rendered

<a id="unreal.MaterialProxySettings.mesh_min_draw_distance"></a>

#### mesh_min_draw_distance

```python
@mesh_min_draw_distance.setter
def mesh_min_draw_distance(value: float) -> None
```

<a id="unreal.MaterialProxySettings.gutter_space"></a>

#### gutter_space

```python
@property
def gutter_space() -> float
```

(float):  [Read-Write] Gutter space to take into account

<a id="unreal.MaterialProxySettings.gutter_space"></a>

#### gutter_space

```python
@gutter_space.setter
def gutter_space(value: float) -> None
```

<a id="unreal.MaterialProxySettings.metallic_constant"></a>

#### metallic_constant

```python
@property
def metallic_constant() -> float
```

(float):  [Read-Write] Constant value to use for the Metallic property

<a id="unreal.MaterialProxySettings.metallic_constant"></a>

#### metallic_constant

```python
@metallic_constant.setter
def metallic_constant(value: float) -> None
```

<a id="unreal.MaterialProxySettings.roughness_constant"></a>

#### roughness_constant

```python
@property
def roughness_constant() -> float
```

(float):  [Read-Write] Constant value to use for the Roughness property

<a id="unreal.MaterialProxySettings.roughness_constant"></a>

#### roughness_constant

```python
@roughness_constant.setter
def roughness_constant(value: float) -> None
```

<a id="unreal.MaterialProxySettings.anisotropy_constant"></a>

#### anisotropy_constant

```python
@property
def anisotropy_constant() -> float
```

(float):  [Read-Write] Constant value to use for the Anisotropy property

<a id="unreal.MaterialProxySettings.anisotropy_constant"></a>

#### anisotropy_constant

```python
@anisotropy_constant.setter
def anisotropy_constant(value: float) -> None
```

<a id="unreal.MaterialProxySettings.specular_constant"></a>

#### specular_constant

```python
@property
def specular_constant() -> float
```

(float):  [Read-Write] Constant value to use for the Specular property

<a id="unreal.MaterialProxySettings.specular_constant"></a>

#### specular_constant

```python
@specular_constant.setter
def specular_constant(value: float) -> None
```

<a id="unreal.MaterialProxySettings.opacity_constant"></a>

#### opacity_constant

```python
@property
def opacity_constant() -> float
```

(float):  [Read-Write] Constant value to use for the Opacity property

<a id="unreal.MaterialProxySettings.opacity_constant"></a>

#### opacity_constant

```python
@opacity_constant.setter
def opacity_constant(value: float) -> None
```

<a id="unreal.MaterialProxySettings.opacity_mask_constant"></a>

#### opacity_mask_constant

```python
@property
def opacity_mask_constant() -> float
```

(float):  [Read-Write] Constant value to use for the Opacity mask property

<a id="unreal.MaterialProxySettings.opacity_mask_constant"></a>

#### opacity_mask_constant

```python
@opacity_mask_constant.setter
def opacity_mask_constant(value: float) -> None
```

<a id="unreal.MaterialProxySettings.ambient_occlusion_constant"></a>

#### ambient_occlusion_constant

```python
@property
def ambient_occlusion_constant() -> float
```

(float):  [Read-Write] Constant value to use for the Ambient Occlusion property

<a id="unreal.MaterialProxySettings.ambient_occlusion_constant"></a>

#### ambient_occlusion_constant

```python
@ambient_occlusion_constant.setter
def ambient_occlusion_constant(value: float) -> None
```

<a id="unreal.MaterialProxySettings.blend_mode"></a>

#### blend_mode

```python
@property
def blend_mode() -> BlendMode
```

(BlendMode):  [Read-Write] Target blend mode for the generated material

<a id="unreal.MaterialProxySettings.blend_mode"></a>

#### blend_mode

```python
@blend_mode.setter
def blend_mode(value: BlendMode) -> None
```

<a id="unreal.MaterialProxySettings.allow_two_sided_material"></a>

#### allow_two_sided_material

```python
@property
def allow_two_sided_material() -> bool
```

(bool):  [Read-Write] Whether or not to allow the generated material can be two-sided

<a id="unreal.MaterialProxySettings.allow_two_sided_material"></a>

#### allow_two_sided_material

```python
@allow_two_sided_material.setter
def allow_two_sided_material(value: bool) -> None
```

<a id="unreal.MaterialProxySettings.normal_map"></a>

#### normal_map

```python
@property
def normal_map() -> bool
```

(bool):  [Read-Write] Whether to generate a texture for the Normal property

<a id="unreal.MaterialProxySettings.normal_map"></a>

#### normal_map

```python
@normal_map.setter
def normal_map(value: bool) -> None
```

<a id="unreal.MaterialProxySettings.tangent_map"></a>

#### tangent_map

```python
@property
def tangent_map() -> bool
```

(bool):  [Read-Write] Whether to generate a texture for the Tangent property

<a id="unreal.MaterialProxySettings.tangent_map"></a>

#### tangent_map

```python
@tangent_map.setter
def tangent_map(value: bool) -> None
```

<a id="unreal.MaterialProxySettings.metallic_map"></a>

#### metallic_map

```python
@property
def metallic_map() -> bool
```

(bool):  [Read-Write] Whether to generate a texture for the Metallic property

<a id="unreal.MaterialProxySettings.metallic_map"></a>

#### metallic_map

```python
@metallic_map.setter
def metallic_map(value: bool) -> None
```

<a id="unreal.MaterialProxySettings.roughness_map"></a>

#### roughness_map

```python
@property
def roughness_map() -> bool
```

(bool):  [Read-Write] Whether to generate a texture for the Roughness property

<a id="unreal.MaterialProxySettings.roughness_map"></a>

#### roughness_map

```python
@roughness_map.setter
def roughness_map(value: bool) -> None
```

<a id="unreal.MaterialProxySettings.anisotropy_map"></a>

#### anisotropy_map

```python
@property
def anisotropy_map() -> bool
```

(bool):  [Read-Write] Whether to generate a texture for the Anisotropy property

<a id="unreal.MaterialProxySettings.anisotropy_map"></a>

#### anisotropy_map

```python
@anisotropy_map.setter
def anisotropy_map(value: bool) -> None
```

<a id="unreal.MaterialProxySettings.specular_map"></a>

#### specular_map

```python
@property
def specular_map() -> bool
```

(bool):  [Read-Write] Whether to generate a texture for the Specular property

<a id="unreal.MaterialProxySettings.specular_map"></a>

#### specular_map

```python
@specular_map.setter
def specular_map(value: bool) -> None
```

<a id="unreal.MaterialProxySettings.emissive_map"></a>

#### emissive_map

```python
@property
def emissive_map() -> bool
```

(bool):  [Read-Write] Whether to generate a texture for the Emissive property

<a id="unreal.MaterialProxySettings.emissive_map"></a>

#### emissive_map

```python
@emissive_map.setter
def emissive_map(value: bool) -> None
```

<a id="unreal.MaterialProxySettings.opacity_map"></a>

#### opacity_map

```python
@property
def opacity_map() -> bool
```

(bool):  [Read-Write] Whether to generate a texture for the Opacity property

<a id="unreal.MaterialProxySettings.opacity_map"></a>

#### opacity_map

```python
@opacity_map.setter
def opacity_map(value: bool) -> None
```

<a id="unreal.MaterialProxySettings.opacity_mask_map"></a>

#### opacity_mask_map

```python
@property
def opacity_mask_map() -> bool
```

(bool):  [Read-Write] Whether to generate a texture for the Opacity Mask property

<a id="unreal.MaterialProxySettings.opacity_mask_map"></a>

#### opacity_mask_map

```python
@opacity_mask_map.setter
def opacity_mask_map(value: bool) -> None
```

<a id="unreal.MaterialProxySettings.ambient_occlusion_map"></a>

#### ambient_occlusion_map

```python
@property
def ambient_occlusion_map() -> bool
```

(bool):  [Read-Write] Whether to generate a texture for the Ambient Occlusion property

<a id="unreal.MaterialProxySettings.ambient_occlusion_map"></a>

#### ambient_occlusion_map

```python
@ambient_occlusion_map.setter
def ambient_occlusion_map(value: bool) -> None
```

<a id="unreal.MaterialProxySettings.diffuse_texture_size"></a>

#### diffuse_texture_size

```python
@property
def diffuse_texture_size() -> IntPoint
```

(IntPoint):  [Read-Write] Override Diffuse texture size

<a id="unreal.MaterialProxySettings.diffuse_texture_size"></a>

#### diffuse_texture_size

```python
@diffuse_texture_size.setter
def diffuse_texture_size(value: IntPoint) -> None
```

<a id="unreal.MaterialProxySettings.normal_texture_size"></a>

#### normal_texture_size

```python
@property
def normal_texture_size() -> IntPoint
```

(IntPoint):  [Read-Write] Override Normal texture size

<a id="unreal.MaterialProxySettings.normal_texture_size"></a>

#### normal_texture_size

```python
@normal_texture_size.setter
def normal_texture_size(value: IntPoint) -> None
```

<a id="unreal.MaterialProxySettings.tangent_texture_size"></a>

#### tangent_texture_size

```python
@property
def tangent_texture_size() -> IntPoint
```

(IntPoint):  [Read-Write] Override Tangent texture size

<a id="unreal.MaterialProxySettings.tangent_texture_size"></a>

#### tangent_texture_size

```python
@tangent_texture_size.setter
def tangent_texture_size(value: IntPoint) -> None
```

<a id="unreal.MaterialProxySettings.metallic_texture_size"></a>

#### metallic_texture_size

```python
@property
def metallic_texture_size() -> IntPoint
```

(IntPoint):  [Read-Write] Override Metallic texture size

<a id="unreal.MaterialProxySettings.metallic_texture_size"></a>

#### metallic_texture_size

```python
@metallic_texture_size.setter
def metallic_texture_size(value: IntPoint) -> None
```

<a id="unreal.MaterialProxySettings.roughness_texture_size"></a>

#### roughness_texture_size

```python
@property
def roughness_texture_size() -> IntPoint
```

(IntPoint):  [Read-Write] Override Roughness texture size

<a id="unreal.MaterialProxySettings.roughness_texture_size"></a>

#### roughness_texture_size

```python
@roughness_texture_size.setter
def roughness_texture_size(value: IntPoint) -> None
```

<a id="unreal.MaterialProxySettings.anisotropy_texture_size"></a>

#### anisotropy_texture_size

```python
@property
def anisotropy_texture_size() -> IntPoint
```

(IntPoint):  [Read-Write] Override Anisotropy texture size

<a id="unreal.MaterialProxySettings.anisotropy_texture_size"></a>

#### anisotropy_texture_size

```python
@anisotropy_texture_size.setter
def anisotropy_texture_size(value: IntPoint) -> None
```

<a id="unreal.MaterialProxySettings.specular_texture_size"></a>

#### specular_texture_size

```python
@property
def specular_texture_size() -> IntPoint
```

(IntPoint):  [Read-Write] Override Specular texture size

<a id="unreal.MaterialProxySettings.specular_texture_size"></a>

#### specular_texture_size

```python
@specular_texture_size.setter
def specular_texture_size(value: IntPoint) -> None
```

<a id="unreal.MaterialProxySettings.emissive_texture_size"></a>

#### emissive_texture_size

```python
@property
def emissive_texture_size() -> IntPoint
```

(IntPoint):  [Read-Write] Override Emissive texture size

<a id="unreal.MaterialProxySettings.emissive_texture_size"></a>

#### emissive_texture_size

```python
@emissive_texture_size.setter
def emissive_texture_size(value: IntPoint) -> None
```

<a id="unreal.MaterialProxySettings.opacity_texture_size"></a>

#### opacity_texture_size

```python
@property
def opacity_texture_size() -> IntPoint
```

(IntPoint):  [Read-Write] Override Opacity texture size

<a id="unreal.MaterialProxySettings.opacity_texture_size"></a>

#### opacity_texture_size

```python
@opacity_texture_size.setter
def opacity_texture_size(value: IntPoint) -> None
```

<a id="unreal.MaterialProxySettings.opacity_mask_texture_size"></a>

#### opacity_mask_texture_size

```python
@property
def opacity_mask_texture_size() -> IntPoint
```

(IntPoint):  [Read-Write] Override Opacity Mask texture size

<a id="unreal.MaterialProxySettings.opacity_mask_texture_size"></a>

#### opacity_mask_texture_size

```python
@opacity_mask_texture_size.setter
def opacity_mask_texture_size(value: IntPoint) -> None
```

<a id="unreal.MaterialProxySettings.ambient_occlusion_texture_size"></a>

#### ambient_occlusion_texture_size

```python
@property
def ambient_occlusion_texture_size() -> IntPoint
```

(IntPoint):  [Read-Write] Override Ambient Occlusion texture size

<a id="unreal.MaterialProxySettings.ambient_occlusion_texture_size"></a>

#### ambient_occlusion_texture_size

```python
@ambient_occlusion_texture_size.setter
def ambient_occlusion_texture_size(value: IntPoint) -> None
```

<a id="unreal.MeshMergingSettings"></a>