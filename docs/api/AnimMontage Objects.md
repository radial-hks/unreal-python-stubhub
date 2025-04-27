## AnimMontage Objects

```python
class AnimMontage(AnimCompositeBase)
```

Any property you're adding to AnimMontage and parent class has to be considered for Child Asset

Child Asset is considered to be only asset mapping feature using everything else in the class
For example, you can just use all parent's setting  for the montage, but only remap assets
This isn't magic bullet unfortunately and it is consistent effort of keeping the data synced with parent
If you add new property, please make sure those property has to be copied for children.
If it does, please add the copy in the function RefreshParentAssetData

**C++ Source:**

- **Module**: Engine
- **File**: AnimMontage.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_mapping_table`` (AssetMappingTable):  [Read-Only] Asset mapping table when ParentAsset is set
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``blend_in`` (AlphaBlend):  [Read-Write] Blend in option.
- ``blend_mode_in`` (MontageBlendMode):  [Read-Write]
- ``blend_mode_out`` (MontageBlendMode):  [Read-Write]
- ``blend_out`` (AlphaBlend):  [Read-Write] Blend out option. This is only used when it blends out itself. If it's interrupted by other montages, it will use new montage's BlendIn option to blend out.
- ``blend_out_trigger_time`` (float):  [Read-Write] Time from Sequence End to trigger blend out.
  <0 means using BlendOutTime, so BlendOut finishes as Montage ends.
  >=0 means using 'SequenceEnd - BlendOutTriggerTime' to trigger blend out.
- ``blend_profile_in`` (BlendProfile):  [Read-Write] The blend profile to use.
- ``blend_profile_out`` (BlendProfile):  [Read-Write] The blend profile to use.
- ``common_target_frame_rate`` (FrameRate):  [Read-Only] Frame-rate used to represent this Animation Montage (best fitting for placed Animation Sequences)
- ``controller`` (AnimationDataController):  [Read-Only] UAnimDataController instance set to operate on DataModel
- ``data_model`` (AnimDataModel):  [Read-Only]
- ``data_model_interface`` (AnimationDataModel):  [Read-Only] IAnimationDataModel instance containing (source) animation data
- ``enable_auto_blend_out`` (bool):  [Read-Write] When it hits end, it automatically blends out. If this is false, it won't blend out but keep the last pose until stopped explicitly
- ``loop`` (bool):  [Read-Write] The default looping behavior of this animation.
  Asset players can override this
- ``meta_data`` (Array[AnimMetaData]):  [Read-Write] Meta data that can be saved with the asset

  You can query by GetMetaData function
- ``parent_asset`` (AnimationAsset):  [Read-Only] Parent Asset, if set, you won't be able to edit any data in here but just mapping table

  During cooking, this data will be used to bake out to normal asset
- ``preview_base_pose`` (AnimSequence):  [Read-Write] Preview Base pose for additive BlendSpace *
- ``preview_pose_asset`` (PoseAsset):  [Read-Write] The default skeletal mesh to use when previewing this asset - this only applies when you open Persona using this asset//
  todo:: note that this doesn't retarget right now
- ``rate_scale`` (float):  [Read-Write] Number for tweaking playback rate of this animation globally.
- ``sequence_length`` (float):  [Read-Only]
- ``skeleton`` (Skeleton):  [Read-Only] Pointer to the Skeleton this asset can be played on .
- ``sync_group`` (Name):  [Read-Write] If you're using marker based sync for this montage, make sure to add sync group name. For now we only support one group
- ``sync_slot_index`` (int32):  [Read-Write] Index of the slot track used for collecting sync markers
- ``thumbnail_info`` (ThumbnailInfo):  [Read-Only] Information for thumbnail rendering
- ``time_stretch_curve`` (TimeStretchCurve):  [Read-Write] Time stretch curve will only be used when the montage has a non-default play rate
- ``time_stretch_curve_name`` (Name):  [Read-Write] Name of optional TimeStretchCurveName to look for in Montage. Time stretch curve will only be used when the montage has a non-default play rate

<a id="unreal.AnimMontage.blend_mode_in"></a>

#### blend_mode_in

```python
@property
def blend_mode_in() -> MontageBlendMode
```

(MontageBlendMode):  [Read-Only]

<a id="unreal.AnimMontage.blend_mode_out"></a>

#### blend_mode_out

```python
@property
def blend_mode_out() -> MontageBlendMode
```

(MontageBlendMode):  [Read-Only]

<a id="unreal.AnimMontage.blend_profile_in"></a>

#### blend_profile_in

```python
@property
def blend_profile_in() -> BlendProfile
```

(BlendProfile):  [Read-Only] The blend profile to use.

<a id="unreal.AnimMontage.blend_profile_out"></a>

#### blend_profile_out

```python
@property
def blend_profile_out() -> BlendProfile
```

(BlendProfile):  [Read-Only] The blend profile to use.

