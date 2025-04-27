## CollisionEnabled Objects

```python
class CollisionEnabled(EnumBase)
```

Enum used to describe what type of collision is enabled on a body.

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.CollisionEnabled.NO_COLLISION"></a>

#### NO_COLLISION

0: Will not create any representation in the physics engine. Cannot be used for spatial queries (raycasts, sweeps, overlaps) or simulation (rigid body, constraints). Best performance possible (especially for moving objects)

<a id="unreal.CollisionEnabled.QUERY_ONLY"></a>

#### QUERY_ONLY

1: Only used for spatial queries (raycasts, sweeps, and overlaps). Cannot be used for simulation (rigid body, constraints). Useful for character movement and things that do not need physical simulation. Performance gains by keeping data out of simulation tree.

<a id="unreal.CollisionEnabled.PHYSICS_ONLY"></a>

#### PHYSICS_ONLY

2: Only used only for physics simulation (rigid body, constraints). Cannot be used for spatial queries (raycasts, sweeps, overlaps). Useful for jiggly bits on characters that do not need per bone detection. Performance gains by keeping data out of query tree

<a id="unreal.CollisionEnabled.QUERY_AND_PHYSICS"></a>

#### QUERY_AND_PHYSICS

3: Can be used for both spatial queries (raycasts, sweeps, overlaps) and simulation (rigid body, constraints).

<a id="unreal.CollisionEnabled.PROBE_ONLY"></a>

#### PROBE_ONLY

4: Only used for probing the physics simulation (rigid body, constraints). Cannot be used for spatial queries (raycasts,
              sweeps, overlaps). Useful for when you want to detect potential physics interactions and pass contact data to hit callbacks
              or contact modification, but don't want to physically react to these contacts.

<a id="unreal.CollisionEnabled.QUERY_AND_PROBE"></a>

#### QUERY_AND_PROBE

5: Can be used for both spatial queries (raycasts, sweeps, overlaps) and probing the physics simulation (rigid body,
              constraints). Will not allow for actual physics interaction, but will generate contact data, trigger hit callbacks, and
              contacts will appear in contact modification.

<a id="unreal.CollisionChannel"></a>