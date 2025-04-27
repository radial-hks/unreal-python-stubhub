## InterchangeGenericAnimationPipeline Objects

```python
class InterchangeGenericAnimationPipeline(InterchangePipelineBase)
```

Interchange Generic Animation Pipeline

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangePipelines
- **File**: InterchangeGenericAnimationPipeline.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``add_curve_metadata_to_skeleton`` (bool):  [Read-Write] Determines whether to automatically add curve metadata to an animation's skeleton. If this setting is disabled, curve metadata will be added to skeletal meshes for morph targets, but no metadata entry will be created for general curves.
- ``animation_range`` (InterchangeAnimationRange):  [Read-Write] Determines which animation range to import: the range defined at export, the range of frames with animation, or a manually defined range.
- ``custom_bone_animation_sample_rate`` (int32):  [Read-Write] Sample fbx animation data at the specified sample rate, 0 find automaticaly the best sample rate
- ``delete_existing_custom_attribute_curves`` (bool):  [Read-Write] If enabled, all previous node attributes imported as Animation Curves will be deleted when doing a reimport.
- ``delete_existing_morph_target_curves`` (bool):  [Read-Write] If enabled, all previous morph target curves will be deleted when doing a reimport.
- ``delete_existing_non_curve_custom_attributes`` (bool):  [Read-Write] If enabled, all previous node attributes imported as Animation Attributes will be deleted when doing a reimport.
- ``do_not_import_curve_with_zero`` (bool):  [Read-Write] When importing a custom attribute or morph target as a curve, only import if it has a value other than zero. This avoids adding extra curves to evaluate.
- ``frame_import_range`` (Int32Interval):  [Read-Write] The frame range used when the Animation Length setting is set to Set Range.
- ``import_animations`` (bool):  [Read-Write] If enabled, import all animation assets found in the source.
- ``import_bone_tracks`` (bool):  [Read-Write] Import bone transform tracks. If false, this will discard any bone transform tracks.
- ``import_custom_attribute`` (bool):  [Read-Write] If enabled, import node attributes as either Animation Curves or Animation Attributes.
- ``material_curve_suffixes`` (Array[str]):  [Read-Write] Set the Material Curve Type for custom attributes that have the specified suffixes. This setting is not used if the Set Material Curve Type setting is enabled.
- ``remove_curve_redundant_keys`` (bool):  [Read-Write] When importing custom attributes as curves, remove redundant keys.
- ``set_material_drive_parameter_on_custom_attribute`` (bool):  [Read-Write] Set the material curve type for all custom attributes.
- ``snap_to_closest_frame_boundary`` (bool):  [Read-Write] If enabled, snaps the animation to the closest frame boundary using the import sampling rate.
- ``use30_hz_to_bake_bone_animation`` (bool):  [Read-Write] If enabled, samples all animation curves to 30 FPS

<a id="unreal.InterchangeGenericAnimationPipeline.import_animations"></a>

#### import_animations

```python
@property
def import_animations() -> bool
```

(bool):  [Read-Write] If enabled, import all animation assets found in the source.

<a id="unreal.InterchangeGenericAnimationPipeline.import_animations"></a>

#### import_animations

```python
@import_animations.setter
def import_animations(value: bool) -> None
```

<a id="unreal.InterchangeGenericAnimationPipeline.import_bone_tracks"></a>

#### import_bone_tracks

```python
@property
def import_bone_tracks() -> bool
```

(bool):  [Read-Write] Import bone transform tracks. If false, this will discard any bone transform tracks.

<a id="unreal.InterchangeGenericAnimationPipeline.import_bone_tracks"></a>

#### import_bone_tracks

```python
@import_bone_tracks.setter
def import_bone_tracks(value: bool) -> None
```

<a id="unreal.InterchangeGenericAnimationPipeline.animation_range"></a>

#### animation_range

```python
@property
def animation_range() -> InterchangeAnimationRange
```

(InterchangeAnimationRange):  [Read-Write] Determines which animation range to import: the range defined at export, the range of frames with animation, or a manually defined range.

