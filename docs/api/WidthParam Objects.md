## WidthParam Objects

```python
class WidthParam(StructBase)
```

Width Param

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ratio`` (float):  [Read-Write] 区间起点在样条线上的位置比率 (0-1)
- ``width`` (Vector2f):  [Read-Write] 区间样条线起点宽度

<a id="unreal.WidthParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(ratio: float = 0.000000,
             width: Vector2f = [0.000000, 0.000000]) -> None
```

<a id="unreal.WidthParam.ratio"></a>

#### ratio

```python
@property
def ratio() -> float
```

(float):  [Read-Write] 区间起点在样条线上的位置比率 (0-1)

<a id="unreal.WidthParam.ratio"></a>

#### ratio

```python
@ratio.setter
def ratio(value: float) -> None
```

<a id="unreal.WidthParam.width"></a>

#### width

```python
@property
def width() -> Vector2f
```

(Vector2f):  [Read-Write] 区间样条线起点宽度

<a id="unreal.WidthParam.width"></a>

#### width

```python
@width.setter
def width(value: Vector2f) -> None
```

<a id="unreal.EarthRoadInstanceShapeGrammar"></a>