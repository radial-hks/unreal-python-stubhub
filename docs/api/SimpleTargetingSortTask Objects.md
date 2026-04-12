## SimpleTargetingSortTask Objects

```python
class SimpleTargetingSortTask(TargetingSortTask_Base)
```

class: USimpleTargetingSortTask This is a blueprintable TargetingTask class made for reordering Targets in the results list. Override the GetScoreForTarget Blueprint Function to provide a score for each element and then Targets will be sorted by score.

**C++ Source:**

- **Plugin**: TargetingSystem
- **Module**: TargetingSystem
- **File**: SimpleTargetingSortTask.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ascending`` (bool):  [Read-Write]
- ``stable_sort`` (bool):  [Read-Write] Should this task use a (slightly slower) sorting algorithm that preserves the relative ordering of targets with equal scores?

<a id="unreal.SimpleTargetingSortTask.bp_get_score_for_target"></a>

#### bp\_get\_score\_for\_target

```python
def bp_get_score_for_target(targeting_handle: TargetingRequestHandle,
                            target_data: TargetingDefaultResultData) -> float
```

x.bp_get_score_for_target(targeting_handle, target_data) -> float
Called on every target to get a Score for sorting. This score will be added to the Score float in FTargetingDefaultResultData

Args:
    targeting_handle (TargetingRequestHandle): 
    target_data (TargetingDefaultResultData): 

Returns:
    float:

<a id="unreal.TargetingFilterTask_ActorClass"></a>