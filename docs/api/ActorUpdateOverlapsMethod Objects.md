## ActorUpdateOverlapsMethod Objects

```python
class ActorUpdateOverlapsMethod(EnumBase)
```

Chooses a method for actors to update overlap state (objects it is touching) on initialization, currently only used during level streaming.

**C++ Source:**

- **Module**: Engine
- **File**: Actor.h

<a id="unreal.ActorUpdateOverlapsMethod.USE_CONFIG_DEFAULT"></a>

#### USE_CONFIG_DEFAULT

0: Use the default value specified by the native class or config value.

<a id="unreal.ActorUpdateOverlapsMethod.ALWAYS_UPDATE"></a>

#### ALWAYS_UPDATE

1: Always update overlap state on initialization.

<a id="unreal.ActorUpdateOverlapsMethod.ONLY_UPDATE_MOVABLE"></a>

#### ONLY_UPDATE_MOVABLE

2: Only update if root component has Movable mobility.

<a id="unreal.ActorUpdateOverlapsMethod.NEVER_UPDATE"></a>

#### NEVER_UPDATE

3: Never update overlap state on initialization.

<a id="unreal.SpawnActorScaleMethod"></a>