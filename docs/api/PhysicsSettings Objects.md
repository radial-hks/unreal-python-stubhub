## PhysicsSettings Objects

```python
class PhysicsSettings(PhysicsSettingsCore)
```

Default physics settings.

**C++ Source:**

- **Module**: Engine
- **File**: PhysicsSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``anim_physics_min_delta_time`` (float):  [Read-Write] Min Delta Time below which anim dynamics and rigidbody nodes will not simulate.
- ``async_fixed_time_step_size`` (float):  [Read-Write] If using async, the time step size to tick at. This feature is still experimental. Certain functionality might not work correctly
- ``bounce_threshold_velocity`` (float):  [Read-Write] Minimum relative velocity required for an object to bounce. A typical value for simulation stability is about 0.2 * gravity
- ``chaos_settings`` (ChaosPhysicsSettings):  [Read-Write] Chaos physics engine settings
- ``contact_offset_multiplier`` (float):  [Read-Write] Contact offset multiplier. When creating a physics shape we look at its bounding volume and multiply its minimum value by this multiplier. A bigger number will generate contact points earlier which results in higher stability at the cost of performance.
- ``default_broadphase_settings`` (BroadphaseSettings):  [Read-Write] If we want to Enable MPB or not globally. This is then overridden by project settings if not enabled. *
- ``default_degrees_of_freedom`` (SettingsDOF):  [Read-Write] Useful for constraining all objects in the world, for example if you are making a 2D game using 3D environments.
- ``default_fluid_friction`` (float):  [Read-Write] Default fluid friction for Physics Volumes.
- ``default_gravity_z`` (float):  [Read-Write] Default gravity.
- ``default_shape_complexity`` (CollisionTraceFlag):  [Read-Write] Determines the default physics shape complexity.
- ``default_terminal_velocity`` (float):  [Read-Write] Default terminal velocity for Physics Volumes.
- ``disable_active_actors`` (bool):  [Read-Write] If true, physx will not update unreal with any bodies that have moved during the simulation. This should only be used if you have no physx simulation or you are manually updating the unreal data via polling physx.
- ``disable_ccd`` (bool):  [Read-Write] If true CCD will be ignored. This is an optimization when CCD is never used which removes the need for physx to check it internally.
- ``disable_kinematic_kinematic_pairs`` (bool):  [Read-Write] Whether to disable generating KK pairs, enabling this speeds up contact generation, however it is required when using APEX destruction.
- ``disable_kinematic_static_pairs`` (bool):  [Read-Write] Whether to disable generating KS pairs, enabling this makes switching between dynamic and static slower for actors - but speeds up contact generation by early rejecting these pairs
- ``enable2d_physics`` (bool):  [Read-Write] Can 2D physics be used (Box2D)?
- ``enable_enhanced_determinism`` (bool):  [Read-Write] If set to true, the scene will use enhanced determinism at the cost of a bit more resources. See eENABLE_ENHANCED_DETERMINISM to learn about the specifics
- ``enable_pcm`` (bool):  [Read-Write] Enables persistent contact manifolds. This will generate fewer contact points, but with more accuracy. Reduces stability of stacking, but can help energy conservation.
- ``enable_shape_sharing`` (bool):  [Read-Write] Enables shape sharing between sync and async scene for static rigid actors
- ``enable_stabilization`` (bool):  [Read-Write] Enables stabilization of contacts for slow moving bodies. This will help improve the stability of stacking.
- ``friction_combine_mode`` (FrictionCombineMode):  [Read-Write] Friction combine mode, controls how friction is computed for multiple materials.
- ``initial_average_frame_rate`` (float):  [Read-Write] Physics delta time initial average.
- ``max_angular_velocity`` (float):  [Read-Write] Max angular velocity that a simulated object can achieve.
- ``max_contact_offset`` (float):  [Read-Write] Max Contact offset.
- ``max_depenetration_velocity`` (float):  [Read-Write] Max velocity which may be used to depenetrate simulated physics objects. 0 means no maximum.
- ``max_physics_delta_time`` (float):  [Read-Write] Max Physics Delta Time to be clamped.
- ``max_substep_delta_time`` (float):  [Read-Write] Max delta time (in seconds) for an individual simulation substep.
- ``max_substeps`` (int32):  [Read-Write] Max number of substeps for physics simulation.
- ``min_contact_offset`` (float):  [Read-Write] Min Contact offset.
- ``min_delta_velocity_for_hit_events`` (float):  [Read-Write] Minimum velocity delta required on a collinding object for Chaos to send a hit event
- ``min_physics_delta_time`` (float):  [Read-Write] Min Physics Delta Time; the simulation will not step if the delta time is below this value
- ``phys_x_tree_rebuild_rate`` (int32):  [Read-Write] The number of frames it takes to rebuild the PhysX scene query AABB tree. The bigger the number, the smaller fetchResults takes per frame, but the more the tree deteriorates until a new tree is built
- ``physic_error_correction`` (RigidBodyErrorCorrection):  [Read-Write] Default settings for physics replication using EPhysicsReplicationMode::Default
- ``physical_surfaces`` (Array[PhysicalSurfaceName]):  [Read-Write] PhysicalMaterial Surface Types
- ``physics_prediction`` (PhysicsPredictionSettings):  [Read-Write] Settings for Networked Physics Prediction, experimental.
- ``ragdoll_aggregate_threshold`` (int32):  [Read-Write] Threshold for ragdoll bodies above which they will be added to an aggregate before being added to the scene
- ``restitution_combine_mode`` (FrictionCombineMode):  [Read-Write] Restitution combine mode, controls how restitution is computed for multiple materials.
- ``simulate_anim_physics_after_reset`` (bool):  [Read-Write] Whether to simulate anim physics nodes in the tick where they're reset.
- ``simulate_scratch_memory_size`` (int32):  [Read-Write] Amount of memory to reserve for PhysX simulate(), this is per pxscene and will be rounded up to the next 16K boundary
- ``simulate_skeletal_mesh_on_dedicated_server`` (bool):  [Read-Write] If true, simulate physics for this component on a dedicated server.
  This should be set if simulating physics and replicating with a dedicated server.
