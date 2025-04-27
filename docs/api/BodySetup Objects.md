## BodySetup Objects

```python
class BodySetup(BodySetupCore)
```

BodySetup contains all collision information that is associated with a single asset.
A single BodySetup instance is shared among many BodyInstances so that geometry data is not duplicated.
Assets typically implement a GetBodySetup function that is used during physics state creation.
see: GetBodySetup
see: FBodyInstance

**C++ Source:**

- **Module**: Engine
- **File**: BodySetup.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``agg_geom`` (KAggregateGeom):  [Read-Write] Simplified collision representation of this
- ``bone_name`` (Name):  [Read-Only] Used in the PhysicsAsset case. Associates this Body with Bone in a skeletal mesh.
- ``collision_reponse`` (BodyCollisionResponse):  [Read-Write] Collision Type for this body. This eventually changes response to collision to others *
- ``collision_trace_flag`` (CollisionTraceFlag):  [Read-Write] Collision Trace behavior - by default, it will keep simple(convex)/complex(per-poly) separate *
- ``consider_for_bounds`` (bool):  [Read-Write] Should this BodySetup be considered for the bounding box of the PhysicsAsset (and hence SkeletalMeshComponent).
  There is a speed improvement from having less BodySetups processed each frame when updating the bounds.
- ``default_instance`` (BodyInstance):  [Read-Write] Default properties of the body instance, copied into objects on instantiation, was URB_BodyInstance
- ``double_sided_geometry`` (bool):  [Read-Write] If true, the physics triangle mesh will use double sided faces when doing scene queries.
  This is useful for planes and single sided meshes that need traces to work on both sides.
- ``never_needs_cooked_collision_data`` (bool):  [Read-Write] TODO Chaos this is to opt out of CreatePhysicsMeshes for certain meshes
  Better long term mesh is to not call CreatePhysicsMeshes until it is known there is a mesh instance that needs it.
- ``phys_material`` (PhysicalMaterial):  [Read-Write] Physical material to use for simple collision on this body. Encodes information about density, friction etc.
- ``physics_type`` (PhysicsType):  [Read-Write] If simulated it will use physics, if kinematic it will not be affected by physics, but can interact with physically simulated bodies. Default will inherit from OwnerComponent's behavior.
- ``walkable_slope_override`` (WalkableSlopeOverride):  [Read-Write] Custom walkable slope setting for this body.

<a id="unreal.RB_BodySetup"></a>