## GameplayEffectSpec Objects

```python
class GameplayEffectSpec(StructBase)
```

GameplayEffect Specification. Tells us:
    -What UGameplayEffect (const data)
    -What Level
 -Who instigated

FGameplayEffectSpec is modifiable. We start with initial conditions and modifications be applied to it. In this sense, it is stateful/mutable but it
is still distinct from an FActiveGameplayEffect which in an applied instance of an FGameplayEffectSpec.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffect.h

<a id="unreal.GameplayEffectSpec.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.GameplayEffectContextHandle"></a>