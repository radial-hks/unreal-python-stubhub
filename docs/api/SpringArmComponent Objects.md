## SpringArmComponent Objects

```python
class SpringArmComponent(SceneComponent)
```

This component tries to maintain its children at a fixed distance from the parent,
but will retract the children if there is a collision, and spring back when there is no collision.

Example: Use as a 'camera boom' or 'selfie stick' to keep the follow camera for a player from colliding into the world.

**C++ Source:**

- **Module**: Engine
- **File**: SpringArmComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``camera_lag_max_distance`` (float):  [Read-Write] Max distance the camera target may lag behind the current location. If set to zero, no max distance is enforced.
- ``camera_lag_max_time_step`` (float):  [Read-Write] Max time step used when sub-stepping camera lag.
- ``camera_lag_speed`` (float):  [Read-Write] If bEnableCameraLag is true, controls how quickly camera reaches target position. Low values are slower (more lag), high values are faster (less lag), while zero is instant (no lag).
- ``camera_rotation_lag_speed`` (float):  [Read-Write] If bEnableCameraRotationLag is true, controls how quickly camera reaches target position. Low values are slower (more lag), high values are faster (less lag), while zero is instant (no lag).
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``clamp_to_max_physics_delta_time`` (bool):  [Read-Write] If true AND the view target is simulating using physics then use the same max timestep cap as the physics system. Prevents camera jitter when delta time is clamped within Chaos Physics.
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``do_collision_test`` (bool):  [Read-Write] If true, do a collision test using ProbeChannel and ProbeSize to prevent camera clipping into level.
- ``draw_debug_lag_markers`` (bool):  [Read-Write] If true and camera location lag is enabled, draws markers at the camera target (in green) and the lagged position (in yellow).
  A line is drawn between the two locations, in green normally but in red if the distance to the lag target has been clamped (by CameraLagMaxDistance).
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``enable_camera_lag`` (bool):  [Read-Write] If true, camera lags behind target position to smooth its movement.
  see: CameraLagSpeed
- ``enable_camera_rotation_lag`` (bool):  [Read-Write] If true, camera lags behind target rotation to smooth its movement.
  see: CameraRotationLagSpeed
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``inherit_pitch`` (bool):  [Read-Write] Should we inherit pitch from parent component. Does nothing if using Absolute Rotation.
- ``inherit_roll`` (bool):  [Read-Write] Should we inherit roll from parent component. Does nothing if using Absolute Rotation.
- ``inherit_yaw`` (bool):  [Read-Write] Should we inherit yaw from parent component. Does nothing if using Absolute Rotation.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``probe_channel`` (CollisionChannel):  [Read-Write] Collision channel of the query probe (defaults to ECC_Camera)
- ``probe_size`` (float):  [Read-Write] How big should the query probe sphere be (in unreal units)
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``socket_offset`` (Vector):  [Read-Write] offset at end of spring arm; use this instead of the relative offset of the attached component to ensure the line trace works as desired
- ``target_arm_length`` (float):  [Read-Write] Natural length of the spring arm when there are no collisions
- ``target_offset`` (Vector):  [Read-Write] Offset at start of spring, applied in world space. Use this if you want a world-space offset from the parent component instead of the usual relative-space offset.
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``use_camera_lag_substepping`` (bool):  [Read-Write] If bUseCameraLagSubstepping is true, sub-step camera damping so that it handles fluctuating frame rates well (though this comes at a cost).
  see: CameraLagMaxTimeStep
- ``use_pawn_control_rotation`` (bool):  [Read-Write] If this component is placed on a pawn, should it use the view/control rotation of the pawn where possible?
  When disabled, the component will revert to using the stored RelativeRotation of the component.
  Note that this component itself does not rotate, but instead maintains its relative rotation to its parent as normal,
  and just repositions and rotates its children as desired by the inherited rotation settings. Use GetTargetRotation()
  if you want the rotation target based on all the settings (UsePawnControlRotation, InheritPitch, etc).
  see: GetTargetRotation(), APawn::GetViewRotation()
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.SpringArmComponent.target_arm_length"></a>

