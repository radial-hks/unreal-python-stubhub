## GameplayAbilityTriggerSource Objects

```python
class GameplayAbilityTriggerSource(EnumBase)
```

Defines what type of trigger will activate the ability, paired to a tag

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayAbilityTypes.h

<a id="unreal.GameplayAbilityTriggerSource.GAMEPLAY_EVENT"></a>

#### GAMEPLAY\_EVENT

0: Triggered from a gameplay event, will come with payload

<a id="unreal.GameplayAbilityTriggerSource.OWNED_TAG_ADDED"></a>

#### OWNED\_TAG\_ADDED

1: Triggered if the ability's owner gets a tag added, triggered once whenever it's added

<a id="unreal.GameplayAbilityTriggerSource.OWNED_TAG_PRESENT"></a>

#### OWNED\_TAG\_PRESENT

2: Triggered if the ability's owner gets tag added, removed when the tag is removed

<a id="unreal.GameplayCueNotify_EffectPlaySpace"></a>