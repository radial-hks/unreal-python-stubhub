## AnimComposite Objects

```python
class AnimComposite(AnimCompositeBase)
```

Animation Composites serve as a way to combine multiple animations together and treat them as a single unit.

**C++ Source:**

- **Module**: Engine
- **File**: AnimComposite.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_mapping_table`` (AssetMappingTable):  [Read-Only] Asset mapping table when ParentAsset is set
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``common_target_frame_rate`` (FrameRate):  [Read-Only] Frame-rate used to represent this Animation Montage (best fitting for placed Animation Sequences)
- ``controller`` (AnimationDataController):  [Read-Only] UAnimDataController instance set to operate on DataModel
- ``data_model`` (AnimDataModel):  [Read-Only]
- ``data_model_interface`` (AnimationDataModel):  [Read-Only] IAnimationDataModel instance containing (source) animation data
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
- ``thumbnail_info`` (ThumbnailInfo):  [Read-Only] Information for thumbnail rendering

<a id="unreal.AnimDataModel"></a>