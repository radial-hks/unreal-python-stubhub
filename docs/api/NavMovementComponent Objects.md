## NavMovementComponent Objects

```python
class NavMovementComponent(MovementComponent)
```

NavMovementComponent defines base functionality for MovementComponents that move any 'agent' that may be involved in AI pathfinding.

**C++ Source:**

- **Module**: Engine
- **File**: NavMovementComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

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
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``fixed_path_braking_distance`` (float):  [Read-Write]
  deprecated: FixedPathBrakingDistance is deprecated, please use NavMovementProperties.FixedPathBrakingDistance instead.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
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

<a id="unreal.NavMovementComponent.fixed_path_braking_distance"></a>

#### fixed_path_braking_distance

```python
@property
def fixed_path_braking_distance() -> float
```

(float):  [Read-Write]
deprecated: FixedPathBrakingDistance is deprecated, please use NavMovementProperties.FixedPathBrakingDistance instead.

<a id="unreal.NavMovementComponent.fixed_path_braking_distance"></a>

#### fixed_path_braking_distance

```python
@fixed_path_braking_distance.setter
def fixed_path_braking_distance(value: float) -> None
```

<a id="unreal.NavMovementComponent.update_nav_agent_with_owners_collision"></a>

#### update_nav_agent_with_owners_collision

```python
@property
def update_nav_agent_with_owners_collision() -> bool
```

(bool):  [Read-Write]
deprecated: bUpdateNavAgentWithOwnersCollision is deprecated, please use NavMovementProperties.bUpdateNavAgentWithOwnersCollision instead.

<a id="unreal.NavMovementComponent.update_nav_agent_with_owners_collision"></a>

#### update_nav_agent_with_owners_collision

```python
@update_nav_agent_with_owners_collision.setter
def update_nav_agent_with_owners_collision(value: bool) -> None
```

<a id="unreal.NavMovementComponent.use_acceleration_for_paths"></a>

#### use_acceleration_for_paths

```python
@property
def use_acceleration_for_paths() -> bool
```

(bool):  [Read-Write]
deprecated: bUseAccelerationForPaths is deprecated, please use NavMovementProperties.bUseAccelerationForPaths instead.

<a id="unreal.NavMovementComponent.use_acceleration_for_paths"></a>

#### use_acceleration_for_paths

```python
@use_acceleration_for_paths.setter
def use_acceleration_for_paths(value: bool) -> None
```

<a id="unreal.NavMovementComponent.use_fixed_braking_distance_for_paths"></a>

#### use_fixed_braking_distance_for_paths

```python
@property
def use_fixed_braking_distance_for_paths() -> bool
```

(bool):  [Read-Write]
deprecated: bUseFixedBrakingDistanceForPaths is deprecated, please use NavMovementProperties.bUseFixedBrakingDistanceForPaths instead.

<a id="unreal.NavMovementComponent.use_fixed_braking_distance_for_paths"></a>

#### use_fixed_braking_distance_for_paths

```python
@use_fixed_braking_distance_for_paths.setter
def use_fixed_braking_distance_for_paths(value: bool) -> None
```

<a id="unreal.NavMovementComponent.nav_agent_props"></a>

#### nav_agent_props

```python
@property
def nav_agent_props() -> NavAgentProperties
```

(NavAgentProperties):  [Read-Write] Properties that define how the component can move.

<a id="unreal.NavMovementComponent.nav_agent_props"></a>

#### nav_agent_props

```python
@nav_agent_props.setter
def nav_agent_props(value: NavAgentProperties) -> None
```

<a id="unreal.NavMovementComponent.is_swimming"></a>

#### is_swimming

```python
def is_swimming() -> bool
```

x.is_swimming() -> bool
Returns true if currently swimming (moving through a fluid volume)

Returns:
    bool:

<a id="unreal.NavMovementComponent.is_moving_on_ground"></a>

#### is_moving_on_ground

```python
def is_moving_on_ground() -> bool
```

x.is_moving_on_ground() -> bool
Returns true if currently moving on the ground (e.g. walking or driving)

Returns:
    bool:

<a id="unreal.NavMovementComponent.is_flying"></a>

#### is_flying

```python
def is_flying() -> bool
```

x.is_flying() -> bool
Returns true if currently flying (moving through a non-fluid volume without resting on the ground)

Returns:
    bool:

<a id="unreal.NavMovementComponent.is_falling"></a>

#### is_falling

```python
def is_falling() -> bool
```

x.is_falling() -> bool
Returns true if currently falling (not flying, in a non-fluid volume, and not on the ground)

Returns:
    bool:

<a id="unreal.NavMovementComponent.is_crouching"></a>

#### is_crouching

```python
def is_crouching() -> bool
```

x.is_crouching() -> bool
Returns true if currently crouching

Returns:
    bool:

<a id="unreal.NavMovementComponent.get_velocity_for_nav_movement"></a>

#### get_velocity_for_nav_movement

```python
def get_velocity_for_nav_movement() -> Vector
```

x.get_velocity_for_nav_movement() -> Vector
Get the current velocity of the movement component

Returns:
    Vector:

<a id="unreal.NavMovementComponent.stop_movement_keep_pathing"></a>

#### stop_movement_keep_pathing

```python
def stop_movement_keep_pathing() -> None
```

x.stop_movement_keep_pathing() -> None
Stops movement immediately (reset velocity) but keeps following current path

<a id="unreal.NavMovementComponent.stop_active_movement"></a>

#### stop_active_movement

```python
def stop_active_movement() -> None
```

x.stop_active_movement() -> None
Stops applying further movement (usually zeros acceleration).

<a id="unreal.NavMovementComponent.request_path_move"></a>

#### request_path_move

```python
def request_path_move(move_input: Vector) -> None
```

x.request_path_move(move_input) -> None
path following: request movement through a new move input (normal vector = full strength)

Args:
    move_input (Vector):

<a id="unreal.NavMovementComponent.request_direct_move"></a>

#### request_direct_move

```python
def request_direct_move(move_velocity: Vector, force_max_speed: bool) -> None
```

x.request_direct_move(move_velocity, force_max_speed) -> None
path following: request movement through a velocity directly

Args:
    move_velocity (Vector): 
    force_max_speed (bool):

<a id="unreal.NavMovementComponent.get_max_speed_for_nav_movement"></a>

#### get_max_speed_for_nav_movement

```python
def get_max_speed_for_nav_movement() -> float
```

x.get_max_speed_for_nav_movement() -> float
Get maximum movement speed of the agent

Returns:
    float:

<a id="unreal.PawnMovementComponent"></a>