## MovementComponent Objects

```python
class MovementComponent(ActorComponent)
```

MovementComponent is an abstract component class that defines functionality for moving a PrimitiveComponent (our UpdatedComponent) each tick.
Base functionality includes:
   - Restricting movement to a plane or axis.
   - Utility functions for special handling of collision results (SlideAlongSurface(), ComputeSlideVector(), TwoWallAdjust()).
   - Utility functions for moving when there may be initial penetration (SafeMoveUpdatedComponent(), ResolvePenetration()).
   - Automatically registering the component tick and finding a component to move on the owning Actor.
Normally the root component of the owning actor is moved, however another component may be selected (see SetUpdatedComponent()).
During swept (non-teleporting) movement only collision of UpdatedComponent is considered, attached components will teleport to the end location ignoring collision.

**C++ Source:**

- **Module**: Engine
- **File**: MovementComponent.h

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
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
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
- ``update_only_if_rendered`` (bool):  [Read-Write] If true, skips TickComponent() if UpdatedComponent was not recently rendered.
- ``updated_component`` (SceneComponent):  [Read-Write] The component we move and update.
  If this is null at startup and bAutoRegisterUpdatedComponent is true, the owning Actor's root component will automatically be set as our UpdatedComponent at startup.
  see: bAutoRegisterUpdatedComponent, SetUpdatedComponent(), UpdatedPrimitive
- ``updated_primitive`` (PrimitiveComponent):  [Read-Write] UpdatedComponent, cast as a UPrimitiveComponent. May be invalid if UpdatedComponent was null or not a UPrimitiveComponent.
- ``velocity`` (Vector):  [Read-Write] Current velocity of updated component.

<a id="unreal.MovementComponent.updated_component"></a>

#### updated_component

```python
@property
def updated_component() -> SceneComponent
```

(SceneComponent):  [Read-Only] The component we move and update.
If this is null at startup and bAutoRegisterUpdatedComponent is true, the owning Actor's root component will automatically be set as our UpdatedComponent at startup.
see: bAutoRegisterUpdatedComponent, SetUpdatedComponent(), UpdatedPrimitive

<a id="unreal.MovementComponent.updated_primitive"></a>

#### updated_primitive

```python
@property
def updated_primitive() -> PrimitiveComponent
```

(PrimitiveComponent):  [Read-Only] UpdatedComponent, cast as a UPrimitiveComponent. May be invalid if UpdatedComponent was null or not a UPrimitiveComponent.

<a id="unreal.MovementComponent.velocity"></a>

#### velocity

```python
@property
def velocity() -> Vector
```

(Vector):  [Read-Write] Current velocity of updated component.

<a id="unreal.MovementComponent.velocity"></a>

#### velocity

```python
@velocity.setter
def velocity(value: Vector) -> None
```

<a id="unreal.MovementComponent.plane_constraint_normal"></a>

#### plane_constraint_normal

```python
@property
def plane_constraint_normal() -> Vector
```

(Vector):  [Read-Only] The normal or axis of the plane that constrains movement, if bConstrainToPlane is enabled.
If for example you wanted to constrain movement to the X-Z plane (so that Y cannot change), the normal would be set to X=0 Y=1 Z=0.
This is recalculated whenever PlaneConstraintAxisSetting changes. It is normalized once the component is registered with the game world.
see: bConstrainToPlane, SetPlaneConstraintNormal(), SetPlaneConstraintFromVectors()

<a id="unreal.MovementComponent.plane_constraint_origin"></a>

#### plane_constraint_origin

```python
@property
def plane_constraint_origin() -> Vector
```

(Vector):  [Read-Only] The origin of the plane that constrains movement, if plane constraint is enabled.
This defines the behavior of snapping a position to the plane, such as by SnapUpdatedComponentToPlane().
see: bConstrainToPlane, SetPlaneConstraintOrigin().

<a id="unreal.MovementComponent.update_only_if_rendered"></a>

#### update_only_if_rendered

```python
@property
def update_only_if_rendered() -> bool
```

(bool):  [Read-Write] If true, skips TickComponent() if UpdatedComponent was not recently rendered.

<a id="unreal.MovementComponent.update_only_if_rendered"></a>

#### update_only_if_rendered

```python
@update_only_if_rendered.setter
def update_only_if_rendered(value: bool) -> None
```

<a id="unreal.MovementComponent.auto_update_tick_registration"></a>

#### auto_update_tick_registration

```python
@property
def auto_update_tick_registration() -> bool
```

(bool):  [Read-Only] If true, whenever the updated component is changed, this component will enable or disable its tick dependent on whether it has something to update.
This will NOT enable tick at startup if bAutoActivate is false, because presumably you have a good reason for not wanting it to start ticking initially.

<a id="unreal.MovementComponent.tick_before_owner"></a>

#### tick_before_owner

```python
@property
def tick_before_owner() -> bool
```

