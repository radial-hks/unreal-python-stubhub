## DMMaterialChannelListPreset Objects

```python
class DMMaterialChannelListPreset(StructBase)
```

DMMaterial Channel List Preset

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DynamicMaterialEditorSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ambient_occlusion`` (bool):  [Read-Write]
- ``anisotropy`` (bool):  [Read-Write]
- ``base_color`` (bool):  [Read-Write]
- ``default_animated`` (bool):  [Read-Write]
- ``default_blend_mode`` (BlendMode):  [Read-Write]
- ``default_shading_model`` (DMMaterialShadingModel):  [Read-Write]
- ``default_two_sided`` (bool):  [Read-Write]
- ``displacement`` (bool):  [Read-Write]
- ``emissive`` (bool):  [Read-Write]
- ``metallic`` (bool):  [Read-Write]
- ``name`` (Name):  [Read-Write]
- ``normal`` (bool):  [Read-Write]
- ``opacity`` (bool):  [Read-Write]
- ``pixel_depth_offset`` (bool):  [Read-Write]
- ``refraction`` (bool):  [Read-Write]
- ``roughness`` (bool):  [Read-Write]
- ``specular`` (bool):  [Read-Write]
- ``subsurface_color`` (bool):  [Read-Write]
- ``surface_thickness`` (bool):  [Read-Write]
- ``tangent`` (bool):  [Read-Write]
- ``world_position_offset`` (bool):  [Read-Write]

<a id="unreal.DMMaterialChannelListPreset.__init__"></a>

#### __init__

```python
def __init__(
        name: Name = "None",
        base_color: bool = False,
        emissive: bool = False,
        opacity: bool = False,
        roughness: bool = False,
        specular: bool = False,
        metallic: bool = False,
        normal: bool = False,
        pixel_depth_offset: bool = False,
        world_position_offset: bool = False,
        ambient_occlusion: bool = False,
        anisotropy: bool = False,
        refraction: bool = False,
        tangent: bool = False,
        displacement: bool = False,
        subsurface_color: bool = False,
        surface_thickness: bool = False,
        default_blend_mode: BlendMode = BlendMode.BLEND_OPAQUE,
        default_shading_model: DMMaterialShadingModel = DMMaterialShadingModel.
    UNLIT,
        default_animated: bool = False,
        default_two_sided: bool = False) -> None
```

<a id="unreal.DMMaterialChannelListPreset.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.DMMaterialChannelListPreset.base_color"></a>

#### base_color

```python
@property
def base_color() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DMMaterialChannelListPreset.emissive"></a>

#### emissive

```python
@property
def emissive() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DMMaterialChannelListPreset.opacity"></a>

#### opacity

```python
@property
def opacity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMMaterialChannelListPreset.opacity"></a>

#### opacity

```python
@opacity.setter
def opacity(value: bool) -> None
```

<a id="unreal.DMMaterialChannelListPreset.roughness"></a>

#### roughness

```python
@property
def roughness() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMMaterialChannelListPreset.roughness"></a>

#### roughness

```python
@roughness.setter
def roughness(value: bool) -> None
```

<a id="unreal.DMMaterialChannelListPreset.specular"></a>

#### specular

```python
@property
def specular() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMMaterialChannelListPreset.specular"></a>

#### specular

```python
@specular.setter
def specular(value: bool) -> None
```

<a id="unreal.DMMaterialChannelListPreset.metallic"></a>

#### metallic

```python
@property
def metallic() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMMaterialChannelListPreset.metallic"></a>

#### metallic

```python
@metallic.setter
def metallic(value: bool) -> None
```

<a id="unreal.DMMaterialChannelListPreset.normal"></a>

#### normal

```python
@property
def normal() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMMaterialChannelListPreset.normal"></a>

#### normal

```python
@normal.setter
def normal(value: bool) -> None
```

<a id="unreal.DMMaterialChannelListPreset.pixel_depth_offset"></a>

#### pixel_depth_offset

```python
@property
def pixel_depth_offset() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMMaterialChannelListPreset.pixel_depth_offset"></a>

