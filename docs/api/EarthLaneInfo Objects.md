## EarthLaneInfo Objects

```python
class EarthLaneInfo(StructBase)
```

定义预制体子资产数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``direction`` (EarthPlaceDirection):  [Read-Write] 放置是否顺着点序方向
- ``dividing_lane_asset`` (EarthModuleAsset):  [Read-Write] 子资产引用
- ``end_width`` (float):  [Read-Write]
- ``guide_mesh_lane_asset`` (EarthModuleAsset):  [Read-Write] 交通指示标志
- ``lane_asset`` (EarthModuleAsset):  [Read-Write] 子资产引用
- ``lanenum`` (int32):  [Read-Write] 宽度
- ``road_lane_type`` (EarthRoadLaneType):  [Read-Write] 生成Lane类型
- ``start_width`` (float):  [Read-Write] 宽度
- ``xy_offset`` (float):  [Read-Write] 位移
- ``z_offset`` (float):  [Read-Write] 位移

<a id="unreal.EarthLaneInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(road_lane_type: EarthRoadLaneType = EarthRoadLaneType.LANE,
             start_width: float = 0.000000,
             end_width: float = 0.000000,
             xy_offset: float = 0.000000,
             z_offset: float = 0.000000,
             lanenum: int = 0,
             direction: EarthPlaceDirection = EarthPlaceDirection.FORWARD,
             guide_mesh_lane_asset: EarthModuleAsset = None,
             lane_asset: EarthModuleAsset = None,
             dividing_lane_asset: EarthModuleAsset = None) -> None
```

<a id="unreal.EarthLaneInfo.road_lane_type"></a>

#### road\_lane\_type

```python
@property
def road_lane_type() -> EarthRoadLaneType
```

(EarthRoadLaneType):  [Read-Write] 生成Lane类型

<a id="unreal.EarthLaneInfo.road_lane_type"></a>

#### road\_lane\_type

```python
@road_lane_type.setter
def road_lane_type(value: EarthRoadLaneType) -> None
```

<a id="unreal.EarthLaneInfo.start_width"></a>

#### start\_width

```python
@property
def start_width() -> float
```

(float):  [Read-Write] 宽度

<a id="unreal.EarthLaneInfo.start_width"></a>

#### start\_width

```python
@start_width.setter
def start_width(value: float) -> None
```

<a id="unreal.EarthLaneInfo.end_width"></a>

#### end\_width

```python
@property
def end_width() -> float
```

(float):  [Read-Write]

<a id="unreal.EarthLaneInfo.end_width"></a>

#### end\_width

```python
@end_width.setter
def end_width(value: float) -> None
```

<a id="unreal.EarthLaneInfo.xy_offset"></a>

#### xy\_offset

```python
@property
def xy_offset() -> float
```

(float):  [Read-Write] 位移

<a id="unreal.EarthLaneInfo.xy_offset"></a>

#### xy\_offset

```python
@xy_offset.setter
def xy_offset(value: float) -> None
```

<a id="unreal.EarthLaneInfo.z_offset"></a>

#### z\_offset

```python
@property
def z_offset() -> float
```

(float):  [Read-Write] 位移

<a id="unreal.EarthLaneInfo.z_offset"></a>

#### z\_offset

```python
@z_offset.setter
def z_offset(value: float) -> None
```

<a id="unreal.EarthLaneInfo.lanenum"></a>

#### lanenum

```python
@property
def lanenum() -> int
```

(int32):  [Read-Write] 宽度

<a id="unreal.EarthLaneInfo.lanenum"></a>

#### lanenum

```python
@lanenum.setter
def lanenum(value: int) -> None
```

<a id="unreal.EarthLaneInfo.direction"></a>

#### direction

```python
@property
def direction() -> EarthPlaceDirection
```

(EarthPlaceDirection):  [Read-Write] 放置是否顺着点序方向

<a id="unreal.EarthLaneInfo.direction"></a>

#### direction

```python
@direction.setter
def direction(value: EarthPlaceDirection) -> None
```

<a id="unreal.EarthLaneInfo.guide_mesh_lane_asset"></a>

#### guide\_mesh\_lane\_asset

```python
@property
def guide_mesh_lane_asset() -> EarthModuleAsset
```

(EarthModuleAsset):  [Read-Write] 交通指示标志

<a id="unreal.EarthLaneInfo.guide_mesh_lane_asset"></a>

#### guide\_mesh\_lane\_asset

```python
@guide_mesh_lane_asset.setter
def guide_mesh_lane_asset(value: EarthModuleAsset) -> None
```

<a id="unreal.EarthLaneInfo.lane_asset"></a>

#### lane\_asset

```python
@property
def lane_asset() -> EarthModuleAsset
```

(EarthModuleAsset):  [Read-Write] 子资产引用

<a id="unreal.EarthLaneInfo.lane_asset"></a>

#### lane\_asset

```python
@lane_asset.setter
def lane_asset(value: EarthModuleAsset) -> None
```

<a id="unreal.EarthLaneInfo.dividing_lane_asset"></a>

#### dividing\_lane\_asset

```python
@property
def dividing_lane_asset() -> EarthModuleAsset
```

(EarthModuleAsset):  [Read-Write] 子资产引用

<a id="unreal.EarthLaneInfo.dividing_lane_asset"></a>

#### dividing\_lane\_asset

```python
@dividing_lane_asset.setter
def dividing_lane_asset(value: EarthModuleAsset) -> None
```

<a id="unreal.EarthRemoveLaneInfo"></a>