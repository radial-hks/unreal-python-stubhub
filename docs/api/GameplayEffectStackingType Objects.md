## GameplayEffectStackingType Objects

```python
class GameplayEffectStackingType(EnumBase)
```

Enumeration for ways a single GameplayEffect asset can stack.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffectTypes.h

<a id="unreal.GameplayEffectStackingType.NONE"></a>

#### NONE

0: No stacking. Multiple applications of this GameplayEffect are treated as separate instances.

<a id="unreal.GameplayEffectStackingType.AGGREGATE_BY_SOURCE"></a>

#### AGGREGATE\_BY\_SOURCE

1: Each caster has its own stack.

<a id="unreal.GameplayEffectStackingType.AGGREGATE_BY_TARGET"></a>

#### AGGREGATE\_BY\_TARGET

2: Each target has its own stack.

<a id="unreal.GameplayEffectStackingDurationPolicy"></a>