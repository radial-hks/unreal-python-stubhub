## SimpleTargetingFilterTask Objects

```python
class SimpleTargetingFilterTask(TargetingFilterTask_BasicFilterTemplate)
```

class: USimpleTargetingSelectionTask This is a blueprintable TargetingTask class made for filtering out Targets from the results list. Override the ShouldRemoveTarget Blueprint Function to define the rules for this filter.

**C++ Source:**

- **Plugin**: TargetingSystem
- **Module**: TargetingSystem
- **File**: SimpleTargetingFilterTask.h

<a id="unreal.SimpleTargetingFilterTask.bp_should_filter_target"></a>

#### bp\_should\_filter\_target

```python
def bp_should_filter_target(targeting_handle: TargetingRequestHandle,
                            target_data: TargetingDefaultResultData) -> bool
```

x.bp_should_filter_target(targeting_handle, target_data) -> bool
Returns true if a Target should be removed from the results of this TargetingRequest

Args:
    targeting_handle (TargetingRequestHandle): 
    target_data (TargetingDefaultResultData): 

Returns:
    bool:

<a id="unreal.SimpleTargetingSelectionTask"></a>