## EnhancedInputUserWidgetValidator Objects

```python
class EnhancedInputUserWidgetValidator(EditorValidatorBase)
```

Validates Widget Blueprints that have any Enhanced Input
nodes in them to ensure that they have the correct "bAutomaticallyRegisterInputOnConstruction"
setting value.

Widgets require bAutomaticallyRegisterInputOnConstruction to be true in order to
receive callbacks from Enhanced Input.

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: InputBlueprintNodes
- **File**: EnhancedInputUserWidgetValidator.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_enabled`` (bool):  [Read-Write]
- ``only_print_custom_message`` (bool):  [Read-Write] Whether we should also print out the source validator when printing validation errors.

<a id="unreal.TakeMetaData"></a>