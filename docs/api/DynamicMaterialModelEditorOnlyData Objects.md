## DynamicMaterialModelEditorOnlyData Objects

```python
class DynamicMaterialModelEditorOnlyData(Object)
```

Dynamic Material Model Editor Only Data

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DynamicMaterialModelEditorOnlyData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ambient_occlusion`` (DMMaterialProperty):  [Read-Write]
- ``anisotropy`` (DMMaterialProperty):  [Read-Write]
- ``base_color`` (DMMaterialProperty):  [Read-Write]
- ``blend_mode`` (BlendMode):  [Read-Write]
- ``create_material_package`` (bool):  [Read-Only]
- ``custom1`` (DMMaterialProperty):  [Read-Write]
- ``custom2`` (DMMaterialProperty):  [Read-Write]
- ``custom3`` (DMMaterialProperty):  [Read-Write]
- ``custom4`` (DMMaterialProperty):  [Read-Write]
- ``displacement`` (DMMaterialProperty):  [Read-Write]
- ``domain`` (MaterialDomain):  [Read-Write]
- ``emissive_color`` (DMMaterialProperty):  [Read-Write]
- ``expressions`` (Array[MaterialExpression]):  [Read-Only]
- ``has_pixel_animation`` (bool):  [Read-Write] Whether the opaque material has any pixel animations happening, that isn't included in the geometric velocities.
  This allows to disable renderer's heuristics that assumes animation is fully described with motion vector, such as TSR's anti-flickering heuristic.
- ``material_model`` (DynamicMaterialModel):  [Read-Only]
- ``material_stats`` (MaterialStatistics):  [Read-Only]
- ``metallic`` (DMMaterialProperty):  [Read-Write]
- ``nanite_tessellation_enabled`` (bool):  [Read-Write] Whether tessellation is enabled on the material. NOTE: Required for displacement to work.
- ``normal`` (DMMaterialProperty):  [Read-Write]
- ``opacity`` (DMMaterialProperty):  [Read-Write]
- ``opacity_mask`` (DMMaterialProperty):  [Read-Write]
- ``output_translucent_velocity_enabled`` (bool):  [Read-Write] When true, translucent materials will output motion vectors and write to depth buffer in velocity pass.
- ``pixel_depth_offset`` (DMMaterialProperty):  [Read-Write]
- ``property_slot_map`` (Map[DMMaterialPropertyType, DMMaterialSlot]):  [Read-Only]
- ``refraction`` (DMMaterialProperty):  [Read-Write]
- ``responsive_aa_enabled`` (bool):  [Read-Write] Indicates that the material should be rendered using responsive anti-aliasing. Improves sharpness of small moving particles such as sparks.
  Only use for small moving features because it will cause aliasing of the background.
- ``roughness`` (DMMaterialProperty):  [Read-Write]
- ``shading_model`` (DMMaterialShadingModel):  [Read-Write]
- ``slots`` (Array[DMMaterialSlot]):  [Read-Only]
- ``specular`` (DMMaterialProperty):  [Read-Write]
- ``state`` (DMState):  [Read-Only]
- ``subsurface_color`` (DMMaterialProperty):  [Read-Write]
- ``surface_thickness`` (DMMaterialProperty):  [Read-Write]
- ``tangent`` (DMMaterialProperty):  [Read-Write]
- ``two_sided`` (bool):  [Read-Write] Indicates that the material should be rendered without backface culling and the normal should be flipped for backfaces.
- ``world_position_offset`` (DMMaterialProperty):  [Read-Write]

<a id="unreal.DynamicMaterialModelEditorOnlyData.material_model"></a>

#### material_model

```python
@property
def material_model() -> DynamicMaterialModel
```

(DynamicMaterialModel):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.state"></a>

#### state

```python
@property
def state() -> DMState
```

(DMState):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.domain"></a>

#### domain

```python
@property
def domain() -> MaterialDomain
```

(MaterialDomain):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.blend_mode"></a>

#### blend_mode

```python
@property
def blend_mode() -> BlendMode
```

(BlendMode):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.shading_model"></a>

#### shading_model

```python
@property
def shading_model() -> DMMaterialShadingModel
```

