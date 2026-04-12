## EarthLaneProfileReplacementFragment Objects

```python
class EarthLaneProfileReplacementFragment(EarthPropertyFragment)
```

Earth Lane Profile Replacement Fragment

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``lane_index`` (int32):  [Read-Write] 替换LaneProfileIndex（指FullLaneProfileIndex）
- ``lane_replacements`` (Array[EarthReplacementLaneInfo]):  [Read-Write]
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthLaneProfileReplacementFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             lane_index: int = 0,
             lane_replacements: Array[EarthReplacementLaneInfo] = []) -> None
```

<a id="unreal.EarthLaneProfileReplacementFragment.lane_index"></a>

#### lane\_index

```python
@property
def lane_index() -> int
```

(int32):  [Read-Write] 替换LaneProfileIndex（指FullLaneProfileIndex）

<a id="unreal.EarthLaneProfileReplacementFragment.lane_index"></a>

#### lane\_index

```python
@lane_index.setter
def lane_index(value: int) -> None
```

<a id="unreal.EarthLaneProfileReplacementFragment.lane_replacements"></a>

#### lane\_replacements

```python
@property
def lane_replacements() -> Array[EarthReplacementLaneInfo]
```

(Array[EarthReplacementLaneInfo]):  [Read-Write]

<a id="unreal.EarthLaneProfileReplacementFragment.lane_replacements"></a>

#### lane\_replacements

```python
@lane_replacements.setter
def lane_replacements(value: Array[EarthReplacementLaneInfo]) -> None
```

<a id="unreal.EarthLaneProfileModifyFragment"></a>