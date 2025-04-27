## AnimSequence Objects

```python
class AnimSequence(AnimSequenceBase)
```

Anim Sequence

**C++ Source:**

- **Module**: Engine
- **File**: AnimSequence.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additive_anim_type`` (AdditiveAnimationType):  [Read-Write] Additive animation type. *
- ``allow_frame_stripping`` (bool):  [Read-Write] Allow frame stripping to be performed on this animation if the platform requests it
  Can be disabled if animation has high frequency movements that are being lost.
- ``animation_track_names`` (Array[Name]):  [Read-Only]
- ``asset_import_data`` (AssetImportData):  [Read-Only] Importing data and options used for this mesh
- ``asset_mapping_table`` (AssetMappingTable):  [Read-Only] Asset mapping table when ParentAsset is set
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``bone_compression_settings`` (AnimBoneCompressionSettings):  [Read-Write] The bone compression settings used to compress bones in this sequence.
- ``compression_error_threshold_scale`` (float):  [Read-Write] Set a scale for error threshold on compression. This is useful if the animation will
  be played back at a different scale (e.g. if you know the animation will be played
  on an actor/component that is scaled up by a factor of 10, set this value to 10)
- ``controller`` (AnimationDataController):  [Read-Only] UAnimDataController instance set to operate on DataModel
- ``curve_compression_settings`` (AnimCurveCompressionSettings):  [Read-Write] The curve compression settings used to compress curves in this sequence.
- ``data_model`` (AnimDataModel):  [Read-Only]
- ``data_model_interface`` (AnimationDataModel):  [Read-Only] IAnimationDataModel instance containing (source) animation data
- ``do_not_override_compression`` (bool):  [Read-Write] Do not attempt to override compression scheme when running CompressAnimations commandlet.
  Some high frequency animations are too sensitive and shouldn't be changed.
- ``enable_root_motion`` (bool):  [Read-Write] If this is on, it will allow extracting of root motion *
- ``force_root_lock`` (bool):  [Read-Write] Force Root Bone Lock even if Root Motion is not enabled
- ``interpolation`` (AnimInterpolationType):  [Read-Write] This defines how values between keys are calculated *
- ``loop`` (bool):  [Read-Write] The default looping behavior of this animation.
  Asset players can override this
- ``meta_data`` (Array[AnimMetaData]):  [Read-Write] Meta data that can be saved with the asset

  You can query by GetMetaData function
- ``number_of_sampled_frames`` (int32):  [Read-Only]
- ``number_of_sampled_keys`` (int32):  [Read-Only]
- ``parent_asset`` (AnimationAsset):  [Read-Only] Parent Asset, if set, you won't be able to edit any data in here but just mapping table

  During cooking, this data will be used to bake out to normal asset
- ``per_bone_custom_attribute_data`` (Array[CustomAttributePerBoneData]):  [Read-Only]
- ``platform_target_frame_rate`` (PerPlatformFrameRate):  [Read-Only]
- ``preview_pose_asset`` (PoseAsset):  [Read-Write] The default skeletal mesh to use when previewing this asset - this only applies when you open Persona using this asset//
  todo:: note that this doesn't retarget right now
- ``rate_scale`` (float):  [Read-Write] Number for tweaking playback rate of this animation globally.
- ``ref_frame_index`` (int32):  [Read-Write] Additve reference frame if RefPoseType == AnimFrame *
- ``ref_pose_seq`` (AnimSequence):  [Read-Write] Additive reference animation if it's relevant - i.e. AnimScaled or AnimFrame *
- ``ref_pose_type`` (AdditiveBasePoseType):  [Read-Write] Additive refrerence pose type. Refer above enum type
- ``retarget_source`` (Name):  [Read-Write] Base pose to use when retargeting
- ``retarget_source_asset`` (SkeletalMesh):  [Read-Write]
- ``root_motion_root_lock`` (RootMotionRootLock):  [Read-Write] Root Bone will be locked to that position when extracting root motion.*
- ``sequence_length`` (float):  [Read-Only]
- ``skeleton`` (Skeleton):  [Read-Only] Pointer to the Skeleton this asset can be played on .
- ``strip_anim_data_on_dedicated_server`` (StripAnimDataOnDedicatedServerSettings):  [Read-Write] Enum used to decide whether we should strip animation data on dedicated server
- ``thumbnail_info`` (ThumbnailInfo):  [Read-Only] Information for thumbnail rendering
- ``use_normalized_root_motion_scale`` (bool):  [Read-Write] If this is on, it will use a normalized scale value for the root motion extracted: FVector(1.0, 1.0, 1.0) *
- ``variable_frame_stripping_settings`` (VariableFrameStrippingSettings):  [Read-Write]

<a id="unreal.AnimSequence.update_retarget_source_asset_data"></a>

