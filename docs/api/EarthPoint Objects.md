## EarthPoint Objects

```python
class EarthPoint(StructBase)
```

点数据

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthPoint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bounds_max`` (Vector):  [Read-Write] 包围盒最大值
- ``bounds_min`` (Vector):  [Read-Write] 包围盒最小值
- ``color`` (Vector4):  [Read-Write] 颜色
- ``seed`` (int32):  [Read-Write] 随机种子
- ``transform`` (Transform):  [Read-Write] 坐标变换

<a id="unreal.EarthPoint.__init__"></a>

#### \_\_init\_\_

```python
def __init__(transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
             bounds_min: Vector = [0.000000, 0.000000, 0.000000],
             bounds_max: Vector = [0.000000, 0.000000, 0.000000],
             color: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000],
             seed: int = 0) -> None
```

<a id="unreal.EarthPoint.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write] 坐标变换

<a id="unreal.EarthPoint.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.EarthPoint.bounds_min"></a>

#### bounds\_min

```python
@property
def bounds_min() -> Vector
```

(Vector):  [Read-Write] 包围盒最小值

<a id="unreal.EarthPoint.bounds_min"></a>

#### bounds\_min

```python
@bounds_min.setter
def bounds_min(value: Vector) -> None
```

<a id="unreal.EarthPoint.bounds_max"></a>

#### bounds\_max

```python
@property
def bounds_max() -> Vector
```

(Vector):  [Read-Write] 包围盒最大值

<a id="unreal.EarthPoint.bounds_max"></a>

#### bounds\_max

```python
@bounds_max.setter
def bounds_max(value: Vector) -> None
```

<a id="unreal.EarthPoint.color"></a>

#### color

```python
@property
def color() -> Vector4
```

(Vector4):  [Read-Write] 颜色

<a id="unreal.EarthPoint.color"></a>

#### color

```python
@color.setter
def color(value: Vector4) -> None
```

<a id="unreal.EarthPoint.seed"></a>

#### seed

```python
@property
def seed() -> int
```

(int32):  [Read-Write] 随机种子

<a id="unreal.EarthPoint.seed"></a>

#### seed

```python
@seed.setter
def seed(value: int) -> None
```

<a id="unreal.EarthRegionOutline"></a>