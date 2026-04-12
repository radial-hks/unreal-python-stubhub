## EarthModelerLaneInfo Objects

```python
class EarthModelerLaneInfo(StructBase)
```

Modeler道路工具RoadLane定义

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadModelerFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``build_end`` (bool):  [Read-Write] 是否生成终点模型
- ``build_start`` (bool):  [Read-Write] 是否生成起点模型
- ``direction`` (EarthPlaceDirection):  [Read-Write] 放置是否顺着点序方向
- ``dividing_lane_asset`` (EarthPrefabAsset):  [Read-Write] 特殊资产
- ``dividing_lane_modeler_asset`` (EarthRoadModelerLanePath):  [Read-Write] 特殊资产ModelerLane引用
- ``end_width`` (float):  [Read-Write]
- ``lanenum`` (int32):  [Read-Write] 宽度
- ``primary_asset`` (EarthPrefabAsset):  [Read-Write] 主资产//RoadLaneType != EEarthModelerRoadLaneType::Cycle && RoadLaneType != EEarthModelerRoadLaneType::Parking &&
- ``primary_modeler_asset`` (EarthRoadModelerLanePath):  [Read-Write] 主资产ModelerLane引用
- ``road_lane_type`` (EarthModelerRoadLaneType):  [Read-Write] 生成Lane类型
- ``secondary_assets_array`` (Array[EarthSecondaryAssetInfo]):  [Read-Write] 子资产
- ``start_width`` (float):  [Read-Write] 宽度

<a id="unreal.EarthModelerLaneInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        road_lane_type: EarthModelerRoadLaneType = EarthModelerRoadLaneType.
    DRIVE,
        primary_modeler_asset: EarthRoadModelerLanePath = [[""]],
        start_width: float = 0.000000,
        end_width: float = 0.000000,
        lanenum: int = 0,
        build_start: bool = False,
        build_end: bool = False,
        direction: EarthPlaceDirection = EarthPlaceDirection.FORWARD,
        primary_asset: EarthPrefabAsset = None,
        secondary_assets_array: Array[EarthSecondaryAssetInfo] = [],
        dividing_lane_asset: EarthPrefabAsset = None,
        dividing_lane_modeler_asset: EarthRoadModelerLanePath = [[""]
                                                                 ]) -> None