(DMMaterialShadingModel):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.has_pixel_animation"></a>

#### has_pixel_animation

```python
@property
def has_pixel_animation() -> bool
```

(bool):  [Read-Only] Whether the opaque material has any pixel animations happening, that isn't included in the geometric velocities.
This allows to disable renderer's heuristics that assumes animation is fully described with motion vector, such as TSR's anti-flickering heuristic.

<a id="unreal.DynamicMaterialModelEditorOnlyData.b_pixel_animation_flag"></a>

#### b_pixel_animation_flag

```python
@property
def b_pixel_animation_flag() -> bool
```

deprecated: 'b_pixel_animation_flag' was renamed to 'has_pixel_animation'.

<a id="unreal.DynamicMaterialModelEditorOnlyData.two_sided"></a>

#### two_sided

```python
@property
def two_sided() -> bool
```

(bool):  [Read-Only] Indicates that the material should be rendered without backface culling and the normal should be flipped for backfaces.

<a id="unreal.DynamicMaterialModelEditorOnlyData.b_two_sided_flag"></a>

#### b_two_sided_flag

```python
@property
def b_two_sided_flag() -> bool
```

deprecated: 'b_two_sided_flag' was renamed to 'two_sided'.

<a id="unreal.DynamicMaterialModelEditorOnlyData.output_translucent_velocity_enabled"></a>

#### output_translucent_velocity_enabled

```python
@property
def output_translucent_velocity_enabled() -> bool
```

(bool):  [Read-Only] When true, translucent materials will output motion vectors and write to depth buffer in velocity pass.

<a id="unreal.DynamicMaterialModelEditorOnlyData.nanite_tessellation_enabled"></a>

#### nanite_tessellation_enabled

```python
@property
def nanite_tessellation_enabled() -> bool
```

(bool):  [Read-Only] Whether tessellation is enabled on the material. NOTE: Required for displacement to work.

<a id="unreal.DynamicMaterialModelEditorOnlyData.responsive_aa_enabled"></a>

#### responsive_aa_enabled

```python
@property
def responsive_aa_enabled() -> bool
```

(bool):  [Read-Only] Indicates that the material should be rendered using responsive anti-aliasing. Improves sharpness of small moving particles such as sparks.
Only use for small moving features because it will cause aliasing of the background.

<a id="unreal.DynamicMaterialModelEditorOnlyData.property_slot_map"></a>

#### property_slot_map

```python
@property
def property_slot_map() -> Map[DMMaterialPropertyType, DMMaterialSlot]
```

(Map[DMMaterialPropertyType, DMMaterialSlot]):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.slots"></a>

#### slots

```python
@property
def slots() -> Array[DMMaterialSlot]
```

(Array[DMMaterialSlot]):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.expressions"></a>

#### expressions

```python
@property
def expressions() -> Array[MaterialExpression]
```

(Array[MaterialExpression]):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.create_material_package"></a>

#### create_material_package

