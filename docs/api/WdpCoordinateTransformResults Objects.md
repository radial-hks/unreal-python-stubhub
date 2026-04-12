## WdpCoordinateTransformResults Objects

```python
class WdpCoordinateTransformResults(ResultBase)
```

Wdp Coordinate Transform Results

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: ApplicationAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]
- ``to`` (Array[Vector]):  [Read-Write]

<a id="unreal.WdpCoordinateTransformResults.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             to: Array[Vector] = []) -> None
```

<a id="unreal.WdpCoordinateTransformResults.to"></a>

#### to

```python
@property
def to() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.WdpCoordinateTransformResults.to"></a>

#### to

```python
@to.setter
def to(value: Array[Vector]) -> None
```

<a id="unreal.WdpScreenPositionResult"></a>