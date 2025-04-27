## GameplayCameraSystemComponent Objects

```python
class GameplayCameraSystemComponent(SceneComponent)
```

A component that hosts a camera system.

**C++ Source:**

- **Plugin**: GameplayCameras
- **Module**: GameplayCameras
- **File**: GameplayCameraSystemComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``auto_activate_for_player`` (AutoReceiveInput):  [Read-Write] If AutoActivate is set, auto-activates the camera system for the given player.
  This sets this actor as the view target, and is equivalent to calling ActivateCameraSystem on BeginPlay.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``set_player_controller_rotation`` (bool):  [Read-Write] If enabled, sets the evaluated camera orientation as the player controller rotation every frame.
  This is set on the player controller that this component was activated for.
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.GameplayCameraSystemComponent.auto_activate_for_player"></a>

#### auto_activate_for_player

```python
@property
def auto_activate_for_player() -> AutoReceiveInput
```

(AutoReceiveInput):  [Read-Write] If AutoActivate is set, auto-activates the camera system for the given player.
This sets this actor as the view target, and is equivalent to calling ActivateCameraSystem on BeginPlay.

<a id="unreal.GameplayCameraSystemComponent.auto_activate_for_player"></a>

#### auto_activate_for_player

```python
@auto_activate_for_player.setter
def auto_activate_for_player(value: AutoReceiveInput) -> None
```

<a id="unreal.GameplayCameraSystemComponent.set_player_controller_rotation"></a>

#### set_player_controller_rotation

```python
@property
def set_player_controller_rotation() -> bool
```

(bool):  [Read-Write] If enabled, sets the evaluated camera orientation as the player controller rotation every frame.
This is set on the player controller that this component was activated for.

<a id="unreal.GameplayCameraSystemComponent.set_player_controller_rotation"></a>

#### set_player_controller_rotation

```python
@set_player_controller_rotation.setter
def set_player_controller_rotation(value: bool) -> None
```

<a id="unreal.GameplayCameraSystemComponent.is_camera_system_active_for_play_controller"></a>

#### is_camera_system_active_for_play_controller

```python
def is_camera_system_active_for_play_controller(
        player_controller: PlayerController) -> bool
```

x.is_camera_system_active_for_play_controller(player_controller) -> bool
Returns whether this component's actor is set as the view target for the given player.

Args:
    player_controller (PlayerController): 

Returns:
    bool:

<a id="unreal.GameplayCameraSystemComponent.deactivate_camera_system"></a>

#### deactivate_camera_system

```python
def deactivate_camera_system(next_view_target: Actor = None) -> None
```

x.deactivate_camera_system(next_view_target=None) -> None
Removes this component's actor from being the view target.

Args:
    next_view_target (Actor):

<a id="unreal.GameplayCameraSystemComponent.activate_camera_system_for_player_index"></a>

#### activate_camera_system_for_player_index

```python
def activate_camera_system_for_player_index(player_index: int) -> None
```

x.activate_camera_system_for_player_index(player_index) -> None
Sets this component's actor as the view target for the given player.

Args:
    player_index (int32):

<a id="unreal.GameplayCameraSystemComponent.activate_camera_system_for_player_controller"></a>

#### activate_camera_system_for_player_controller

```python
def activate_camera_system_for_player_controller(
        player_controller: PlayerController) -> None
```

x.activate_camera_system_for_player_controller(player_controller) -> None
Sets this component's actor as the view target for the given player.

Args:
    player_controller (PlayerController):

<a id="unreal.GameplayControlRotationComponent"></a>