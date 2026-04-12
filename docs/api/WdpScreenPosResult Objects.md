## WdpScreenPosResult Objects

```python
class WdpScreenPosResult(ResultBase)
```

Wdp Screen Pos Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: ApplicationAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``screen_pos`` (Vector2D):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.WdpScreenPosResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             screen_pos: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.WdpScreenPosResult.screen_pos"></a>

#### screen\_pos

```python
@property
def screen_pos() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.WdpScreenPosResult.screen_pos"></a>

#### screen\_pos

```python
@screen_pos.setter
def screen_pos(value: Vector2D) -> None
```

<a id="unreal.VisibleParams"></a>