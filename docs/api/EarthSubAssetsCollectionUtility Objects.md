## EarthSubAssetsCollectionUtility Objects

```python
class EarthSubAssetsCollectionUtility(AssetActionUtility)
```

将资产创建为预制体的子资产集合的工具

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefabEditor
- **File**: EarthSubAssetsCollectionUtility.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_action_for_blueprints`` (bool):  [Read-Write] Is this action designed to work specifically on Blueprints (true) or on all assets (false).
  If true, SupportedClasses is treated as a filter against the Parent Class of selected Blueprint assets.
- ``supported_classes`` (Array[Class]):  [Read-Write] The supported classes controls the list of classes that may be operated on by all of the asset functions in this
  utility class.
  note: When bIsActionForBlueprints is true, this will compare against the generated class of any Blueprint assets.
- ``supported_conditions`` (Array[AssetActionSupportCondition]):  [Read-Write] The supported conditions for any asset to use these utility functions.  Note: all of these conditions must pass
  in sequence.  So if you have earlier failure conditions you want to be run first, put them first in the list,
  if those fail, their failure reason will be handled first.

<a id="unreal.EarthSubAssetsCollectionUtility.create_sub_assets_collection"></a>

#### create\_sub\_assets\_collection

```python
def create_sub_assets_collection(sub_assets_struct: ScriptStruct) -> None
```

x.create_sub_assets_collection(sub_assets_struct) -> None
根据子资产结构体类型，将选中的预制体资产保存为数据表

Args:
    sub_assets_struct (ScriptStruct):

<a id="unreal.SkyCreator"></a>