<a id="unreal.InterchangeGenericAnimationPipeline.animation_range"></a>

#### animation_range

```python
@animation_range.setter
def animation_range(value: InterchangeAnimationRange) -> None
```

<a id="unreal.InterchangeGenericAnimationPipeline.frame_import_range"></a>

#### frame_import_range

```python
@property
def frame_import_range() -> Int32Interval
```

(Int32Interval):  [Read-Write] The frame range used when the Animation Length setting is set to Set Range.

<a id="unreal.InterchangeGenericAnimationPipeline.frame_import_range"></a>

#### frame_import_range

```python
@frame_import_range.setter
def frame_import_range(value: Int32Interval) -> None
```

<a id="unreal.InterchangeGenericAnimationPipeline.use30_hz_to_bake_bone_animation"></a>

#### use30_hz_to_bake_bone_animation

```python
@property
def use30_hz_to_bake_bone_animation() -> bool
```

(bool):  [Read-Write] If enabled, samples all animation curves to 30 FPS

<a id="unreal.InterchangeGenericAnimationPipeline.use30_hz_to_bake_bone_animation"></a>

#### use30_hz_to_bake_bone_animation

```python
@use30_hz_to_bake_bone_animation.setter
def use30_hz_to_bake_bone_animation(value: bool) -> None
```

<a id="unreal.InterchangeGenericAnimationPipeline.custom_bone_animation_sample_rate"></a>

#### custom_bone_animation_sample_rate

```python
@property
def custom_bone_animation_sample_rate() -> int
```

(int32):  [Read-Write] Sample fbx animation data at the specified sample rate, 0 find automaticaly the best sample rate

<a id="unreal.InterchangeGenericAnimationPipeline.custom_bone_animation_sample_rate"></a>

#### custom_bone_animation_sample_rate

```python
@custom_bone_animation_sample_rate.setter
def custom_bone_animation_sample_rate(value: int) -> None
```

<a id="unreal.InterchangeGenericAnimationPipeline.snap_to_closest_frame_boundary"></a>

#### snap_to_closest_frame_boundary

```python
@property
def snap_to_closest_frame_boundary() -> bool
```

(bool):  [Read-Write] If enabled, snaps the animation to the closest frame boundary using the import sampling rate.

<a id="unreal.InterchangeGenericAnimationPipeline.snap_to_closest_frame_boundary"></a>

#### snap_to_closest_frame_boundary

```python
@snap_to_closest_frame_boundary.setter
def snap_to_closest_frame_boundary(value: bool) -> None
```

<a id="unreal.InterchangeGenericAnimationPipeline.import_custom_attribute"></a>

#### import_custom_attribute

```python
@property
def import_custom_attribute() -> bool
```

(bool):  [Read-Write] If enabled, import node attributes as either Animation Curves or Animation Attributes.

<a id="unreal.InterchangeGenericAnimationPipeline.import_custom_attribute"></a>

#### import_custom_attribute

```python
@import_custom_attribute.setter
def import_custom_attribute(value: bool) -> None
```

<a id="unreal.InterchangeGenericAnimationPipeline.add_curve_metadata_to_skeleton"></a>

#### add_curve_metadata_to_skeleton

```python
@property
def add_curve_metadata_to_skeleton() -> bool
```

(bool):  [Read-Write] Determines whether to automatically add curve metadata to an animation's skeleton. If this setting is disabled, curve metadata will be added to skeletal meshes for morph targets, but no metadata entry will be created for general curves.

<a id="unreal.InterchangeGenericAnimationPipeline.add_curve_metadata_to_skeleton"></a>

#### add_curve_metadata_to_skeleton

```python
@add_curve_metadata_to_skeleton.setter
def add_curve_metadata_to_skeleton(value: bool) -> None
```

<a id="unreal.InterchangeGenericAnimationPipeline.set_material_drive_parameter_on_custom_attribute"></a>

#### set_material_drive_parameter_on_custom_attribute

```python
@property
def set_material_drive_parameter_on_custom_attribute() -> bool
```

(bool):  [Read-Write] Set the material curve type for all custom attributes.

