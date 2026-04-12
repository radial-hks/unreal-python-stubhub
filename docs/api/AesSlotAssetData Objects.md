## AesSlotAssetData Objects

```python
class AesSlotAssetData(AesAssetData)
```

插槽资产数据

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesSlotAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child_assets`` (Array[AesAssetChildMetaData]):  [Read-Write] 自定义子资产引用列表
- ``collision_data`` (AesAssetCollisionData):  [Read-Write] 资产碰撞数据
- ``meta_data`` (AesAssetMetaData):  [Read-Write] 资产元数据
- ``size_data`` (AesAssetSizeData):  [Read-Write] 资产尺寸数据
- ``tag_data_list`` (Array[AesSlotAssetTagData]):  [Read-Write] 资产标签数据

<a id="unreal.AesSlotAssetData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(meta_data: AesAssetMetaData = [
    "None", 0, 0, "None", False, {}, "", [""]
],
             size_data: AesAssetSizeData = [[[0.000000, 0.000000, 0.000000],
                                             [-0.000000, 0.000000, 0.000000],
                                             [1.000000, 1.000000, 1.000000]],
                                            False, []],
             collision_data: AesAssetCollisionData = [
                 AesAssetCollisionType.NONE,
                 ["/Script/AesRenderResource.AesCollisionComponent"]
             ],
             child_assets: Array[AesAssetChildMetaData] = [],
             tag_data_list: Array[AesSlotAssetTagData] = []) -> None
```

<a id="unreal.AesSlotAssetData.tag_data_list"></a>

#### tag\_data\_list

```python
@property
def tag_data_list() -> Array[AesSlotAssetTagData]
```

(Array[AesSlotAssetTagData]):  [Read-Write] 资产标签数据

<a id="unreal.AesSlotAssetData.tag_data_list"></a>

#### tag\_data\_list

```python
@tag_data_list.setter
def tag_data_list(value: Array[AesSlotAssetTagData]) -> None
```

<a id="unreal.AesVegetationSpecie"></a>