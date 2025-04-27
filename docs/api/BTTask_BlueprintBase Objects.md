## BTTask_BlueprintBase Objects

```python
class BTTask_BlueprintBase(BTTaskNode)
```

Base class for blueprint based task nodes. Do NOT use it for creating native c++ classes!

When task receives Abort event, all latent actions associated this instance are being removed.
This prevents from resuming activity started by Execute, but does not handle external events.
Please use them safely (unregister at abort) and call IsTaskExecuting() when in doubt.

**C++ Source:**

- **Module**: AIModule
- **File**: BTTask_BlueprintBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``custom_description`` (str):  [Read-Write]
- ``ignore_restart_self`` (bool):  [Read-Write] if set, task search will be discarded when this task is selected to execute but is already running
- ``node_name`` (str):  [Read-Write] node name
- ``show_property_details`` (bool):  [Read-Write] show detailed information about properties
- ``tick_interval`` (IntervalCountdown):  [Read-Write] If any of the Tick functions is implemented, how often should they be ticked.
      Values < 0 mean 'every tick'.

<a id="unreal.BTTask_BlueprintBase.custom_description"></a>

#### custom_description

```python
@property
def custom_description() -> str
```

(str):  [Read-Write]

<a id="unreal.BTTask_BlueprintBase.custom_description"></a>

#### custom_description

```python
@custom_description.setter
def custom_description(value: str) -> None
```

<a id="unreal.BTTask_BlueprintBase.set_finish_on_message_with_id"></a>

#### set_finish_on_message_with_id

```python
def set_finish_on_message_with_id(message_name: Name,
                                  request_id: int = -1) -> None
```

x.set_finish_on_message_with_id(message_name, request_id=-1) -> None
task execution will be finished (with result 'Success') after receiving specified message with indicated ID

Args:
    message_name (Name): 
    request_id (int32):

<a id="unreal.BTTask_BlueprintBase.set_finish_on_message"></a>

#### set_finish_on_message

```python
def set_finish_on_message(message_name: Name) -> None
```

x.set_finish_on_message(message_name) -> None
task execution will be finished (with result 'Success') after receiving specified message

Args:
    message_name (Name):

<a id="unreal.BTTask_BlueprintBase.receive_tick_ai"></a>

#### receive_tick_ai

```python
def receive_tick_ai(owner_controller: AIController, controlled_pawn: Pawn,
                    delta_seconds: float) -> None
```

x.receive_tick_ai(owner_controller, controlled_pawn, delta_seconds) -> None
Alternative AI version of tick function.
see: ReceiveTick for more details
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_controller (AIController): 
    controlled_pawn (Pawn): 
    delta_seconds (float):

<a id="unreal.BTTask_BlueprintBase.receive_tick"></a>

#### receive_tick

```python
def receive_tick(owner_actor: Actor, delta_seconds: float) -> None
```

x.receive_tick(owner_actor, delta_seconds) -> None
tick function
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_actor (Actor): 
    delta_seconds (float):

<a id="unreal.BTTask_BlueprintBase.receive_execute_ai"></a>

#### receive_execute_ai

```python
def receive_execute_ai(owner_controller: AIController,
                       controlled_pawn: Pawn) -> None
```

x.receive_execute_ai(owner_controller, controlled_pawn) -> None
Alternative AI version of ReceiveExecute
see: ReceiveExecute for more details
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_controller (AIController): 
    controlled_pawn (Pawn):

<a id="unreal.BTTask_BlueprintBase.receive_execute"></a>

#### receive_execute

```python
def receive_execute(owner_actor: Actor) -> None
```

x.receive_execute(owner_actor) -> None
entry point, task will stay active until FinishExecute is called.
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_actor (Actor):

<a id="unreal.BTTask_BlueprintBase.receive_abort_ai"></a>

#### receive_abort_ai

```python
def receive_abort_ai(owner_controller: AIController,
                     controlled_pawn: Pawn) -> None
```

x.receive_abort_ai(owner_controller, controlled_pawn) -> None
Alternative AI version of ReceiveAbort
see: ReceiveAbort for more details
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_controller (AIController): 
    controlled_pawn (Pawn):

<a id="unreal.BTTask_BlueprintBase.receive_abort"></a>

#### receive_abort

```python
def receive_abort(owner_actor: Actor) -> None
```

x.receive_abort(owner_actor) -> None
if blueprint graph contains this event, task will stay active until FinishAbort is called
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_actor (Actor):

<a id="unreal.BTTask_BlueprintBase.is_task_executing"></a>

#### is_task_executing

```python
def is_task_executing() -> bool
```

x.is_task_executing() -> bool
check if task is currently being executed

Returns:
    bool:

<a id="unreal.BTTask_BlueprintBase.is_task_aborting"></a>

#### is_task_aborting

```python
def is_task_aborting() -> bool
```

x.is_task_aborting() -> bool
check if task is currently being aborted

Returns:
    bool:

<a id="unreal.BTTask_BlueprintBase.finish_execute"></a>

#### finish_execute

```python
def finish_execute(success: bool) -> None
```

x.finish_execute(success) -> None
finishes task execution with Success or Fail result

Args:
    success (bool):

<a id="unreal.BTTask_BlueprintBase.finish_abort"></a>

#### finish_abort

```python
def finish_abort() -> None
```

x.finish_abort() -> None
aborts task execution

<a id="unreal.AIHelperLibrary"></a>