## AnimStreamable Objects

```python
class AnimStreamable(AnimSequenceBase)
```

Anim Streamable

**C++ Source:**

- **Module**: Engine
- **File**: AnimStreamable.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_mapping_table`` (AssetMappingTable):  [Read-Only] Asset mapping table when ParentAsset is set
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``bone_compression_settings`` (AnimBoneCompressionSettings):  [Read-Write] The bone compression settings used to compress bones in this sequence.
- ``controller`` (AnimationDataController):  [Read-Only] UAnimDataController instance set to operate on DataModel
- ``curve_compression_settings`` (AnimCurveCompressionSettings):  [Read-Write] The curve compression settings used to compress curves in this sequence.
- ``data_model`` (AnimDataModel):  [Read-Only]
- ``data_model_interface`` (AnimationDataModel):  [Read-Only] IAnimationDataModel instance containing (source) animation data
- ``enable_root_motion`` (bool):  [Read-Write] If this is on, it will allow extracting of root motion *
- ``force_root_lock`` (bool):  [Read-Write] Force Root Bone Lock even if Root Motion is not enabled
- ``interpolation`` (AnimInterpolationType):  [Read-Write] This defines how values between keys are calculated *
- ``loop`` (bool):  [Read-Write] The default looping behavior of this animation.
  Asset players can override this
- ``meta_data`` (Array[AnimMetaData]):  [Read-Write] Meta data that can be saved with the asset

  You can query by GetMetaData function
- ``parent_asset`` (AnimationAsset):  [Read-Only] Parent Asset, if set, you won't be able to edit any data in here but just mapping table

  During cooking, this data will be used to bake out to normal asset
- ``preview_pose_asset`` (PoseAsset):  [Read-Write] The default skeletal mesh to use when previewing this asset - this only applies when you open Persona using this asset//
  todo:: note that this doesn't retarget right now
- ``rate_scale`` (float):  [Read-Write] Number for tweaking playback rate of this animation globally.
- ``retarget_source`` (Name):  [Read-Write] Base pose to use when retargeting
- ``root_motion_root_lock`` (RootMotionRootLock):  [Read-Write] Root Bone will be locked to that position when extracting root motion.*
- ``sequence_length`` (float):  [Read-Only]
- ``skeleton`` (Skeleton):  [Read-Only] Pointer to the Skeleton this asset can be played on .
- ``thumbnail_info`` (ThumbnailInfo):  [Read-Only] Information for thumbnail rendering
- ``use_normalized_root_motion_scale`` (bool):  [Read-Write] If this is on, it will use a normalized scale value for the root motion extracted: FVector(1.0, 1.0, 1.0) *
- ``variable_frame_stripping_settings`` (VariableFrameStrippingSettings):  [Read-Write] The settings used to control whether or not to use variable frame stripping and its amount

<a id="unreal.AnimationAttributeIdentifierExtensions"></a>