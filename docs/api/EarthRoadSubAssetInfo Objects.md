## EarthRoadSubAssetInfo Objects

```python
class EarthRoadSubAssetInfo(EarthSubAssetInfo)
```

定义带Index指定的道路的预制体子资产信息的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthCommonFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_scale`` (bool):  [Read-Write] 是否允许缩放子资产
- ``asset`` (EarthPrefabAsset):  [Read-Write] 子资产引用
- ``lane_tags`` (Array[EarthRoadLaneType]):  [Read-Write] 子资产权重
- ``lod_config`` (Map[int32, int32]):  [Read-Write] 子资产细节级别设置，针对不同的最大细节级别X，需设置子资产在细节级别Y使用，若为空，则子资产在任意细节级别都使用
- ``seed`` (int32):  [Read-Write] 子资产随机种子偏移值
- ``size_extend`` (Vector2D):  [Read-Write] 子资产尺寸扩展值
- ``transform`` (Transform):  [Read-Write] 子资产的实例变换信息

<a id="unreal.EarthRoadSubAssetInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(asset: EarthPrefabAsset = None,
             transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
             size_extend: Vector2D = [0.000000, 0.000000],
             seed: int = 0,
             lod_config: Map[int, int] = {},
             allow_scale: bool = False,
             lane_tags: Array[EarthRoadLaneType] = []) -> None
```

<a id="unreal.EarthRoadSubAssetInfo.lane_tags"></a>

#### lane\_tags

```python
@property
def lane_tags() -> Array[EarthRoadLaneType]
```

(Array[EarthRoadLaneType]):  [Read-Write] 子资产权重

<a id="unreal.EarthRoadSubAssetInfo.lane_tags"></a>

#### lane\_tags

```python
@lane_tags.setter
def lane_tags(value: Array[EarthRoadLaneType]) -> None
```

<a id="unreal.EarthMaterialInfo"></a>