```

<a id="unreal.EarthModelerLaneInfo.road_lane_type"></a>

#### road\_lane\_type

```python
@property
def road_lane_type() -> EarthModelerRoadLaneType
```

(EarthModelerRoadLaneType):  [Read-Write] 生成Lane类型

<a id="unreal.EarthModelerLaneInfo.road_lane_type"></a>

#### road\_lane\_type

```python
@road_lane_type.setter
def road_lane_type(value: EarthModelerRoadLaneType) -> None
```

<a id="unreal.EarthModelerLaneInfo.primary_modeler_asset"></a>

#### primary\_modeler\_asset

```python
@property
def primary_modeler_asset() -> EarthRoadModelerLanePath
```

(EarthRoadModelerLanePath):  [Read-Write] 主资产ModelerLane引用

<a id="unreal.EarthModelerLaneInfo.primary_modeler_asset"></a>

#### primary\_modeler\_asset

```python
@primary_modeler_asset.setter
def primary_modeler_asset(value: EarthRoadModelerLanePath) -> None
```

<a id="unreal.EarthModelerLaneInfo.start_width"></a>

#### start\_width

```python
@property
def start_width() -> float
```

(float):  [Read-Write] 宽度

<a id="unreal.EarthModelerLaneInfo.start_width"></a>

#### start\_width

```python
@start_width.setter
def start_width(value: float) -> None
```

<a id="unreal.EarthModelerLaneInfo.end_width"></a>

#### end\_width

```python
@property
def end_width() -> float
```

(float):  [Read-Write]

<a id="unreal.EarthModelerLaneInfo.end_width"></a>

#### end\_width

```python
@end_width.setter
def end_width(value: float) -> None
```

<a id="unreal.EarthModelerLaneInfo.lanenum"></a>

#### lanenum

```python
@property
def lanenum() -> int
```

(int32):  [Read-Write] 宽度

<a id="unreal.EarthModelerLaneInfo.lanenum"></a>

#### lanenum

```python
@lanenum.setter
def lanenum(value: int) -> None
```

<a id="unreal.EarthModelerLaneInfo.build_start"></a>

#### build\_start

```python
@property
def build_start() -> bool
```

(bool):  [Read-Write] 是否生成起点模型

<a id="unreal.EarthModelerLaneInfo.build_start"></a>

#### build\_start

```python
@build_start.setter
def build_start(value: bool) -> None
```

<a id="unreal.EarthModelerLaneInfo.build_end"></a>

#### build\_end

```python
@property
def build_end() -> bool
```

(bool):  [Read-Write] 是否生成终点模型

<a id="unreal.EarthModelerLaneInfo.build_end"></a>

#### build\_end

```python
@build_end.setter
def build_end(value: bool) -> None
```

<a id="unreal.EarthModelerLaneInfo.direction"></a>

#### direction

```python
@property
def direction() -> EarthPlaceDirection
```

(EarthPlaceDirection):  [Read-Write] 放置是否顺着点序方向

<a id="unreal.EarthModelerLaneInfo.direction"></a>

#### direction

```python
@direction.setter
def direction(value: EarthPlaceDirection) -> None
```

<a id="unreal.EarthModelerLaneInfo.primary_asset"></a>

#### primary\_asset

```python
@property
def primary_asset() -> EarthPrefabAsset
```

(EarthPrefabAsset):  [Read-Write] 主资产//RoadLaneType != EEarthModelerRoadLaneType::Cycle && RoadLaneType != EEarthModelerRoadLaneType::Parking &&

<a id="unreal.EarthModelerLaneInfo.primary_asset"></a>

#### primary\_asset

```python
@primary_asset.setter
def primary_asset(value: EarthPrefabAsset) -> None
```

<a id="unreal.EarthModelerLaneInfo.secondary_assets_array"></a>

#### secondary\_assets\_array

```python
@property
def secondary_assets_array() -> Array[EarthSecondaryAssetInfo]
```

(Array[EarthSecondaryAssetInfo]):  [Read-Write] 子资产

<a id="unreal.EarthModelerLaneInfo.secondary_assets_array"></a>

#### secondary\_assets\_array

```python
@secondary_assets_array.setter
def secondary_assets_array(value: Array[EarthSecondaryAssetInfo]) -> None
```

<a id="unreal.EarthModelerLaneInfo.dividing_lane_asset"></a>

#### dividing\_lane\_asset

```python
@property
def dividing_lane_asset() -> EarthPrefabAsset
```

(EarthPrefabAsset):  [Read-Write] 特殊资产

<a id="unreal.EarthModelerLaneInfo.dividing_lane_asset"></a>

#### dividing\_lane\_asset

```python
@dividing_lane_asset.setter
def dividing_lane_asset(value: EarthPrefabAsset) -> None
```

<a id="unreal.EarthModelerLaneInfo.dividing_lane_modeler_asset"></a>

#### dividing\_lane\_modeler\_asset

```python
@property
def dividing_lane_modeler_asset() -> EarthRoadModelerLanePath
```

(EarthRoadModelerLanePath):  [Read-Write] 特殊资产ModelerLane引用

<a id="unreal.EarthModelerLaneInfo.dividing_lane_modeler_asset"></a>

#### dividing\_lane\_modeler\_asset

```python
@dividing_lane_modeler_asset.setter
def dividing_lane_modeler_asset(value: EarthRoadModelerLanePath) -> None
```

<a id="unreal.EarthRoadModelerLanePath"></a>