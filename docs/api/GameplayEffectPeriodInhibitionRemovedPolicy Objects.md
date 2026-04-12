## GameplayEffectPeriodInhibitionRemovedPolicy Objects

```python
class GameplayEffectPeriodInhibitionRemovedPolicy(EnumBase)
```

Enumeration of policies for dealing with the period of a gameplay effect when inhibition is removed

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffect.h

<a id="unreal.GameplayEffectPeriodInhibitionRemovedPolicy.NEVER_RESET"></a>

#### NEVER\_RESET

0: Does not reset. The period timing will continue as if the inhibition hadn't occurred.

<a id="unreal.GameplayEffectPeriodInhibitionRemovedPolicy.RESET_PERIOD"></a>

#### RESET\_PERIOD

1: Resets the period. The next execution will occur one full period from when inhibition is removed.

<a id="unreal.GameplayEffectPeriodInhibitionRemovedPolicy.EXECUTE_AND_RESET_PERIOD"></a>

#### EXECUTE\_AND\_RESET\_PERIOD

2: Executes immediately and resets the period.

<a id="unreal.GameplayEffectStackingType"></a>