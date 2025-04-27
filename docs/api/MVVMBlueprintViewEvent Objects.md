## MVVMBlueprintViewEvent Objects

```python
class MVVMBlueprintViewEvent(Object)
```

Binding for an event that MVVM will listen too. Does not imply
the MVVM graph itself will use events.

Ex: UButton::OnClick

**C++ Source:**

- **Plugin**: ModelViewViewModel
- **Module**: ModelViewViewModelBlueprint
- **File**: MVVMBlueprintViewEvent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``compile`` (bool):  [Read-Write] The event is visible in the editor, but is not compiled and cannot be used at runtime.
- ``destination_path`` (MVVMBlueprintPropertyPath):  [Read-Only]
- ``enabled`` (bool):  [Read-Write] Whether the event is enabled or disabled by default. The instance may enable the event at runtime.
- ``event_key`` (MVVMViewClass_EventKey):  [Read-Only]
- ``event_path`` (MVVMBlueprintPropertyPath):  [Read-Only]
- ``graph_name`` (Name):  [Read-Only]
- ``saved_pins`` (Array[MVVMBlueprintPin]):  [Read-Only] The pin that are modified and we saved data.
  The data may not be modified. We used the default value of the K2Node in that case.

<a id="unreal.MVVMBlueprintViewCondition"></a>