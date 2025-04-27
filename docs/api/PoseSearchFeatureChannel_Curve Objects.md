## PoseSearchFeatureChannel_Curve Objects

```python
class PoseSearchFeatureChannel_Curve(PoseSearchFeatureChannel)
```

Pose Search Feature Channel Curve

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchFeatureChannel_Curve.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``curve_name`` (Name):  [Read-Write]
- ``debug_color`` (LinearColor):  [Read-Write]
- ``input_query_pose`` (InputQueryPose):  [Read-Write]
- ``normalization_group`` (Name):  [Read-Write] if set, all the channels of the same class with the same cardinality, and the same NormalizationGroup, will be normalized together.
  for example in a locomotion database of a character holding a weapon, containing non mirrorable animations, you'd still want to normalize together
  left foot and right foot position and Curve
- ``sample_role`` (Name):  [Read-Write]
- ``sample_time_offset`` (float):  [Read-Write] the data relative to the sampling time associated to this channel will be offset by SampleTimeOffset seconds.
  For example, if Curve is DistanceToWall, and SampleTimeOffset is 0.5, this channel will try to match the future DistanceToWall curve of the character 0.5 seconds ahead
- ``weight`` (float):  [Read-Write]

<a id="unreal.PoseSearchFeatureChannel_Curve.curve_name"></a>

#### curve_name

```python
@property
def curve_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.PoseSearchFeatureChannel_Curve.bp_get_curve_value"></a>

#### bp_get_curve_value

```python
def bp_get_curve_value(anim_instance: AnimInstance) -> float
```

x.bp_get_curve_value(anim_instance) -> float
BP Get Curve Value

Args:
    anim_instance (AnimInstance): 

Returns:
    float:

<a id="unreal.PoseSearchFeatureChannel_FilterCrashingLegs"></a>