## ClipColumnarHeatMapParam Objects

```python
class ClipColumnarHeatMapParam(ParamsBase)
```

Clip Columnar Heat Map Param

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: ColumnarHeatMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (str):  [Read-Write]
- ``eid`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``polygon`` (Polygon_ColumnarHeatMapClip):  [Read-Write]

<a id="unreal.ClipColumnarHeatMapParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: str = "",
             polygon: Polygon_ColumnarHeatMapClip = [[[], []]],
             color: str = "") -> None
```

<a id="unreal.ClipColumnarHeatMapParam.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.ClipColumnarHeatMapParam.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.ClipColumnarHeatMapParam.polygon"></a>

#### polygon

```python
@property
def polygon() -> Polygon_ColumnarHeatMapClip
```

(Polygon_ColumnarHeatMapClip):  [Read-Write]

<a id="unreal.ClipColumnarHeatMapParam.polygon"></a>

#### polygon

```python
@polygon.setter
def polygon(value: Polygon_ColumnarHeatMapClip) -> None
```

<a id="unreal.ClipColumnarHeatMapParam.color"></a>

#### color

```python
@property
def color() -> str
```

(str):  [Read-Write]

<a id="unreal.ClipColumnarHeatMapParam.color"></a>

#### color

```python
@color.setter
def color(value: str) -> None
```

<a id="unreal.ColumnarHeatMapInfoParam"></a>