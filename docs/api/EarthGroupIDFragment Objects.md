## EarthGroupIDFragment Objects

```python
class EarthGroupIDFragment(EarthExternalFragment)
```

定义群组识别码片段

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthCommonFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``group_id`` (int32):  [Read-Write] 群组识别码
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthGroupIDFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             group_id: int = 0) -> None
```

<a id="unreal.EarthGroupIDFragment.group_id"></a>

#### group\_id

```python
@property
def group_id() -> int
```

(int32):  [Read-Write] 群组识别码

<a id="unreal.EarthGroupIDFragment.group_id"></a>

#### group\_id

```python
@group_id.setter
def group_id(value: int) -> None
```

<a id="unreal.EarthDerivedPrefabActorFragment"></a>