## AnimNotifyState_PoseSearchBlockTransition Objects

```python
class AnimNotifyState_PoseSearchBlockTransition(AnimNotifyState_PoseSearchBase
                                                )
```

A pose search search will not return results that overlap this notify, but the animation segment can still play
if a previous search result advances into it.

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchAnimNotifies.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``notify_color`` (Color):  [Read-Write] Color of Notify in editor
- ``should_fire_in_editor`` (bool):  [Read-Write] Whether this notify state instance should fire in animation editors

<a id="unreal.AnimNotifyState_PoseSearchModifyCost"></a>