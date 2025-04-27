## GameplayTask_TimeLimitedExecution Objects

```python
class GameplayTask_TimeLimitedExecution(GameplayTask)
```

Adds time limit for running a child task
- child task needs to be created with UGameplayTask_TimeLimitedExecution passed as TaskOwner
- activations are tied together and when either UGameplayTask_TimeLimitedExecution or child task is activated, other one starts as well
- OnFinished and OnTimeExpired are mutually exclusive

**C++ Source:**

- **Module**: GameplayTasks
- **File**: GameplayTask_TimeLimitedExecution.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_finished`` (TaskFinishDelegate):  [Read-Write] called when child task finishes execution before time runs out
- ``on_time_expired`` (TaskFinishDelegate):  [Read-Write] called when time runs out

<a id="unreal.GameplayTask_TimeLimitedExecution.on_finished"></a>

#### on_finished

```python
@property
def on_finished() -> TaskFinishDelegate
```

(TaskFinishDelegate):  [Read-Write] called when child task finishes execution before time runs out

<a id="unreal.GameplayTask_TimeLimitedExecution.on_finished"></a>

#### on_finished

```python
@on_finished.setter
def on_finished(value: TaskFinishDelegate) -> None
```

<a id="unreal.GameplayTask_TimeLimitedExecution.on_time_expired"></a>

#### on_time_expired

```python
@property
def on_time_expired() -> TaskFinishDelegate
```

(TaskFinishDelegate):  [Read-Write] called when time runs out

<a id="unreal.GameplayTask_TimeLimitedExecution.on_time_expired"></a>

#### on_time_expired

```python
@on_time_expired.setter
def on_time_expired(value: TaskFinishDelegate) -> None
```

<a id="unreal.GameplayTask_WaitDelay"></a>