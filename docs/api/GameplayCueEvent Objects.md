## GameplayCueEvent Objects

```python
class GameplayCueEvent(EnumBase)
```

Indicates what type of action happened to a specific gameplay cue tag. Sometimes you will get multiple events at once

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffectTypes.h

<a id="unreal.GameplayCueEvent.ON_ACTIVE"></a>

#### ON\_ACTIVE

0: Called when a GameplayCue with duration is first activated, this will only be called if the client witnessed the activation

<a id="unreal.GameplayCueEvent.WHILE_ACTIVE"></a>

#### WHILE\_ACTIVE

1: Called when a GameplayCue with duration is first seen as active, even if it wasn't actually just applied (Join in progress, etc)

<a id="unreal.GameplayCueEvent.EXECUTED"></a>

#### EXECUTED

2: Called when a GameplayCue is executed, this is used for instant effects or periodic ticks

<a id="unreal.GameplayCueEvent.REMOVED"></a>

#### REMOVED

3: Called when a GameplayCue with duration is removed

<a id="unreal.GameplayAbilityActivationMode"></a>