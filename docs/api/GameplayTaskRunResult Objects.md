## GameplayTaskRunResult Objects

```python
class GameplayTaskRunResult(EnumBase)
```

EGameplay Task Run Result

**C++ Source:**

- **Module**: GameplayTasks
- **File**: GameplayTasksComponent.h

<a id="unreal.GameplayTaskRunResult.ERROR"></a>

#### ERROR

0: When tried running a null-task

<a id="unreal.GameplayTaskRunResult.FAILED"></a>

#### FAILED

1

<a id="unreal.GameplayTaskRunResult.SUCCESS_PAUSED"></a>

#### SUCCESS_PAUSED

2: Successfully registered for running, but currently paused due to higher priority tasks running

<a id="unreal.GameplayTaskRunResult.SUCCESS_ACTIVE"></a>

#### SUCCESS_ACTIVE

3: Successfully activated

<a id="unreal.GameplayTaskRunResult.SUCCESS_FINISHED"></a>

#### SUCCESS_FINISHED

4: Successfully activated, but finished instantly

<a id="unreal.AIRequestPriority"></a>