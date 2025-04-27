## ProjectileMovementComponent Objects

```python
class ProjectileMovementComponent(MovementComponent)
```

ProjectileMovementComponent updates the position of another component during its tick.

Behavior such as bouncing after impacts and homing toward a target are supported.

Normally the root component of the owning actor is moved, however another component may be selected (see SetUpdatedComponent()).
If the updated component is simulating physics, only the initial launch parameters (when initial velocity is non-zero)
will affect the projectile, and the physics sim will take over from there.
see: UMovementComponent

**C++ Source:**

- **Module**: Engine
- **File**: ProjectileMovementComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``auto_register_physics_volume_updates`` (bool):  [Read-Write] If true, then applies the value of bComponentShouldUpdatePhysicsVolume to the UpdatedComponent. If false, will not change bShouldUpdatePhysicsVolume on the UpdatedComponent at all.
  see: bComponentShouldUpdatePhysicsVolume
- ``auto_register_updated_component`` (bool):  [Read-Write] If true, registers the owner's Root component as the UpdatedComponent if there is not one currently assigned.
- ``auto_update_tick_registration`` (bool):  [Read-Write] If true, whenever the updated component is changed, this component will enable or disable its tick dependent on whether it has something to update.
  This will NOT enable tick at startup if bAutoActivate is false, because presumably you have a good reason for not wanting it to start ticking initially.
- ``bounce_additional_iterations`` (int32):  [Read-Write] On the first few bounces (up to this amount), allow extra iterations over MaxSimulationIterations if necessary.
- ``bounce_angle_affects_friction`` (bool):  [Read-Write] Controls the effects of friction on velocity parallel to the impact surface when bouncing.
  If true, friction will be modified based on the angle of impact, making friction higher for perpendicular impacts and lower for glancing impacts.
  If false, a bounce will retain a proportion of tangential velocity equal to (1.0 - Friction), acting as a "horizontal restitution".
- ``bounce_velocity_stop_simulating_threshold`` (float):  [Read-Write] If velocity is below this threshold after a bounce, stops simulating and triggers the OnProjectileStop event.
  Ignored if bShouldBounce is false, in which case the projectile stops simulating on the first impact.
  see: StopSimulating(), OnProjectileStop
- ``bounciness`` (float):  [Read-Write] Percentage of velocity maintained after the bounce in the direction of the normal of impact (coefficient of restitution).
  1.0 = no velocity lost, 0.0 = no bounce. Ignored if bShouldBounce is false.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_should_update_physics_volume`` (bool):  [Read-Write] If true, enables bShouldUpdatePhysicsVolume on the UpdatedComponent during initialization from SetUpdatedComponent(), otherwise disables such updates.
  Only enabled if bAutoRegisterPhysicsVolumeUpdates is true.
  WARNING: UpdatePhysicsVolume is potentially expensive if overlap events are also *disabled* because it requires a separate query against all physics volumes in the world.
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``constrain_to_plane`` (bool):  [Read-Write] If true, movement will be constrained to a plane.
  see: PlaneConstraintNormal, PlaneConstraintOrigin, PlaneConstraintAxisSetting
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``force_sub_stepping`` (bool):  [Read-Write] If true, forces sub-stepping to break up movement into discrete smaller steps to improve accuracy of the trajectory.
  Objects that move in a straight line typically do *not* need to set this, as movement always uses continuous collision detection (sweeps) so collision is not missed.
  Sub-stepping is automatically enabled when under the effects of gravity or when homing towards a target.
  see: MaxSimulationTimeStep, MaxSimulationIterations
- ``friction`` (float):  [Read-Write] Coefficient of friction, affecting the resistance to sliding along a surface.
  Normal range is [0,1] : 0.0 = no friction, 1.0+ = very high friction.
  Also affects the percentage of velocity maintained after the bounce in the direction tangent to the normal of impact.
  Ignored if bShouldBounce is false.
  see: bBounceAngleAffectsFriction
- ``homing_acceleration_magnitude`` (float):  [Read-Write] The magnitude of our acceleration towards the homing target. Overall velocity magnitude will still be limited by MaxSpeed.
- ``homing_target_component`` (SceneComponent):  [Read-Only] The current target we are homing towards. Can only be set at runtime (when projectile is spawned or updating).
  see: bIsHomingProjectile
- ``initial_speed`` (float):  [Read-Write] Initial speed of projectile. If greater than zero, this will override the initial Velocity value and instead treat Velocity as a direction.
- ``initial_velocity_in_local_space`` (bool):  [Read-Write] If true, the initial Velocity is interpreted as being in local space upon startup.
  see: SetVelocityInLocalSpace()
- ``interp_location_max_lag_distance`` (float):  [Read-Write] Max distance behind UpdatedComponent which the interpolated component is allowed to lag.
- ``interp_location_snap_to_target_distance`` (float):  [Read-Write] Max distance behind UpdatedComponent beyond which the interpolated component is snapped to the target location instead.
  For instance if the target teleports this far beyond the interpolated component, the interpolation is snapped to match the target.
