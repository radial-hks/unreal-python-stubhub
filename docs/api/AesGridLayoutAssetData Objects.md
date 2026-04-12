## AesGridLayoutAssetData Objects

```python
class AesGridLayoutAssetData(AesAssetData)
```

网格排布资产数据

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesGridLayoutAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child_assets`` (Array[AesAssetChildMetaData]):  [Read-Write] 自定义子资产引用列表
- ``collision_data`` (AesAssetCollisionData):  [Read-Write] 资产碰撞数据
- ``meta_data`` (AesAssetMetaData):  [Read-Write] 资产元数据
- ``size_data`` (AesAssetSizeData):  [Read-Write] 资产尺寸数据
- ``tag_data`` (AesGridLayoutAssetTagData):  [Read-Write] 资产标签数据

<a id="unreal.AesGridLayoutAssetData.__init__"></a>

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
    tag_data: AesGridLayoutAssetTagData = [
        1200.000000, 150.000000, [0.000000, 0.000000], []
    ]
) -> None
```

<a id="unreal.AesGridLayoutAssetData.tag_data"></a>

#### tag\_data

```python
@property
def tag_data() -> AesGridLayoutAssetTagData
```

(AesGridLayoutAssetTagData):  [Read-Write] 资产标签数据

<a id="unreal.AesGridLayoutAssetData.tag_data"></a>

#### tag\_data

```python
@tag_data.setter
def tag_data(value: AesGridLayoutAssetTagData) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData"></a>