<a id="unreal.InterchangeGenericAnimationPipeline.set_material_drive_parameter_on_custom_attribute"></a>

#### set_material_drive_parameter_on_custom_attribute

```python
@set_material_drive_parameter_on_custom_attribute.setter
def set_material_drive_parameter_on_custom_attribute(value: bool) -> None
```

<a id="unreal.InterchangeGenericAnimationPipeline.material_curve_suffixes"></a>

#### material_curve_suffixes

```python
@property
def material_curve_suffixes() -> Array[str]
```

(Array[str]):  [Read-Write] Set the Material Curve Type for custom attributes that have the specified suffixes. This setting is not used if the Set Material Curve Type setting is enabled.

<a id="unreal.InterchangeGenericAnimationPipeline.material_curve_suffixes"></a>

#### material_curve_suffixes

```python
@material_curve_suffixes.setter
def material_curve_suffixes(value: Array[str]) -> None
```

<a id="unreal.InterchangeGenericAnimationPipeline.remove_curve_redundant_keys"></a>

#### remove_curve_redundant_keys

```python
@property
def remove_curve_redundant_keys() -> bool
```

(bool):  [Read-Write] When importing custom attributes as curves, remove redundant keys.

<a id="unreal.InterchangeGenericAnimationPipeline.remove_curve_redundant_keys"></a>

#### remove_curve_redundant_keys

```python
@remove_curve_redundant_keys.setter
def remove_curve_redundant_keys(value: bool) -> None
```

<a id="unreal.InterchangeGenericAnimationPipeline.do_not_import_curve_with_zero"></a>

#### do_not_import_curve_with_zero

```python
@property
def do_not_import_curve_with_zero() -> bool
```

(bool):  [Read-Write] When importing a custom attribute or morph target as a curve, only import if it has a value other than zero. This avoids adding extra curves to evaluate.

<a id="unreal.InterchangeGenericAnimationPipeline.do_not_import_curve_with_zero"></a>

#### do_not_import_curve_with_zero

```python
@do_not_import_curve_with_zero.setter
def do_not_import_curve_with_zero(value: bool) -> None
```

<a id="unreal.InterchangeGenericAnimationPipeline.delete_existing_non_curve_custom_attributes"></a>

#### delete_existing_non_curve_custom_attributes

```python
@property
def delete_existing_non_curve_custom_attributes() -> bool
```

(bool):  [Read-Write] If enabled, all previous node attributes imported as Animation Attributes will be deleted when doing a reimport.

<a id="unreal.InterchangeGenericAnimationPipeline.delete_existing_non_curve_custom_attributes"></a>

#### delete_existing_non_curve_custom_attributes

```python
@delete_existing_non_curve_custom_attributes.setter
def delete_existing_non_curve_custom_attributes(value: bool) -> None
```

<a id="unreal.InterchangeGenericAnimationPipeline.delete_existing_custom_attribute_curves"></a>

#### delete_existing_custom_attribute_curves

```python
@property
def delete_existing_custom_attribute_curves() -> bool
```

(bool):  [Read-Write] If enabled, all previous node attributes imported as Animation Curves will be deleted when doing a reimport.

<a id="unreal.InterchangeGenericAnimationPipeline.delete_existing_custom_attribute_curves"></a>

#### delete_existing_custom_attribute_curves

```python
@delete_existing_custom_attribute_curves.setter
def delete_existing_custom_attribute_curves(value: bool) -> None
```

<a id="unreal.InterchangeGenericAnimationPipeline.delete_existing_morph_target_curves"></a>

#### delete_existing_morph_target_curves

```python
@property
def delete_existing_morph_target_curves() -> bool
```

(bool):  [Read-Write] If enabled, all previous morph target curves will be deleted when doing a reimport.

<a id="unreal.InterchangeGenericAnimationPipeline.delete_existing_morph_target_curves"></a>

#### delete_existing_morph_target_curves

```python
@delete_existing_morph_target_curves.setter
def delete_existing_morph_target_curves(value: bool) -> None
```

<a id="unreal.InterchangeGenericAssetsPipeline"></a>