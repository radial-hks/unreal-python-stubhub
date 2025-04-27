## GameplayTask Objects

```python
class GameplayTask(Object)
```

Gameplay Task

**C++ Source:**

- **Module**: GameplayTasks
- **File**: GameplayTask.h

<a id="unreal.GameplayTask.end_task"></a>

#### end_task

```python
def end_task() -> None
```

x.end_task() -> None
Called explicitly to end the task (usually by the task itself). Calls OnDestroy.
NOTE:: you need to call EndTask before sending out any "on completed" delegates. If you don't the task will still be in an "active" state while the event receivers may assume it's already "finished"

<a id="unreal.GameplayTaskResource"></a>