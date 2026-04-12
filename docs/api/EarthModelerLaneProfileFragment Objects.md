## EarthModelerLaneProfileFragment Objects

```python
class EarthModelerLaneProfileFragment(EarthPropertyFragment)
```

Earth Modeler Lane Profile Fragment

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_modules`` (Array[EarthModelerLaneInfo]):  [Read-Write]
- ``lanes`` (Array[EarthModelerLaneInfo]):  [Read-Write]
- ``name`` (Name):  [Read-Write]
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthModelerLaneProfileFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             name: Name = "None",
             lanes: Array[EarthModelerLaneInfo] = [],
             additional_modules: Array[EarthModelerLaneInfo] = []) -> None
```

<a id="unreal.EarthModelerLaneProfileFragment.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.EarthModelerLaneProfileFragment.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.EarthModelerLaneProfileFragment.lanes"></a>

#### lanes

```python
@property
def lanes() -> Array[EarthModelerLaneInfo]
```

(Array[EarthModelerLaneInfo]):  [Read-Write]

<a id="unreal.EarthModelerLaneProfileFragment.lanes"></a>

#### lanes

```python
@lanes.setter
def lanes(value: Array[EarthModelerLaneInfo]) -> None
```

<a id="unreal.EarthModelerLaneProfileFragment.additional_modules"></a>

#### additional\_modules

```python
@property
def additional_modules() -> Array[EarthModelerLaneInfo]
```

(Array[EarthModelerLaneInfo]):  [Read-Write]

<a id="unreal.EarthModelerLaneProfileFragment.additional_modules"></a>

#### additional\_modules

```python
@additional_modules.setter
def additional_modules(value: Array[EarthModelerLaneInfo]) -> None
```

<a id="unreal.EarthModelerLaneInfo"></a>