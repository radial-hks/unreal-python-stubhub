## PoseSearchFeatureChannel_Heading Objects

```python
class PoseSearchFeatureChannel_Heading(PoseSearchFeatureChannel)
```

Pose Search Feature Channel Heading

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchFeatureChannel_Heading.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone`` (BoneReference):  [Read-Write]
- ``component_stripping`` (ComponentStrippingVector):  [Read-Write]
- ``debug_color`` (LinearColor):  [Read-Write]
- ``heading_axis`` (HeadingAxis):  [Read-Write]
- ``input_query_pose`` (InputQueryPose):  [Read-Write]
- ``normalization_group`` (Name):  [Read-Write] if set, all the channels of the same class with the same cardinality, and the same NormalizationGroup, will be normalized together.
  for example in a locomotion database of a character holding a weapon, containing non mirrorable animations, you'd still want to normalize together
  left foot and right foot position and velocity
- ``origin_bone`` (BoneReference):  [Read-Write]
- ``origin_role`` (Name):  [Read-Write]
- ``origin_time_offset`` (float):  [Read-Write] the data relative to the sampling time associated to this channel origin (root / trajectory bone) will be offsetted by OriginTimeOffset seconds.
  For example, if Bone is the head bone, SampleTimeOffset is 0.5, and OriginTimeOffset is 0.5, this channel will try to match
  the future heading of the character head bone 0.5 seconds ahead, relative to the future root bone 0.5 seconds ahead
- ``permutation_time_type`` (PermutationTimeType):  [Read-Write]
- ``sample_role`` (Name):  [Read-Write]
- ``sample_time_offset`` (float):  [Read-Write] the data relative to the sampling time associated to this channel will be offsetted by SampleTimeOffset seconds.
  For example, if Bone is the head bone, and SampleTimeOffset is 0.5, this channel will try to match the future heading of the character head bone 0.5 seconds ahead
- ``sampling_attribute_id`` (int32):  [Read-Write] if SamplingAttributeId >= 0, ALL the animations contained in the pose search database referencing the schema containing this channel are expected to have
  UAnimNotifyState_PoseSearchSamplingAttribute notify state with a matching SamplingAttributeId, and the UAnimNotifyState_PoseSearchSamplingAttribute properties
  will be used as source of data instead of this channel "Bone". UAnimNotifyState_PoseSearchSamplingAttribute properties will be then converted into OriginBone space
- ``weight`` (float):  [Read-Write]

<a id="unreal.PoseSearchFeatureChannel_Heading.bp_get_world_rotation"></a>

#### bp_get_world_rotation

```python
def bp_get_world_rotation(anim_instance: AnimInstance) -> Quat
```

x.bp_get_world_rotation(anim_instance) -> Quat
BP Get World Rotation

Args:
    anim_instance (AnimInstance): 

Returns:
    Quat:

<a id="unreal.PoseSearchFeatureChannel_Padding"></a>