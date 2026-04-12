## WdpGetPickedPointsResult Objects

```python
class WdpGetPickedPointsResult(ResultBase)
```

Wdp Get Picked Points Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpPickPointAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``picked_points`` (Array[Vector]):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.WdpGetPickedPointsResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             picked_points: Array[Vector] = []) -> None
```

<a id="unreal.WdpGetPickedPointsResult.picked_points"></a>

#### picked\_points

```python
@property
def picked_points() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.WdpGetPickedPointsResult.picked_points"></a>

#### picked\_points

```python
@picked_points.setter
def picked_points(value: Array[Vector]) -> None
```

<a id="unreal.WdpGetPickedPolylinesParams"></a>