## ClipHeatMapParam Objects

```python
class ClipHeatMapParam(ParamsBase)
```

Clip Heat Map Param

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: HeatMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (str):  [Read-Write]
- ``eid`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``polygon`` (Polygon_HeatMapClip):  [Read-Write]

<a id="unreal.ClipHeatMapParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: str = "",
             polygon: Polygon_HeatMapClip = [[[], []]],
             color: str = "") -> None
```

<a id="unreal.ClipHeatMapParam.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.ClipHeatMapParam.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.ClipHeatMapParam.polygon"></a>

#### polygon

```python
@property
def polygon() -> Polygon_HeatMapClip
```

(Polygon_HeatMapClip):  [Read-Write]

<a id="unreal.ClipHeatMapParam.polygon"></a>

#### polygon

```python
@polygon.setter
def polygon(value: Polygon_HeatMapClip) -> None
```

<a id="unreal.ClipHeatMapParam.color"></a>

#### color

```python
@property
def color() -> str
```

(str):  [Read-Write]

<a id="unreal.ClipHeatMapParam.color"></a>

#### color

```python
@color.setter
def color(value: str) -> None
```

<a id="unreal.ModifyHeatMapfeatures"></a>