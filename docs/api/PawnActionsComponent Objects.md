## PawnActionsComponent Objects

```python
class PawnActionsComponent(ActorComponent)
```

Pawn Actions Component

**C++ Source:**

- **Module**: AIModule
- **File**: PawnActionsComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``controlled_pawn`` (Pawn):  [Read-Write]
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.PawnActionsComponent.controlled_pawn"></a>

#### controlled_pawn

```python
@property
def controlled_pawn() -> Pawn
```

(Pawn):  [Read-Only]

<a id="unreal.PawnActionsComponent.push_action"></a>

#### push_action

```python
def push_action(new_action: PawnAction,
                priority: AIRequestPriority,
                instigator: Object = None) -> bool
```

x.push_action(new_action, priority, instigator=None) -> bool
K2 Push Action
deprecated: PawnActions have been deprecated and are no longer being supported. It will get removed in following UE5 releases. Use GameplayTasks or AITasks instead.

Args:
    new_action (PawnAction): 
    priority (AIRequestPriority): 
    instigator (Object): 

Returns:
    bool:

<a id="unreal.PawnActionsComponent.perform_action"></a>

#### perform_action

```python
@classmethod
def perform_action(
        cls,
        pawn: Pawn,
        action: PawnAction,
        priority: AIRequestPriority = AIRequestPriority.HARD_SCRIPT) -> bool
```

X.perform_action(pawn, action, priority=AIRequestPriority.HARD_SCRIPT) -> bool
blueprint interface
deprecated: PawnActions have been deprecated and are no longer being supported. It will get removed in following UE5 releases. Use GameplayTasks or AITasks instead.

Args:
    pawn (Pawn): 
    action (PawnAction): 
    priority (AIRequestPriority): 

Returns:
    bool:

<a id="unreal.PawnActionsComponent.force_abort_action"></a>

#### force_abort_action

```python
def force_abort_action(action_to_abort: PawnAction) -> PawnActionAbortState
```

x.force_abort_action(action_to_abort) -> PawnActionAbortState
Aborts given action instance
deprecated: PawnActions have been deprecated and are no longer being supported. It will get removed in following UE5 releases. Use GameplayTasks or AITasks instead.

Args:
    action_to_abort (PawnAction): 

Returns:
    PawnActionAbortState:

<a id="unreal.PawnActionsComponent.abort_action"></a>

#### abort_action

```python
def abort_action(action_to_abort: PawnAction) -> PawnActionAbortState
```

x.abort_action(action_to_abort) -> PawnActionAbortState
Aborts given action instance
deprecated: PawnActions have been deprecated and are no longer being supported. It will get removed in following UE5 releases. Use GameplayTasks or AITasks instead.

Args:
    action_to_abort (PawnAction): 

Returns:
    PawnActionAbortState:

<a id="unreal.PawnAction_BlueprintBase"></a>