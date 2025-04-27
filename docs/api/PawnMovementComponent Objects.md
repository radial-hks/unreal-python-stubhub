## PawnMovementComponent Objects

```python
class PawnMovementComponent(NavMovementComponent)
```

PawnMovementComponent can be used to update movement for an associated Pawn.
It also provides ways to accumulate and read directional input in a generic way (with AddInputVector(), ConsumeInputVector(), etc).
see: APawn

**C++ Source:**

- **Module**: Engine
- **File**: PawnMovementComponent.h

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

<a id="unreal.PawnMovementComponent.is_move_input_ignored"></a>

#### is_move_input_ignored

```python
def is_move_input_ignored() -> bool
```

x.is_move_input_ignored() -> bool
Helper to see if move input is ignored. If there is no Pawn or UpdatedComponent, returns true, otherwise defers to the Pawn's implementation of IsMoveInputIgnored().

Returns:
    bool:

<a id="unreal.PawnMovementComponent.get_pending_input_vector"></a>

#### get_pending_input_vector

```python
def get_pending_input_vector() -> Vector
```

x.get_pending_input_vector() -> Vector
Return the pending input vector in world space. This is the most up-to-date value of the input vector, pending ConsumeMovementInputVector() which clears it.
PawnMovementComponents implementing movement usually want to use either this or ConsumeInputVector() as these functions represent the most recent state of input.
see: AddInputVector(), ConsumeInputVector(), GetLastInputVector()

Returns:
    Vector: The pending input vector in world space.

<a id="unreal.PawnMovementComponent.get_input_vector"></a>

#### get_input_vector

```python
def get_input_vector() -> Vector
```

deprecated: 'get_input_vector' was renamed to 'get_pending_input_vector'.

<a id="unreal.PawnMovementComponent.get_pawn_owner"></a>

#### get_pawn_owner

```python
def get_pawn_owner() -> Pawn
```

x.get_pawn_owner() -> Pawn
Return the Pawn that owns UpdatedComponent.

Returns:
    Pawn:

<a id="unreal.PawnMovementComponent.get_last_input_vector"></a>

#### get_last_input_vector

```python
def get_last_input_vector() -> Vector
```

x.get_last_input_vector() -> Vector
Return the last input vector in world space that was processed by ConsumeInputVector(), which is usually done by the Pawn or PawnMovementComponent.
Any user that needs to know about the input that last affected movement should use this function.
see: AddInputVector(), ConsumeInputVector(), GetPendingInputVector()

Returns:
    Vector: The last input vector in world space that was processed by ConsumeInputVector().

<a id="unreal.PawnMovementComponent.consume_input_vector"></a>

#### consume_input_vector

```python
def consume_input_vector() -> Vector
```

x.consume_input_vector() -> Vector
Returns the pending input vector and resets it to zero.
       * This should be used during a movement update (by the Pawn or PawnMovementComponent) to prevent accumulation of control input between frames.
       * Copies the pending input vector to the saved input vector (GetLastMovementInputVector()).
       *

Returns:
    Vector: The pending input vector.

<a id="unreal.PawnMovementComponent.add_input_vector"></a>

#### add_input_vector

```python
def add_input_vector(world_vector: Vector, force: bool = False) -> None
```

x.add_input_vector(world_vector, force=False) -> None
Adds the given vector to the accumulated input in world space. Input vectors are usually between 0 and 1 in magnitude.
They are accumulated during a frame then applied as acceleration during the movement update.
see: APawn::AddMovementInput()

Args:
    world_vector (Vector): Direction in world space to apply input
    force (bool): If true always add the input, ignoring the result of IsMoveInputIgnored().

<a id="unreal.CharacterMovementComponent"></a>