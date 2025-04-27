## AnimNotify_PlayMontageNotify Objects

```python
class AnimNotify_PlayMontageNotify(AnimNotify)
```

UAnimNotify_PlayMontageNotify

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNotify_PlayMontageNotify.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``notify_color`` (Color):  [Read-Write] Color of Notify in editor
- ``notify_name`` (Name):  [Read-Write] Name of notify that is passed to the PlayMontage K2Node.
- ``should_fire_in_editor`` (bool):  [Read-Write] Whether this notify instance should fire in animation editors

<a id="unreal.AnimNotify_PlayMontageNotify.notify_name"></a>

#### notify_name

```python
@property
def notify_name() -> Name
```

(Name):  [Read-Only] Name of notify that is passed to the PlayMontage K2Node.

<a id="unreal.AnimNotifyState"></a>