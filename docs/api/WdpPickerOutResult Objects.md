## WdpPickerOutResult Objects

```python
class WdpPickerOutResult(EidResult)
```

Wdp Picker Out Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpPickerAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``point`` (Vector):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.WdpPickerOutResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             point: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.WdpPickerOutResult.point"></a>

#### point

```python
@property
def point() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.WdpPickerOutResult.point"></a>

#### point

```python
@point.setter
def point(value: Vector) -> None
```

<a id="unreal.WdpRectPickerResult"></a>