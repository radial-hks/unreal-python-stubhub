## WdpGetPickedPolylinesResult Objects

```python
class WdpGetPickedPolylinesResult(ResultBase)
```

Wdp Get Picked Polylines Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpPickPolylineAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``picked_polylines`` (Array[WdpPolyline]):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.WdpGetPickedPolylinesResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             picked_polylines: Array[WdpPolyline] = []) -> None
```

<a id="unreal.WdpGetPickedPolylinesResult.picked_polylines"></a>

#### picked\_polylines

```python
@property
def picked_polylines() -> Array[WdpPolyline]
```

(Array[WdpPolyline]):  [Read-Write]

<a id="unreal.WdpGetPickedPolylinesResult.picked_polylines"></a>

#### picked\_polylines

```python
@picked_polylines.setter
def picked_polylines(value: Array[WdpPolyline]) -> None
```

<a id="unreal.SelectionFilter"></a>