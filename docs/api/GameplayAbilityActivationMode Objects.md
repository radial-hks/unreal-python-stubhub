## GameplayAbilityActivationMode Objects

```python
class GameplayAbilityActivationMode(EnumBase)
```

Describes the status of activating this ability, this is updated as prediction is handled

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayAbilitySpec.h

<a id="unreal.GameplayAbilityActivationMode.AUTHORITY"></a>

#### AUTHORITY

0: We are the authority activating this ability

<a id="unreal.GameplayAbilityActivationMode.NON_AUTHORITY"></a>

#### NON\_AUTHORITY

1: We are not the authority but aren't predicting yet. This is a mostly invalid state to be in

<a id="unreal.GameplayAbilityActivationMode.PREDICTING"></a>

#### PREDICTING

2: We are predicting the activation of this ability

<a id="unreal.GameplayAbilityActivationMode.CONFIRMED"></a>

#### CONFIRMED

3: We are not the authority, but the authority has confirmed this activation

<a id="unreal.GameplayAbilityActivationMode.REJECTED"></a>

#### REJECTED

4: We tried to activate it, and server told us we couldn't (even though we thought we could)

<a id="unreal.GameplayAbilityInputBinds"></a>