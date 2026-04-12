## RoadHeatMapInfoParam Objects

```python
class RoadHeatMapInfoParam(ParamsBase)
```

Road Heat Map Info Param

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: RoadHeatMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``location`` (Vector):  [Read-Write]

<a id="unreal.RoadHeatMapInfoParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: str = "",
             location: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RoadHeatMapInfoParam.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.RoadHeatMapInfoParam.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.RoadHeatMapInfoParam.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RoadHeatMapInfoParam.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.RoadHeatMapFilterParam"></a>