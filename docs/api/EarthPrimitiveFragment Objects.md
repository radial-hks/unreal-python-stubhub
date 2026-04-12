## EarthPrimitiveFragment Objects

```python
class EarthPrimitiveFragment(EarthSpatialFragment)
```

片元数据片段

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthSpatialFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``area`` (double):  [Read-Write] 面积，单位为平方米
- ``bounds_rotation`` (Rotator):  [Read-Write] 最小面积包围盒的旋转值
- ``clockwise`` (bool):  [Read-Write] 是否是顺时针的点序
- ``closed_loop`` (bool):  [Read-Write] 是否为闭环
- ``min_area_bounds`` (Box):  [Read-Write] 最小面积包围盒
- ``owned_component`` (ActorComponent):  [Read-Write] 空间片段所拥有的组件
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证
- ``vertices`` (Array[Vector]):  [Read-Write] 顶点数组

<a id="unreal.EarthPrimitiveFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        validated: bool = False,
        valid: bool = False,
        owned_component: ActorComponent = None,
        vertices: Array[Vector] = [],
        area: float = 0.000000,
        closed_loop: bool = False,
        clockwise: bool = False,
        min_area_bounds: Box = [[0.000000, 0.000000, 0.000000],
                                [0.000000, 0.000000, 0.000000], False],
        bounds_rotation: Rotator = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.EarthPrimitiveFragment.vertices"></a>

#### vertices

```python
@property
def vertices() -> Array[Vector]
```

(Array[Vector]):  [Read-Write] 顶点数组

<a id="unreal.EarthPrimitiveFragment.vertices"></a>

#### vertices

```python
@vertices.setter
def vertices(value: Array[Vector]) -> None
```

<a id="unreal.EarthPrimitiveFragment.area"></a>

#### area

```python
@property
def area() -> float
```

(double):  [Read-Write] 面积，单位为平方米

<a id="unreal.EarthPrimitiveFragment.area"></a>

#### area

```python
@area.setter
def area(value: float) -> None
```

<a id="unreal.EarthPrimitiveFragment.closed_loop"></a>

#### closed\_loop

```python
@property
def closed_loop() -> bool
```

(bool):  [Read-Write] 是否为闭环

<a id="unreal.EarthPrimitiveFragment.closed_loop"></a>

#### closed\_loop

```python
@closed_loop.setter
def closed_loop(value: bool) -> None
```

<a id="unreal.EarthPrimitiveFragment.clockwise"></a>

#### clockwise

```python
@property
def clockwise() -> bool
```

(bool):  [Read-Write] 是否是顺时针的点序

<a id="unreal.EarthPrimitiveFragment.clockwise"></a>

#### clockwise

```python
@clockwise.setter
def clockwise(value: bool) -> None
```

<a id="unreal.EarthPrimitiveFragment.min_area_bounds"></a>

#### min\_area\_bounds

```python
@property
def min_area_bounds() -> Box
```

(Box):  [Read-Write] 最小面积包围盒

<a id="unreal.EarthPrimitiveFragment.min_area_bounds"></a>

#### min\_area\_bounds

```python
@min_area_bounds.setter
def min_area_bounds(value: Box) -> None
```

<a id="unreal.EarthPrimitiveFragment.bounds_rotation"></a>

#### bounds\_rotation

```python
@property
def bounds_rotation() -> Rotator
```

(Rotator):  [Read-Write] 最小面积包围盒的旋转值

<a id="unreal.EarthPrimitiveFragment.bounds_rotation"></a>

#### bounds\_rotation

```python
@bounds_rotation.setter
def bounds_rotation(value: Rotator) -> None
```

<a id="unreal.EarthOutlineFragment"></a>