#### pixel_depth_offset

```python
@pixel_depth_offset.setter
def pixel_depth_offset(value: bool) -> None
```

<a id="unreal.DMMaterialChannelListPreset.world_position_offset"></a>

#### world_position_offset

```python
@property
def world_position_offset() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMMaterialChannelListPreset.world_position_offset"></a>

#### world_position_offset

```python
@world_position_offset.setter
def world_position_offset(value: bool) -> None
```

<a id="unreal.DMMaterialChannelListPreset.ambient_occlusion"></a>

#### ambient_occlusion

```python
@property
def ambient_occlusion() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMMaterialChannelListPreset.ambient_occlusion"></a>

#### ambient_occlusion

```python
@ambient_occlusion.setter
def ambient_occlusion(value: bool) -> None
```

<a id="unreal.DMMaterialChannelListPreset.anisotropy"></a>

#### anisotropy

```python
@property
def anisotropy() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMMaterialChannelListPreset.anisotropy"></a>

#### anisotropy

```python
@anisotropy.setter
def anisotropy(value: bool) -> None
```

<a id="unreal.DMMaterialChannelListPreset.refraction"></a>

#### refraction

```python
@property
def refraction() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMMaterialChannelListPreset.refraction"></a>

#### refraction

```python
@refraction.setter
def refraction(value: bool) -> None
```

<a id="unreal.DMMaterialChannelListPreset.tangent"></a>

#### tangent

```python
@property
def tangent() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMMaterialChannelListPreset.tangent"></a>

#### tangent

```python
@tangent.setter
def tangent(value: bool) -> None
```

<a id="unreal.DMMaterialChannelListPreset.displacement"></a>

#### displacement

```python
@property
def displacement() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMMaterialChannelListPreset.displacement"></a>

#### displacement

```python
@displacement.setter
def displacement(value: bool) -> None
```

<a id="unreal.DMMaterialChannelListPreset.subsurface_color"></a>

#### subsurface_color

```python
@property
def subsurface_color() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMMaterialChannelListPreset.subsurface_color"></a>

#### subsurface_color

```python
@subsurface_color.setter
def subsurface_color(value: bool) -> None
```

<a id="unreal.DMMaterialChannelListPreset.surface_thickness"></a>

#### surface_thickness

```python
@property
def surface_thickness() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMMaterialChannelListPreset.surface_thickness"></a>

#### surface_thickness

```python
@surface_thickness.setter
def surface_thickness(value: bool) -> None
```

<a id="unreal.DMMaterialChannelListPreset.default_blend_mode"></a>

#### default_blend_mode

```python
@property
def default_blend_mode() -> BlendMode
```

(BlendMode):  [Read-Write]

<a id="unreal.DMMaterialChannelListPreset.default_blend_mode"></a>

#### default_blend_mode

```python
@default_blend_mode.setter
def default_blend_mode(value: BlendMode) -> None
```

<a id="unreal.DMMaterialChannelListPreset.default_shading_model"></a>

#### default_shading_model

```python
@property
def default_shading_model() -> DMMaterialShadingModel
```

(DMMaterialShadingModel):  [Read-Write]

<a id="unreal.DMMaterialChannelListPreset.default_shading_model"></a>

#### default_shading_model

```python
@default_shading_model.setter
def default_shading_model(value: DMMaterialShadingModel) -> None
```

<a id="unreal.DMMaterialChannelListPreset.default_animated"></a>

#### default_animated

```python
@property
def default_animated() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMMaterialChannelListPreset.default_animated"></a>

#### default_animated

```python
@default_animated.setter
def default_animated(value: bool) -> None
```

<a id="unreal.DMMaterialChannelListPreset.default_two_sided"></a>

#### default_two_sided

```python
@property
def default_two_sided() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMMaterialChannelListPreset.default_two_sided"></a>

#### default_two_sided

```python
@default_two_sided.setter
def default_two_sided(value: bool) -> None
```

<a id="unreal.AvaShapeRoundedCornerSettings"></a>