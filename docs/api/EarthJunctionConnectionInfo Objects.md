## EarthJunctionConnectionInfo Objects

```python
class EarthJunctionConnectionInfo(EarthPropertyFragment)
```

Earth Junction Connection Info

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``lane_directions`` (Array[EarthLaneDirection]):  [Read-Write]
- ``road_connection_side`` (int32):  [Read-Write]
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthJunctionConnectionInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             road_connection_side: int = 0,
             lane_directions: Array[EarthLaneDirection] = []) -> None
```

<a id="unreal.EarthJunctionConnectionInfo.road_connection_side"></a>

#### road\_connection\_side

```python
@property
def road_connection_side() -> int
```

(int32):  [Read-Write]

<a id="unreal.EarthJunctionConnectionInfo.road_connection_side"></a>

#### road\_connection\_side

```python
@road_connection_side.setter
def road_connection_side(value: int) -> None
```

<a id="unreal.EarthJunctionConnectionInfo.lane_directions"></a>

#### lane\_directions

```python
@property
def lane_directions() -> Array[EarthLaneDirection]
```

(Array[EarthLaneDirection]):  [Read-Write]

<a id="unreal.EarthJunctionConnectionInfo.lane_directions"></a>

#### lane\_directions

```python
@lane_directions.setter
def lane_directions(value: Array[EarthLaneDirection]) -> None
```

<a id="unreal.EarthJunctionOverwriteFragment"></a>