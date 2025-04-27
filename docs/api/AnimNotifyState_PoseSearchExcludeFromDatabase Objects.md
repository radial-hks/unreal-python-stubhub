## AnimNotifyState_PoseSearchExcludeFromDatabase Objects

```python
class AnimNotifyState_PoseSearchExcludeFromDatabase(
        AnimNotifyState_PoseSearchBase)
```

Use this notify state to remove animation segments from the database completely, they will never play or return from
a search result

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchAnimNotifies.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``notify_color`` (Color):  [Read-Write] Color of Notify in editor
- ``should_fire_in_editor`` (bool):  [Read-Write] Whether this notify state instance should fire in animation editors

<a id="unreal.AnimNotifyState_PoseSearchBlockTransition"></a>