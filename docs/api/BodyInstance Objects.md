## BodyInstance Objects

```python
class BodyInstance(BodyInstanceCore)
```

Container for a physics representation of an object

**C++ Source:**

- **Module**: Engine
- **File**: BodyInstance.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angular_damping`` (float):  [Read-Write] 'Drag' force added to reduce angular movement
- ``auto_weld`` (bool):  [Read-Write] If true and is attached to a parent, the two bodies will be joined into a single rigid body. Physical settings like collision profile and body settings are determined by the root
- ``collision_enabled`` (CollisionEnabled):  [Read-Write] Type of collision enabled.

        No Collision      : Will not create any representation in the physics engine. Cannot be used for spatial queries (raycasts, sweeps, overlaps) or simulation (rigid body, constraints). Best performance possible (especially for moving objects)
        Query Only        : Only used for spatial queries (raycasts, sweeps, and overlaps). Cannot be used for simulation (rigid body, constraints). Useful for character movement and things that do not need physical simulation. Performance gains by keeping data out of simulation tree.
        Physics Only      : Only used only for physics simulation (rigid body, constraints). Cannot be used for spatial queries (raycasts, sweeps, overlaps). Useful for jiggly bits on characters that do not need per bone detection. Performance gains by keeping data out of query tree
        Collision Enabled : Can be used for both spatial queries (raycasts, sweeps, overlaps) and simulation (rigid body, constraints).
- ``collision_profile_name`` (Name):  [Read-Write] Collision Profile Name *
- ``collision_responses`` (CollisionResponse):  [Read-Write] Custom Channels for Responses
- ``com_nudge`` (Vector):  [Read-Write] User specified offset for this object's Center of Mass. The offset is defined in bone space and will be added to the calculated location.
- ``custom_dof_plane_normal`` (Vector):  [Read-Write] Locks physical movement along a custom plane for a given normal.
- ``custom_sleep_threshold_multiplier`` (float):  [Read-Write] If the SleepFamily is set to custom, multiply the natural sleep threshold by this amount. A higher number will cause the body to sleep sooner.
- ``dof_mode`` (DOFMode):  [Read-Write] [Physx Only] Locks physical movement along specified axis.
- ``enable_gravity`` (bool):  [Read-Write] If object should have the force of gravity applied
- ``generate_wake_events`` (bool):  [Read-Write] Should 'wake/sleep' events fire when this object is woken up or put to sleep by the physics simulation.
- ``gravity_group_index`` (uint8):  [Read-Write] What gravity group the BI should use, which determines rate of acceleration
- ``ignore_analytic_collisions`` (bool):  [Read-Write] If true ignore analytic collisions and treat objects as a general implicit surface
- ``inertia_conditioning`` (bool):  [Read-Write]
  brief: Enable automatic inertia conditioning to stabilize constraints. Inertia conditioning increases inertia when an object is long and thin and also when it has joints that are outside the collision shapes of the body. Increasing the inertia reduces the amount of rotation applied at joints which helps stabilize joint chains, especially when bodies are small. In principle you can get the same behaviour by setting the InertiaTensorScale appropriately, but this takes some of the guesswork out of it.
  note: This only changes the inertia used in the low-level solver. That inertia is not visible to the BodyInstance which will still report the inertia calculated from the mass, shapes, and InertiaTensorScale.
  note: When enabled, the effective inertia depends on the joints attached to the body so the inertia will change when joints are added or removed (automatically - no user action required).
