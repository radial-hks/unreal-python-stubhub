## EarthLaneProfilesFragment Objects

```python
class EarthLaneProfilesFragment(EarthPropertyFragment)
```

Earth Lane Profiles Fragment

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``lane_profiles`` (Array[EarthLaneProfileFragment]):  [Read-Write]
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthLaneProfilesFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             lane_profiles: Array[EarthLaneProfileFragment] = []) -> None
```

<a id="unreal.EarthLaneProfilesFragment.lane_profiles"></a>

#### lane\_profiles

```python
@property
def lane_profiles() -> Array[EarthLaneProfileFragment]
```

(Array[EarthLaneProfileFragment]):  [Read-Write]

<a id="unreal.EarthLaneProfilesFragment.lane_profiles"></a>

#### lane\_profiles

```python
@lane_profiles.setter
def lane_profiles(value: Array[EarthLaneProfileFragment]) -> None
```

<a id="unreal.EarthModelerLaneProfileFragment"></a>