## AesInstanceSplineAssetData Objects

```python
class AesInstanceSplineAssetData(AesAssetData)
```

实例样条线资产数据

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesInstanceSplineAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child_assets`` (Array[AesAssetChildMetaData]):  [Read-Write] 自定义子资产引用列表
- ``collision_data`` (AesAssetCollisionData):  [Read-Write] 资产碰撞数据
- ``meta_data`` (AesAssetMetaData):  [Read-Write] 资产元数据
- ``size_data`` (AesAssetSizeData):  [Read-Write] 资产尺寸数据
- ``tag_data`` (AesInstanceSplineAssetTagData):  [Read-Write] 资产标签数据

<a id="unreal.AesInstanceSplineAssetData.__init__"></a>

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
    tag_data: AesInstanceSplineAssetTagData = [
        False, False, SplinePointType.CURVE, 0.000000, 0.000000,
        [[""], ["/Script/AesRenderResource.AesInstancedStaticMeshComponent"],
         [], []], [],
        [[""], ["/Script/AesRenderResource.AesInstancedStaticMeshComponent"],
         [], []], False, False, SplineDeformType.CURVE, SplineMeshAxis.X,
        [0.000000, 0.000000,
         0.000000], False, False, AesSplineSizeControlType.SCALE,
        [0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000],
        [0.000000, 0.000000], 0.000000, [0.000000, 0.000000],
        [0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000],
        0.000000, SplineResampleType.INTERPOLATING, False,
        SplinePlacementType.CONTINUOUS, 0.000000, 0.000000,
        SplineAlignmentType.NORMAL, 1.000000, 1.000000, False,
        [0.000000, 0.000000,
         0.000000], [0.000000, 0.000000,
                     0.000000], True, True, False, 0.000000, {
                         "FID": 0.000000
                     }
    ]
) -> None
```

<a id="unreal.AesInstanceSplineAssetData.tag_data"></a>

#### tag\_data

```python
@property
def tag_data() -> AesInstanceSplineAssetTagData
```

(AesInstanceSplineAssetTagData):  [Read-Write] 资产标签数据

<a id="unreal.AesInstanceSplineAssetData.tag_data"></a>

#### tag\_data

```python
@tag_data.setter
def tag_data(value: AesInstanceSplineAssetTagData) -> None
```

<a id="unreal.AesLandmarkAssetTagData"></a>