## EarthOuterFragment Objects

```python
class EarthOuterFragment(EarthExternalFragment)
```

父对象数据片段

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthCommonFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``outer`` (Object):  [Read-Write] 父对象
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthOuterFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             outer: Object = None) -> None
```

<a id="unreal.EarthOuterFragment.outer"></a>

#### outer

```python
@property
def outer() -> Object
```

(Object):  [Read-Write] 父对象

<a id="unreal.EarthOuterFragment.outer"></a>

#### outer

```python
@outer.setter
def outer(value: Object) -> None
```

<a id="unreal.EarthLODFragment"></a>