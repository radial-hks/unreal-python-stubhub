## GameplayAbilityInstancingPolicy Objects

```python
class GameplayAbilityInstancingPolicy(EnumBase)
```

How the ability is instanced when executed. This limits what an ability can do in its implementation. For example, a NonInstanced
Ability cannot have state. It is probably unsafe for an InstancedPerActor ability to have latent actions, etc.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayAbilityTypes.h

<a id="unreal.GameplayAbilityInstancingPolicy.NON_INSTANCED"></a>

#### NON\_INSTANCED

0: This ability is never instanced. Anything that executes the ability is operating on the CDO.

<a id="unreal.GameplayAbilityInstancingPolicy.INSTANCED_PER_ACTOR"></a>

#### INSTANCED\_PER\_ACTOR

1: Each actor gets their own instance of this ability. State can be saved, replication is possible.

<a id="unreal.GameplayAbilityInstancingPolicy.INSTANCED_PER_EXECUTION"></a>

#### INSTANCED\_PER\_EXECUTION

2: We instance this ability each time it is executed. Replication currently unsupported.

<a id="unreal.GameplayAbilityNetExecutionPolicy"></a>