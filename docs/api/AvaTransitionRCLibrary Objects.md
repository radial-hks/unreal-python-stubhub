## AvaTransitionRCLibrary Objects

```python
class AvaTransitionRCLibrary(BlueprintFunctionLibrary)
```

Ava Transition RCLibrary

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: Avalanche
- **File**: AvaTransitionRCLibrary.h

<a id="unreal.AvaTransitionRCLibrary.get_changed_rc_controllers"></a>

#### get_changed_rc_controllers

```python
@classmethod
def get_changed_rc_controllers(
        cls, transition_node: Object) -> Array[RCVirtualPropertyBase]
```

X.get_changed_rc_controllers(transition_node) -> Array[RCVirtualPropertyBase]
Get Changed RCControllers

Args:
    transition_node (Object): 

Returns:
    Array[RCVirtualPropertyBase]:

<a id="unreal.AvaTransitionRCLibrary.compare_rc_controller_values"></a>

#### compare_rc_controller_values

```python
@classmethod
def compare_rc_controller_values(
    cls,
    transition_node: Object,
    controller_id: AvaRCControllerId,
    value_comparison_type:
    AvaTransitionComparisonResult = AvaTransitionComparisonResult.DIFFERENT
) -> bool
```

X.compare_rc_controller_values(transition_node, controller_id, value_comparison_type=AvaTransitionComparisonResult.DIFFERENT) -> bool
Compare RCController Values

Args:
    transition_node (Object): 
    controller_id (AvaRCControllerId): 
    value_comparison_type (AvaTransitionComparisonResult): 

Returns:
    bool:

<a id="unreal.AvaGizmoObjectInterface"></a>