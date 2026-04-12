## EarthLaneProfileFragment Objects

```python
class EarthLaneProfileFragment(EarthPropertyFragment)
```

Earth Lane Profile Fragment

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``lanes`` (Array[EarthLaneInfo]):  [Read-Write]
- ``name`` (Name):  [Read-Write]
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthLaneProfileFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             name: Name = "None",
             lanes: Array[EarthLaneInfo] = []) -> None
```

<a id="unreal.EarthLaneProfileFragment.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.EarthLaneProfileFragment.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.EarthLaneProfileFragment.lanes"></a>

#### lanes

```python
@property
def lanes() -> Array[EarthLaneInfo]
```

(Array[EarthLaneInfo]):  [Read-Write]

<a id="unreal.EarthLaneProfileFragment.lanes"></a>

#### lanes

```python
@lanes.setter
def lanes(value: Array[EarthLaneInfo]) -> None
```

<a id="unreal.EarthLaneProfilesFragment"></a>