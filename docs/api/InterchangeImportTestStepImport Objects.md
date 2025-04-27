## InterchangeImportTestStepImport Objects

```python
class InterchangeImportTestStepImport(InterchangeImportTestStepBase)
```

Interchange Import Test Step Import

**C++ Source:**

- **Plugin**: InterchangeTests
- **Module**: InterchangeTests
- **File**: InterchangeImportTestStepImport.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``empty_destination_folder_prior_to_import`` (bool):  [Read-Write] Whether the destination folder should be emptied prior to import
- ``import_into_level`` (bool):  [Read-Write] Whether we should use the import into level workflow
- ``pipeline_stack`` (Array[InterchangePipelineBase]):  [Read-Write] The pipeline stack to use when importing (an empty array will use the defaults)
- ``save_then_reload_imported_assets`` (bool):  [Read-Write] Whether imported assets should be saved and freshly reloaded after import
- ``source_file`` (FilePath):  [Read-Write] The source file to import (path relative to the json script)
- ``tests`` (Array[InterchangeTestFunction]):  [Read-Write] An array of results to check against

<a id="unreal.InterchangeImportTestStepReimport"></a>