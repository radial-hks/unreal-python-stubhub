## StateTreeTaskBlueprintBase Objects

```python
class StateTreeTaskBlueprintBase(StateTreeNodeBlueprintBase)
```

* Base class for Blueprint based Tasks.

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeModule
- **File**: StateTreeTaskBlueprintBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``description`` (Text):  [Read-Write] Description of the node.
- ``icon_color`` (Color):  [Read-Write] Color of the icon.
- ``icon_name`` (Name):  [Read-Write] Name of the icon in format:
               StyleSetName | StyleName [ | SmallStyleName | StatusOverlayStyleName]
               SmallStyleName and StatusOverlayStyleName are optional.
               Example: "StateTreeEditorStyle|Node.Animation"
- ``should_call_tick_only_on_events`` (bool):  [Read-Write] If set to true, Tick() is called. Default false.
- ``should_copy_bound_properties_on_exit_state`` (bool):  [Read-Write] If set to true, copy the values of bound properties before calling ExitState(). Default true.
- ``should_copy_bound_properties_on_tick`` (bool):  [Read-Write] If set to true, copy the values of bound properties before calling Tick(). Default true.
- ``should_state_change_on_reselect`` (bool):  [Read-Write] If set to true, the task will receive EnterState/ExitState even if the state was previously active.
  Generally this should be true for action type tasks, like playing animation,
  and false on state like tasks like claiming a resource that is expected to be acquired on child states.

<a id="unreal.StateTreeTaskBlueprintBase.receive_tick"></a>

#### receive_tick

```python
def receive_tick(delta_time: float) -> StateTreeRunStatus
```

x.receive_tick(delta_time) -> StateTreeRunStatus
Receive Tick
deprecated: Use the new Tick event without without return value instead. Task status is now controlled via FinishTask node, instead of a return value. Default status is running.

Args:
    delta_time (float): 

Returns:
    StateTreeRunStatus:

<a id="unreal.StateTreeTaskBlueprintBase.receive_state_completed"></a>

#### receive_state_completed

```python
def receive_state_completed(
        completion_status: StateTreeRunStatus,
        completed_active_states: StateTreeActiveStates) -> None
```

x.receive_state_completed(completion_status, completed_active_states) -> None
Called right after a state has been completed, but before new state has been selected. StateCompleted is called in reverse order to allow to propagate state to other Tasks that
are executed earlier in the tree. Note that StateCompleted is not called if conditional transition changes the state.

Args:
    completion_status (StateTreeRunStatus): Describes the running status of the completed state (Succeeded/Failed).
    completed_active_states (StateTreeActiveStates): Active states at the time of completion.

<a id="unreal.StateTreeTaskBlueprintBase.receive_latent_tick"></a>

#### receive_latent_tick

```python
def receive_latent_tick(delta_time: float) -> None
```

x.receive_latent_tick(delta_time) -> None
Called during state tree tick when the task is on active state.
Use FinishTask() to set the task execution completed. State completion is controlled by completed tasks.

Triggering GameplayTasks and other latent action should generally be done on EnterState. Tick is called on each update (or event)
and can cause huge amount of task added if the logic is not handled carefully.
Tick should be generally be used for monitoring that require polling, or actions that require constant ticking.

Note: The method is called only if bShouldCallTick or bShouldCallTickOnlyOnEvents is set.

Args:
    delta_time (float): Time since last StateTree tick.

<a id="unreal.StateTreeTaskBlueprintBase.receive_latent_enter_state"></a>

#### receive_latent_enter_state

```python
def receive_latent_enter_state(transition: StateTreeTransitionResult) -> None
```

x.receive_latent_enter_state(transition) -> None
Called when a new state is entered and task is part of active states.
Use FinishTask() to set the task execution completed. State completion is controlled by completed tasks.

GameplayTasks and other latent actions should be generally triggered on EnterState. When using a GameplayTasks it's required
to manually cancel active tasks on ExitState if the GameplayTask's lifetime is tied to the State Tree task.

Args:
    transition (StateTreeTransitionResult): Describes the states involved in the transition

<a id="unreal.StateTreeTaskBlueprintBase.receive_exit_state"></a>

#### receive_exit_state

```python
def receive_exit_state(transition: StateTreeTransitionResult) -> None
```

x.receive_exit_state(transition) -> None
Called when a current state is exited and task is part of active states.

Args:
    transition (StateTreeTransitionResult): Describes the states involved in the transition

<a id="unreal.StateTreeTaskBlueprintBase.receive_enter_state"></a>

#### receive_enter_state

```python
def receive_enter_state(
        transition: StateTreeTransitionResult) -> StateTreeRunStatus
```

x.receive_enter_state(transition) -> StateTreeRunStatus
Receive Enter State
deprecated: Use the new EnterState event without without return value instead. Task status is now controlled via FinishTask node, instead of a return value. Default status is running.

Args:
    transition (StateTreeTransitionResult): 

Returns:
    StateTreeRunStatus:

<a id="unreal.StateTreeTaskBlueprintBase.finish_task"></a>

#### finish_task

```python
def finish_task(succeeded: bool = True) -> None
```

x.finish_task(succeeded=True) -> None
Finish the task and sets it's status.

Args:
    succeeded (bool):

<a id="unreal.StateTree"></a>