<a id="unreal.AnimMontage.is_valid_section_name"></a>

#### is_valid_section_name

```python
def is_valid_section_name(section_name: Name) -> bool
```

x.is_valid_section_name(section_name) -> bool


Args:
    section_name (Name): 

Returns:
    bool: true if valid section

<a id="unreal.AnimMontage.is_valid_additive_slot"></a>

#### is_valid_additive_slot

```python
def is_valid_additive_slot(slot_node_name: Name) -> bool
```

x.is_valid_additive_slot(slot_node_name) -> bool
Check if this slot has a valid additive animation for the specified slot.
The slot name should not include the group name.
i.e. for "DefaultGroup.DefaultSlot", the slot name is "DefaultSlot".

Args:
    slot_node_name (Name): 

Returns:
    bool:

<a id="unreal.AnimMontage.is_dynamic_montage"></a>

#### is_dynamic_montage

```python
def is_dynamic_montage() -> bool
```

x.is_dynamic_montage() -> bool
Is Dynamic Montage

Returns:
    bool:

<a id="unreal.AnimMontage.get_section_name"></a>

#### get_section_name

```python
def get_section_name(section_index: int) -> Name
```

x.get_section_name(section_index) -> Name
Get SectionName from SectionIndex. Returns NAME_None if not found

Args:
    section_index (int32): 

Returns:
    Name:

<a id="unreal.AnimMontage.get_section_index"></a>

#### get_section_index

```python
def get_section_index(section_name: Name) -> int
```

x.get_section_index(section_name) -> int32
Get SectionIndex from SectionName. Returns INDEX_None if not found

Args:
    section_name (Name): 

Returns:
    int32:

<a id="unreal.AnimMontage.get_num_sections"></a>

#### get_num_sections

```python
def get_num_sections() -> int
```

x.get_num_sections() -> int32
Returns the number of sections this montage has

Returns:
    int32:

<a id="unreal.AnimMontage.get_group_name"></a>

#### get_group_name

```python
def get_group_name() -> Name
```

x.get_group_name() -> Name
Get the Montage's Group Name. This is the group from the first slot.

Returns:
    Name:

<a id="unreal.AnimMontage.get_first_anim_reference"></a>

#### get_first_anim_reference

```python
def get_first_anim_reference() -> AnimSequenceBase
```

x.get_first_anim_reference() -> AnimSequenceBase
Get First Anim Reference

Returns:
    AnimSequenceBase:

<a id="unreal.AnimMontage.get_default_blend_out_time"></a>

#### get_default_blend_out_time

```python
def get_default_blend_out_time() -> float
```

x.get_default_blend_out_time() -> float
Get Default Blend Out Time

Returns:
    float:

<a id="unreal.AnimMontage.get_default_blend_in_time"></a>

#### get_default_blend_in_time

```python
def get_default_blend_in_time() -> float
```

x.get_default_blend_in_time() -> float
Get Default Blend in Time

Returns:
    float:

<a id="unreal.AnimMontage.get_blend_out_args"></a>

#### get_blend_out_args

```python
def get_blend_out_args() -> AlphaBlendArgs
```

x.get_blend_out_args() -> AlphaBlendArgs
Get Blend Out Args

Returns:
    AlphaBlendArgs:

<a id="unreal.AnimMontage.get_blend_in_args"></a>

#### get_blend_in_args

```python
def get_blend_in_args() -> AlphaBlendArgs
```

x.get_blend_in_args() -> AlphaBlendArgs
Get Blend in Args

Returns:
    AlphaBlendArgs:

<a id="unreal.AnimMontage.create_slot_animation_as_dynamic_montage_with_blend_settings"></a>

#### create_slot_animation_as_dynamic_montage_with_blend_settings

```python
@classmethod
def create_slot_animation_as_dynamic_montage_with_blend_settings(
        cls,
        asset: AnimSequenceBase,
        slot_node_name: Name,
        blend_in_settings: MontageBlendSettings,
        blend_out_settings: MontageBlendSettings,
        play_rate: float = 1.000000,
        loop_count: int = 1,
        blend_out_trigger_time: float = -1.000000) -> AnimMontage
```

X.create_slot_animation_as_dynamic_montage_with_blend_settings(asset, slot_node_name, blend_in_settings, blend_out_settings, play_rate=1.000000, loop_count=1, blend_out_trigger_time=-1.000000) -> AnimMontage
Utility function to create dynamic montage from AnimSequence with blend in settings

Args:
    asset (AnimSequenceBase): 
    slot_node_name (Name): 
    blend_in_settings (MontageBlendSettings): 
    blend_out_settings (MontageBlendSettings): 
    play_rate (float): 
    loop_count (int32): 
    blend_out_trigger_time (float): 

Returns:
    AnimMontage:

<a id="unreal.UAnimNotifyLibrary"></a>