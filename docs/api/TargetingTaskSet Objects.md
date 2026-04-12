## TargetingTaskSet Objects

```python
class TargetingTaskSet(StructBase)
```

struct: FTargetingTaskSet A set of tasks to be used by targeting requests to find/processes targets

**C++ Source:**

- **Plugin**: TargetingSystem
- **Module**: TargetingSystem
- **File**: TargetingSystemTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``tasks`` (Array[TargetingTask]):  [Read-Write] The set of tasks that will be used to satisfy a targeting request

<a id="unreal.TargetingTaskSet.__init__"></a>

#### \_\_init\_\_

```python
def __init__(tasks: Array[TargetingTask] = []) -> None
```

<a id="unreal.TargetingTaskSet.tasks"></a>

#### tasks

```python
@property
def tasks() -> Array[TargetingTask]
```

(Array[TargetingTask]):  [Read-Write] The set of tasks that will be used to satisfy a targeting request

<a id="unreal.TargetingTaskSet.tasks"></a>

#### tasks

```python
@tasks.setter
def tasks(value: Array[TargetingTask]) -> None
```

<a id="unreal.TargetingDefaultResultData"></a>