- ``inertia_tensor_scale`` (Vector):  [Read-Write] Per-instance scaling of inertia (bigger number means  it'll be harder to rotate)
- ``linear_damping`` (float):  [Read-Write] 'Drag' force added to reduce linear movement
- ``lock_rotation`` (bool):  [Read-Write] [Physx Only] When a Locked Axis Mode is selected, will lock rotation to the specified axis
- ``lock_translation`` (bool):  [Read-Write] [Physx Only] When a Locked Axis Mode is selected, will lock translation on the specified axis
- ``lock_x_rotation`` (bool):  [Read-Write] [Physx Only] Lock rotation about the X-axis
- ``lock_x_translation`` (bool):  [Read-Write] [Physx Only] Lock translation along the X-axis
- ``lock_y_rotation`` (bool):  [Read-Write] [Physx Only] Lock rotation about the Y-axis
- ``lock_y_translation`` (bool):  [Read-Write] [Physx Only] Lock translation along the Y-axis
- ``lock_z_rotation`` (bool):  [Read-Write] [Physx Only] Lock rotation about the Z-axis
- ``lock_z_translation`` (bool):  [Read-Write] [Physx Only] Lock translation along the Z-axis
- ``mass_in_kg_override`` (float):  [Read-Write] Mass of the body in KG. By default we compute this based on physical material and mass scale.
  see: bOverrideMass to set this directly
- ``mass_scale`` (float):  [Read-Write] Per-instance scaling of mass
- ``max_angular_velocity`` (float):  [Read-Write] The maximum angular velocity for this instance [degrees/s]
- ``max_depenetration_velocity`` (float):  [Read-Write] The maximum velocity used to depenetrate this object from others when spawned or teleported with initial overlaps (does not affect overlaps as a result of normal movement).
  A value of zero will allow objects that are spawned overlapping to go to sleep without moving rather than pop out of each other. E.g., use zero if you spawn dynamic rocks
  partially embedded in the ground and want them to be interactive but not pop out of the ground when touched.
  A negative value is equivalent to bOverrideMaxDepenetrationVelocity = false, meaning use the project setting.
  This overrides the CollisionInitialOverlapDepenetrationVelocity project setting on a per-body basis (and not the MaxDepenetrationVelocity solver setting that will be deprecated).
- ``notify_rigid_body_collision`` (bool):  [Read-Write] Should 'Hit' events fire when this object collides during physics simulation.
- ``object_type`` (CollisionChannel):  [Read-Write] Enum indicating what type of object this should be considered as when it moves
- ``one_way_interaction`` (bool):  [Read-Write] If set to true, this body will treat bodies that do not have the flag set as having infinite mass
- ``override_mass`` (bool):  [Read-Write] If true, mass will not be automatically computed and you must set it directly
- ``override_max_angular_velocity`` (bool):  [Read-Write] Override the default max angular velocity
- ``override_max_depenetration_velocity`` (bool):  [Read-Write] Whether this body instance has its own custom MaxDepenetrationVelocity
- ``override_solver_async_delta_time`` (bool):  [Read-Write] Set the desired delta time for the body. *
- ``override_walkable_slope_on_instance`` (bool):  [Read-Write] Whether this instance of the object has its own custom walkable slope override setting.
- ``phys_material_override`` (PhysicalMaterial):  [Read-Write] Allows you to override the PhysicalMaterial to use for simple collision on this body.
- ``position_solver_iteration_count`` (uint8):  [Read-Write] [PhysX Only] This physics body's solver iteration count for position. Increasing this will be more CPU intensive, but better stabilized.
- ``projection_solver_iteration_count`` (uint8):  [Read-Write] [PhysX Only] This physics body's solver iteration count for projection. Increasing this will be more CPU intensive, but better stabilized.
- ``simulate_physics`` (bool):  [Read-Write] If true, this body will use simulation. If false, will be 'fixed' (ie kinematic) and move where it is told.
  For a Skeletal Mesh Component, simulating requires a physics asset setup and assigned on the SkeletalMesh asset.
  For a Static Mesh Component, simulating requires simple collision to be setup on the StaticMesh asset.
- ``sleep_family`` (SleepFamily):  [Read-Write] The set of values used in considering when put this body to sleep.
- ``smooth_edge_collisions`` (bool):  [Read-Write] Remove unnecessary edge collisions to allow smooth sliding over surfaces composed of multiple actors/components.
  This is fairly expensive and should only be enabled on hero objects.
- ``solver_async_delta_time`` (float):  [Read-Write] Override value for physics solver async delta time.  With multiple actors specifying this, the solver will use the smallest delta time *
- ``stabilization_threshold_multiplier`` (float):  [Read-Write] Stabilization factor for this body if Physics stabilization is enabled. A higher number will cause more aggressive stabilization at the risk of loss of momentum at low speeds. A value of 0 will disable stabilization for this body.
- ``start_awake`` (bool):  [Read-Write] If object should start awake, or if it should initially be sleeping
- ``update_kinematic_from_simulation`` (bool):  [Read-Write] When kinematic, whether the actor transform should be updated as a result of movement in the simulation, rather than immediately whenever a target transform is set.
- ``update_mass_when_scale_changes`` (bool):  [Read-Write] If true, it will update mass when scale change *
- ``use_ccd`` (bool):  [Read-Write] If true Continuous Collision Detection (CCD) will be used for this component
- ``use_macd`` (bool):  [Read-Write] [EXPERIMENTAL] If true Motion-Aware Collision Detection (MACD) will be used for this component
- ``velocity_solver_iteration_count`` (uint8):  [Read-Write] [PhysX Only] This physics body's solver iteration count for velocity. Increasing this will be more CPU intensive, but better stabilized.
- ``walkable_slope_override`` (WalkableSlopeOverride):  [Read-Write] Custom walkable slope override setting for this instance.
  see: GetWalkableSlopeOverride(), SetWalkableSlopeOverride()

<a id="unreal.BodyInstance.__init__"></a>

#### __init__

```python
def __init__(simulate_physics: bool = False,
             enable_gravity: bool = False,
             update_kinematic_from_simulation: bool = False,
             auto_weld: bool = False,
             start_awake: bool = False,
             generate_wake_events: bool = False,
             update_mass_when_scale_changes: bool = False,
             position_solver_iteration_count: int = 0,
             velocity_solver_iteration_count: int = 0,
             projection_solver_iteration_count: int = 0,
             sleep_family: SleepFamily = SleepFamily.NORMAL,
             use_ccd: bool = False,
             ignore_analytic_collisions: bool = False,
             notify_rigid_body_collision: bool = False,
             smooth_edge_collisions: bool = False,
             inertia_conditioning: bool = False,
             one_way_interaction: bool = False,
             override_solver_async_delta_time: bool = False,
             solver_async_delta_time: float = 0.000000,
             max_depenetration_velocity: float = 0.000000,
             mass_in_kg_override: float = 0.000000,
             linear_damping: float = 0.000000,
             angular_damping: float = 0.000000,
             com_nudge: Vector = [0.000000, 0.000000, 0.000000],
             mass_scale: float = 0.000000,
             gravity_group_index: int = 0,
             inertia_tensor_scale: Vector = [0.000000, 0.000000, 0.000000],
             walkable_slope_override: WalkableSlopeOverride = [
                 WalkableSlopeBehavior.WALKABLE_SLOPE_DEFAULT, 0.000000
             ],
             phys_material_override: PhysicalMaterial = None,
             max_angular_velocity: float = 0.000000,
             custom_sleep_threshold_multiplier: float = 0.000000,
             stabilization_threshold_multiplier: float = 0.000000) -> None
```

<a id="unreal.BodyInstance.position_solver_iteration_count"></a>

#### position_solver_iteration_count

```python
@property
def position_solver_iteration_count() -> int
```

(uint8):  [Read-Only] [PhysX Only] This physics body's solver iteration count for position. Increasing this will be more CPU intensive, but better stabilized.

<a id="unreal.BodyInstance.velocity_solver_iteration_count"></a>

#### velocity_solver_iteration_count

```python
@property
def velocity_solver_iteration_count() -> int
```

(uint8):  [Read-Only] [PhysX Only] This physics body's solver iteration count for velocity. Increasing this will be more CPU intensive, but better stabilized.

<a id="unreal.BodyInstance.projection_solver_iteration_count"></a>

#### projection_solver_iteration_count

```python
@property
def projection_solver_iteration_count() -> int
```

(uint8):  [Read-Only] [PhysX Only] This physics body's solver iteration count for projection. Increasing this will be more CPU intensive, but better stabilized.

<a id="unreal.BodyInstance.sleep_family"></a>

#### sleep_family

```python
@property
def sleep_family() -> SleepFamily
```

(SleepFamily):  [Read-Write] The set of values used in considering when put this body to sleep.

<a id="unreal.BodyInstance.sleep_family"></a>

#### sleep_family

```python
@sleep_family.setter
def sleep_family(value: SleepFamily) -> None
```

<a id="unreal.BodyInstance.use_ccd"></a>

#### use_ccd

```python
@property
def use_ccd() -> bool
```

(bool):  [Read-Only] If true Continuous Collision Detection (CCD) will be used for this component

<a id="unreal.BodyInstance.ignore_analytic_collisions"></a>

#### ignore_analytic_collisions

```python
@property
def ignore_analytic_collisions() -> bool
```

(bool):  [Read-Only] If true ignore analytic collisions and treat objects as a general implicit surface

<a id="unreal.BodyInstance.notify_rigid_body_collision"></a>

#### notify_rigid_body_collision

```python
@property
def notify_rigid_body_collision() -> bool
```

(bool):  [Read-Only] Should 'Hit' events fire when this object collides during physics simulation.

<a id="unreal.BodyInstance.smooth_edge_collisions"></a>

#### smooth_edge_collisions

```python
@property
def smooth_edge_collisions() -> bool
```

(bool):  [Read-Only] Remove unnecessary edge collisions to allow smooth sliding over surfaces composed of multiple actors/components.
This is fairly expensive and should only be enabled on hero objects.

<a id="unreal.BodyInstance.inertia_conditioning"></a>

#### inertia_conditioning

```python
@property
def inertia_conditioning() -> bool
```

(bool):  [Read-Write]
brief: Enable automatic inertia conditioning to stabilize constraints. Inertia conditioning increases inertia when an object is long and thin and also when it has joints that are outside the collision shapes of the body. Increasing the inertia reduces the amount of rotation applied at joints which helps stabilize joint chains, especially when bodies are small. In principle you can get the same behaviour by setting the InertiaTensorScale appropriately, but this takes some of the guesswork out of it.
note: This only changes the inertia used in the low-level solver. That inertia is not visible to the BodyInstance which will still report the inertia calculated from the mass, shapes, and InertiaTensorScale.
note: When enabled, the effective inertia depends on the joints attached to the body so the inertia will change when joints are added or removed (automatically - no user action required).

<a id="unreal.BodyInstance.inertia_conditioning"></a>

#### inertia_conditioning

```python
@inertia_conditioning.setter
def inertia_conditioning(value: bool) -> None
```

<a id="unreal.BodyInstance.one_way_interaction"></a>

#### one_way_interaction

```python
@property
def one_way_interaction() -> bool
```

(bool):  [Read-Write] If set to true, this body will treat bodies that do not have the flag set as having infinite mass

<a id="unreal.BodyInstance.one_way_interaction"></a>

#### one_way_interaction

```python
@one_way_interaction.setter
def one_way_interaction(value: bool) -> None
```

<a id="unreal.BodyInstance.override_solver_async_delta_time"></a>

#### override_solver_async_delta_time

```python
@property
def override_solver_async_delta_time() -> bool
```

(bool):  [Read-Only] Set the desired delta time for the body. *

<a id="unreal.BodyInstance.solver_async_delta_time"></a>

#### solver_async_delta_time

```python
@property
def solver_async_delta_time() -> float
```

(float):  [Read-Only] Override value for physics solver async delta time.  With multiple actors specifying this, the solver will use the smallest delta time *

<a id="unreal.BodyInstance.max_depenetration_velocity"></a>

#### max_depenetration_velocity

```python
@property
def max_depenetration_velocity() -> float
```

(float):  [Read-Only] The maximum velocity used to depenetrate this object from others when spawned or teleported with initial overlaps (does not affect overlaps as a result of normal movement).
A value of zero will allow objects that are spawned overlapping to go to sleep without moving rather than pop out of each other. E.g., use zero if you spawn dynamic rocks
partially embedded in the ground and want them to be interactive but not pop out of the ground when touched.
A negative value is equivalent to bOverrideMaxDepenetrationVelocity = false, meaning use the project setting.
This overrides the CollisionInitialOverlapDepenetrationVelocity project setting on a per-body basis (and not the MaxDepenetrationVelocity solver setting that will be deprecated).

<a id="unreal.BodyInstance.mass_in_kg_override"></a>

#### mass_in_kg_override

```python
@property
def mass_in_kg_override() -> float
```

(float):  [Read-Only] Mass of the body in KG. By default we compute this based on physical material and mass scale.
see: bOverrideMass to set this directly

<a id="unreal.BodyInstance.mass_in_kg"></a>

#### mass_in_kg

```python
@property
def mass_in_kg() -> float
```

deprecated: 'mass_in_kg' was renamed to 'mass_in_kg_override'.

<a id="unreal.BodyInstance.linear_damping"></a>

#### linear_damping

```python
@property
def linear_damping() -> float
```

(float):  [Read-Write] 'Drag' force added to reduce linear movement

<a id="unreal.BodyInstance.linear_damping"></a>

#### linear_damping

```python
@linear_damping.setter
def linear_damping(value: float) -> None
```

<a id="unreal.BodyInstance.angular_damping"></a>

#### angular_damping

```python
@property
def angular_damping() -> float
```

(float):  [Read-Write] 'Drag' force added to reduce angular movement

<a id="unreal.BodyInstance.angular_damping"></a>

#### angular_damping

```python
@angular_damping.setter
def angular_damping(value: float) -> None
```

<a id="unreal.BodyInstance.com_nudge"></a>

#### com_nudge

```python
@property
def com_nudge() -> Vector
```

(Vector):  [Read-Write] User specified offset for this object's Center of Mass. The offset is defined in bone space and will be added to the calculated location.

<a id="unreal.BodyInstance.com_nudge"></a>

#### com_nudge

```python
@com_nudge.setter
def com_nudge(value: Vector) -> None
```

<a id="unreal.BodyInstance.mass_scale"></a>

#### mass_scale

```python
@property
def mass_scale() -> float
```

(float):  [Read-Write] Per-instance scaling of mass

<a id="unreal.BodyInstance.mass_scale"></a>

#### mass_scale

```python
@mass_scale.setter
def mass_scale(value: float) -> None
```

<a id="unreal.BodyInstance.gravity_group_index"></a>

#### gravity_group_index

```python
@property
def gravity_group_index() -> int
```

(uint8):  [Read-Only] What gravity group the BI should use, which determines rate of acceleration

<a id="unreal.BodyInstance.inertia_tensor_scale"></a>

#### inertia_tensor_scale

```python
@property
def inertia_tensor_scale() -> Vector
```

(Vector):  [Read-Write] Per-instance scaling of inertia (bigger number means  it'll be harder to rotate)

<a id="unreal.BodyInstance.inertia_tensor_scale"></a>

#### inertia_tensor_scale

```python
@inertia_tensor_scale.setter
def inertia_tensor_scale(value: Vector) -> None
```

<a id="unreal.BodyInstance.walkable_slope_override"></a>

#### walkable_slope_override

```python
@property
def walkable_slope_override() -> WalkableSlopeOverride
```

(WalkableSlopeOverride):  [Read-Only] Custom walkable slope override setting for this instance.
see: GetWalkableSlopeOverride(), SetWalkableSlopeOverride()

<a id="unreal.BodyInstance.phys_material_override"></a>

#### phys_material_override

```python
@property
def phys_material_override() -> PhysicalMaterial
```

(PhysicalMaterial):  [Read-Only] Allows you to override the PhysicalMaterial to use for simple collision on this body.

<a id="unreal.BodyInstance.max_angular_velocity"></a>

#### max_angular_velocity

```python
@property
def max_angular_velocity() -> float
```

(float):  [Read-Only] The maximum angular velocity for this instance [degrees/s]

<a id="unreal.BodyInstance.custom_sleep_threshold_multiplier"></a>

#### custom_sleep_threshold_multiplier

```python
@property
def custom_sleep_threshold_multiplier() -> float
```

(float):  [Read-Only] If the SleepFamily is set to custom, multiply the natural sleep threshold by this amount. A higher number will cause the body to sleep sooner.

<a id="unreal.BodyInstance.stabilization_threshold_multiplier"></a>

#### stabilization_threshold_multiplier

```python
@property
def stabilization_threshold_multiplier() -> float
```

(float):  [Read-Only] Stabilization factor for this body if Physics stabilization is enabled. A higher number will cause more aggressive stabilization at the risk of loss of momentum at low speeds. A value of 0 will disable stabilization for this body.

<a id="unreal.CollisionResponseContainer"></a>