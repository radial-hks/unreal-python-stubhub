## GameplayEffectGrantedAbilityRemovePolicy Objects

```python
class GameplayEffectGrantedAbilityRemovePolicy(EnumBase)
```

Describes what happens when a GameplayEffect, that is granting an active ability, is removed from its owner.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayAbilitySpec.h

<a id="unreal.GameplayEffectGrantedAbilityRemovePolicy.CANCEL_ABILITY_IMMEDIATELY"></a>

#### CANCEL\_ABILITY\_IMMEDIATELY

0: Active abilities are immediately canceled and the ability is removed.

<a id="unreal.GameplayEffectGrantedAbilityRemovePolicy.REMOVE_ABILITY_ON_END"></a>

#### REMOVE\_ABILITY\_ON\_END

1: Active abilities are allowed to finish, and then removed.

<a id="unreal.GameplayEffectGrantedAbilityRemovePolicy.DO_NOTHING"></a>

#### DO\_NOTHING

2: Granted abilities are left lone when the granting GameplayEffect is removed.

<a id="unreal.GameplayEffectAttributeCaptureSource"></a>