#### target_arm_length

```python
@property
def target_arm_length() -> float
```

(float):  [Read-Write] Natural length of the spring arm when there are no collisions

<a id="unreal.SpringArmComponent.target_arm_length"></a>

#### target_arm_length

```python
@target_arm_length.setter
def target_arm_length(value: float) -> None
```

<a id="unreal.SpringArmComponent.socket_offset"></a>

#### socket_offset

```python
@property
def socket_offset() -> Vector
```

(Vector):  [Read-Write] offset at end of spring arm; use this instead of the relative offset of the attached component to ensure the line trace works as desired

<a id="unreal.SpringArmComponent.socket_offset"></a>

#### socket_offset

```python
@socket_offset.setter
def socket_offset(value: Vector) -> None
```

<a id="unreal.SpringArmComponent.target_offset"></a>

#### target_offset

```python
@property
def target_offset() -> Vector
```

(Vector):  [Read-Write] Offset at start of spring, applied in world space. Use this if you want a world-space offset from the parent component instead of the usual relative-space offset.

<a id="unreal.SpringArmComponent.target_offset"></a>

#### target_offset

```python
@target_offset.setter
def target_offset(value: Vector) -> None
```

<a id="unreal.SpringArmComponent.probe_size"></a>

#### probe_size

```python
@property
def probe_size() -> float
```

(float):  [Read-Write] How big should the query probe sphere be (in unreal units)

<a id="unreal.SpringArmComponent.probe_size"></a>

#### probe_size

```python
@probe_size.setter
def probe_size(value: float) -> None
```

<a id="unreal.SpringArmComponent.probe_channel"></a>

#### probe_channel

```python
@property
def probe_channel() -> CollisionChannel
```

(CollisionChannel):  [Read-Write] Collision channel of the query probe (defaults to ECC_Camera)

<a id="unreal.SpringArmComponent.probe_channel"></a>

#### probe_channel

```python
@probe_channel.setter
def probe_channel(value: CollisionChannel) -> None
```

<a id="unreal.SpringArmComponent.do_collision_test"></a>

#### do_collision_test

```python
@property
def do_collision_test() -> bool
```

(bool):  [Read-Write] If true, do a collision test using ProbeChannel and ProbeSize to prevent camera clipping into level.

<a id="unreal.SpringArmComponent.do_collision_test"></a>

#### do_collision_test

```python
@do_collision_test.setter
def do_collision_test(value: bool) -> None
```

<a id="unreal.SpringArmComponent.use_pawn_control_rotation"></a>

#### use_pawn_control_rotation

```python
@property
def use_pawn_control_rotation() -> bool
```

(bool):  [Read-Write] If this component is placed on a pawn, should it use the view/control rotation of the pawn where possible?
When disabled, the component will revert to using the stored RelativeRotation of the component.
Note that this component itself does not rotate, but instead maintains its relative rotation to its parent as normal,
and just repositions and rotates its children as desired by the inherited rotation settings. Use GetTargetRotation()
if you want the rotation target based on all the settings (UsePawnControlRotation, InheritPitch, etc).
see: GetTargetRotation(), APawn::GetViewRotation()

<a id="unreal.SpringArmComponent.use_pawn_control_rotation"></a>

#### use_pawn_control_rotation

```python
@use_pawn_control_rotation.setter
def use_pawn_control_rotation(value: bool) -> None
```

<a id="unreal.SpringArmComponent.b_use_controller_view_rotation"></a>

#### b_use_controller_view_rotation

```python
@property
def b_use_controller_view_rotation() -> bool
```

deprecated: 'b_use_controller_view_rotation' was renamed to 'use_pawn_control_rotation'.

<a id="unreal.SpringArmComponent.b_use_controller_view_rotation"></a>

#### b_use_controller_view_rotation

```python
@b_use_controller_view_rotation.setter
def b_use_controller_view_rotation(value: bool) -> None
```

