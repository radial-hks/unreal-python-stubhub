## EarthRoadPropertyFragment Objects

```python
class EarthRoadPropertyFragment(EarthPropertyFragment)
```

Earth Road Property Fragment

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``build_end`` (bool):  [Read-Write]
- ``build_start`` (bool):  [Read-Write]
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthRoadPropertyFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             build_start: bool = False,
             build_end: bool = False) -> None
```

<a id="unreal.EarthRoadPropertyFragment.build_start"></a>

#### build\_start

```python
@property
def build_start() -> bool
```

(bool):  [Read-Write]

<a id="unreal.EarthRoadPropertyFragment.build_start"></a>

#### build\_start

```python
@build_start.setter
def build_start(value: bool) -> None
```

<a id="unreal.EarthRoadPropertyFragment.build_end"></a>

#### build\_end

```python
@property
def build_end() -> bool
```

(bool):  [Read-Write]

<a id="unreal.EarthRoadPropertyFragment.build_end"></a>

#### build\_end

```python
@build_end.setter
def build_end(value: bool) -> None
```

<a id="unreal.EarthRoadEditorFragment"></a>