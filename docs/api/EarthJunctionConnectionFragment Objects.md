## EarthJunctionConnectionFragment Objects

```python
class EarthJunctionConnectionFragment(EarthPropertyFragment)
```

Earth Junction Connection Fragment

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``road_ids`` (Array[int64]):  [Read-Write] 连接道路ID
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthJunctionConnectionFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             road_ids: Array[int] = []) -> None
```

<a id="unreal.EarthJunctionConnectionFragment.road_ids"></a>

#### road\_ids

```python
@property
def road_ids() -> Array[int]
```

(Array[int64]):  [Read-Write] 连接道路ID

<a id="unreal.EarthJunctionConnectionFragment.road_ids"></a>

#### road\_ids

```python
@road_ids.setter
def road_ids(value: Array[int]) -> None
```

<a id="unreal.EarthJunctionLaneFragment"></a>