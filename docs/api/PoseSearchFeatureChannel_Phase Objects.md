## PoseSearchFeatureChannel_Phase Objects

```python
class PoseSearchFeatureChannel_Phase(PoseSearchFeatureChannel)
```

Pose Search Feature Channel Phase

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchFeatureChannel_Phase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone`` (BoneReference):  [Read-Write]
- ``debug_color`` (LinearColor):  [Read-Write]
- ``input_query_pose`` (InputQueryPose):  [Read-Write]
- ``normalization_group`` (Name):  [Read-Write] if set, all the channels of the same class with the same cardinality, and the same NormalizationGroup, will be normalized together.
  for example in a locomotion database of a character holding a weapon, containing non mirrorable animations, you'd still want to normalize together
  left foot and right foot position and velocity
- ``sample_role`` (Name):  [Read-Write]
- ``weight`` (float):  [Read-Write]

<a id="unreal.PoseSearchFeatureChannel_Pose"></a>