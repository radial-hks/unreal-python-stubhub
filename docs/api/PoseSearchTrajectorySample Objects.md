## PoseSearchTrajectorySample Objects

```python
class PoseSearchTrajectorySample(StructBase)
```

Pose Search Trajectory Sample

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchFeatureChannel_Trajectory.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``debug_color`` (LinearColor):  [Read-Write]
- ``flags`` (int32):  [Read-Write] This allows the user to define what information from the channel you want to compare to.
- ``normalization_group`` (Name):  [Read-Write] if set, all the channels of the same class with the same cardinality, and the same NormalizationGroup, will be normalized together.
  for example in a locomotion database of a character holding a weapon, containing non mirrorable animations, you'd still want to normalize together
  left foot and right foot position and velocity
- ``offset`` (float):  [Read-Write] the data relative to the sampling time associated to this FPoseSearchTrajectorySample will be offsetted by Offset seconds.
  For example, Flags is Position, and Offset is 0.5, this channel will try to match the future position of the trajectory 0.5 seconds ahead
- ``weight`` (float):  [Read-Write]

<a id="unreal.PoseSearchTrajectorySample.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.PoseSearchInteractionAssetItem"></a>