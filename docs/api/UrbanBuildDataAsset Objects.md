## UrbanBuildDataAsset Objects

```python
class UrbanBuildDataAsset(DataAsset)
```

Urban Build Data Asset

**C++ Source:**

- **Plugin**: AesBuilderCommon
- **Module**: UrbanBuildDataAsset
- **File**: UrbanBuildDataAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data_asset_data_sets`` (Map[Name, SoftObjectPath]):  [Read-Write]
- ``data_table_sets`` (Map[Name, SoftObjectPath]):  [Read-Write]
- ``material_data_sets`` (Map[Name, SoftObjectPath]):  [Read-Write]
- ``prefab_data_sets`` (Map[Name, SoftObjectPath]):  [Read-Write]
- ``resource_data_sets`` (Map[Name, UrbanResourceStruct]):  [Read-Write]
- ``static_mesh_data_sets`` (Map[Name, SoftObjectPath]):  [Read-Write]
- ``texture2d_array_data_sets`` (Map[Name, Texture2DArrayAsset]):  [Read-Write]
- ``texture_data_sets`` (Map[Name, SoftObjectPath]):  [Read-Write]

<a id="unreal.UrbanBuildDataAsset.resource_data_sets"></a>

#### resource\_data\_sets

```python
@property
def resource_data_sets() -> Map[Name, UrbanResourceStruct]
```

(Map[Name, UrbanResourceStruct]):  [Read-Write]

<a id="unreal.UrbanBuildDataAsset.resource_data_sets"></a>

#### resource\_data\_sets

```python
@resource_data_sets.setter
def resource_data_sets(value: Map[Name, UrbanResourceStruct]) -> None
```

<a id="unreal.UrbanBuildSystem"></a>