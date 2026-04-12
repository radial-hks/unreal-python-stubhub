## AbilityTask\_PerformTargeting Objects

```python
class AbilityTask_PerformTargeting(AbilityTask)
```

Ability Task Perform Targeting

**C++ Source:**

- **Plugin**: TargetingSystem
- **Module**: TargetingSystem
- **File**: AbilityTask_PerformTargeting.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_target_ready`` (TargetReadyDelegate):  [Read-Write] Called when the targeting request has been completed and results are ready

<a id="unreal.AbilityTask_PerformTargeting.on_target_ready"></a>

#### on\_target\_ready

```python
@property
def on_target_ready() -> TargetReadyDelegate
```

(TargetReadyDelegate):  [Read-Write] Called when the targeting request has been completed and results are ready

<a id="unreal.AbilityTask_PerformTargeting.on_target_ready"></a>

#### on\_target\_ready

```python
@on_target_ready.setter
def on_target_ready(value: TargetReadyDelegate) -> None
```

<a id="unreal.AsyncAction_PerformTargeting"></a>