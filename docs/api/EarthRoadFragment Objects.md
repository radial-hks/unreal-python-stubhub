## EarthRoadFragment Objects

```python
class EarthRoadFragment(EarthEntityFragment)
```

Earth Road Fragment

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``chamfer_corner`` (bool):  [Read-Write] 点是否倒角
- ``chamfer_length`` (float):  [Read-Write] 切角长度
- ``end_extension`` (float):  [Read-Write]
- ``end_lane_width`` (Vector2f):  [Read-Write]
- ``end_lanes`` (IntPoint):  [Read-Write]
- ``end_width`` (float):  [Read-Only]
- ``f_class`` (str):  [Read-Write] 道路类型
- ``level`` (int32):  [Read-Write] 道路Level
- ``lod_config`` (Map[int32, int32]):  [Read-Write] 子资产细节级别设置，针对不同的最大细节级别X，需设置子资产在细节级别Y使用，若为空，则子资产在任意细节级别都使用
- ``reverse`` (bool):  [Read-Write] 是否调转曲线前进方向
- ``side`` (EarthDrivingDirection):  [Read-Write] 道路行驶方向
- ``start_extension`` (float):  [Read-Write] 收尾端缩进长度
- ``start_lane_width`` (Vector2f):  [Read-Write] 车道路宽度
- ``start_lanes`` (IntPoint):  [Read-Write] 左右车道数
- ``start_width`` (float):  [Read-Only] 道路总宽度
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthRoadFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             start_width: float = 0.000000,
             end_width: float = 0.000000,
             reverse: bool = False,
             f_class: str = "",
             level: int = 0,
             start_extension: float = 0.000000,
             end_extension: float = 0.000000,
             side: EarthDrivingDirection = EarthDrivingDirection.RIGHT,
             start_lanes: IntPoint = [0, 0],
             end_lanes: IntPoint = [0, 0],
             start_lane_width: Vector2f = [0.000000, 0.000000],
             end_lane_width: Vector2f = [0.000000, 0.000000],
             chamfer_corner: bool = False,
             chamfer_length: float = 0.000000,
             lod_config: Map[int, int] = {}) -> None
```

<a id="unreal.EarthRoadFragment.start_width"></a>

#### start\_width

```python
@property
def start_width() -> float
```

(float):  [Read-Only] 道路总宽度

<a id="unreal.EarthRoadFragment.end_width"></a>

#### end\_width

```python
@property
def end_width() -> float
```

(float):  [Read-Only]

<a id="unreal.EarthRoadFragment.reverse"></a>

#### reverse

```python
@property
def reverse() -> bool
```

(bool):  [Read-Write] 是否调转曲线前进方向

<a id="unreal.EarthRoadFragment.reverse"></a>

#### reverse

```python
@reverse.setter
def reverse(value: bool) -> None
```

<a id="unreal.EarthRoadFragment.f_class"></a>

#### f\_class

```python
@property
def f_class() -> str
```

(str):  [Read-Write] 道路类型

<a id="unreal.EarthRoadFragment.f_class"></a>

#### f\_class

```python
@f_class.setter
def f_class(value: str) -> None
```

<a id="unreal.EarthRoadFragment.level"></a>

#### level

```python
@property
def level() -> int
```

(int32):  [Read-Write] 道路Level

<a id="unreal.EarthRoadFragment.level"></a>

#### level

```python
@level.setter
def level(value: int) -> None
```

<a id="unreal.EarthRoadFragment.start_extension"></a>

#### start\_extension

```python
@property
def start_extension() -> float
```

(float):  [Read-Write] 收尾端缩进长度

<a id="unreal.EarthRoadFragment.start_extension"></a>

#### start\_extension

```python
@start_extension.setter
def start_extension(value: float) -> None
```

<a id="unreal.EarthRoadFragment.end_extension"></a>

#### end\_extension

```python
@property
def end_extension() -> float
```

(float):  [Read-Write]

<a id="unreal.EarthRoadFragment.end_extension"></a>

#### end\_extension

```python
@end_extension.setter
def end_extension(value: float) -> None
```

<a id="unreal.EarthRoadFragment.side"></a>

#### side

```python
@property
def side() -> EarthDrivingDirection
```

(EarthDrivingDirection):  [Read-Write] 道路行驶方向

<a id="unreal.EarthRoadFragment.side"></a>

#### side

```python
@side.setter
def side(value: EarthDrivingDirection) -> None
```

<a id="unreal.EarthRoadFragment.start_lanes"></a>

#### start\_lanes

```python
@property
def start_lanes() -> IntPoint
```

(IntPoint):  [Read-Write] 左右车道数

<a id="unreal.EarthRoadFragment.start_lanes"></a>

#### start\_lanes

```python
@start_lanes.setter
def start_lanes(value: IntPoint) -> None
```

<a id="unreal.EarthRoadFragment.end_lanes"></a>

#### end\_lanes

```python
@property
def end_lanes() -> IntPoint
```

(IntPoint):  [Read-Write]

<a id="unreal.EarthRoadFragment.end_lanes"></a>

#### end\_lanes

```python
@end_lanes.setter
def end_lanes(value: IntPoint) -> None
```

<a id="unreal.EarthRoadFragment.start_lane_width"></a>

#### start\_lane\_width

```python
@property
def start_lane_width() -> Vector2f
```

(Vector2f):  [Read-Write] 车道路宽度

<a id="unreal.EarthRoadFragment.start_lane_width"></a>

#### start\_lane\_width

```python
@start_lane_width.setter
def start_lane_width(value: Vector2f) -> None
```

<a id="unreal.EarthRoadFragment.end_lane_width"></a>

#### end\_lane\_width

```python
@property
def end_lane_width() -> Vector2f
```

(Vector2f):  [Read-Write]

<a id="unreal.EarthRoadFragment.end_lane_width"></a>

#### end\_lane\_width

```python
@end_lane_width.setter
def end_lane_width(value: Vector2f) -> None
```

<a id="unreal.EarthRoadFragment.chamfer_corner"></a>

#### chamfer\_corner

```python
@property
def chamfer_corner() -> bool
```

(bool):  [Read-Write] 点是否倒角

<a id="unreal.EarthRoadFragment.chamfer_corner"></a>

#### chamfer\_corner

```python
@chamfer_corner.setter
def chamfer_corner(value: bool) -> None
```

<a id="unreal.EarthRoadFragment.chamfer_length"></a>

#### chamfer\_length

```python
@property
def chamfer_length() -> float
```

(float):  [Read-Write] 切角长度

<a id="unreal.EarthRoadFragment.chamfer_length"></a>

#### chamfer\_length

```python
@chamfer_length.setter
def chamfer_length(value: float) -> None
```

<a id="unreal.EarthRoadFragment.lod_config"></a>

#### lod\_config

```python
@property
def lod_config() -> Map[int, int]
```

(Map[int32, int32]):  [Read-Write] 子资产细节级别设置，针对不同的最大细节级别X，需设置子资产在细节级别Y使用，若为空，则子资产在任意细节级别都使用

<a id="unreal.EarthRoadFragment.lod_config"></a>

#### lod\_config

```python
@lod_config.setter
def lod_config(value: Map[int, int]) -> None
```

<a id="unreal.EarthLaneProfileReplacementFragment"></a>