- ``interp_location_time`` (float):  [Read-Write] "Time" over which most of the location interpolation occurs, when the UpdatedComponent (target) moves ahead of the interpolated component.
  Since the implementation uses exponential lagged smoothing, this is a rough time value and experimentation should inform a final result.
  A value of zero is effectively instantaneous interpolation.
- ``interp_movement`` (bool):  [Read-Write] If true and there is an interpolated component set, location (and optionally rotation) interpolation is enabled which allows the interpolated object to smooth uneven updates
  of the UpdatedComponent's location (usually to smooth network updates). This requires using SetInterpolatedComponent() to indicate the visual component that lags behind the collision,
  and using MoveInterpolationTarget() when the new target location/rotation is received (usually on a net update).
  see: SetInterpolatedComponent(), MoveInterpolationTarget()
- ``interp_rotation`` (bool):  [Read-Write] If true and there is an interpolated component set, rotation interpolation is enabled which allows the interpolated object to smooth uneven updates
  of the UpdatedComponent's rotation (usually to smooth network updates).
  Rotation interpolation is *only* applied if bInterpMovement is also enabled.
  see: SetInterpolatedComponent(), MoveInterpolationTarget()
- ``interp_rotation_time`` (float):  [Read-Write] "Time" over which most of the rotation interpolation occurs, when the UpdatedComponent (target) moves ahead of the interpolated component.
  Since the implementation uses exponential lagged smoothing, this is a rough time value and experimentation should inform a final result.
  A value of zero is effectively instantaneous interpolation.
- ``interpolation_use_scoped_movement`` (bool):  [Read-Write] If true, uses FScopedMovementUpdate to avoid moving the attached interpolated object's children more than once during a tick when it would both interpolate and move during projectile simulation.
  This also defers overlap updates for the interpolated object until after the simulation update completes.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``is_homing_projectile`` (bool):  [Read-Write] If true, we will accelerate toward our homing target. HomingTargetComponent must be set after the projectile is spawned.
  see: HomingTargetComponent, HomingAccelerationMagnitude
- ``is_sliding`` (bool):  [Read-Only] If true, projectile is sliding / rolling along a surface.
- ``max_simulation_iterations`` (int32):  [Read-Write] Max number of iterations used for each discrete simulation step.
  Increasing this value can address precision issues with fast-moving objects or complex collision scenarios, at the cost of performance.

  WARNING: if (MaxSimulationTimeStep * MaxSimulationIterations) is too low for the min framerate, the last simulation step may exceed MaxSimulationTimeStep to complete the simulation.
  see: MaxSimulationTimeStep, bForceSubStepping
- ``max_simulation_time_step`` (float):  [Read-Write] Max time delta for each discrete simulation step.
  Lowering this value can address precision issues with fast-moving objects or complex collision scenarios, at the cost of performance.

  WARNING: if (MaxSimulationTimeStep * MaxSimulationIterations) is too low for the min framerate, the last simulation step may exceed MaxSimulationTimeStep to complete the simulation.
  see: MaxSimulationIterations, bForceSubStepping
- ``max_speed`` (float):  [Read-Write] Limit on speed of projectile (0 means no limit).
- ``min_friction_fraction`` (float):  [Read-Write] When bounce angle affects friction, apply at least this fraction of normal friction.
  Helps consistently slow objects sliding or rolling along surfaces or in valleys when the usual friction amount would take a very long time to settle.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``on_projectile_bounce`` (OnProjectileBounceDelegate):  [Read-Write] Called when projectile impacts something and bounces are enabled.
- ``on_projectile_stop`` (OnProjectileStopDelegate):  [Read-Write] Called when projectile has come to a stop (velocity is below simulation threshold, bounces are disabled, or it is forcibly stopped).
- ``plane_constraint_axis_setting`` (PlaneConstraintAxisSetting):  [Read-Write] Setting that controls behavior when movement is restricted to a 2D plane defined by a specific axis/normal,
  so that movement along the locked axis is not be possible.
  see: SetPlaneConstraintAxisSetting
- ``plane_constraint_normal`` (Vector):  [Read-Write] The normal or axis of the plane that constrains movement, if bConstrainToPlane is enabled.
  If for example you wanted to constrain movement to the X-Z plane (so that Y cannot change), the normal would be set to X=0 Y=1 Z=0.
  This is recalculated whenever PlaneConstraintAxisSetting changes. It is normalized once the component is registered with the game world.
  see: bConstrainToPlane, SetPlaneConstraintNormal(), SetPlaneConstraintFromVectors()
- ``plane_constraint_origin`` (Vector):  [Read-Write] The origin of the plane that constrains movement, if plane constraint is enabled.
  This defines the behavior of snapping a position to the plane, such as by SnapUpdatedComponentToPlane().
  see: bConstrainToPlane, SetPlaneConstraintOrigin().
