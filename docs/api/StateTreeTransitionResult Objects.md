## StateTreeTransitionResult Objects

```python
class StateTreeTransitionResult(StructBase)
```

Describes a state tree transition. Source is the state where the transition started, Target describes the state where the transition pointed at,
and Next describes the selected state. The reason Transition and Next are different is that Transition state can be a selector state,
in which case the children will be visited until a leaf state is found, which will be the next state.

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeModule
- **File**: StateTreeExecutionTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``change_type`` (StateTreeStateChangeType):  [Read-Write] If the change type is Sustained, then the CurrentState was reselected, or if Changed then the state was just activated.
- ``current_run_status`` (StateTreeRunStatus):  [Read-Write] Current Run status.
- ``current_state`` (StateTreeStateHandle):  [Read-Write] The current state being executed. On enter/exit callbacks this is the state of the task.
- ``next_active_frames`` (Array[StateTreeExecutionFrame]):  [Read-Write] States selected as result of the transition.
- ``priority`` (StateTreeTransitionPriority):  [Read-Write] Priority of the transition that caused the state change.
- ``source_root_state`` (StateTreeStateHandle):  [Read-Write] Root state the execution frame where the transition was requested.
- ``source_state`` (StateTreeStateHandle):  [Read-Write] Transition source state.
- ``source_state_tree`` (StateTree):  [Read-Write] StateTree asset that was active when the transition was requested.
- ``target_state`` (StateTreeStateHandle):  [Read-Write] Transition target state.

<a id="unreal.StateTreeTransitionResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        next_active_frames: Array[StateTreeExecutionFrame] = [],
        current_run_status: StateTreeRunStatus = StateTreeRunStatus.RUNNING,
        source_state: StateTreeStateHandle = [],
        target_state: StateTreeStateHandle = [],
        current_state: StateTreeStateHandle = [],
        change_type: StateTreeStateChangeType = StateTreeStateChangeType.NONE,
        priority: StateTreeTransitionPriority = 0,
        source_state_tree: StateTree = None,
        source_root_state: StateTreeStateHandle = []) -> None
```

<a id="unreal.StateTreeTransitionResult.next_active_frames"></a>

#### next\_active\_frames

```python
@property
def next_active_frames() -> Array[StateTreeExecutionFrame]
```

(Array[StateTreeExecutionFrame]):  [Read-Only] States selected as result of the transition.

<a id="unreal.StateTreeTransitionResult.current_run_status"></a>

#### current\_run\_status

```python
@property
def current_run_status() -> StateTreeRunStatus
```

(StateTreeRunStatus):  [Read-Only] Current Run status.

<a id="unreal.StateTreeTransitionResult.source_state"></a>

#### source\_state

```python
@property
def source_state() -> StateTreeStateHandle
```

(StateTreeStateHandle):  [Read-Only] Transition source state.

<a id="unreal.StateTreeTransitionResult.target_state"></a>

#### target\_state

```python
@property
def target_state() -> StateTreeStateHandle
```

(StateTreeStateHandle):  [Read-Only] Transition target state.

<a id="unreal.StateTreeTransitionResult.current_state"></a>

#### current\_state

```python
@property
def current_state() -> StateTreeStateHandle
```

(StateTreeStateHandle):  [Read-Only] The current state being executed. On enter/exit callbacks this is the state of the task.

<a id="unreal.StateTreeTransitionResult.change_type"></a>

#### change\_type

```python
@property
def change_type() -> StateTreeStateChangeType
```

(StateTreeStateChangeType):  [Read-Only] If the change type is Sustained, then the CurrentState was reselected, or if Changed then the state was just activated.

<a id="unreal.StateTreeTransitionResult.priority"></a>

#### priority

```python
@property
def priority() -> StateTreeTransitionPriority
```

(StateTreeTransitionPriority):  [Read-Only] Priority of the transition that caused the state change.

<a id="unreal.StateTreeTransitionResult.source_state_tree"></a>

#### source\_state\_tree

```python
@property
def source_state_tree() -> StateTree
```

(StateTree):  [Read-Only] StateTree asset that was active when the transition was requested.

<a id="unreal.StateTreeTransitionResult.source_root_state"></a>

#### source\_root\_state

```python
@property
def source_root_state() -> StateTreeStateHandle
```

(StateTreeStateHandle):  [Read-Only] Root state the execution frame where the transition was requested.

<a id="unreal.StateTreeEvent"></a>