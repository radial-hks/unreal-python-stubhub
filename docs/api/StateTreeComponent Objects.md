## StateTreeComponent Objects

```python
class StateTreeComponent(BrainComponent)
```

State Tree Component

**C++ Source:**

- **Plugin**: GameplayStateTree
- **Module**: GameplayStateTreeModule
- **File**: StateTreeComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``linked_state_tree_overrides`` (StateTreeReferenceOverrides):  [Read-Write] Overrides for linked State Trees. This table is used to override State Tree references on linked states.
  If a linked state's tag is exact match of the tag specified on the table, the reference from the table is used instead.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``on_state_tree_run_status_changed`` (StateTreeRunStatusChanged):  [Read-Write] Called when the run status of the StateTree has changed
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``start_logic_automatically`` (bool):  [Read-Write] If true, the StateTree logic is started on begin play. Otherwise StartLogic() needs to be called.
- ``state_tree_ref`` (StateTreeReference):  [Read-Write] State Tree asset to run on the component.

<a id="unreal.StateTreeComponent.on_state_tree_run_status_changed"></a>

#### on\_state\_tree\_run\_status\_changed

```python
@property
def on_state_tree_run_status_changed() -> StateTreeRunStatusChanged
```

(StateTreeRunStatusChanged):  [Read-Write] Called when the run status of the StateTree has changed

<a id="unreal.StateTreeComponent.on_state_tree_run_status_changed"></a>

#### on\_state\_tree\_run\_status\_changed

```python
@on_state_tree_run_status_changed.setter
def on_state_tree_run_status_changed(value: StateTreeRunStatusChanged) -> None
```

<a id="unreal.StateTreeComponent.set_start_logic_automatically"></a>

#### set\_start\_logic\_automatically

```python
def set_start_logic_automatically(start_logic_automatically: bool) -> None
```

x.set_start_logic_automatically(start_logic_automatically) -> None
Sets whether the State Tree is started automatically on being play.
This function sets the bStartLogicAutomatically property, and should be used mostly from constructions sscripts.
If you wish to start the logic manually, call StartLogic().

Args:
    start_logic_automatically (bool):

<a id="unreal.StateTreeComponent.send_state_tree_event"></a>

#### send\_state\_tree\_event

```python
def send_state_tree_event(event: StateTreeEvent) -> None
```

x.send_state_tree_event(event) -> None
Sends event to the running StateTree.

Args:
    event (StateTreeEvent):

<a id="unreal.StateTreeComponent.get_state_tree_run_status"></a>

#### get\_state\_tree\_run\_status

```python
def get_state_tree_run_status() -> StateTreeRunStatus
```

x.get_state_tree_run_status() -> StateTreeRunStatus
Returns the current run status of the StateTree.

Returns:
    StateTreeRunStatus:

<a id="unreal.StateTreeBrainComponent"></a>