```python
@property
def create_material_package() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.material_stats"></a>

#### material_stats

```python
@property
def material_stats() -> MaterialStatistics
```

(MaterialStatistics):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.base_color"></a>

#### base_color

```python
@property
def base_color() -> DMMaterialProperty
```

(DMMaterialProperty):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.emissive_color"></a>

#### emissive_color

```python
@property
def emissive_color() -> DMMaterialProperty
```

(DMMaterialProperty):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.opacity"></a>

#### opacity

```python
@property
def opacity() -> DMMaterialProperty
```

(DMMaterialProperty):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.opacity_mask"></a>

#### opacity_mask

```python
@property
def opacity_mask() -> DMMaterialProperty
```

(DMMaterialProperty):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.roughness"></a>

#### roughness

```python
@property
def roughness() -> DMMaterialProperty
```

(DMMaterialProperty):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.specular"></a>

#### specular

```python
@property
def specular() -> DMMaterialProperty
```

(DMMaterialProperty):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.metallic"></a>

#### metallic

```python
@property
def metallic() -> DMMaterialProperty
```

(DMMaterialProperty):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.normal"></a>

#### normal

```python
@property
def normal() -> DMMaterialProperty
```

(DMMaterialProperty):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.pixel_depth_offset"></a>

#### pixel_depth_offset

```python
@property
def pixel_depth_offset() -> DMMaterialProperty
```

(DMMaterialProperty):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.world_position_offset"></a>

#### world_position_offset

```python
@property
def world_position_offset() -> DMMaterialProperty
```

(DMMaterialProperty):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.ambient_occlusion"></a>

#### ambient_occlusion

```python
@property
def ambient_occlusion() -> DMMaterialProperty
```

(DMMaterialProperty):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.anisotropy"></a>

#### anisotropy

```python
@property
def anisotropy() -> DMMaterialProperty
```

(DMMaterialProperty):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.refraction"></a>

#### refraction

```python
@property
def refraction() -> DMMaterialProperty
```

(DMMaterialProperty):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.tangent"></a>

#### tangent

```python
@property
def tangent() -> DMMaterialProperty
```

(DMMaterialProperty):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.displacement"></a>

#### displacement

```python
@property
def displacement() -> DMMaterialProperty
```

(DMMaterialProperty):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.subsurface_color"></a>

#### subsurface_color

```python
@property
def subsurface_color() -> DMMaterialProperty
```

(DMMaterialProperty):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.surface_thickness"></a>

#### surface_thickness

```python
@property
def surface_thickness() -> DMMaterialProperty
```

(DMMaterialProperty):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.custom1"></a>

#### custom1

```python
@property
def custom1() -> DMMaterialProperty
```

(DMMaterialProperty):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.custom2"></a>

#### custom2

```python
@property
def custom2() -> DMMaterialProperty
```

(DMMaterialProperty):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.custom3"></a>

#### custom3

```python
@property
def custom3() -> DMMaterialProperty
```

(DMMaterialProperty):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.custom4"></a>

#### custom4

```python
@property
def custom4() -> DMMaterialProperty
```

(DMMaterialProperty):  [Read-Only]

<a id="unreal.DynamicMaterialModelEditorOnlyData.unassign_material_property"></a>

#### unassign_material_property

```python
def unassign_material_property(property_: DMMaterialPropertyType) -> None
```

x.unassign_material_property(property_) -> None
Unassign Material Property

Args:
    property_ (DMMaterialPropertyType):

<a id="unreal.DynamicMaterialModelEditorOnlyData.set_shading_model"></a>

#### set_shading_model

```python
def set_shading_model(shading_model: DMMaterialShadingModel) -> None
```

x.set_shading_model(shading_model) -> None
Set Shading Model

Args:
    shading_model (DMMaterialShadingModel):

<a id="unreal.DynamicMaterialModelEditorOnlyData.set_responsive_aa_enabled"></a>

#### set_responsive_aa_enabled

```python
def set_responsive_aa_enabled(enabled: bool) -> None
```

x.set_responsive_aa_enabled(enabled) -> None
Set Responsive AAEnabled

Args:
    enabled (bool):

<a id="unreal.DynamicMaterialModelEditorOnlyData.set_output_translucent_velocity_enabled"></a>

#### set_output_translucent_velocity_enabled

```python
def set_output_translucent_velocity_enabled(enabled: bool) -> None
```

x.set_output_translucent_velocity_enabled(enabled) -> None
Set Output Translucent Velocity Enabled

Args:
    enabled (bool):

<a id="unreal.DynamicMaterialModelEditorOnlyData.set_nanite_tessellation_enabled"></a>

#### set_nanite_tessellation_enabled

```python
def set_nanite_tessellation_enabled(enabled: bool) -> None
```

x.set_nanite_tessellation_enabled(enabled) -> None
Set Nanite Tessellation Enabled

Args:
    enabled (bool):

<a id="unreal.DynamicMaterialModelEditorOnlyData.set_is_two_sided"></a>

#### set_is_two_sided

```python
def set_is_two_sided(enabled: bool) -> None
```

x.set_is_two_sided(enabled) -> None
Set Is Two Sided

Args:
    enabled (bool):

<a id="unreal.DynamicMaterialModelEditorOnlyData.set_two_sided_flag"></a>

#### set_two_sided_flag

```python
def set_two_sided_flag(enabled: bool) -> None
```

deprecated: 'set_two_sided_flag' was renamed to 'set_is_two_sided'.

<a id="unreal.DynamicMaterialModelEditorOnlyData.set_has_pixel_animation"></a>

#### set_has_pixel_animation

```python
def set_has_pixel_animation(has_animation: bool) -> None
```

x.set_has_pixel_animation(has_animation) -> None
Set Has Pixel Animation

Args:
    has_animation (bool):

<a id="unreal.DynamicMaterialModelEditorOnlyData.set_pixel_animation_flag"></a>

#### set_pixel_animation_flag

```python
def set_pixel_animation_flag(has_animation: bool) -> None
```

deprecated: 'set_pixel_animation_flag' was renamed to 'set_has_pixel_animation'.

<a id="unreal.DynamicMaterialModelEditorOnlyData.set_domain"></a>

#### set_domain

```python
def set_domain(domain: MaterialDomain) -> None
```

x.set_domain(domain) -> None
Set Domain

Args:
    domain (MaterialDomain):

<a id="unreal.DynamicMaterialModelEditorOnlyData.set_channel_list_preset"></a>

#### set_channel_list_preset

```python
def set_channel_list_preset(preset_name: Name) -> None
```

x.set_channel_list_preset(preset_name) -> None
Set Channel List Preset

Args:
    preset_name (Name):

<a id="unreal.DynamicMaterialModelEditorOnlyData.set_blend_mode"></a>

#### set_blend_mode

```python
def set_blend_mode(blend_mode: BlendMode) -> None
```

x.set_blend_mode(blend_mode) -> None
Set Blend Mode

Args:
    blend_mode (BlendMode):

<a id="unreal.DynamicMaterialModelEditorOnlyData.remove_slot_for_material_property"></a>

#### remove_slot_for_material_property

```python
def remove_slot_for_material_property(
        type: DMMaterialPropertyType) -> DMMaterialSlot
