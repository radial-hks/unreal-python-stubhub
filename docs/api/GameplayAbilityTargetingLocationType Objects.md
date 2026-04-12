## GameplayAbilityTargetingLocationType Objects

```python
class GameplayAbilityTargetingLocationType(EnumBase)
```

What type of location calculation to use when an ability asks for our transform

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayAbilityTargetTypes.h

<a id="unreal.GameplayAbilityTargetingLocationType.LITERAL_TRANSFORM"></a>

#### LITERAL\_TRANSFORM

0: We report an actual raw transform. This is also the final fallback if other methods fail

<a id="unreal.GameplayAbilityTargetingLocationType.ACTOR_TRANSFORM"></a>

#### ACTOR\_TRANSFORM

1: We pull the transform from an associated actor directly

<a id="unreal.GameplayAbilityTargetingLocationType.SOCKET_TRANSFORM"></a>

#### SOCKET\_TRANSFORM

2: We aim from a named socket on the player's skeletal mesh component

<a id="unreal.GameplayAbilityInstancingPolicy"></a>