<a id="unreal.SpringArmComponent.b_use_pawn_view_rotation"></a>

#### b_use_pawn_view_rotation

```python
@property
def b_use_pawn_view_rotation() -> bool
```

deprecated: 'b_use_pawn_view_rotation' was renamed to 'use_pawn_control_rotation'.

<a id="unreal.SpringArmComponent.b_use_pawn_view_rotation"></a>

#### b_use_pawn_view_rotation

```python
@b_use_pawn_view_rotation.setter
def b_use_pawn_view_rotation(value: bool) -> None
```

<a id="unreal.SpringArmComponent.inherit_pitch"></a>

#### inherit_pitch

```python
@property
def inherit_pitch() -> bool
```

(bool):  [Read-Write] Should we inherit pitch from parent component. Does nothing if using Absolute Rotation.

<a id="unreal.SpringArmComponent.inherit_pitch"></a>

#### inherit_pitch

```python
@inherit_pitch.setter
def inherit_pitch(value: bool) -> None
```

<a id="unreal.SpringArmComponent.inherit_yaw"></a>

#### inherit_yaw

```python
@property
def inherit_yaw() -> bool
```

(bool):  [Read-Write] Should we inherit yaw from parent component. Does nothing if using Absolute Rotation.

<a id="unreal.SpringArmComponent.inherit_yaw"></a>

#### inherit_yaw

```python
@inherit_yaw.setter
def inherit_yaw(value: bool) -> None
```

<a id="unreal.SpringArmComponent.inherit_roll"></a>

#### inherit_roll

```python
@property
def inherit_roll() -> bool
```

(bool):  [Read-Write] Should we inherit roll from parent component. Does nothing if using Absolute Rotation.

<a id="unreal.SpringArmComponent.inherit_roll"></a>

#### inherit_roll

```python
@inherit_roll.setter
def inherit_roll(value: bool) -> None
```

<a id="unreal.SpringArmComponent.enable_camera_lag"></a>

#### enable_camera_lag

```python
@property
def enable_camera_lag() -> bool
```

(bool):  [Read-Write] If true, camera lags behind target position to smooth its movement.
see: CameraLagSpeed

<a id="unreal.SpringArmComponent.enable_camera_lag"></a>

#### enable_camera_lag

```python
@enable_camera_lag.setter
def enable_camera_lag(value: bool) -> None
```

<a id="unreal.SpringArmComponent.enable_camera_rotation_lag"></a>

#### enable_camera_rotation_lag

```python
@property
def enable_camera_rotation_lag() -> bool
```

(bool):  [Read-Write] If true, camera lags behind target rotation to smooth its movement.
see: CameraRotationLagSpeed

<a id="unreal.SpringArmComponent.enable_camera_rotation_lag"></a>

#### enable_camera_rotation_lag

```python
@enable_camera_rotation_lag.setter
def enable_camera_rotation_lag(value: bool) -> None
```

<a id="unreal.SpringArmComponent.use_camera_lag_substepping"></a>

#### use_camera_lag_substepping

```python
@property
def use_camera_lag_substepping() -> bool
```

(bool):  [Read-Write] If bUseCameraLagSubstepping is true, sub-step camera damping so that it handles fluctuating frame rates well (though this comes at a cost).
see: CameraLagMaxTimeStep

<a id="unreal.SpringArmComponent.use_camera_lag_substepping"></a>

#### use_camera_lag_substepping

```python
@use_camera_lag_substepping.setter
def use_camera_lag_substepping(value: bool) -> None
```

<a id="unreal.SpringArmComponent.draw_debug_lag_markers"></a>

#### draw_debug_lag_markers

```python
@property
def draw_debug_lag_markers() -> bool
```

(bool):  [Read-Write] If true and camera location lag is enabled, draws markers at the camera target (in green) and the lagged position (in yellow).
A line is drawn between the two locations, in green normally but in red if the distance to the lag target has been clamped (by CameraLagMaxDistance).

