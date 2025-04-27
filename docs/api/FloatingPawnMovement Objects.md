## FloatingPawnMovement Objects

```python
class FloatingPawnMovement(PawnMovementComponent)
```

FloatingPawnMovement is a movement component that provides simple movement for any Pawn class.
Limits on speed and acceleration are provided, while gravity is not implemented.

Normally the root component of the owning actor is moved, however another component may be selected (see SetUpdatedComponent()).
During swept (non-teleporting) movement only collision of UpdatedComponent is considered, attached components will teleport to the end location ignoring collision.

**C++ Source:**

- **Module**: Engine
- **File**: FloatingPawnMovement.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``acceleration`` (float):  [Read-Write] Acceleration applied by input (rate of change of velocity)
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``auto_register_physics_volume_updates`` (bool):  [Read-Write] If true, then applies the value of bComponentShouldUpdatePhysicsVolume to the UpdatedComponent. If false, will not change bShouldUpdatePhysicsVolume on the UpdatedComponent at all.
  see: bComponentShouldUpdatePhysicsVolume
- ``auto_register_updated_component`` (bool):  [Read-Write] If true, registers the owner's Root component as the UpdatedComponent if there is not one currently assigned.
- ``auto_update_tick_registration`` (bool):  [Read-Write] If true, whenever the updated component is changed, this component will enable or disable its tick dependent on whether it has something to update.
  This will NOT enable tick at startup if bAutoActivate is false, because presumably you have a good reason for not wanting it to start ticking initially.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_should_update_physics_volume`` (bool):  [Read-Write] If true, enables bShouldUpdatePhysicsVolume on the UpdatedComponent during initialization from SetUpdatedComponent(), otherwise disables such updates.
  Only enabled if bAutoRegisterPhysicsVolumeUpdates is true.
  WARNING: UpdatePhysicsVolume is potentially expensive if overlap events are also *disabled* because it requires a separate query against all physics volumes in the world.
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``constrain_to_plane`` (bool):  [Read-Write] If true, movement will be constrained to a plane.
  see: PlaneConstraintNormal, PlaneConstraintOrigin, PlaneConstraintAxisSetting
- ``deceleration`` (float):  [Read-Write] Deceleration applied when there is no input (rate of change of velocity)
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``fixed_path_braking_distance`` (float):  [Read-Write]
  deprecated: FixedPathBrakingDistance is deprecated, please use NavMovementProperties.FixedPathBrakingDistance instead.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``max_speed`` (float):  [Read-Write] Maximum velocity magnitude allowed for the controlled Pawn.
- ``nav_agent_props`` (NavAgentProperties):  [Read-Write] Properties that define how the component can move.
- ``nav_movement_properties`` (NavMovementProperties):  [Read-Write]
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
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
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``snap_to_plane_at_start`` (bool):  [Read-Write] If true and plane constraints are enabled, then the updated component will be snapped to the plane when first attached.
- ``tick_before_owner`` (bool):  [Read-Write] If true, after registration we will add a tick dependency to tick before our owner (if we can both tick).
  This is important when our tick causes an update in the owner's position, so that when the owner ticks it uses the most recent position without lag.
  Disabling this can improve performance if both objects tick but the order of ticks doesn't matter.
- ``turning_boost`` (float):  [Read-Write] Setting affecting extra force applied when changing direction, making turns have less drift and become more responsive.
  Velocity magnitude is not allowed to increase, that only happens due to normal acceleration. It may decrease with large direction changes.
  Larger values apply extra force to reach the target direction more quickly, while a zero value disables any extra turn force.
- ``update_nav_agent_with_owners_collision`` (bool):  [Read-Write]
  deprecated: bUpdateNavAgentWithOwnersCollision is deprecated, please use NavMovementProperties.bUpdateNavAgentWithOwnersCollision instead.
- ``update_only_if_rendered`` (bool):  [Read-Write] If true, skips TickComponent() if UpdatedComponent was not recently rendered.
- ``updated_component`` (SceneComponent):  [Read-Write] The component we move and update.
  If this is null at startup and bAutoRegisterUpdatedComponent is true, the owning Actor's root component will automatically be set as our UpdatedComponent at startup.
  see: bAutoRegisterUpdatedComponent, SetUpdatedComponent(), UpdatedPrimitive
- ``updated_primitive`` (PrimitiveComponent):  [Read-Write] UpdatedComponent, cast as a UPrimitiveComponent. May be invalid if UpdatedComponent was null or not a UPrimitiveComponent.
- ``use_acceleration_for_paths`` (bool):  [Read-Write]
  deprecated: bUseAccelerationForPaths is deprecated, please use NavMovementProperties.bUseAccelerationForPaths instead.
- ``use_fixed_braking_distance_for_paths`` (bool):  [Read-Write]
  deprecated: bUseFixedBrakingDistanceForPaths is deprecated, please use NavMovementProperties.bUseFixedBrakingDistanceForPaths instead.
- ``velocity`` (Vector):  [Read-Write] Current velocity of updated component.

<a id="unreal.FloatingPawnMovement.max_speed"></a>

#### max_speed

```python
@property
def max_speed() -> float
```

(float):  [Read-Write] Maximum velocity magnitude allowed for the controlled Pawn.

<a id="unreal.FloatingPawnMovement.max_speed"></a>

#### max_speed

```python
@max_speed.setter
def max_speed(value: float) -> None
```

<a id="unreal.FloatingPawnMovement.acceleration"></a>

#### acceleration

```python
@property
def acceleration() -> float
```

(float):  [Read-Write] Acceleration applied by input (rate of change of velocity)

<a id="unreal.FloatingPawnMovement.acceleration"></a>

#### acceleration

```python
@acceleration.setter
def acceleration(value: float) -> None
```

<a id="unreal.FloatingPawnMovement.accel_rate"></a>

#### accel_rate

```python
@property
def accel_rate() -> float
```

deprecated: 'accel_rate' was renamed to 'acceleration'.

<a id="unreal.FloatingPawnMovement.accel_rate"></a>

#### accel_rate

```python
@accel_rate.setter
def accel_rate(value: float) -> None
```

<a id="unreal.FloatingPawnMovement.deceleration"></a>

#### deceleration

```python
@property
def deceleration() -> float
```

(float):  [Read-Write] Deceleration applied when there is no input (rate of change of velocity)

<a id="unreal.FloatingPawnMovement.deceleration"></a>

#### deceleration

```python
@deceleration.setter
def deceleration(value: float) -> None
```

<a id="unreal.FloatingPawnMovement.decel_rate"></a>

#### decel_rate

```python
@property
def decel_rate() -> float
```

deprecated: 'decel_rate' was renamed to 'deceleration'.

<a id="unreal.FloatingPawnMovement.decel_rate"></a>

#### decel_rate

```python
@decel_rate.setter
def decel_rate(value: float) -> None
```

<a id="unreal.FloatingPawnMovement.turning_boost"></a>

#### turning_boost

```python
@property
def turning_boost() -> float
```

(float):  [Read-Write] Setting affecting extra force applied when changing direction, making turns have less drift and become more responsive.
Velocity magnitude is not allowed to increase, that only happens due to normal acceleration. It may decrease with large direction changes.
Larger values apply extra force to reach the target direction more quickly, while a zero value disables any extra turn force.

<a id="unreal.FloatingPawnMovement.turning_boost"></a>

#### turning_boost

```python
@turning_boost.setter
def turning_boost(value: float) -> None
```

<a id="unreal.DefaultPawnMovement"></a>