## DatasmithAssetImportData Objects

```python
class DatasmithAssetImportData(AssetImportData)
```

Datasmith Asset Import Data

**C++ Source:**

- **Plugin**: DatasmithContent
- **Module**: DatasmithContent
- **File**: DatasmithAssetImportData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_data`` (Array[DatasmithAdditionalData]):  [Read-Write]
- ``asset_import_options`` (DatasmithAssetImportOptions):  [Read-Write]
- ``datasmith_import_info`` (DatasmithImportInfo):  [Read-Write]
- ``source_data`` (AssetImportInfo):  [Read-Only] Source file data describing the files that were used to import this asset.

<a id="unreal.DatasmithAssetImportData.asset_import_options"></a>

#### asset_import_options

```python
@property
def asset_import_options() -> DatasmithAssetImportOptions
```

(DatasmithAssetImportOptions):  [Read-Write]

<a id="unreal.DatasmithAssetImportData.asset_import_options"></a>

#### asset_import_options

```python
@asset_import_options.setter
def asset_import_options(value: DatasmithAssetImportOptions) -> None
```

<a id="unreal.DatasmithStaticMeshImportData"></a>