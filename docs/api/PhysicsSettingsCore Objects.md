## PhysicsSettingsCore Objects

```python
class PhysicsSettingsCore(DeveloperSettings)
```

Default physics settings.

**C++ Source:**

- **Module**: PhysicsCore
- **File**: PhysicsSettingsCore.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bounce_threshold_velocity`` (float):  [Read-Write] Minimum relative velocity required for an object to bounce. A typical value for simulation stability is about 0.2 * gravity
- ``contact_offset_multiplier`` (float):  [Read-Write] Contact offset multiplier. When creating a physics shape we look at its bounding volume and multiply its minimum value by this multiplier. A bigger number will generate contact points earlier which results in higher stability at the cost of performance.
- ``default_fluid_friction`` (float):  [Read-Write] Default fluid friction for Physics Volumes.
- ``default_gravity_z`` (float):  [Read-Write] Default gravity.
- ``default_shape_complexity`` (CollisionTraceFlag):  [Read-Write] Determines the default physics shape complexity.
- ``default_terminal_velocity`` (float):  [Read-Write] Default terminal velocity for Physics Volumes.
- ``enable2d_physics`` (bool):  [Read-Write] Can 2D physics be used (Box2D)?
- ``enable_enhanced_determinism`` (bool):  [Read-Write] If set to true, the scene will use enhanced determinism at the cost of a bit more resources. See eENABLE_ENHANCED_DETERMINISM to learn about the specifics
- ``enable_pcm`` (bool):  [Read-Write] Enables persistent contact manifolds. This will generate fewer contact points, but with more accuracy. Reduces stability of stacking, but can help energy conservation.
- ``enable_shape_sharing`` (bool):  [Read-Write] Enables shape sharing between sync and async scene for static rigid actors
- ``enable_stabilization`` (bool):  [Read-Write] Enables stabilization of contacts for slow moving bodies. This will help improve the stability of stacking.
- ``friction_combine_mode`` (FrictionCombineMode):  [Read-Write] Friction combine mode, controls how friction is computed for multiple materials.
- ``max_angular_velocity`` (float):  [Read-Write] Max angular velocity that a simulated object can achieve.
- ``max_contact_offset`` (float):  [Read-Write] Max Contact offset.
- ``max_depenetration_velocity`` (float):  [Read-Write] Max velocity which may be used to depenetrate simulated physics objects. 0 means no maximum.
- ``min_contact_offset`` (float):  [Read-Write] Min Contact offset.
- ``ragdoll_aggregate_threshold`` (int32):  [Read-Write] Threshold for ragdoll bodies above which they will be added to an aggregate before being added to the scene
- ``restitution_combine_mode`` (FrictionCombineMode):  [Read-Write] Restitution combine mode, controls how restitution is computed for multiple materials.
- ``simulate_scratch_memory_size`` (int32):  [Read-Write] Amount of memory to reserve for PhysX simulate(), this is per pxscene and will be rounded up to the next 16K boundary
- ``simulate_skeletal_mesh_on_dedicated_server`` (bool):  [Read-Write] If true, simulate physics for this component on a dedicated server.
  This should be set if simulating physics and replicating with a dedicated server.
- ``solver_options`` (ChaosSolverConfiguration):  [Read-Write] Options to apply to Chaos solvers on creation
- ``triangle_mesh_triangle_min_area_threshold`` (float):  [Read-Write] Triangles from triangle meshes (BSP) with an area less than or equal to this value will be removed from physics collision data. Set to less than 0 to disable.
- ``warn_missing_locks`` (bool):  [Read-Write] Whether to warn when physics locks are used incorrectly. Turning this off is not recommended and should only be used by very advanced users.

<a id="unreal.PhysicsSettings"></a>