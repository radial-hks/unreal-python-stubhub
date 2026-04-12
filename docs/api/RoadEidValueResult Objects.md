## RoadEidValueResult Objects

```python
class RoadEidValueResult(ResultBase)
```

Road Eid Value Result

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: RoadHeatMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (str):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]
- ``value`` (str):  [Read-Write]

<a id="unreal.RoadEidValueResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             eid: str = "",
             value: str = "") -> None
```

<a id="unreal.RoadEidValueResult.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.RoadEidValueResult.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.RoadEidValueResult.value"></a>

#### value

```python
@property
def value() -> str
```

(str):  [Read-Write]

<a id="unreal.RoadEidValueResult.value"></a>

#### value

```python
@value.setter
def value(value: str) -> None
```

<a id="unreal.SectionTransformParams"></a>