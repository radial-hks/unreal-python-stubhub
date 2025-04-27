## MirrorDataTable Objects

```python
class MirrorDataTable(DataTable)
```

AutoExpandCategories = "MirrorDataTable,ImportOptions"

**C++ Source:**

- **Module**: Engine
- **File**: MirrorDataTable.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_data`` (AssetImportData):  [Read-Only] The file this data table was imported from, may be empty
- ``ignore_extra_fields`` (bool):  [Read-Write] Set to true to ignore extra fields in the import data, if false it will warn about them
- ``ignore_missing_fields`` (bool):  [Read-Write] Set to true to ignore any fields that are expected but missing, if false it will warn about them
- ``import_key_field`` (str):  [Read-Write] Explicit field in import data to use as key. If this is empty it uses Name for JSON and the first field found for CSV
- ``mirror_axis`` (AxisType):  [Read-Write]
- ``mirror_find_replace_expressions`` (Array[MirrorFindReplaceExpression]):  [Read-Write]
- ``mirror_root_motion`` (bool):  [Read-Write]
- ``preserve_existing_values`` (bool):  [Read-Write] Set to true to preserve existing values for any fields that are expected but missing in the CSV file. If false, missing fields will be populated with default values.
- ``row_struct`` (ScriptStruct):  [Read-Only] Structure to use for each row of the table, must inherit from FTableRowBase
- ``skeleton`` (Skeleton):  [Read-Write]
- ``strip_from_client_builds`` (bool):  [Read-Write] Set to true to not cook this data table into client builds. Useful for sensitive tables that only servers should know about.

<a id="unreal.NodeMappingContainer"></a>