- ``previous_hit_normal`` (Vector):  [Read-Only] Saved HitResult Normal from previous simulation step that resulted in an impact. If PreviousHitTime is 1.0, then the hit was not in the last step.
- ``previous_hit_time`` (float):  [Read-Only] Saved HitResult Time (0 to 1) from previous simulation step. Equal to 1.0 when there was no impact.
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``projectile_gravity_scale`` (float):  [Read-Write] Custom gravity scale for this projectile. Set to 0 for no gravity.
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``rotation_follows_velocity`` (bool):  [Read-Write] If true, this projectile will have its rotation updated each frame to match the direction of its velocity.
- ``rotation_remains_vertical`` (bool):  [Read-Write] If true, this projectile will have its rotation updated each frame to maintain the rotations Yaw only. (bRotationFollowsVelocity is required to be true)
- ``should_bounce`` (bool):  [Read-Write] If true, simple bounces will be simulated. Set this to false to stop simulating on contact.
- ``simulation_enabled`` (bool):  [Read-Write] If true, does normal simulation ticking and update. If false, simulation is halted, but component will still tick (allowing interpolation to run).
- ``simulation_use_scoped_movement`` (bool):  [Read-Write] If true, uses FScopedMovementUpdate to avoid moving the UpdatedComponent more than once during a tick during simulation.
  This also defers overlap updates and some impact events until after the simulation update completes, so it may delay important events and continue deflection, so use with caution.
- ``snap_to_plane_at_start`` (bool):  [Read-Write] If true and plane constraints are enabled, then the updated component will be snapped to the plane when first attached.
- ``sweep_collision`` (bool):  [Read-Write] If true, movement uses swept collision checks.
  If false, collision effectively teleports to the destination. Note that when this is disabled, movement will never generate blocking collision hits (though overlaps will be updated).
- ``throttle_interpolation`` (bool):  [Read-Write] If true, throttle interpolation when not relevant.
  see: ThrottleInterpolationSkipFramesNotRecent, ThrottleInterpolationSkipFramesRecent, ThrottleInterpolationThresholdNotRenderedShortTime, ThrottleInterpolationThresholdNotRenderedLongTime
- ``throttle_interpolation_skip_frames_not_recent`` (int32):  [Read-Write] When not recently relevant, skip this many frames of interpolation if throttling is enabled.
- ``throttle_interpolation_skip_frames_recent`` (int32):  [Read-Write] When recently relevant, skip this many frames of interpolation if throttling is enabled.
- ``throttle_interpolation_threshold_not_rendered_long_time`` (float):  [Read-Write] Time after not rendered for a long time when we consider throttling interpolation.
- ``throttle_interpolation_threshold_not_rendered_short_time`` (float):  [Read-Write] Time after not rendered recently when we consider throttling interpolation.
- ``tick_before_owner`` (bool):  [Read-Write] If true, after registration we will add a tick dependency to tick before our owner (if we can both tick).
  This is important when our tick causes an update in the owner's position, so that when the owner ticks it uses the most recent position without lag.
  Disabling this can improve performance if both objects tick but the order of ticks doesn't matter.
- ``update_only_if_rendered`` (bool):  [Read-Write] If true, skips TickComponent() if UpdatedComponent was not recently rendered.
- ``updated_component`` (SceneComponent):  [Read-Write] The component we move and update.
  If this is null at startup and bAutoRegisterUpdatedComponent is true, the owning Actor's root component will automatically be set as our UpdatedComponent at startup.
  see: bAutoRegisterUpdatedComponent, SetUpdatedComponent(), UpdatedPrimitive
- ``updated_primitive`` (PrimitiveComponent):  [Read-Write] UpdatedComponent, cast as a UPrimitiveComponent. May be invalid if UpdatedComponent was null or not a UPrimitiveComponent.
- ``velocity`` (Vector):  [Read-Write] Current velocity of updated component.

<a id="unreal.ProjectileMovementComponent.initial_speed"></a>

#### initial_speed

```python
@property
def initial_speed() -> float
```

(float):  [Read-Write] Initial speed of projectile. If greater than zero, this will override the initial Velocity value and instead treat Velocity as a direction.

<a id="unreal.ProjectileMovementComponent.initial_speed"></a>

#### initial_speed

```python
@initial_speed.setter
def initial_speed(value: float) -> None
```

<a id="unreal.ProjectileMovementComponent.speed"></a>

#### speed

```python
@property
def speed() -> float
```

deprecated: 'speed' was renamed to 'initial_speed'.

<a id="unreal.ProjectileMovementComponent.speed"></a>

#### speed

```python
@speed.setter
def speed(value: float) -> None
```

<a id="unreal.ProjectileMovementComponent.max_speed"></a>

#### max_speed

```python
@property
def max_speed() -> float
```

(float):  [Read-Write] Limit on speed of projectile (0 means no limit).

<a id="unreal.ProjectileMovementComponent.max_speed"></a>

#### max_speed

```python
@max_speed.setter
def max_speed(value: float) -> None
```

<a id="unreal.ProjectileMovementComponent.rotation_follows_velocity"></a>

#### rotation_follows_velocity

```python
@property
def rotation_follows_velocity() -> bool
```

(bool):  [Read-Write] If true, this projectile will have its rotation updated each frame to match the direction of its velocity.

