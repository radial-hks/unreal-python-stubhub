## RoadHeatMapData Objects

```python
class RoadHeatMapData(StructBase)
```

Road Heat Map Data

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: RoadHeatMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``point_entity_eid`` (str):  [Read-Write]
- ``value`` (float):  [Read-Write]

<a id="unreal.RoadHeatMapData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(point_entity_eid: str = "", value: float = 0.000000) -> None
```

<a id="unreal.RoadHeatMapData.point_entity_eid"></a>

#### point\_entity\_eid

```python
@property
def point_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.RoadHeatMapData.point_entity_eid"></a>

#### point\_entity\_eid

```python
@point_entity_eid.setter
def point_entity_eid(value: str) -> None
```

<a id="unreal.RoadHeatMapData.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write]

<a id="unreal.RoadHeatMapData.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.CreateRoadHeatMapParams"></a>