(bool):  [Read-Only] If true, after registration we will add a tick dependency to tick before our owner (if we can both tick).
This is important when our tick causes an update in the owner's position, so that when the owner ticks it uses the most recent position without lag.
Disabling this can improve performance if both objects tick but the order of ticks doesn't matter.

<a id="unreal.MovementComponent.auto_register_updated_component"></a>

#### auto_register_updated_component

```python
@property
def auto_register_updated_component() -> bool
```

(bool):  [Read-Only] If true, registers the owner's Root component as the UpdatedComponent if there is not one currently assigned.

<a id="unreal.MovementComponent.constrain_to_plane"></a>

#### constrain_to_plane

```python
@property
def constrain_to_plane() -> bool
```

(bool):  [Read-Only] If true, movement will be constrained to a plane.
see: PlaneConstraintNormal, PlaneConstraintOrigin, PlaneConstraintAxisSetting

<a id="unreal.MovementComponent.snap_to_plane_at_start"></a>

#### snap_to_plane_at_start

```python
@property
def snap_to_plane_at_start() -> bool
```

(bool):  [Read-Only] If true and plane constraints are enabled, then the updated component will be snapped to the plane when first attached.

<a id="unreal.MovementComponent.auto_register_physics_volume_updates"></a>

#### auto_register_physics_volume_updates

```python
@property
def auto_register_physics_volume_updates() -> bool
```

(bool):  [Read-Only] If true, then applies the value of bComponentShouldUpdatePhysicsVolume to the UpdatedComponent. If false, will not change bShouldUpdatePhysicsVolume on the UpdatedComponent at all.
see: bComponentShouldUpdatePhysicsVolume

<a id="unreal.MovementComponent.component_should_update_physics_volume"></a>

#### component_should_update_physics_volume

```python
@property
def component_should_update_physics_volume() -> bool
```

(bool):  [Read-Only] If true, enables bShouldUpdatePhysicsVolume on the UpdatedComponent during initialization from SetUpdatedComponent(), otherwise disables such updates.
Only enabled if bAutoRegisterPhysicsVolumeUpdates is true.
WARNING: UpdatePhysicsVolume is potentially expensive if overlap events are also *disabled* because it requires a separate query against all physics volumes in the world.

<a id="unreal.MovementComponent.stop_movement_immediately"></a>

#### stop_movement_immediately

```python
def stop_movement_immediately() -> None
```

x.stop_movement_immediately() -> None
Stops movement immediately (zeroes velocity, usually zeros acceleration for components with acceleration).

<a id="unreal.MovementComponent.snap_updated_component_to_plane"></a>

#### snap_updated_component_to_plane

```python
def snap_updated_component_to_plane() -> None
```

x.snap_updated_component_to_plane() -> None
Snap the updated component to the plane constraint, if enabled.

<a id="unreal.MovementComponent.set_updated_component"></a>

#### set_updated_component

```python
def set_updated_component(new_updated_component: SceneComponent) -> None
```

x.set_updated_component(new_updated_component) -> None
Assign the component we move and update.

Args:
    new_updated_component (SceneComponent):

<a id="unreal.MovementComponent.set_plane_constraint_origin"></a>

#### set_plane_constraint_origin

```python
def set_plane_constraint_origin(plane_origin: Vector) -> None
```

x.set_plane_constraint_origin(plane_origin) -> None
Sets the origin of the plane that constrains movement, enforced if the plane constraint is enabled.

Args:
    plane_origin (Vector):

<a id="unreal.MovementComponent.set_plane_constraint_normal"></a>

#### set_plane_constraint_normal

```python
def set_plane_constraint_normal(plane_normal: Vector) -> None
```

x.set_plane_constraint_normal(plane_normal) -> None
Sets the normal of the plane that constrains movement, enforced if the plane constraint is enabled.
Changing the normal automatically sets PlaneConstraintAxisSetting to "Custom".

Args:
    plane_normal (Vector): The normal of the plane. If non-zero in length, it will be normalized.

<a id="unreal.MovementComponent.set_plane_constraint_from_vectors"></a>

#### set_plane_constraint_from_vectors

```python
def set_plane_constraint_from_vectors(forward: Vector, up: Vector) -> None
```

x.set_plane_constraint_from_vectors(forward, up) -> None
Uses the Forward and Up vectors to compute the plane that constrains movement, enforced if the plane constraint is enabled.

Args:
    forward (Vector): 
    up (Vector):

<a id="unreal.MovementComponent.set_plane_constraint_enabled"></a>

#### set_plane_constraint_enabled

```python
def set_plane_constraint_enabled(enabled: bool) -> None
```

x.set_plane_constraint_enabled(enabled) -> None
Sets whether or not the plane constraint is enabled.

Args:
    enabled (bool):

<a id="unreal.MovementComponent.set_plane_constraint_axis_setting"></a>

#### set_plane_constraint_axis_setting

```python
def set_plane_constraint_axis_setting(
        new_axis_setting: PlaneConstraintAxisSetting) -> None
```

