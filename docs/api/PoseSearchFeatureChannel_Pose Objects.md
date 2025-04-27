## PoseSearchFeatureChannel_Pose Objects

```python
class PoseSearchFeatureChannel_Pose(PoseSearchFeatureChannel_GroupBase)
```

UPoseSearchFeatureChannel_Pose

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchFeatureChannel_Pose.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``input_query_pose`` (InputQueryPose):  [Read-Write]
- ``sample_role`` (Name):  [Read-Write]
- ``sampled_bones`` (Array[PoseSearchBone]):  [Read-Write] List of skeletal joints and associated Flags (Velocity, Position, etc) to sample.
- ``use_character_space_velocities`` (bool):  [Read-Write] if bUseCharacterSpaceVelocities is true, velocities will be calculated from the positions in character space, otherwise they will be calculated using global space positions
- ``weight`` (float):  [Read-Write]

<a id="unreal.PoseSearchFeatureChannel_Position"></a>