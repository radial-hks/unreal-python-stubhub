## PathFollowingComponent Objects

```python
class PathFollowingComponent(ActorComponent)
```

Path Following Component

**C++ Source:**

- **Module**: AIModule
- **File**: PathFollowingComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``movement_comp`` (NavMovementComponent):  [Read-Write]
  deprecated: MovementComp is deprecated, please use NavMovementInterface and the INavMoveInterface instead.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.PathFollowingComponent.movement_comp"></a>

#### movement_comp

```python
@property
def movement_comp() -> NavMovementComponent
```

(NavMovementComponent):  [Read-Write]
deprecated: MovementComp is deprecated, please use NavMovementInterface and the INavMoveInterface instead.

<a id="unreal.PathFollowingComponent.movement_comp"></a>

#### movement_comp

```python
@movement_comp.setter
def movement_comp(value: NavMovementComponent) -> None
```

<a id="unreal.PathFollowingComponent.get_path_destination"></a>

#### get_path_destination

```python
def get_path_destination() -> Vector
```

x.get_path_destination() -> Vector
Get Path Destination
deprecated: This function is now deprecated, please use AIController.GetImmediateMoveDestination instead

Returns:
    Vector:

<a id="unreal.PathFollowingComponent.get_path_action_type"></a>

#### get_path_action_type

```python
def get_path_action_type() -> PathFollowingAction
```

x.get_path_action_type() -> PathFollowingAction
Get Path Action Type
deprecated: This function is now deprecated, please use AIController.GetMoveStatus instead

Returns:
    PathFollowingAction:

<a id="unreal.CrowdFollowingComponent"></a>