## AnimNotifyState_PoseSearchSamplingAttribute Objects

```python
class AnimNotifyState_PoseSearchSamplingAttribute(
        AnimNotifyState_PoseSearchSamplingEvent)
```

UPoseSearchFeatureChannel(s) can use this UAnimNotifyState_PoseSearchSamplingAttribute as animation space position, rotation, and linear velocity provider
during database indexing by specifying their SamplingAttributeId property to match UAnimNotifyState_PoseSearchSamplingAttribute::SamplingAttributeId

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchAnimNotifies.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone`` (BoneReference):  [Read-Write]
- ``linear_velocity`` (Vector):  [Read-Write]
- ``notify_color`` (Color):  [Read-Write] Color of Notify in editor
- ``position`` (Vector):  [Read-Write]
- ``rotation`` (Quat):  [Read-Write]
- ``sampling_attribute_id`` (int32):  [Read-Write]
- ``should_fire_in_editor`` (bool):  [Read-Write] Whether this notify state instance should fire in animation editors

<a id="unreal.AnimNotifyState_PoseSearchBranchIn"></a>