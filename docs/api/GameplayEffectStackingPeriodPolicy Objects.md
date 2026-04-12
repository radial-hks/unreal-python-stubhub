## GameplayEffectStackingPeriodPolicy Objects

```python
class GameplayEffectStackingPeriodPolicy(EnumBase)
```

Enumeration of policies for dealing with the period of a gameplay effect while stacking

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffect.h

<a id="unreal.GameplayEffectStackingPeriodPolicy.RESET_ON_SUCCESSFUL_APPLICATION"></a>

#### RESET\_ON\_SUCCESSFUL\_APPLICATION

0: Any progress toward the next tick of a periodic effect is discarded upon any successful stack application

<a id="unreal.GameplayEffectStackingPeriodPolicy.NEVER_RESET"></a>

#### NEVER\_RESET

1: The progress toward the next tick of a periodic effect will never be reset, regardless of stack applications

<a id="unreal.GameplayEffectStackingExpirationPolicy"></a>