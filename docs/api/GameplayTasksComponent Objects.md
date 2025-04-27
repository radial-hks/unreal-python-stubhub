## GameplayTasksComponent Objects

```python
class GameplayTasksComponent(ActorComponent)
```

The core ActorComponent for interfacing with the GameplayAbilities System

**C++ Source:**

- **Module**: GameplayTasks
- **File**: GameplayTasksComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_claimed_resources_change`` (OnClaimedResourcesChangeSignature):  [Read-Write]
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.GameplayTasksComponent.on_claimed_resources_change"></a>

#### on_claimed_resources_change

```python
@property
def on_claimed_resources_change() -> OnClaimedResourcesChangeSignature
```

(OnClaimedResourcesChangeSignature):  [Read-Write]

<a id="unreal.GameplayTasksComponent.on_claimed_resources_change"></a>

#### on_claimed_resources_change

```python
@on_claimed_resources_change.setter
def on_claimed_resources_change(
        value: OnClaimedResourcesChangeSignature) -> None
```

<a id="unreal.GameplayTasksComponent.run_gameplay_task"></a>

#### run_gameplay_task

```python
@classmethod
def run_gameplay_task(
        cls, task_owner: GameplayTaskOwnerInterface, task: GameplayTask,
        priority: int, additional_required_resources: Array[Class],
        additional_claimed_resources: Array[Class]) -> GameplayTaskRunResult
```

X.run_gameplay_task(task_owner, task, priority, additional_required_resources, additional_claimed_resources) -> GameplayTaskRunResult
K2 Run Gameplay Task

Args:
    task_owner (GameplayTaskOwnerInterface): 
    task (GameplayTask): 
    priority (uint8): 
    additional_required_resources (Array[type(Class)]): 
    additional_claimed_resources (Array[type(Class)]): 

Returns:
    GameplayTaskRunResult:

<a id="unreal.GameplayTask_ClaimResource"></a>