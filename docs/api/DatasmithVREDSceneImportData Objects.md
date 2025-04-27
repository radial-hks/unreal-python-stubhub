## DatasmithVREDSceneImportData Objects

```python
class DatasmithVREDSceneImportData(DatasmithFBXSceneImportData)
```

Datasmith VREDScene Import Data

**C++ Source:**

- **Plugin**: DatasmithContent
- **Module**: DatasmithContent
- **File**: DatasmithAssetImportData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_options`` (DatasmithImportBaseOptions):  [Read-Write]
- ``clean_var`` (bool):  [Read-Only]
- ``clip_info_path`` (str):  [Read-Only]
- ``colorize_materials`` (bool):  [Read-Only]
- ``datasmith_import_info`` (DatasmithImportInfo):  [Read-Write]
- ``generate_lightmap_u_vs`` (bool):  [Read-Only]
- ``import_clip_info`` (bool):  [Read-Only]
- ``import_light_info`` (bool):  [Read-Only]
- ``import_mats`` (bool):  [Read-Only]
- ``import_var`` (bool):  [Read-Only]
- ``intermediate_serialization`` (uint8):  [Read-Only] Corresponds to a EDatasmithFBXIntermediateSerializationType
- ``light_info_path`` (str):  [Read-Only]
- ``mats_path`` (str):  [Read-Only]
- ``merge_nodes`` (bool):  [Read-Only]
- ``optimize_duplicated_nodes`` (bool):  [Read-Only]
- ``source_data`` (AssetImportInfo):  [Read-Only] Source file data describing the files that were used to import this asset.
- ``textures_dir`` (str):  [Read-Only]
- ``var_path`` (str):  [Read-Only]

<a id="unreal.DatasmithUserData"></a>