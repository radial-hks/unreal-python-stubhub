## DirtyFilesChangelistValidator Objects

```python
class DirtyFilesChangelistValidator(EditorValidatorBase)
```

Validates there is no unsaved files in the changelist about to be submitted.

**C++ Source:**

- **Plugin**: DataValidation
- **Module**: DataValidation
- **File**: DirtyFilesChangelistValidator.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_enabled`` (bool):  [Read-Write]
- ``only_print_custom_message`` (bool):  [Read-Write] Whether we should also print out the source validator when printing validation errors.

<a id="unreal.EditorValidatorSubsystem"></a>