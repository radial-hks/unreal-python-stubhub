## AnimNotifyState_PoseSearchOverrideContinuingPoseCostBias Objects

```python
class AnimNotifyState_PoseSearchOverrideContinuingPoseCostBias(
        AnimNotifyState_PoseSearchBase)
```

Pose search cost for the continuing pose will be affected by this, making the animation segment more or less
likely to be continuing playing based on the notify parameters

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchAnimNotifies.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cost_addend`` (float):  [Read-Write] A negative value reduces the cost and makes the segment more likely to continuing playing. A positive value, conversely,
  makes the segment less likely to continuing playing
- ``notify_color`` (Color):  [Read-Write] Color of Notify in editor
- ``should_fire_in_editor`` (bool):  [Read-Write] Whether this notify state instance should fire in animation editors

<a id="unreal.AnimNotifyState_PoseSearchSamplingEvent"></a>