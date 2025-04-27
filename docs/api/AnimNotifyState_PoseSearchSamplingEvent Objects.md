## AnimNotifyState_PoseSearchSamplingEvent Objects

```python
class AnimNotifyState_PoseSearchSamplingEvent(AnimNotifyState_PoseSearchBase)
```

UPoseSearchFeatureChannel(s) can use this UAnimNotifyState_PoseSearchSamplingEvent to demarcate events identified by SamplingAttributeId
during database indexing by specifying their SamplingAttributeId property to match UAnimNotifyState_PoseSearchSamplingAttribute::SamplingAttributeId

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchAnimNotifies.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``notify_color`` (Color):  [Read-Write] Color of Notify in editor
- ``sampling_attribute_id`` (int32):  [Read-Write]
- ``should_fire_in_editor`` (bool):  [Read-Write] Whether this notify state instance should fire in animation editors

<a id="unreal.AnimNotifyState_PoseSearchSamplingAttribute"></a>