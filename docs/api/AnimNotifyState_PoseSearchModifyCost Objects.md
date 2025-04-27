## AnimNotifyState_PoseSearchModifyCost Objects

```python
class AnimNotifyState_PoseSearchModifyCost(AnimNotifyState_PoseSearchBase)
```

Pose search cost will be affected by this, making the animation segment more or less likely to be selected based
on the notify parameters

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchAnimNotifies.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cost_addend`` (float):  [Read-Write] A negative value reduces the cost and makes the segment more likely to be chosen. A positive value, conversely,
  makes the segment less likely to be chosen
- ``notify_color`` (Color):  [Read-Write] Color of Notify in editor
- ``should_fire_in_editor`` (bool):  [Read-Write] Whether this notify state instance should fire in animation editors

<a id="unreal.AnimNotifyState_PoseSearchOverrideContinuingPoseCostBias"></a>