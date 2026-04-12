## TargetingSortTask\_Base Objects

```python
class TargetingSortTask_Base(TargetingTask)
```

class: TargetingSortTask_Base A base class that has the basic setup for a sort task.

**C++ Source:**

- **Plugin**: TargetingSystem
- **Module**: TargetingSystem
- **File**: TargetingSortTask_Base.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ascending`` (bool):  [Read-Write]
- ``stable_sort`` (bool):  [Read-Write] Should this task use a (slightly slower) sorting algorithm that preserves the relative ordering of targets with equal scores?

<a id="unreal.SimpleTargetingSortTask"></a>