x.set_plane_constraint_axis_setting(new_axis_setting) -> None
Set the plane constraint axis setting.
Changing this setting will modify the current value of PlaneConstraintNormal.

Args:
    new_axis_setting (PlaneConstraintAxisSetting): New plane constraint axis setting.

<a id="unreal.MovementComponent.move_updated_component"></a>

#### move_updated_component

```python
def move_updated_component(delta: Vector,
                           new_rotation: Rotator,
                           sweep: bool = True,
                           teleport: bool = False) -> Optional[HitResult]
```

x.move_updated_component(delta, new_rotation, sweep=True, teleport=False) -> HitResult or None
Moves our UpdatedComponent by the given Delta, and sets rotation to NewRotation.
Respects the plane constraint, if enabled.

Args:
    delta (Vector): 
    new_rotation (Rotator): 
    sweep (bool): 
    teleport (bool): 

Returns:
    HitResult or None: True if some movement occurred, false if no movement occurred. Result of any impact will be stored in OutHit.

    out_hit (HitResult):

<a id="unreal.MovementComponent.is_exceeding_max_speed"></a>

#### is_exceeding_max_speed

```python
def is_exceeding_max_speed(max_speed: float) -> bool
```

x.is_exceeding_max_speed(max_speed) -> bool
Returns true if the current velocity is exceeding the given max speed (usually the result of GetMaxSpeed()), within a small error tolerance.
Note that under normal circumstances updates cause by acceleration will not cause this to be true, however external forces or changes in the max speed limit
can cause the max speed to be violated.

Args:
    max_speed (float): 

Returns:
    bool:

<a id="unreal.MovementComponent.get_plane_constraint_origin"></a>

#### get_plane_constraint_origin

```python
def get_plane_constraint_origin() -> Vector
```

x.get_plane_constraint_origin() -> Vector
Get the plane constraint origin. This defines the behavior of snapping a position to the plane, such as by SnapUpdatedComponentToPlane().

Returns:
    Vector: The origin of the plane that constrains movement, if the plane constraint is enabled.

<a id="unreal.MovementComponent.get_plane_constraint_normal"></a>

#### get_plane_constraint_normal

```python
def get_plane_constraint_normal() -> Vector
```

x.get_plane_constraint_normal() -> Vector
Returns the normal of the plane that constrains movement, enforced if the plane constraint is enabled.

Returns:
    Vector:

<a id="unreal.MovementComponent.get_plane_constraint_axis_setting"></a>

#### get_plane_constraint_axis_setting

```python
def get_plane_constraint_axis_setting() -> PlaneConstraintAxisSetting
```

x.get_plane_constraint_axis_setting() -> PlaneConstraintAxisSetting
Get the plane constraint axis setting.

Returns:
    PlaneConstraintAxisSetting:

<a id="unreal.MovementComponent.get_physics_volume"></a>

#### get_physics_volume

```python
def get_physics_volume() -> PhysicsVolume
```

x.get_physics_volume() -> PhysicsVolume
Returns the PhysicsVolume this MovementComponent is using, or the world's default physics volume if none. *

Returns:
    PhysicsVolume:

<a id="unreal.MovementComponent.get_max_speed"></a>

#### get_max_speed

```python
def get_max_speed() -> float
```

x.get_max_speed() -> float
Returns maximum speed of component in current movement mode.

Returns:
    float:

<a id="unreal.MovementComponent.get_gravity_z"></a>

#### get_gravity_z

```python
def get_gravity_z() -> float
```

x.get_gravity_z() -> float
Returns gravity that affects this component

Returns:
    float:

<a id="unreal.MovementComponent.constrain_normal_to_plane"></a>

#### constrain_normal_to_plane

```python
def constrain_normal_to_plane(normal: Vector) -> Vector
```

x.constrain_normal_to_plane(normal) -> Vector
Constrain a normal vector (of unit length) to the plane constraint, if enabled.

Args:
    normal (Vector): 

Returns:
    Vector:

<a id="unreal.MovementComponent.constrain_location_to_plane"></a>

#### constrain_location_to_plane

```python
def constrain_location_to_plane(location: Vector) -> Vector
```

x.constrain_location_to_plane(location) -> Vector
Constrain a position vector to the plane constraint, if enabled.

Args:
    location (Vector): 

Returns:
    Vector:

<a id="unreal.MovementComponent.constrain_position_to_plane"></a>

#### constrain_position_to_plane

```python
def constrain_position_to_plane(location: Vector) -> Vector
```

deprecated: 'constrain_position_to_plane' was renamed to 'constrain_location_to_plane'.

<a id="unreal.MovementComponent.constrain_direction_to_plane"></a>

#### constrain_direction_to_plane

```python
def constrain_direction_to_plane(direction: Vector) -> Vector
```

x.constrain_direction_to_plane(direction) -> Vector
Constrain a direction vector to the plane constraint, if enabled.
see: SetPlaneConstraint

Args:
    direction (Vector): 

Returns:
    Vector:

<a id="unreal.NavMovementComponent"></a>