<a id="unreal.ProjectileMovementComponent.rotation_follows_velocity"></a>

#### rotation_follows_velocity

```python
@rotation_follows_velocity.setter
def rotation_follows_velocity(value: bool) -> None
```

<a id="unreal.ProjectileMovementComponent.rotation_remains_vertical"></a>

#### rotation_remains_vertical

```python
@property
def rotation_remains_vertical() -> bool
```

(bool):  [Read-Write] If true, this projectile will have its rotation updated each frame to maintain the rotations Yaw only. (bRotationFollowsVelocity is required to be true)

<a id="unreal.ProjectileMovementComponent.rotation_remains_vertical"></a>

#### rotation_remains_vertical

```python
@rotation_remains_vertical.setter
def rotation_remains_vertical(value: bool) -> None
```

<a id="unreal.ProjectileMovementComponent.should_bounce"></a>

#### should_bounce

```python
@property
def should_bounce() -> bool
```

(bool):  [Read-Write] If true, simple bounces will be simulated. Set this to false to stop simulating on contact.

<a id="unreal.ProjectileMovementComponent.should_bounce"></a>

#### should_bounce

```python
@should_bounce.setter
def should_bounce(value: bool) -> None
```

<a id="unreal.ProjectileMovementComponent.initial_velocity_in_local_space"></a>

#### initial_velocity_in_local_space

```python
@property
def initial_velocity_in_local_space() -> bool
```

(bool):  [Read-Write] If true, the initial Velocity is interpreted as being in local space upon startup.
see: SetVelocityInLocalSpace()

<a id="unreal.ProjectileMovementComponent.initial_velocity_in_local_space"></a>

#### initial_velocity_in_local_space

```python
@initial_velocity_in_local_space.setter
def initial_velocity_in_local_space(value: bool) -> None
```

<a id="unreal.ProjectileMovementComponent.force_sub_stepping"></a>

#### force_sub_stepping

```python
@property
def force_sub_stepping() -> bool
```

(bool):  [Read-Write] If true, forces sub-stepping to break up movement into discrete smaller steps to improve accuracy of the trajectory.
Objects that move in a straight line typically do *not* need to set this, as movement always uses continuous collision detection (sweeps) so collision is not missed.
Sub-stepping is automatically enabled when under the effects of gravity or when homing towards a target.
see: MaxSimulationTimeStep, MaxSimulationIterations

<a id="unreal.ProjectileMovementComponent.force_sub_stepping"></a>

#### force_sub_stepping

```python
@force_sub_stepping.setter
def force_sub_stepping(value: bool) -> None
```

<a id="unreal.ProjectileMovementComponent.simulation_enabled"></a>

#### simulation_enabled

```python
@property
def simulation_enabled() -> bool
```

(bool):  [Read-Write] If true, does normal simulation ticking and update. If false, simulation is halted, but component will still tick (allowing interpolation to run).

<a id="unreal.ProjectileMovementComponent.simulation_enabled"></a>

#### simulation_enabled

```python
@simulation_enabled.setter
def simulation_enabled(value: bool) -> None
```

<a id="unreal.ProjectileMovementComponent.sweep_collision"></a>

#### sweep_collision

```python
@property
def sweep_collision() -> bool
```

(bool):  [Read-Write] If true, movement uses swept collision checks.
If false, collision effectively teleports to the destination. Note that when this is disabled, movement will never generate blocking collision hits (though overlaps will be updated).

<a id="unreal.ProjectileMovementComponent.sweep_collision"></a>

#### sweep_collision

```python
@sweep_collision.setter
def sweep_collision(value: bool) -> None
```

<a id="unreal.ProjectileMovementComponent.is_homing_projectile"></a>

#### is_homing_projectile

```python
@property
def is_homing_projectile() -> bool
```

(bool):  [Read-Write] If true, we will accelerate toward our homing target. HomingTargetComponent must be set after the projectile is spawned.
see: HomingTargetComponent, HomingAccelerationMagnitude

<a id="unreal.ProjectileMovementComponent.is_homing_projectile"></a>

#### is_homing_projectile

```python
@is_homing_projectile.setter
def is_homing_projectile(value: bool) -> None
```

<a id="unreal.ProjectileMovementComponent.bounce_angle_affects_friction"></a>

#### bounce_angle_affects_friction

```python
@property
def bounce_angle_affects_friction() -> bool
```

(bool):  [Read-Write] Controls the effects of friction on velocity parallel to the impact surface when bouncing.
If true, friction will be modified based on the angle of impact, making friction higher for perpendicular impacts and lower for glancing impacts.
If false, a bounce will retain a proportion of tangential velocity equal to (1.0 - Friction), acting as a "horizontal restitution".

<a id="unreal.ProjectileMovementComponent.bounce_angle_affects_friction"></a>

#### bounce_angle_affects_friction

```python
@bounce_angle_affects_friction.setter
def bounce_angle_affects_friction(value: bool) -> None
```

<a id="unreal.ProjectileMovementComponent.is_sliding"></a>

#### is_sliding

```python
@property
def is_sliding() -> bool
```

