## GameplayEffectCue Objects

```python
class GameplayEffectCue(StructBase)
```

FGameplayEffectCue
    This is a cosmetic cue that can be tied to a UGameplayEffect.
 This is essentially a GameplayTag + a Min/Max level range that is used to map the level of a GameplayEffect to a normalized value used by the GameplayCue system.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffect.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gameplay_cue_tags`` (GameplayTagContainer):  [Read-Write] Tags passed to the gameplay cue handler when this cue is activated
- ``magnitude_attribute`` (GameplayAttribute):  [Read-Write] The attribute to use as the source for cue magnitude. If none use level
- ``max_level`` (float):  [Read-Write] The maximum level that this Cue supports
- ``min_level`` (float):  [Read-Write] The minimum level that this Cue supports

<a id="unreal.GameplayEffectCue.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.InheritedTagContainer"></a>