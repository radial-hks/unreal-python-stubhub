## AnimNotify\_GameplayCue Objects

```python
class AnimNotify_GameplayCue(AnimNotify)
```

UAnimNotify_GameplayCue

    An animation notify used for instantaneous gameplay cues (Burst/Latent).

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: AnimNotify_GameplayCue.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gameplay_cue`` (GameplayCueTag):  [Read-Write] GameplayCue tag to invoke.
- ``notify_color`` (Color):  [Read-Write] Color of Notify in editor
- ``should_fire_in_editor`` (bool):  [Read-Write] Whether this notify instance should fire in animation editors

<a id="unreal.AnimNotify_GameplayCue.gameplay_cue"></a>

#### gameplay\_cue

```python
@property
def gameplay_cue() -> GameplayCueTag
```

(GameplayCueTag):  [Read-Only] GameplayCue tag to invoke.

<a id="unreal.AnimNotify_GameplayCueState"></a>