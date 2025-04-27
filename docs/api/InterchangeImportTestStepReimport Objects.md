## InterchangeImportTestStepReimport Objects

```python
class InterchangeImportTestStepReimport(InterchangeImportTestStepBase)
```

Interchange Import Test Step Reimport

**C++ Source:**

- **Plugin**: InterchangeTests
- **Module**: InterchangeTests
- **File**: InterchangeImportTestStepReimport.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_name_to_reimport`` (str):  [Read-Write] If there were multiple assets of the above type imported, specify the concrete name here.
- ``asset_type_to_reimport`` (type(Class)):  [Read-Write] The type of the asset to reimport. If only one such asset was imported, this is unambiguous.
- ``save_then_reload_imported_assets`` (bool):  [Read-Write] Determines whether imported assets should be saved and freshly reloaded after import.
- ``source_file_to_reimport`` (FilePath):  [Read-Write] The source file to import (path relative to the json script).
- ``tests`` (Array[InterchangeTestFunction]):  [Read-Write] An array of results to check against

<a id="unreal.InterchangeImportTestPlanFactory"></a>