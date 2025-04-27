## TestBTDecorator_Blueprint Objects

```python
class TestBTDecorator_Blueprint(BTDecorator_BlueprintBase)
```

Test BTDecorator Blueprint

**C++ Source:**

- **Module**: AITestSuite
- **File**: TestBTDecorator_Blueprint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``check_condition_only_black_board_changes`` (bool):  [Read-Write] Applies only if Decorator has any FBlackboardKeySelector property and if decorator is
      set to abort BT flow. Is set to true ReceiveConditionCheck will be called only on changes
     to observed BB keys. If false or no BB keys observed ReceiveConditionCheck will be called every tick
- ``custom_description`` (str):  [Read-Write]
- ``flow_abort_mode`` (BTFlowAbortMode):  [Read-Write] flow controller settings
- ``inverse_condition`` (bool):  [Read-Write] if set, condition check result will be inversed
- ``node_name`` (str):  [Read-Write] node name
- ``show_property_details`` (bool):  [Read-Write] show detailed information about properties

<a id="unreal.MockTask_Log"></a>