- ``solver_options`` (ChaosSolverConfiguration):  [Read-Write] Options to apply to Chaos solvers on creation
- ``substepping`` (bool):  [Read-Write] Whether to substep the physics simulation. This feature is still experimental. Certain functionality might not work correctly
- ``substepping_async`` (bool):  [Read-Write] Whether to substep the async physics simulation. This feature is still experimental. Certain functionality might not work correctly
- ``support_uv_from_hit_results`` (bool):  [Read-Write] If true, store extra information to allow FindCollisionUV to derive UV info from a line trace hit result, using the FindCollisionUV utility
- ``suppress_face_remap_table`` (bool):  [Read-Write] If true, the internal physx face to UE face mapping will not be generated. This is a memory optimization available if you do not rely on face indices returned by scene queries.
- ``sync_scene_smoothing_factor`` (float):  [Read-Write] Physics delta time smoothing factor for sync scene.
- ``tick_physics_async`` (bool):  [Read-Write] Whether to tick physics simulation on an async thread. This feature is still experimental. Certain functionality might not work correctly
- ``triangle_mesh_triangle_min_area_threshold`` (float):  [Read-Write] Triangles from triangle meshes (BSP) with an area less than or equal to this value will be removed from physics collision data. Set to less than 0 to disable.
- ``warn_missing_locks`` (bool):  [Read-Write] Whether to warn when physics locks are used incorrectly. Turning this off is not recommended and should only be used by very advanced users.

<a id="unreal.PhysicsSettings.get_physics_history_count"></a>

#### get_physics_history_count

```python
def get_physics_history_count() -> int
```

x.get_physics_history_count() -> int32
Get Physics History Count

Returns:
    int32:

<a id="unreal.PhysicsThruster"></a>