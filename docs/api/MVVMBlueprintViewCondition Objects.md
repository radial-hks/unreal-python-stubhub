## MVVMBlueprintViewCondition Objects

```python
class MVVMBlueprintViewCondition(Object)
```

Binding for an event that MVVM will listen too. Does not imply
the MVVM graph itself will use events.

Ex: UButton::OnClick

**C++ Source:**

- **Plugin**: ModelViewViewModel
- **Module**: ModelViewViewModelBlueprint
- **File**: MVVMBlueprintViewCondition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``compile`` (bool):  [Read-Write] The event is visible in the editor, but is not compiled and cannot be used at runtime.
- ``condition_key`` (MVVMViewClass_ConditionKey):  [Read-Only]
- ``condition_operation`` (MVVMConditionOperation):  [Read-Only]
- ``condition_path`` (MVVMBlueprintPropertyPath):  [Read-Only]
- ``destination_path`` (MVVMBlueprintPropertyPath):  [Read-Only]
- ``enabled`` (bool):  [Read-Write] Whether the event is enabled or disabled by default. The instance may enable the event at runtime.
- ``graph_name`` (Name):  [Read-Only]
- ``max_value`` (float):  [Read-Only]
- ``saved_pins`` (Array[MVVMBlueprintPin]):  [Read-Only] The pin that are modified and we saved data.
  The data may not be modified. We used the default value of the K2Node in that case.
- ``value`` (float):  [Read-Only]

<a id="unreal.K2Node_CallFunction"></a>