```

x.remove_slot_for_material_property(type) -> DMMaterialSlot
Remove Slot for Material Property

Args:
    type (DMMaterialPropertyType): 

Returns:
    DMMaterialSlot:

<a id="unreal.DynamicMaterialModelEditorOnlyData.remove_slot"></a>

#### remove_slot

```python
def remove_slot(index: int) -> DMMaterialSlot
```

x.remove_slot(index) -> DMMaterialSlot
Removes the next slot by index. Highly recommended to use RemoveSlotForMaterialProperty(PropertyType).

Args:
    index (int32): 

Returns:
    DMMaterialSlot:

<a id="unreal.DynamicMaterialModelEditorOnlyData.open_material_editor"></a>

#### open_material_editor

```python
def open_material_editor() -> None
```

x.open_material_editor() -> None
Open Material Editor

<a id="unreal.DynamicMaterialModelEditorOnlyData.is_responsive_aa_enabled"></a>

#### is_responsive_aa_enabled

```python
def is_responsive_aa_enabled() -> bool
```

x.is_responsive_aa_enabled() -> bool
Is Responsive AAEnabled

Returns:
    bool:

<a id="unreal.DynamicMaterialModelEditorOnlyData.is_output_translucent_velocity_enabled"></a>

#### is_output_translucent_velocity_enabled

```python
def is_output_translucent_velocity_enabled() -> bool
```

x.is_output_translucent_velocity_enabled() -> bool
Is Output Translucent Velocity Enabled

Returns:
    bool:

<a id="unreal.DynamicMaterialModelEditorOnlyData.is_nanite_tessellation_enabled"></a>

#### is_nanite_tessellation_enabled

```python
def is_nanite_tessellation_enabled() -> bool
```

x.is_nanite_tessellation_enabled() -> bool
Is Nanite Tessellation Enabled

Returns:
    bool:

<a id="unreal.DynamicMaterialModelEditorOnlyData.get_state"></a>

#### get_state

```python
def get_state() -> DMState
```

x.get_state() -> DMState
Get State

Returns:
    DMState:

<a id="unreal.DynamicMaterialModelEditorOnlyData.get_slots"></a>

#### get_slots

```python
def get_slots() -> Array[DMMaterialSlot]
```

x.get_slots() -> Array[DMMaterialSlot]
Get Slots

Returns:
    Array[DMMaterialSlot]:

<a id="unreal.DynamicMaterialModelEditorOnlyData.get_slot_for_material_property"></a>

#### get_slot_for_material_property

```python
def get_slot_for_material_property(
        type: DMMaterialPropertyType) -> DMMaterialSlot
