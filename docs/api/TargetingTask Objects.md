## TargetingTask Objects

```python
class TargetingTask(Object)
```

class: UTargetingTask The base object type that all Targeting Tasks will derive from. The idea is the targeting system will take target requests that are collections of target tasks that will potentially generate/remove and perform operations on sets of targeting results data. Potential Task Implementations: Selection Tasks: Target selection tasks would be used to build up a collection of target request results. It is recommend they are added first in the targeting request. Things like ray casts, AOE shapes, actors under a reticle, etc are cases that generally fall under selection. Filtering Tasks: Target filtering tasks are used to reduce the target result data set to those targets that match a given criteria. Things like actor class, team distance, facing, etc. Sorting Tasks: Target sorting tasks would be useful to take the set and put them in an order the end user might prefer to make decisions on. Distance (min/max), score rating etc.

**C++ Source:**

- **Plugin**: TargetingSystem
- **Module**: TargetingSystem
- **File**: TargetingTask.h

<a id="unreal.TargetingTask.get_targeting_subsystem"></a>

#### get\_targeting\_subsystem

```python
def get_targeting_subsystem(
        targeting_handle: TargetingRequestHandle) -> TargetingSubsystem
```

x.get_targeting_subsystem(targeting_handle) -> TargetingSubsystem
Helper method to get the Targeting Subsystem in TargetingTask Blueprint Types

Args:
    targeting_handle (TargetingRequestHandle): 

Returns:
    TargetingSubsystem:

<a id="unreal.TargetingFilterTask_BasicFilterTemplate"></a>