#### update_retarget_source_asset_data

```python
def update_retarget_source_asset_data() -> None
```

x.update_retarget_source_asset_data() -> None
Update the retarget data pose from the source, if it exist, else clears the retarget data pose saved in RetargetSourceAssetReferencePose.
Warning : This function calls LoadSynchronous at the retarget source asset soft object pointer, so it can not be used at PostLoad

<a id="unreal.AnimSequence.set_retarget_source_asset"></a>

#### set_retarget_source_asset

```python
def set_retarget_source_asset(retarget_source_asset: SkeletalMesh) -> None
```

x.set_retarget_source_asset(retarget_source_asset) -> None
Assigns the passed skeletal mesh to the retarget source

Args:
    retarget_source_asset (SkeletalMesh):

<a id="unreal.AnimSequence.remove_custom_attribute"></a>

#### remove_custom_attribute

```python
def remove_custom_attribute(bone_name: Name, attribute_name: Name) -> None
```

x.remove_custom_attribute(bone_name, attribute_name) -> None
Remove Custom Attribute
deprecated: RemoveCustomAttribute has been deprecated, use UAnimDataController::RemoveAttribute instead

Args:
    bone_name (Name): 
    attribute_name (Name):

<a id="unreal.AnimSequence.remove_all_custom_attributes_for_bone"></a>

#### remove_all_custom_attributes_for_bone

```python
def remove_all_custom_attributes_for_bone(bone_name: Name) -> None
```

x.remove_all_custom_attributes_for_bone(bone_name) -> None
Remove All Custom Attributes for Bone
deprecated: RemoveAllCustomAttributesForBone has been deprecated, use UAnimDataController::RemoveAllAttributesForBone instead

Args:
    bone_name (Name):

<a id="unreal.AnimSequence.remove_all_custom_attributes"></a>

#### remove_all_custom_attributes

```python
def remove_all_custom_attributes() -> None
```

x.remove_all_custom_attributes() -> None
Remove All Custom Attributes
deprecated: RemoveAllCustomAttributes has been deprecated, use UAnimDataController::RemoveAllAttributes instead

<a id="unreal.AnimSequence.get_retarget_source_asset"></a>

#### get_retarget_source_asset

```python
def get_retarget_source_asset() -> SkeletalMesh
```

x.get_retarget_source_asset() -> SkeletalMesh
Returns the retarget source asset soft object pointer.

Returns:
    SkeletalMesh:

<a id="unreal.AnimSequence.clear_retarget_source_asset"></a>

#### clear_retarget_source_asset

```python
def clear_retarget_source_asset() -> None
```

x.clear_retarget_source_asset() -> None
Resets the retarget source asset

<a id="unreal.AnimSequence.add_bone_string_custom_attribute"></a>

#### add_bone_string_custom_attribute

```python
def add_bone_string_custom_attribute(bone_name: Name, attribute_name: Name,
                                     time_keys: Array[float],
                                     value_keys: Array[str]) -> None
```

x.add_bone_string_custom_attribute(bone_name, attribute_name, time_keys, value_keys) -> None
Add Bone String Custom Attribute
deprecated: AddBoneStringCustomAttribute has been deprecated, use UAnimDataController::AddAttribute instead

Args:
    bone_name (Name): 
    attribute_name (Name): 
    time_keys (Array[float]): 
    value_keys (Array[str]):

<a id="unreal.AnimSequence.add_bone_integer_custom_attribute"></a>

#### add_bone_integer_custom_attribute

```python
def add_bone_integer_custom_attribute(bone_name: Name, attribute_name: Name,
                                      time_keys: Array[float],
                                      value_keys: Array[int]) -> None
```

x.add_bone_integer_custom_attribute(bone_name, attribute_name, time_keys, value_keys) -> None
Add Bone Integer Custom Attribute
deprecated: AddBoneIntegerCustomAttribute has been deprecated, use UAnimDataController::AddAttribute instead

Args:
    bone_name (Name): 
    attribute_name (Name): 
    time_keys (Array[float]): 
    value_keys (Array[int32]):

<a id="unreal.AnimSequence.add_bone_float_custom_attribute"></a>

#### add_bone_float_custom_attribute

```python
def add_bone_float_custom_attribute(bone_name: Name, attribute_name: Name,
                                    time_keys: Array[float],
                                    value_keys: Array[float]) -> None
```

x.add_bone_float_custom_attribute(bone_name, attribute_name, time_keys, value_keys) -> None
Add Bone Float Custom Attribute
deprecated: AddBoneFloatCustomAttribute has been deprecated, use UAnimDataController::AddAttribute instead

Args:
    bone_name (Name): 
    attribute_name (Name): 
    time_keys (Array[float]): 
    value_keys (Array[float]):

<a id="unreal.AnimStreamable"></a>