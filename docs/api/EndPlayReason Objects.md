## EndPlayReason Objects

```python
class EndPlayReason(EnumBase)
```

Specifies why an actor is being deleted/removed from a level

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.EndPlayReason.DESTROYED"></a>

#### DESTROYED

0: When the Actor or Component is explicitly destroyed.

<a id="unreal.EndPlayReason.LEVEL_TRANSITION"></a>

#### LEVEL_TRANSITION

1: When the world is being unloaded for a level transition.

<a id="unreal.EndPlayReason.END_PLAY_IN_EDITOR"></a>

#### END_PLAY_IN_EDITOR

2: When the world is being unloaded because PIE is ending.

<a id="unreal.EndPlayReason.REMOVED_FROM_WORLD"></a>

#### REMOVED_FROM_WORLD

3: When the level it is a member of is streamed out.

<a id="unreal.EndPlayReason.QUIT"></a>

#### QUIT

4: When the application is being exited.

<a id="unreal.TickingGroup"></a>