(bool):  [Read-Only] If true, projectile is sliding / rolling along a surface.

<a id="unreal.ProjectileMovementComponent.interp_movement"></a>

#### interp_movement

```python
@property
def interp_movement() -> bool
```

(bool):  [Read-Write] If true and there is an interpolated component set, location (and optionally rotation) interpolation is enabled which allows the interpolated object to smooth uneven updates
of the UpdatedComponent's location (usually to smooth network updates). This requires using SetInterpolatedComponent() to indicate the visual component that lags behind the collision,
and using MoveInterpolationTarget() when the new target location/rotation is received (usually on a net update).
see: SetInterpolatedComponent(), MoveInterpolationTarget()

<a id="unreal.ProjectileMovementComponent.interp_movement"></a>

#### interp_movement

```python
@interp_movement.setter
def interp_movement(value: bool) -> None
```

<a id="unreal.ProjectileMovementComponent.interp_rotation"></a>

#### interp_rotation

```python
@property
def interp_rotation() -> bool
```

(bool):  [Read-Write] If true and there is an interpolated component set, rotation interpolation is enabled which allows the interpolated object to smooth uneven updates
of the UpdatedComponent's rotation (usually to smooth network updates).
Rotation interpolation is *only* applied if bInterpMovement is also enabled.
see: SetInterpolatedComponent(), MoveInterpolationTarget()

<a id="unreal.ProjectileMovementComponent.interp_rotation"></a>

#### interp_rotation

```python
@interp_rotation.setter
def interp_rotation(value: bool) -> None
```

<a id="unreal.ProjectileMovementComponent.throttle_interpolation"></a>

#### throttle_interpolation

```python
@property
def throttle_interpolation() -> bool
```

(bool):  [Read-Write] If true, throttle interpolation when not relevant.
see: ThrottleInterpolationSkipFramesNotRecent, ThrottleInterpolationSkipFramesRecent, ThrottleInterpolationThresholdNotRenderedShortTime, ThrottleInterpolationThresholdNotRenderedLongTime

<a id="unreal.ProjectileMovementComponent.throttle_interpolation"></a>

#### throttle_interpolation

```python
@throttle_interpolation.setter
def throttle_interpolation(value: bool) -> None
```

<a id="unreal.ProjectileMovementComponent.simulation_use_scoped_movement"></a>

#### simulation_use_scoped_movement

```python
@property
def simulation_use_scoped_movement() -> bool
```

(bool):  [Read-Write] If true, uses FScopedMovementUpdate to avoid moving the UpdatedComponent more than once during a tick during simulation.
This also defers overlap updates and some impact events until after the simulation update completes, so it may delay important events and continue deflection, so use with caution.

<a id="unreal.ProjectileMovementComponent.simulation_use_scoped_movement"></a>

#### simulation_use_scoped_movement

```python
@simulation_use_scoped_movement.setter
def simulation_use_scoped_movement(value: bool) -> None
```

<a id="unreal.ProjectileMovementComponent.interpolation_use_scoped_movement"></a>

#### interpolation_use_scoped_movement

```python
@property
def interpolation_use_scoped_movement() -> bool
```

(bool):  [Read-Write] If true, uses FScopedMovementUpdate to avoid moving the attached interpolated object's children more than once during a tick when it would both interpolate and move during projectile simulation.
This also defers overlap updates for the interpolated object until after the simulation update completes.

<a id="unreal.ProjectileMovementComponent.interpolation_use_scoped_movement"></a>

#### interpolation_use_scoped_movement

```python
@interpolation_use_scoped_movement.setter
def interpolation_use_scoped_movement(value: bool) -> None
```

<a id="unreal.ProjectileMovementComponent.previous_hit_time"></a>

#### previous_hit_time

```python
@property
def previous_hit_time() -> float
```

(float):  [Read-Only] Saved HitResult Time (0 to 1) from previous simulation step. Equal to 1.0 when there was no impact.

<a id="unreal.ProjectileMovementComponent.previous_hit_normal"></a>

#### previous_hit_normal

```python
@property
def previous_hit_normal() -> Vector
```

(Vector):  [Read-Only] Saved HitResult Normal from previous simulation step that resulted in an impact. If PreviousHitTime is 1.0, then the hit was not in the last step.

<a id="unreal.ProjectileMovementComponent.projectile_gravity_scale"></a>

#### projectile_gravity_scale

```python
@property
def projectile_gravity_scale() -> float
```

(float):  [Read-Write] Custom gravity scale for this projectile. Set to 0 for no gravity.

<a id="unreal.ProjectileMovementComponent.projectile_gravity_scale"></a>

#### projectile_gravity_scale

```python
@projectile_gravity_scale.setter
def projectile_gravity_scale(value: float) -> None
```

<a id="unreal.ProjectileMovementComponent.bounciness"></a>

#### bounciness

```python
@property
def bounciness() -> float
```

(float):  [Read-Write] Percentage of velocity maintained after the bounce in the direction of the normal of impact (coefficient of restitution).
1.0 = no velocity lost, 0.0 = no bounce. Ignored if bShouldBounce is false.

