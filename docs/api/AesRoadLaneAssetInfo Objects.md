## AesRoadLaneAssetInfo Objects

```python
class AesRoadLaneAssetInfo(StructBase)
```

道路车道资产信息

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesRoadLaneAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset`` (AesAssetMetaData):  [Read-Write] 默认资产模板
- ``filter_by_level`` (int32):  [Read-Write] 是否受level影响
- ``road_lane_type`` (RoadLaneType):  [Read-Write] 默认道路线类型

<a id="unreal.AesRoadLaneAssetInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(asset: AesAssetMetaData = [
    "None", 0, 0, "None", False, {}, "", [""]
],
             road_lane_type: RoadLaneType = RoadLaneType.DRIVING,
             filter_by_level: int = 0) -> None
```

<a id="unreal.AesRoadLaneAssetInfo.asset"></a>

#### asset

```python
@property
def asset() -> AesAssetMetaData
```

(AesAssetMetaData):  [Read-Write] 默认资产模板

<a id="unreal.AesRoadLaneAssetInfo.asset"></a>

#### asset

```python
@asset.setter
def asset(value: AesAssetMetaData) -> None
```

<a id="unreal.AesRoadLaneAssetInfo.road_lane_type"></a>

#### road\_lane\_type

```python
@property
def road_lane_type() -> RoadLaneType
```

(RoadLaneType):  [Read-Write] 默认道路线类型

<a id="unreal.AesRoadLaneAssetInfo.road_lane_type"></a>

#### road\_lane\_type

```python
@road_lane_type.setter
def road_lane_type(value: RoadLaneType) -> None
```

<a id="unreal.AesRoadLaneAssetInfo.filter_by_level"></a>

#### filter\_by\_level

```python
@property
def filter_by_level() -> int
```

(int32):  [Read-Write] 是否受level影响

<a id="unreal.AesRoadLaneAssetInfo.filter_by_level"></a>

#### filter\_by\_level

```python
@filter_by_level.setter
def filter_by_level(value: int) -> None
```

<a id="unreal.AesRoadLaneAssetTagData"></a>