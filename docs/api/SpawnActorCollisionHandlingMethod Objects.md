## SpawnActorCollisionHandlingMethod Objects

```python
class SpawnActorCollisionHandlingMethod(EnumBase)
```

Defines available strategies for handling the case where an actor is spawned in such a way that it penetrates blocking collision.

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.SpawnActorCollisionHandlingMethod.UNDEFINED"></a>

#### UNDEFINED

0: Fall back to default settings.

<a id="unreal.SpawnActorCollisionHandlingMethod.ALWAYS_SPAWN"></a>

#### ALWAYS_SPAWN

1: Actor will spawn in desired location, regardless of collisions.

<a id="unreal.SpawnActorCollisionHandlingMethod.ADJUST_IF_POSSIBLE_BUT_ALWAYS_SPAWN"></a>

#### ADJUST_IF_POSSIBLE_BUT_ALWAYS_SPAWN

2: Actor will try to find a nearby non-colliding location (based on shape components), but will always spawn even if one cannot be found.

<a id="unreal.SpawnActorCollisionHandlingMethod.ADJUST_IF_POSSIBLE_BUT_DONT_SPAWN_IF_COLLIDING"></a>

#### ADJUST_IF_POSSIBLE_BUT_DONT_SPAWN_IF_COLLIDING

3: Actor will try to find a nearby non-colliding location (based on shape components), but will NOT spawn unless one is found.

<a id="unreal.SpawnActorCollisionHandlingMethod.DONT_SPAWN_IF_COLLIDING"></a>

#### DONT_SPAWN_IF_COLLIDING

4: Actor will fail to spawn.

<a id="unreal.RoundingMode"></a>