<a id="unreal.ProjectileMovementComponent.bounciness"></a>

#### bounciness

```python
@bounciness.setter
def bounciness(value: float) -> None
```

<a id="unreal.ProjectileMovementComponent.friction"></a>

#### friction

```python
@property
def friction() -> float
```

(float):  [Read-Write] Coefficient of friction, affecting the resistance to sliding along a surface.
Normal range is [0,1] : 0.0 = no friction, 1.0+ = very high friction.
Also affects the percentage of velocity maintained after the bounce in the direction tangent to the normal of impact.
Ignored if bShouldBounce is false.
see: bBounceAngleAffectsFriction

<a id="unreal.ProjectileMovementComponent.friction"></a>

#### friction

```python
@friction.setter
def friction(value: float) -> None
```

<a id="unreal.ProjectileMovementComponent.bounce_velocity_stop_simulating_threshold"></a>

#### bounce_velocity_stop_simulating_threshold

```python
@property
def bounce_velocity_stop_simulating_threshold() -> float
```

(float):  [Read-Write] If velocity is below this threshold after a bounce, stops simulating and triggers the OnProjectileStop event.
Ignored if bShouldBounce is false, in which case the projectile stops simulating on the first impact.
see: StopSimulating(), OnProjectileStop

<a id="unreal.ProjectileMovementComponent.bounce_velocity_stop_simulating_threshold"></a>

#### bounce_velocity_stop_simulating_threshold

```python
@bounce_velocity_stop_simulating_threshold.setter
def bounce_velocity_stop_simulating_threshold(value: float) -> None
```

<a id="unreal.ProjectileMovementComponent.min_friction_fraction"></a>

#### min_friction_fraction

```python
@property
def min_friction_fraction() -> float
```

(float):  [Read-Write] When bounce angle affects friction, apply at least this fraction of normal friction.
Helps consistently slow objects sliding or rolling along surfaces or in valleys when the usual friction amount would take a very long time to settle.

<a id="unreal.ProjectileMovementComponent.min_friction_fraction"></a>

#### min_friction_fraction

```python
@min_friction_fraction.setter
def min_friction_fraction(value: float) -> None
```

<a id="unreal.ProjectileMovementComponent.on_projectile_bounce"></a>

#### on_projectile_bounce

```python
@property
def on_projectile_bounce() -> OnProjectileBounceDelegate
```

(OnProjectileBounceDelegate):  [Read-Write] Called when projectile impacts something and bounces are enabled.

<a id="unreal.ProjectileMovementComponent.on_projectile_bounce"></a>

#### on_projectile_bounce

```python
@on_projectile_bounce.setter
def on_projectile_bounce(value: OnProjectileBounceDelegate) -> None
```

<a id="unreal.ProjectileMovementComponent.on_projectile_stop"></a>

#### on_projectile_stop

```python
@property
def on_projectile_stop() -> OnProjectileStopDelegate
```

(OnProjectileStopDelegate):  [Read-Write] Called when projectile has come to a stop (velocity is below simulation threshold, bounces are disabled, or it is forcibly stopped).

<a id="unreal.ProjectileMovementComponent.on_projectile_stop"></a>

#### on_projectile_stop

```python
@on_projectile_stop.setter
def on_projectile_stop(value: OnProjectileStopDelegate) -> None
```

<a id="unreal.ProjectileMovementComponent.homing_acceleration_magnitude"></a>

#### homing_acceleration_magnitude

```python
@property
def homing_acceleration_magnitude() -> float
```

(float):  [Read-Write] The magnitude of our acceleration towards the homing target. Overall velocity magnitude will still be limited by MaxSpeed.

<a id="unreal.ProjectileMovementComponent.homing_acceleration_magnitude"></a>

#### homing_acceleration_magnitude

```python
@homing_acceleration_magnitude.setter
def homing_acceleration_magnitude(value: float) -> None
```

<a id="unreal.ProjectileMovementComponent.homing_target_component"></a>

#### homing_target_component

```python
@property
def homing_target_component() -> SceneComponent
```

(SceneComponent):  [Read-Only] The current target we are homing towards. Can only be set at runtime (when projectile is spawned or updating).
see: bIsHomingProjectile

<a id="unreal.ProjectileMovementComponent.max_simulation_time_step"></a>

#### max_simulation_time_step

```python
@property
def max_simulation_time_step() -> float
```

(float):  [Read-Write] Max time delta for each discrete simulation step.
Lowering this value can address precision issues with fast-moving objects or complex collision scenarios, at the cost of performance.

WARNING: if (MaxSimulationTimeStep * MaxSimulationIterations) is too low for the min framerate, the last simulation step may exceed MaxSimulationTimeStep to complete the simulation.
see: MaxSimulationIterations, bForceSubStepping

<a id="unreal.ProjectileMovementComponent.max_simulation_time_step"></a>

#### max_simulation_time_step

```python
@max_simulation_time_step.setter
def max_simulation_time_step(value: float) -> None
```

<a id="unreal.ProjectileMovementComponent.max_simulation_iterations"></a>