<a id="unreal.SpringArmComponent.draw_debug_lag_markers"></a>

#### draw_debug_lag_markers

```python
@draw_debug_lag_markers.setter
def draw_debug_lag_markers(value: bool) -> None
```

<a id="unreal.SpringArmComponent.camera_lag_speed"></a>

#### camera_lag_speed

```python
@property
def camera_lag_speed() -> float
```

(float):  [Read-Write] If bEnableCameraLag is true, controls how quickly camera reaches target position. Low values are slower (more lag), high values are faster (less lag), while zero is instant (no lag).

<a id="unreal.SpringArmComponent.camera_lag_speed"></a>

#### camera_lag_speed

```python
@camera_lag_speed.setter
def camera_lag_speed(value: float) -> None
```

<a id="unreal.SpringArmComponent.camera_rotation_lag_speed"></a>

#### camera_rotation_lag_speed

```python
@property
def camera_rotation_lag_speed() -> float
```

(float):  [Read-Write] If bEnableCameraRotationLag is true, controls how quickly camera reaches target position. Low values are slower (more lag), high values are faster (less lag), while zero is instant (no lag).

<a id="unreal.SpringArmComponent.camera_rotation_lag_speed"></a>

#### camera_rotation_lag_speed

```python
@camera_rotation_lag_speed.setter
def camera_rotation_lag_speed(value: float) -> None
```

<a id="unreal.SpringArmComponent.camera_lag_max_time_step"></a>

#### camera_lag_max_time_step

```python
@property
def camera_lag_max_time_step() -> float
```

(float):  [Read-Write] Max time step used when sub-stepping camera lag.

<a id="unreal.SpringArmComponent.camera_lag_max_time_step"></a>

#### camera_lag_max_time_step

```python
@camera_lag_max_time_step.setter
def camera_lag_max_time_step(value: float) -> None
```

<a id="unreal.SpringArmComponent.camera_lag_max_distance"></a>

#### camera_lag_max_distance

```python
@property
def camera_lag_max_distance() -> float
```

(float):  [Read-Write] Max distance the camera target may lag behind the current location. If set to zero, no max distance is enforced.

<a id="unreal.SpringArmComponent.camera_lag_max_distance"></a>

#### camera_lag_max_distance

```python
@camera_lag_max_distance.setter
def camera_lag_max_distance(value: float) -> None
```

<a id="unreal.SpringArmComponent.clamp_to_max_physics_delta_time"></a>

#### clamp_to_max_physics_delta_time

```python
@property
def clamp_to_max_physics_delta_time() -> bool
```

(bool):  [Read-Write] If true AND the view target is simulating using physics then use the same max timestep cap as the physics system. Prevents camera jitter when delta time is clamped within Chaos Physics.

<a id="unreal.SpringArmComponent.clamp_to_max_physics_delta_time"></a>

#### clamp_to_max_physics_delta_time

```python
@clamp_to_max_physics_delta_time.setter
def clamp_to_max_physics_delta_time(value: bool) -> None
```

<a id="unreal.SpringArmComponent.is_collision_fix_applied"></a>

#### is_collision_fix_applied

```python
def is_collision_fix_applied() -> bool
```

x.is_collision_fix_applied() -> bool
Is the Collision Test displacement being applied?

Returns:
    bool:

<a id="unreal.SpringArmComponent.get_unfixed_camera_position"></a>

#### get_unfixed_camera_position

```python
def get_unfixed_camera_position() -> Vector
```

x.get_unfixed_camera_position() -> Vector
Get the position where the camera should be without applying the Collision Test displacement

Returns:
    Vector:

<a id="unreal.SpringArmComponent.get_target_rotation"></a>

#### get_target_rotation

```python
def get_target_rotation() -> Rotator
```

x.get_target_rotation() -> Rotator
Get the target rotation we inherit, used as the base target for the boom rotation.
This is derived from attachment to our parent and considering the UsePawnControlRotation and absolute rotation flags.

Returns:
    Rotator:

<a id="unreal.TouchInterface"></a>