```

x.get_slot_for_material_property(type) -> DMMaterialSlot
Get Slot for Material Property

Args:
    type (DMMaterialPropertyType): 

Returns:
    DMMaterialSlot:

<a id="unreal.DynamicMaterialModelEditorOnlyData.get_slot_for_enabled_material_property"></a>

#### get_slot_for_enabled_material_property

```python
def get_slot_for_enabled_material_property(
        type: DMMaterialPropertyType) -> DMMaterialSlot
```

x.get_slot_for_enabled_material_property(type) -> DMMaterialSlot
Same as the above method, but will only return the slot if the material property is enabled.

Args:
    type (DMMaterialPropertyType): 

Returns:
    DMMaterialSlot:

<a id="unreal.DynamicMaterialModelEditorOnlyData.get_slot"></a>

#### get_slot

```python
def get_slot(index: int) -> DMMaterialSlot
```

x.get_slot(index) -> DMMaterialSlot
Gets slot by index. Highly recommended to use GetSlotForMaterialProperty(PropertyType).

Args:
    index (int32): 

Returns:
    DMMaterialSlot:

<a id="unreal.DynamicMaterialModelEditorOnlyData.get_shading_model"></a>

#### get_shading_model

```python
def get_shading_model() -> DMMaterialShadingModel
```

x.get_shading_model() -> DMMaterialShadingModel
Get Shading Model

Returns:
    DMMaterialShadingModel:

<a id="unreal.DynamicMaterialModelEditorOnlyData.get_material_stats"></a>

#### get_material_stats

```python
def get_material_stats() -> MaterialStatistics
```

x.get_material_stats() -> MaterialStatistics
Get Material Stats

Returns:
    MaterialStatistics:

<a id="unreal.DynamicMaterialModelEditorOnlyData.get_material_property"></a>

#### get_material_property

```python
def get_material_property(
        material_property: DMMaterialPropertyType) -> DMMaterialProperty
```

x.get_material_property(material_property) -> DMMaterialProperty
Get Material Property

Args:
    material_property (DMMaterialPropertyType): 

Returns:
    DMMaterialProperty:

<a id="unreal.DynamicMaterialModelEditorOnlyData.get_material_properties_for_slot"></a>

#### get_material_properties_for_slot

```python
def get_material_properties_for_slot(
        slot: DMMaterialSlot) -> Array[DMMaterialPropertyType]
