## GameplayTargetingConfirmation Objects

```python
class GameplayTargetingConfirmation(EnumBase)
```

Describes how the targeting information is confirmed

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayAbilityTargetTypes.h

<a id="unreal.GameplayTargetingConfirmation.INSTANT"></a>

#### INSTANT

0: The targeting happens instantly without special logic or user input deciding when to 'fire'

<a id="unreal.GameplayTargetingConfirmation.USER_CONFIRMED"></a>

#### USER\_CONFIRMED

1: The targeting happens when the user confirms the targeting

<a id="unreal.GameplayTargetingConfirmation.CUSTOM"></a>

#### CUSTOM

2: The GameplayTargeting Ability is responsible for deciding when the targeting data is ready. Not supported by all TargetingActors

<a id="unreal.GameplayTargetingConfirmation.CUSTOM_MULTI"></a>

#### CUSTOM\_MULTI

3: The GameplayTargeting Ability is responsible for deciding when the targeting data is ready. Not supported by all TargetingActors. Should not destroy upon data production

<a id="unreal.GameplayAbilityTargetingLocationType"></a>