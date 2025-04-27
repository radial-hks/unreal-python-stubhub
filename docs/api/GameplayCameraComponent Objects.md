## GameplayCameraComponent Objects

```python
class GameplayCameraComponent(SceneComponent)
```

A component that can run a camera asset inside its own camera evaluation context.

**C++ Source:**

- **Plugin**: GameplayCameras
- **Module**: GameplayCameras
- **File**: GameplayCameraComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``auto_activate_for_player`` (AutoReceiveInput):  [Read-Write] If AutoActivate is set, auto-activates this component's camera for the given player.
  This is equivalent to calling ActivateCamera on BeginPlay.
- ``camera`` (CameraAsset):  [Read-Write] The camera asset to run.
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
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.GameplayCameraComponent.camera"></a>

#### camera

```python
@property
def camera() -> CameraAsset
```

(CameraAsset):  [Read-Write] The camera asset to run.

<a id="unreal.GameplayCameraComponent.camera"></a>

#### camera

```python
@camera.setter
def camera(value: CameraAsset) -> None
```

<a id="unreal.GameplayCameraComponent.auto_activate_for_player"></a>

#### auto_activate_for_player

```python
@property
def auto_activate_for_player() -> AutoReceiveInput
```

(AutoReceiveInput):  [Read-Write] If AutoActivate is set, auto-activates this component's camera for the given player.
This is equivalent to calling ActivateCamera on BeginPlay.

<a id="unreal.GameplayCameraComponent.auto_activate_for_player"></a>

#### auto_activate_for_player

```python
@auto_activate_for_player.setter
def auto_activate_for_player(value: AutoReceiveInput) -> None
```

<a id="unreal.GameplayCameraComponent.set_initial_pose"></a>

#### set_initial_pose

```python
def set_initial_pose(camera_pose: BlueprintCameraPose) -> None
```

x.set_initial_pose(camera_pose) -> None
Sets the initial camera pose for this component's camera evaluation context.

Args:
    camera_pose (BlueprintCameraPose):

<a id="unreal.GameplayCameraComponent.get_initial_variable_table"></a>

#### get_initial_variable_table

```python
def get_initial_variable_table() -> BlueprintCameraVariableTable
```

x.get_initial_variable_table() -> BlueprintCameraVariableTable
Gets the initial camera variable table for this component's camera evaluation context.

Returns:
    BlueprintCameraVariableTable:

<a id="unreal.GameplayCameraComponent.get_initial_pose"></a>

#### get_initial_pose

```python
def get_initial_pose() -> BlueprintCameraPose
```

x.get_initial_pose() -> BlueprintCameraPose
Gets the initial camera pose for this component's camera evaluation context.

Returns:
    BlueprintCameraPose:

<a id="unreal.GameplayCameraComponent.deactivate_camera"></a>

#### deactivate_camera

```python
def deactivate_camera() -> None
```

x.deactivate_camera() -> None
Deactivates the camera for the last player it was activated for.

<a id="unreal.GameplayCameraComponent.activate_camera_for_player_index"></a>

#### activate_camera_for_player_index

```python
def activate_camera_for_player_index(player_index: int) -> None
```

x.activate_camera_for_player_index(player_index) -> None
Activates the camera for the given player.

Args:
    player_index (int32):

<a id="unreal.GameplayCameraComponent.activate_camera_for_player_controller"></a>

#### activate_camera_for_player_controller

```python
def activate_camera_for_player_controller(
        player_controller: PlayerController) -> None
```

x.activate_camera_for_player_controller(player_controller) -> None
Activates the camera for the given player.

Args:
    player_controller (PlayerController):

<a id="unreal.GameplayCameraSystemActor"></a>