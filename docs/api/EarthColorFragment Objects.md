## EarthColorFragment Objects

```python
class EarthColorFragment(EarthPropertyFragment)
```

定义颜色数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthCommonFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write] 颜色
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthColorFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        validated: bool = False,
        valid: bool = False,
        color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.EarthColorFragment.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write] 颜色

<a id="unreal.EarthColorFragment.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.EarthTextureIndexFragment"></a>