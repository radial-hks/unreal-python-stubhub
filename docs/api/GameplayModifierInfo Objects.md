## GameplayModifierInfo Objects

```python
class GameplayModifierInfo(StructBase)
```

FGameplayModifierInfo
    Tells us "Who/What we" modify
    Does not tell us how exactly

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffect.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attribute`` (GameplayAttribute):  [Read-Write] The Attribute we modify or the GE we modify modifies.
- ``evaluation_channel_settings`` (GameplayModEvaluationChannelSettings):  [Read-Write] Evaluation channel settings of the modifier
- ``modifier_magnitude`` (GameplayEffectModifierMagnitude):  [Read-Write] Magnitude of the modifier
- ``modifier_op`` (GameplayModOp):  [Read-Write] The numeric operation of this modifier: Override, Add, Multiply, etc
  When multiple modifiers aggregate together, the equation is:
  ((BaseValue + AddBase) * MultiplyAdditive / DivideAdditive * MultiplyCompound) + AddFinal
- ``source_tags`` (GameplayTagRequirements):  [Read-Write]
- ``target_tags`` (GameplayTagRequirements):  [Read-Write]

<a id="unreal.GameplayModifierInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.GameplayEffectCue"></a>