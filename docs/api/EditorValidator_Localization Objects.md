## EditorValidator_Localization Objects

```python
class EditorValidator_Localization(EditorValidatorBase)
```

* Validates that localized assets (within the L10N folder) conform to a corresponding source asset of the correct type.
* Localized assets that fail this validation will never be loaded as localized variants at runtime.

**C++ Source:**

- **Plugin**: DataValidation
- **Module**: DataValidation
- **File**: EditorValidator_Localization.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_enabled`` (bool):  [Read-Write]
- ``only_print_custom_message`` (bool):  [Read-Write] Whether we should also print out the source validator when printing validation errors.

<a id="unreal.PackageFileValidator"></a>