```

x.get_material_properties_for_slot(slot) -> Array[DMMaterialPropertyType]
Get Material Properties for Slot

Args:
    slot (DMMaterialSlot): 

Returns:
    Array[DMMaterialPropertyType]:

<a id="unreal.DynamicMaterialModelEditorOnlyData.get_material_properties"></a>

#### get_material_properties

```python
def get_material_properties(
) -> Map[DMMaterialPropertyType, DMMaterialProperty]
```

x.get_material_properties() -> Map[DMMaterialPropertyType, DMMaterialProperty]
Get Material Properties

Returns:
    Map[DMMaterialPropertyType, DMMaterialProperty]:

<a id="unreal.DynamicMaterialModelEditorOnlyData.get_material_model"></a>

#### get_material_model

```python
def get_material_model() -> DynamicMaterialModel
```

x.get_material_model() -> DynamicMaterialModel
Get Material Model

Returns:
    DynamicMaterialModel:

<a id="unreal.DynamicMaterialModelEditorOnlyData.get_is_two_sided"></a>

#### get_is_two_sided

```python
def get_is_two_sided() -> bool
```

x.get_is_two_sided() -> bool
Get Is Two Sided

Returns:
    bool:

<a id="unreal.DynamicMaterialModelEditorOnlyData.is_two_sided_flag_set"></a>

#### is_two_sided_flag_set

```python
def is_two_sided_flag_set() -> bool
```

deprecated: 'is_two_sided_flag_set' was renamed to 'get_is_two_sided'.

<a id="unreal.DynamicMaterialModelEditorOnlyData.get_has_pixel_animation"></a>

#### get_has_pixel_animation

```python
def get_has_pixel_animation() -> bool
```

x.get_has_pixel_animation() -> bool
Get Has Pixel Animation

Returns:
    bool:

<a id="unreal.DynamicMaterialModelEditorOnlyData.is_pixel_animation_flag_set"></a>

#### is_pixel_animation_flag_set

```python
def is_pixel_animation_flag_set() -> bool
```

deprecated: 'is_pixel_animation_flag_set' was renamed to 'get_has_pixel_animation'.

<a id="unreal.DynamicMaterialModelEditorOnlyData.get_generated_material"></a>

#### get_generated_material

```python
def get_generated_material() -> Material
```

x.get_generated_material() -> Material
Get Generated Material

Returns:
    Material:

<a id="unreal.DynamicMaterialModelEditorOnlyData.get_domain"></a>

#### get_domain

```python
def get_domain() -> MaterialDomain
```

x.get_domain() -> MaterialDomain
Get Domain

Returns:
    MaterialDomain:

<a id="unreal.DynamicMaterialModelEditorOnlyData.get_blend_mode"></a>

#### get_blend_mode

```python
def get_blend_mode() -> BlendMode
```

x.get_blend_mode() -> BlendMode
Get Blend Mode

Returns:
    BlendMode:

<a id="unreal.DynamicMaterialModelEditorOnlyData.build_material"></a>

#### build_material

```python
def build_material(dirty_assets: bool) -> None
```

x.build_material(dirty_assets) -> None
Build Material

Args:
    dirty_assets (bool):

<a id="unreal.DynamicMaterialModelEditorOnlyData.assign_material_property_to_slot"></a>

#### assign_material_property_to_slot

```python
def assign_material_property_to_slot(property_: DMMaterialPropertyType,
                                     slot: DMMaterialSlot) -> None
```

x.assign_material_property_to_slot(property_, slot) -> None
Assign Material Property to Slot

Args:
    property_ (DMMaterialPropertyType): 
    slot (DMMaterialSlot):

<a id="unreal.DynamicMaterialModelEditorOnlyData.add_texture_set"></a>

#### add_texture_set

```python
def add_texture_set(texture_set: DMTextureSet, replace_slots: bool) -> bool
```

x.add_texture_set(texture_set, replace_slots) -> bool
Integrates a Texture Set with the model.

Args:
    texture_set (DMTextureSet): The set to integrate.
    replace_slots (bool): Whether to add to or completely replace slots.

Returns:
    bool: True on success.

<a id="unreal.DynamicMaterialModelEditorOnlyData.add_slot_for_material_property"></a>

#### add_slot_for_material_property

```python
def add_slot_for_material_property(
        type: DMMaterialPropertyType) -> DMMaterialSlot
```

x.add_slot_for_material_property(type) -> DMMaterialSlot
Add Slot for Material Property

Args:
    type (DMMaterialPropertyType): 

Returns:
    DMMaterialSlot:

<a id="unreal.DynamicMaterialModelEditorOnlyData.add_slot"></a>

#### add_slot

```python
def add_slot() -> DMMaterialSlot
```

x.add_slot() -> DMMaterialSlot
Adds the next available slot. Highly recommended to use AddSlotForMaterialProperty(PropertyType).

Returns:
    DMMaterialSlot:

<a id="unreal.DynamicMaterialModelEditorOnlyData.request_material_build"></a>

#### request_material_build

```python
def request_material_build(immediate: bool = False) -> None
```

x.request_material_build(immediate=False) -> None
Called when the model needs to have the material rebuild.

Args:
    immediate (bool):

<a id="unreal.DynamicMaterialModelEditorOnlyData.do_build"></a>

#### do_build

```python
def do_build(dirty_assets: bool) -> None
```

x.do_build(dirty_assets) -> None
Do Build

Args:
    dirty_assets (bool):

<a id="unreal.DynamicMaterialModelFactory"></a>