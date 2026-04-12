## TargetingPreset Objects

```python
class TargetingPreset(DataAsset)
```

class: UTargetingPreset This object is used when a data asset is preferred for task setup. Tasks will be processed in the order they are setup in the task set. It is recommended that selection tasks happen first before any filtering and sorting.

**C++ Source:**

- **Plugin**: TargetingSystem
- **Module**: TargetingSystem
- **File**: TargetingPreset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``targeting_task_set`` (TargetingTaskSet):  [Read-Write] The tasks that make up this targeting preset

<a id="unreal.TargetingPreset.targeting_task_set"></a>

#### targeting\_task\_set

```python
@property
def targeting_task_set() -> TargetingTaskSet
```

(TargetingTaskSet):  [Read-Write] The tasks that make up this targeting preset

<a id="unreal.TargetingPreset.targeting_task_set"></a>

#### targeting\_task\_set

```python
@targeting_task_set.setter
def targeting_task_set(value: TargetingTaskSet) -> None
```

<a id="unreal.TargetingSelectionTask_AOE"></a>