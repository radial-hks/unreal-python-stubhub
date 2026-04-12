## WdpSpringArmComponent Objects

```python
class WdpSpringArmComponent(SpringArmComponent)
```

Wdp Spring Arm Component

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpSpringArmComponent.h

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
- ``collision_ignore_actors`` (Array[Actor]):  [Read-Write] 碰撞忽略的Actors
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
- ``gravity_direction`` (Vector):  [Read-Write] 当前的重力方向
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
- ``rotate_in_surface_space`` (bool):  [Read-Write] 是否将旋转转换到球面模式
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
- ``world_origin_anchor`` (WorldOriginAnchor):  [Read-Only] 用于球面操作的坐标转换Actor

<a id="unreal.WdpSpringArmComponent.world_origin_anchor"></a>

#### world\_origin\_anchor

```python
@property
def world_origin_anchor() -> WorldOriginAnchor
```

(WorldOriginAnchor):  [Read-Only] 用于球面操作的坐标转换Actor

<a id="unreal.WdpSpringArmComponent.update_spring_arm_no_lag"></a>

#### update\_spring\_arm\_no\_lag

```python
def update_spring_arm_no_lag() -> None
```

x.update_spring_arm_no_lag() -> None
瞬时设置旋转，无lag

<a id="unreal.WdpSpringArmComponent.update_gravity_direction"></a>

#### update\_gravity\_direction

```python
def update_gravity_direction(new_gravity_direction: Vector) -> None
```

x.update_gravity_direction(new_gravity_direction) -> None
更新重力方向

Args:
    new_gravity_direction (Vector):

<a id="unreal.WdpSpringArmComponent.remove_collision_ignore_actor"></a>

#### remove\_collision\_ignore\_actor

```python
def remove_collision_ignore_actor(ignore_actor: Actor) -> None
```

x.remove_collision_ignore_actor(ignore_actor) -> None
移除需要被忽略的碰撞Actor

Args:
    ignore_actor (Actor):

<a id="unreal.WdpSpringArmComponent.init_world_origin_anchor"></a>

#### init\_world\_origin\_anchor

```python
def init_world_origin_anchor() -> None
```

x.init_world_origin_anchor() -> None
查找世界坐标锚点，用于支持球面操作

<a id="unreal.WdpSpringArmComponent.get_gravity_world_rotation"></a>

#### get\_gravity\_world\_rotation

```python
def get_gravity_world_rotation(rotation: Rotator) -> Rotator
```

x.get_gravity_world_rotation(rotation) -> Rotator
局部旋转转世界

Args:
    rotation (Rotator): 

Returns:
    Rotator:

<a id="unreal.WdpSpringArmComponent.get_gravity_relative_rotation"></a>

#### get\_gravity\_relative\_rotation

```python
def get_gravity_relative_rotation(rotation: Rotator) -> Rotator
```

x.get_gravity_relative_rotation(rotation) -> Rotator
世界旋转转局部

Args:
    rotation (Rotator): 

Returns:
    Rotator:

<a id="unreal.WdpSpringArmComponent.get_custom_target_rotation"></a>

#### get\_custom\_target\_rotation

```python
def get_custom_target_rotation() -> Rotator
```

x.get_custom_target_rotation() -> Rotator
自定义目标的旋转点

Returns:
    Rotator:

<a id="unreal.WdpSpringArmComponent.clear_collision_ignore_actors"></a>

#### clear\_collision\_ignore\_actors

```python
def clear_collision_ignore_actors() -> None
```

x.clear_collision_ignore_actors() -> None
移除全部需要被忽略的碰撞Actor

<a id="unreal.WdpSpringArmComponent.add_collision_ignore_actor"></a>

#### add\_collision\_ignore\_actor

```python
def add_collision_ignore_actor(ignore_actor: Actor) -> None
```

x.add_collision_ignore_actor(ignore_actor) -> None
添加需要被忽略的碰撞Actor

Args:
    ignore_actor (Actor):

<a id="unreal.WorldOriginAnchor"></a>