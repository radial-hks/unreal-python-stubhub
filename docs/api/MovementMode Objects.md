## MovementMode Objects

```python
class MovementMode(EnumBase)
```

Movement modes for Characters.

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.MovementMode.MOVE_NONE"></a>

#### MOVE_NONE

0: None (movement is disabled).

<a id="unreal.MovementMode.MOVE_WALKING"></a>

#### MOVE_WALKING

1: Walking on a surface.

<a id="unreal.MovementMode.MOVE_NAV_WALKING"></a>

#### MOVE_NAV_WALKING

2: Simplified walking on navigation data (e.g. navmesh).
If GetGenerateOverlapEvents() is true, then we will perform sweeps with each navmesh move.
If GetGenerateOverlapEvents() is false then movement is cheaper but characters can overlap other objects without some extra process to repel/resolve their collisions.

<a id="unreal.MovementMode.MOVE_FALLING"></a>

#### MOVE_FALLING

3: Falling under the effects of gravity, such as after jumping or walking off the edge of a surface.

<a id="unreal.MovementMode.MOVE_SWIMMING"></a>

#### MOVE_SWIMMING

4: Swimming through a fluid volume, under the effects of gravity and buoyancy.

<a id="unreal.MovementMode.MOVE_FLYING"></a>

#### MOVE_FLYING

5: Flying, ignoring the effects of gravity. Affected by the current physics volume's fluid friction.

<a id="unreal.MovementMode.MOVE_CUSTOM"></a>

#### MOVE_CUSTOM

6: User-defined custom movement mode, including many possible sub-modes.

<a id="unreal.AudioComponentPlayState"></a>