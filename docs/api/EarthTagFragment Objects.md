## EarthTagFragment Objects

```python
class EarthTagFragment(EarthPropertyFragment)
```

定义标签数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthCommonFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``tags`` (Array[Name]):  [Read-Write] 标签
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthTagFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             tags: Array[Name] = []) -> None
```

<a id="unreal.EarthTagFragment.tags"></a>

#### tags

```python
@property
def tags() -> Array[Name]
```

(Array[Name]):  [Read-Write] 标签

<a id="unreal.EarthTagFragment.tags"></a>

#### tags

```python
@tags.setter
def tags(value: Array[Name]) -> None
```

<a id="unreal.EarthBoundsFragment"></a>