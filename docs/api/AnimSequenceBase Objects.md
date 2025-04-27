## AnimSequenceBase Objects

```python
class AnimSequenceBase(AnimationAsset)
```

Anim Sequence Base

**C++ Source:**

- **Module**: Engine
- **File**: AnimSequenceBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_mapping_table`` (AssetMappingTable):  [Read-Only] Asset mapping table when ParentAsset is set
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``controller`` (AnimationDataController):  [Read-Only] UAnimDataController instance set to operate on DataModel
- ``data_model`` (AnimDataModel):  [Read-Only]
- ``data_model_interface`` (AnimationDataModel):  [Read-Only] IAnimationDataModel instance containing (source) animation data
- ``loop`` (bool):  [Read-Write] The default looping behavior of this animation.
  Asset players can override this
- ``meta_data`` (Array[AnimMetaData]):  [Read-Write] Meta data that can be saved with the asset

  You can query by GetMetaData function
- ``parent_asset`` (AnimationAsset):  [Read-Only] Parent Asset, if set, you won't be able to edit any data in here but just mapping table

  During cooking, this data will be used to bake out to normal asset
- ``preview_pose_asset`` (PoseAsset):  [Read-Write] The default skeletal mesh to use when previewing this asset - this only applies when you open Persona using this asset//
  todo:: note that this doesn't retarget right now
- ``rate_scale`` (float):  [Read-Write] Number for tweaking playback rate of this animation globally.
- ``sequence_length`` (float):  [Read-Only]
- ``skeleton`` (Skeleton):  [Read-Only] Pointer to the Skeleton this asset can be played on .
- ``thumbnail_info`` (ThumbnailInfo):  [Read-Only] Information for thumbnail rendering

<a id="unreal.AnimSequenceBase.sequence_length"></a>

#### sequence_length

```python
@property
def sequence_length() -> float
```

(float):  [Read-Only]

<a id="unreal.AnimSequenceBase.data_model"></a>

#### data_model

```python
@property
def data_model() -> AnimDataModel
```

(AnimDataModel):  [Read-Only]

<a id="unreal.AnimSequenceBase.data_model_interface"></a>

#### data_model_interface

```python
@property
def data_model_interface() -> AnimationDataModel
```

(AnimationDataModel):  [Read-Only] IAnimationDataModel instance containing (source) animation data

<a id="unreal.AnimSequenceBase.controller"></a>

#### controller

```python
@property
def controller() -> AnimationDataController
```

(AnimationDataController):  [Read-Only] UAnimDataController instance set to operate on DataModel

<a id="unreal.AnimSequenceBase.get_anim_pose_at_time"></a>

#### get_anim_pose_at_time

```python
def get_anim_pose_at_time(
        time: float,
        evaluation_options: AnimPoseEvaluationOptions) -> AnimPose
```

x.get_anim_pose_at_time(time, evaluation_options) -> AnimPose
Evaluates an Animation Sequence Base to generate a valid Anim Pose instance

Args:
    time (double): Time at which the pose should be evaluated
    evaluation_options (AnimPoseEvaluationOptions): Options determining the way the pose should be evaluated

Returns:
    AnimPose: 

    pose (AnimPose): Anim Pose to hold the evaluated data

<a id="unreal.AnimSequenceBase.get_anim_pose_at_frame"></a>

#### get_anim_pose_at_frame

```python
def get_anim_pose_at_frame(
        frame_index: int,
        evaluation_options: AnimPoseEvaluationOptions) -> AnimPose
```

x.get_anim_pose_at_frame(frame_index, evaluation_options) -> AnimPose
Evaluates an Animation Sequence Base to generate a valid Anim Pose instance

Args:
    frame_index (int32): Exact frame at which the pose should be evaluated
    evaluation_options (AnimPoseEvaluationOptions): Options determining the way the pose should be evaluated

Returns:
    AnimPose: 

    pose (AnimPose): Anim Pose to hold the evaluated data

<a id="unreal.AnimSequenceBase.add_transform_attribute"></a>

#### add_transform_attribute

```python
def add_transform_attribute(attribute_name: Name, bone_name: Name,
                            keys: Array[float],
                            values: Array[Transform]) -> bool
```

x.add_transform_attribute(attribute_name, bone_name, keys, values) -> bool
Add Transform Attribute

Args:
    attribute_name (Name): 
    bone_name (Name): 
    keys (Array[float]): 
    values (Array[Transform]): 

Returns:
    bool:

<a id="unreal.AnimPoseExtensions"></a>