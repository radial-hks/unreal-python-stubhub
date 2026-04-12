## AesModularBuildingAssetData Objects

```python
class AesModularBuildingAssetData(AesAssetData)
```

模块化建筑数据

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesModularBuildingAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child_assets`` (Array[AesAssetChildMetaData]):  [Read-Write] 自定义子资产引用列表
- ``collision_data`` (AesAssetCollisionData):  [Read-Write] 资产碰撞数据
- ``meta_data`` (AesAssetMetaData):  [Read-Write] 资产元数据
- ``size_data`` (AesAssetSizeData):  [Read-Write] 资产尺寸数据
- ``tag_data`` (AesModularBuildingAssetTagData):  [Read-Write] 资产标签数据

<a id="unreal.AesModularBuildingAssetData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    meta_data: AesAssetMetaData = ["None", 0, 0, "None", False, {}, "", [""]],
    size_data: AesAssetSizeData = [[[0.000000, 0.000000, 0.000000],
                                    [-0.000000, 0.000000, 0.000000],
                                    [1.000000, 1.000000, 1.000000]], False,
                                   []],
    collision_data: AesAssetCollisionData = [
        AesAssetCollisionType.NONE,
        ["/Script/AesRenderResource.AesCollisionComponent"]
    ],
    child_assets: Array[AesAssetChildMetaData] = [],
    tag_data: AesModularBuildingAssetTagData = [
        300.000000, 0.000000, 600.000000, 1, 0, LandCover.ARTIFICIAL_SURFACES,
        "None", [255, 255, 255, 255], 0.000000, 0, RoofShape.FLAT,
        [255, 255, 255, 255], AesBuildingPrefabType.NONE, "",
        [["None", 0, 0, "None", False, {}, "", [""]], True, True,
         AesAssetTransformControlType.NONE, 0.000000, 0.000000, 0.000000,
         [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
          [1.000000, 1.000000, 1.000000]], [], []], [],
        [["None", 0, 0, "None", False, {}, "", [""]], True, True,
         AesAssetTransformControlType.NONE, 0.000000, 0.000000, 0.000000,
         [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
          [1.000000, 1.000000, 1.000000]], [], []],
        [["None", 0, 0, "None", False, {}, "", [""]], True, True,
         AesAssetTransformControlType.NONE, 0.000000, 0.000000, 0.000000,
         [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
          [1.000000, 1.000000, 1.000000]], [], []],
        [["None", 0, 0, "None", False, {}, "", [""]], True, True,
         AesAssetTransformControlType.NONE, 0.000000, 0.000000, 0.000000,
         [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
          [1.000000, 1.000000, 1.000000]], [], []],
        [["None", 0, 0, "None", False, {}, "", [""]], True, True,
         AesAssetTransformControlType.NONE, 0.000000, 0.000000, 0.000000,
         [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
          [1.000000, 1.000000, 1.000000]], [], []], [], [], 0.000000
    ]
) -> None
```

<a id="unreal.AesModularBuildingAssetData.tag_data"></a>

#### tag\_data

```python
@property
def tag_data() -> AesModularBuildingAssetTagData
```

(AesModularBuildingAssetTagData):  [Read-Write] 资产标签数据

<a id="unreal.AesModularBuildingAssetData.tag_data"></a>

#### tag\_data

```python
@tag_data.setter
def tag_data(value: AesModularBuildingAssetTagData) -> None
```

<a id="unreal.AesObjectAssetTagData"></a>