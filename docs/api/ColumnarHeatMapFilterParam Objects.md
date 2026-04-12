## ColumnarHeatMapFilterParam Objects

```python
class ColumnarHeatMapFilterParam(ParamsBase)
```

Columnar Heat Map Filter Param

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: ColumnarHeatMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (str):  [Read-Write]
- ``filter_value_range`` (Vector2D):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.ColumnarHeatMapFilterParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: str = "",
             filter_value_range: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.ColumnarHeatMapFilterParam.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.ColumnarHeatMapFilterParam.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.ColumnarHeatMapFilterParam.filter_value_range"></a>

#### filter\_value\_range

```python
@property
def filter_value_range() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.ColumnarHeatMapFilterParam.filter_value_range"></a>

#### filter\_value\_range

```python
@filter_value_range.setter
def filter_value_range(value: Vector2D) -> None
```

<a id="unreal.UnColumnarHeatMapFilterParam"></a>