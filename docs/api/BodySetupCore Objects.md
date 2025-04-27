## BodySetupCore Objects

```python
class BodySetupCore(Object)
```

Body Setup Core

**C++ Source:**

- **Module**: PhysicsCore
- **File**: BodySetupCore.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_name`` (Name):  [Read-Only] Used in the PhysicsAsset case. Associates this Body with Bone in a skeletal mesh.
- ``collision_reponse`` (BodyCollisionResponse):  [Read-Write] Collision Type for this body. This eventually changes response to collision to others *
- ``collision_trace_flag`` (CollisionTraceFlag):  [Read-Write] Collision Trace behavior - by default, it will keep simple(convex)/complex(per-poly) separate *
- ``physics_type`` (PhysicsType):  [Read-Write] If simulated it will use physics, if kinematic it will not be affected by physics, but can interact with physically simulated bodies. Default will inherit from OwnerComponent's behavior.

<a id="unreal.BodySetup"></a>