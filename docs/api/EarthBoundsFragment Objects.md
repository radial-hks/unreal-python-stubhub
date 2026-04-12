## EarthBoundsFragment Objects

```python
class EarthBoundsFragment(EarthPropertyFragment)
```

定义包围盒数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthCommonFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bounds`` (Box):  [Read-Write] 包围盒大小
- ``custom_bounds`` (bool):  [Read-Write] 是否使用自定义包围盒大小
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthBoundsFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    validated: bool = False,
    valid: bool = False,
    custom_bounds: bool = False,
    bounds: Box = [[0.000000, 0.000000, 0.000000],
                   [0.000000, 0.000000, 0.000000], False]
) -> None
```

<a id="unreal.EarthBoundsFragment.custom_bounds"></a>

#### custom\_bounds

```python
@property
def custom_bounds() -> bool
```

(bool):  [Read-Write] 是否使用自定义包围盒大小

<a id="unreal.EarthBoundsFragment.custom_bounds"></a>

#### custom\_bounds

```python
@custom_bounds.setter
def custom_bounds(value: bool) -> None
```

<a id="unreal.EarthBoundsFragment.bounds"></a>

#### bounds

```python
@property
def bounds() -> Box
```

(Box):  [Read-Write] 包围盒大小

<a id="unreal.EarthBoundsFragment.bounds"></a>

#### bounds

```python
@bounds.setter
def bounds(value: Box) -> None
```

<a id="unreal.EarthFeatureBuffer"></a>