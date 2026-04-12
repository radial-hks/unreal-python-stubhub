## EarthBuildingSubAsset Objects

```python
class EarthBuildingSubAsset(EarthSubAssetInfo)
```

定义建筑子资产信息的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthBuildingFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_scale`` (bool):  [Read-Write] 是否允许缩放子资产
- ``asset`` (EarthPrefabAsset):  [Read-Write] 子资产引用
- ``lod_config`` (Map[int32, int32]):  [Read-Write] 子资产细节级别设置，针对不同的最大细节级别X，需设置子资产在细节级别Y使用，若为空，则子资产在任意细节级别都使用
- ``seed`` (int32):  [Read-Write] 子资产随机种子偏移值
- ``size_extend`` (Vector2D):  [Read-Write] 子资产尺寸扩展值
- ``transform`` (Transform):  [Read-Write] 子资产的实例变换信息
- ``type`` (EarthBuildingSubAssetType):  [Read-Write] 子资产类型

<a id="unreal.EarthBuildingSubAsset.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    asset: EarthPrefabAsset = None,
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]],
    size_extend: Vector2D = [0.000000, 0.000000],
    seed: int = 0,
    lod_config: Map[int, int] = {},
    allow_scale: bool = False,
    type: EarthBuildingSubAssetType = EarthBuildingSubAssetType.FACADE
) -> None
```

<a id="unreal.EarthBuildingSubAsset.type"></a>

#### type

```python
@property
def type() -> EarthBuildingSubAssetType
```

(EarthBuildingSubAssetType):  [Read-Write] 子资产类型

<a id="unreal.EarthBuildingSubAsset.type"></a>

#### type

```python
@type.setter
def type(value: EarthBuildingSubAssetType) -> None
```

<a id="unreal.EarthPropertyFragment"></a>