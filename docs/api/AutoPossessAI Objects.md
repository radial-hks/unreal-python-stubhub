## AutoPossessAI Objects

```python
class AutoPossessAI(EnumBase)
```

Specifies if an AI pawn will automatically be possessed by an AI controller

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.AutoPossessAI.DISABLED"></a>

#### DISABLED

0: Feature is disabled (do not automatically possess AI).

<a id="unreal.AutoPossessAI.PLACED_IN_WORLD"></a>

#### PLACED_IN_WORLD

1: Only possess by an AI Controller if Pawn is placed in the world.

<a id="unreal.AutoPossessAI.SPAWNED"></a>

#### SPAWNED

2: Only possess by an AI Controller if Pawn is spawned after the world has loaded.

<a id="unreal.AutoPossessAI.PLACED_IN_WORLD_OR_SPAWNED"></a>

#### PLACED_IN_WORLD_OR_SPAWNED

3: Pawn is automatically possessed by an AI Controller whenever it is created.

<a id="unreal.EnvQueryHightlightMode"></a>