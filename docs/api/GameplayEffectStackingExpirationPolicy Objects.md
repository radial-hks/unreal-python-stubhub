## GameplayEffectStackingExpirationPolicy Objects

```python
class GameplayEffectStackingExpirationPolicy(EnumBase)
```

Enumeration of policies for dealing gameplay effect stacks that expire (in duration based effects).

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffect.h

<a id="unreal.GameplayEffectStackingExpirationPolicy.CLEAR_ENTIRE_STACK"></a>

#### CLEAR\_ENTIRE\_STACK

0: The entire stack is cleared when the active gameplay effect expires

<a id="unreal.GameplayEffectStackingExpirationPolicy.REMOVE_SINGLE_STACK_AND_REFRESH_DURATION"></a>

#### REMOVE\_SINGLE\_STACK\_AND\_REFRESH\_DURATION

1: The current stack count will be decremented by 1 and the duration refreshed. The GE is not "reapplied", just continues to exist with one less stacks.

<a id="unreal.GameplayEffectStackingExpirationPolicy.REFRESH_DURATION"></a>

#### REFRESH\_DURATION

2: The duration of the gameplay effect is refreshed. This essentially makes the effect infinite in duration. This can be used to manually handle stack decrements via OnStackCountChange callback

<a id="unreal.WaveTableSamplingMode"></a>