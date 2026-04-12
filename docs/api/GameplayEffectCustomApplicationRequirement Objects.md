## GameplayEffectCustomApplicationRequirement Objects

```python
class GameplayEffectCustomApplicationRequirement(Object)
```

Class used to perform custom gameplay effect modifier calculations, either via blueprint or native code

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffectCustomApplicationRequirement.h

<a id="unreal.GameplayEffectCustomApplicationRequirement.can_apply_gameplay_effect"></a>

#### can\_apply\_gameplay\_effect

```python
def can_apply_gameplay_effect(gameplay_effect: GameplayEffect,
                              spec: GameplayEffectSpec,
                              asc: AbilitySystemComponent) -> bool
```

x.can_apply_gameplay_effect(gameplay_effect, spec, asc) -> bool
Return whether the gameplay effect should be applied or not

Args:
    gameplay_effect (GameplayEffect): 
    spec (GameplayEffectSpec): 
    asc (AbilitySystemComponent): 

Returns:
    bool:

<a id="unreal.GameplayEffectExecutionCalculation"></a>