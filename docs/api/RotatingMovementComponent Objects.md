## RotatingMovementComponent Objects

```python
class RotatingMovementComponent(MovementComponent)
```

Performs continuous rotation of a component at a specific rotation rate.
Rotation can optionally be offset around a pivot point.
Collision testing is not performed during movement.

**C++ Source:**

- **Module**: Engine
- **File**: RotatingMovementComponent.h

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
- ``pivot_translation`` (Vector):  [Read-Write] Translation of pivot point around which we rotate, relative to current rotation.
  For instance, with PivotTranslation set to (X=+100, Y=0, Z=0), rotation will occur
  around the point +100 units along the local X axis from the center of the object,
  rather than around the object's origin (the default).
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
- ``rotation_in_local_space`` (bool):  [Read-Write] Whether rotation is applied in local or world space.
- ``rotation_rate`` (Rotator):  [Read-Write] How fast to update roll/pitch/yaw of the component we update.
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

<a id="unreal.RotatingMovementComponent.rotation_rate"></a>

#### rotation_rate

```python
@property
def rotation_rate() -> Rotator
```

(Rotator):  [Read-Write] How fast to update roll/pitch/yaw of the component we update.

<a id="unreal.RotatingMovementComponent.rotation_rate"></a>

#### rotation_rate

```python
@rotation_rate.setter
def rotation_rate(value: Rotator) -> None
```

<a id="unreal.RotatingMovementComponent.pivot_translation"></a>

#### pivot_translation

```python
@property
def pivot_translation() -> Vector
```

(Vector):  [Read-Write] Translation of pivot point around which we rotate, relative to current rotation.
For instance, with PivotTranslation set to (X=+100, Y=0, Z=0), rotation will occur
around the point +100 units along the local X axis from the center of the object,
rather than around the object's origin (the default).

<a id="unreal.RotatingMovementComponent.pivot_translation"></a>

#### pivot_translation

```python
@pivot_translation.setter
def pivot_translation(value: Vector) -> None
```

<a id="unreal.RotatingMovementComponent.rotation_in_local_space"></a>

#### rotation_in_local_space

```python
@property
def rotation_in_local_space() -> bool
```

(bool):  [Read-Write] Whether rotation is applied in local or world space.

<a id="unreal.RotatingMovementComponent.rotation_in_local_space"></a>

#### rotation_in_local_space

```python
@rotation_in_local_space.setter
def rotation_in_local_space(value: bool) -> None
```

<a id="unreal.MovementComp_Rotating"></a>