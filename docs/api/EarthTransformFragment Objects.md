## EarthTransformFragment Objects

```python
class EarthTransformFragment(EarthExternalFragment)
```

变换数据片段

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthCommonFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``transform`` (Transform):  [Read-Write] 变换
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证
- ``world_space`` (bool):  [Read-Write] 坐标是否为世界空间

<a id="unreal.EarthTransformFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
             world_space: bool = False) -> None
```

<a id="unreal.EarthTransformFragment.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write] 变换

<a id="unreal.EarthTransformFragment.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.EarthTransformFragment.world_space"></a>

#### world\_space

```python
@property
def world_space() -> bool
```

(bool):  [Read-Write] 坐标是否为世界空间

<a id="unreal.EarthTransformFragment.world_space"></a>

#### world\_space

```python
@world_space.setter
def world_space(value: bool) -> None
```

<a id="unreal.EarthPrimitiveDataFragment"></a>