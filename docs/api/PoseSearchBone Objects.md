## PoseSearchBone Objects

```python
class PoseSearchBone(StructBase)
```

Pose Search Bone

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchFeatureChannel_Pose.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``debug_color`` (LinearColor):  [Read-Write]
- ``flags`` (int32):  [Read-Write] This allows the user to define what information from the channel you want to compare to.
- ``normalization_group`` (Name):  [Read-Write] if set, all the channels of the same class with the same cardinality, and the same NormalizationGroup, will be normalized together.
  for example in a locomotion database of a character holding a weapon, containing non mirrorable animations, you'd still want to normalize together
  left foot and right foot position and velocity
- ``reference`` (BoneReference):  [Read-Write]
- ``weight`` (float):  [Read-Write]

<a id="unreal.PoseSearchBone.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.PoseSearchTrajectorySample"></a>