#### max_simulation_iterations

```python
@property
def max_simulation_iterations() -> int
```

(int32):  [Read-Write] Max number of iterations used for each discrete simulation step.
Increasing this value can address precision issues with fast-moving objects or complex collision scenarios, at the cost of performance.

WARNING: if (MaxSimulationTimeStep * MaxSimulationIterations) is too low for the min framerate, the last simulation step may exceed MaxSimulationTimeStep to complete the simulation.
see: MaxSimulationTimeStep, bForceSubStepping

<a id="unreal.ProjectileMovementComponent.max_simulation_iterations"></a>

#### max_simulation_iterations

```python
@max_simulation_iterations.setter
def max_simulation_iterations(value: int) -> None
```

<a id="unreal.ProjectileMovementComponent.bounce_additional_iterations"></a>

#### bounce_additional_iterations

```python
@property
def bounce_additional_iterations() -> int
```

(int32):  [Read-Write] On the first few bounces (up to this amount), allow extra iterations over MaxSimulationIterations if necessary.

<a id="unreal.ProjectileMovementComponent.bounce_additional_iterations"></a>

#### bounce_additional_iterations

```python
@bounce_additional_iterations.setter
def bounce_additional_iterations(value: int) -> None
```

<a id="unreal.ProjectileMovementComponent.interp_location_time"></a>

#### interp_location_time

```python
@property
def interp_location_time() -> float
```

(float):  [Read-Write] "Time" over which most of the location interpolation occurs, when the UpdatedComponent (target) moves ahead of the interpolated component.
Since the implementation uses exponential lagged smoothing, this is a rough time value and experimentation should inform a final result.
A value of zero is effectively instantaneous interpolation.

<a id="unreal.ProjectileMovementComponent.interp_location_time"></a>

#### interp_location_time

```python
@interp_location_time.setter
def interp_location_time(value: float) -> None
```

<a id="unreal.ProjectileMovementComponent.interp_rotation_time"></a>

#### interp_rotation_time

```python
@property
def interp_rotation_time() -> float
```

(float):  [Read-Write] "Time" over which most of the rotation interpolation occurs, when the UpdatedComponent (target) moves ahead of the interpolated component.
Since the implementation uses exponential lagged smoothing, this is a rough time value and experimentation should inform a final result.
A value of zero is effectively instantaneous interpolation.

<a id="unreal.ProjectileMovementComponent.interp_rotation_time"></a>

#### interp_rotation_time

```python
@interp_rotation_time.setter
def interp_rotation_time(value: float) -> None
```

<a id="unreal.ProjectileMovementComponent.interp_location_max_lag_distance"></a>

#### interp_location_max_lag_distance

```python
@property
def interp_location_max_lag_distance() -> float
```

(float):  [Read-Write] Max distance behind UpdatedComponent which the interpolated component is allowed to lag.

<a id="unreal.ProjectileMovementComponent.interp_location_max_lag_distance"></a>

#### interp_location_max_lag_distance

```python
@interp_location_max_lag_distance.setter
def interp_location_max_lag_distance(value: float) -> None
```

<a id="unreal.ProjectileMovementComponent.interp_location_snap_to_target_distance"></a>

#### interp_location_snap_to_target_distance

```python
@property
def interp_location_snap_to_target_distance() -> float
```

(float):  [Read-Write] Max distance behind UpdatedComponent beyond which the interpolated component is snapped to the target location instead.
For instance if the target teleports this far beyond the interpolated component, the interpolation is snapped to match the target.

<a id="unreal.ProjectileMovementComponent.interp_location_snap_to_target_distance"></a>

#### interp_location_snap_to_target_distance

```python
@interp_location_snap_to_target_distance.setter
def interp_location_snap_to_target_distance(value: float) -> None
```

<a id="unreal.ProjectileMovementComponent.throttle_interpolation_threshold_not_rendered_short_time"></a>

#### throttle_interpolation_threshold_not_rendered_short_time

```python
@property
def throttle_interpolation_threshold_not_rendered_short_time() -> float
```

(float):  [Read-Write] Time after not rendered recently when we consider throttling interpolation.

<a id="unreal.ProjectileMovementComponent.throttle_interpolation_threshold_not_rendered_short_time"></a>

#### throttle_interpolation_threshold_not_rendered_short_time

```python
@throttle_interpolation_threshold_not_rendered_short_time.setter
def throttle_interpolation_threshold_not_rendered_short_time(
        value: float) -> None
```

<a id="unreal.ProjectileMovementComponent.throttle_interpolation_threshold_not_rendered_long_time"></a>

#### throttle_interpolation_threshold_not_rendered_long_time

```python
@property
def throttle_interpolation_threshold_not_rendered_long_time() -> float
```

(float):  [Read-Write] Time after not rendered for a long time when we consider throttling interpolation.

<a id="unreal.ProjectileMovementComponent.throttle_interpolation_threshold_not_rendered_long_time"></a>

#### throttle_interpolation_threshold_not_rendered_long_time

