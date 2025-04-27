## GameplayControlRotationComponent Objects

```python
class GameplayControlRotationComponent(ActorComponent)
```

An example component that works with the GameplayCameraComponent to manage a player's
control rotation when the camera changes or moves in a way that was not initiated
by the player themselves.

**C++ Source:**

- **Plugin**: GameplayCameras
- **Module**: GameplayCameras
- **File**: GameplayControlRotationComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``auto_activate_for_player`` (AutoReceiveInput):  [Read-Write] If AutoActivate is set, auto-activates control rotation management for the given player.
  This is equivalent to calling ActivateControlRotationManagement on BeginPlay.
- ``axis_action_angular_speed_threshold`` (float):  [Read-Write] The angular speed, in degrees per second, past which a change in the player input
  will thaw a frozen control rotation.
- ``axis_action_magnitude_threshold`` (float):  [Read-Write] The player input magnitude under which the frozen control rotation is thawed.
- ``axis_actions`` (Array[InputAction]):  [Read-Write] The axis input action(s) to read from.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.GameplayControlRotationComponent.auto_activate_for_player"></a>

#### auto_activate_for_player

```python
@property
def auto_activate_for_player() -> AutoReceiveInput
```

(AutoReceiveInput):  [Read-Write] If AutoActivate is set, auto-activates control rotation management for the given player.
This is equivalent to calling ActivateControlRotationManagement on BeginPlay.

<a id="unreal.GameplayControlRotationComponent.auto_activate_for_player"></a>

#### auto_activate_for_player

```python
@auto_activate_for_player.setter
def auto_activate_for_player(value: AutoReceiveInput) -> None
```

<a id="unreal.GameplayControlRotationComponent.deactivate_control_rotation_management"></a>

#### deactivate_control_rotation_management

```python
def deactivate_control_rotation_management() -> None
```

x.deactivate_control_rotation_management() -> None
Deactivates management of a player controller's control rotation.

<a id="unreal.GameplayControlRotationComponent.activate_control_rotation_management_for_player_index"></a>

#### activate_control_rotation_management_for_player_index

```python
def activate_control_rotation_management_for_player_index(
        player_index: int) -> None
```

x.activate_control_rotation_management_for_player_index(player_index) -> None
Activates management of a player controller's control rotation. The component will set
the control rotation every frame based on the latest camera system update.

Args:
    player_index (int32):

<a id="unreal.GameplayControlRotationComponent.activate_control_rotation_management_for_player_controller"></a>

#### activate_control_rotation_management_for_player_controller

```python
def activate_control_rotation_management_for_player_controller(
        player_controller: PlayerController) -> None
```

x.activate_control_rotation_management_for_player_controller(player_controller) -> None
Activates management of a player controller's control rotation. The component will set
the control rotation every frame based on the latest camera system update.

Args:
    player_controller (PlayerController):

<a id="unreal.BlueprintCameraNodeEvaluator"></a>