## DatasmithDeltaGenSceneImportData Objects

```python
class DatasmithDeltaGenSceneImportData(DatasmithFBXSceneImportData)
```

Datasmith Delta Gen Scene Import Data

**C++ Source:**

- **Plugin**: DatasmithContent
- **Module**: DatasmithContent
- **File**: DatasmithAssetImportData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_options`` (DatasmithImportBaseOptions):  [Read-Write]
- ``colorize_materials`` (bool):  [Read-Only]
- ``datasmith_import_info`` (DatasmithImportInfo):  [Read-Write]
- ``generate_lightmap_u_vs`` (bool):  [Read-Only]
- ``import_pos`` (bool):  [Read-Only]
- ``import_tml`` (bool):  [Read-Only]
- ``import_var`` (bool):  [Read-Only]
- ``intermediate_serialization`` (uint8):  [Read-Only] Corresponds to a EDatasmithFBXIntermediateSerializationType
- ``merge_nodes`` (bool):  [Read-Only]
- ``optimize_duplicated_nodes`` (bool):  [Read-Only]
- ``pos_path`` (str):  [Read-Only]
- ``remove_invisible_nodes`` (bool):  [Read-Only]
- ``simplify_node_hierarchy`` (bool):  [Read-Only]
- ``source_data`` (AssetImportInfo):  [Read-Only] Source file data describing the files that were used to import this asset.
- ``textures_dir`` (str):  [Read-Only]
- ``tml_path`` (str):  [Read-Only]
- ``var_path`` (str):  [Read-Only]

<a id="unreal.DatasmithVREDAssetImportData"></a>