```python
@throttle_interpolation_threshold_not_rendered_long_time.setter
def throttle_interpolation_threshold_not_rendered_long_time(
        value: float) -> None
```

<a id="unreal.ProjectileMovementComponent.throttle_interpolation_skip_frames_recent"></a>

#### throttle_interpolation_skip_frames_recent

```python
@property
def throttle_interpolation_skip_frames_recent() -> int
```

(int32):  [Read-Write] When recently relevant, skip this many frames of interpolation if throttling is enabled.

<a id="unreal.ProjectileMovementComponent.throttle_interpolation_skip_frames_recent"></a>

#### throttle_interpolation_skip_frames_recent

```python
@throttle_interpolation_skip_frames_recent.setter
def throttle_interpolation_skip_frames_recent(value: int) -> None
```

<a id="unreal.ProjectileMovementComponent.throttle_interpolation_skip_frames_not_recent"></a>

#### throttle_interpolation_skip_frames_not_recent

```python
@property
def throttle_interpolation_skip_frames_not_recent() -> int
```

(int32):  [Read-Write] When not recently relevant, skip this many frames of interpolation if throttling is enabled.

<a id="unreal.ProjectileMovementComponent.throttle_interpolation_skip_frames_not_recent"></a>

#### throttle_interpolation_skip_frames_not_recent

```python
@throttle_interpolation_skip_frames_not_recent.setter
def throttle_interpolation_skip_frames_not_recent(value: int) -> None
```

<a id="unreal.ProjectileMovementComponent.stop_simulating"></a>

#### stop_simulating

```python
def stop_simulating(hit_result: HitResult) -> None
```

x.stop_simulating(hit_result) -> None
Clears the reference to UpdatedComponent, fires stop event (OnProjectileStop), and stops ticking (if bAutoUpdateTickRegistration is true).

Args:
    hit_result (HitResult):

<a id="unreal.ProjectileMovementComponent.stop_movement"></a>

#### stop_movement

```python
def stop_movement(hit_result: HitResult) -> None
```

deprecated: 'stop_movement' was renamed to 'stop_simulating'.

<a id="unreal.ProjectileMovementComponent.set_velocity_in_local_space"></a>

#### set_velocity_in_local_space

```python
def set_velocity_in_local_space(new_velocity: Vector) -> None
```

x.set_velocity_in_local_space(new_velocity) -> None
Sets the velocity to the new value, rotated into Actor space.

Args:
    new_velocity (Vector):

<a id="unreal.ProjectileMovementComponent.set_interpolated_component"></a>

#### set_interpolated_component

```python
def set_interpolated_component(component: SceneComponent) -> None
```

x.set_interpolated_component(component) -> None
Assigns the component that will be used for network interpolation/smoothing. It is expected that this is a component attached somewhere below the UpdatedComponent.
When network updates use MoveInterpolationTarget() to move the UpdatedComponent, the interpolated component's relative offset will be maintained and smoothed over
the course of future component ticks. The current relative location and rotation of the component is saved as the target offset for future interpolation.
see: MoveInterpolationTarget(), bInterpMovement, bInterpRotation

Args:
    component (SceneComponent):

<a id="unreal.ProjectileMovementComponent.reset_interpolation"></a>

#### reset_interpolation

```python
def reset_interpolation() -> None
```

x.reset_interpolation() -> None
Resets interpolation so that interpolated component snaps back to the initial location/rotation without any additional offsets.

<a id="unreal.ProjectileMovementComponent.move_interpolation_target"></a>

#### move_interpolation_target

```python
def move_interpolation_target(new_location: Vector,
                              new_rotation: Rotator) -> None
```

x.move_interpolation_target(new_location, new_rotation) -> None
Moves the UpdatedComponent, which is also the interpolation target for the interpolated component. If there is not interpolated component, this simply moves UpdatedComponent.
Use this typically from PostNetReceiveLocationAndRotation() or similar from an Actor.

Args:
    new_location (Vector): 
    new_rotation (Rotator):

<a id="unreal.ProjectileMovementComponent.limit_velocity"></a>

#### limit_velocity

```python
def limit_velocity(new_velocity: Vector) -> Vector
```

x.limit_velocity(new_velocity) -> Vector
Don't allow velocity magnitude to exceed MaxSpeed, if MaxSpeed is non-zero.

Args:
    new_velocity (Vector): 

Returns:
    Vector:

<a id="unreal.ProjectileMovementComponent.is_velocity_under_simulation_threshold"></a>

#### is_velocity_under_simulation_threshold

```python
def is_velocity_under_simulation_threshold() -> bool
```

x.is_velocity_under_simulation_threshold() -> bool
Returns true if velocity magnitude is less than BounceVelocityStopSimulatingThreshold.

Returns:
    bool:

<a id="unreal.ProjectileMovementComponent.is_interpolation_complete"></a>

#### is_interpolation_complete

```python
def is_interpolation_complete() -> bool
```

x.is_interpolation_complete() -> bool
Returns whether interpolation is complete because the target has been reached. True when interpolation is disabled.

Returns:
    bool:

<a id="unreal.MovementComp_Projectile"></a>