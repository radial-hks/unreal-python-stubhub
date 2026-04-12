## WDPGetCameraAnimationResult Objects

```python
class WDPGetCameraAnimationResult(ResultBase)
```

WDPGet Camera Animation Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``show_rotate_icon`` (bool):  [Read-Write]
- ``show_touch_effect`` (bool):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.WDPGetCameraAnimationResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             show_touch_effect: bool = False,
             show_rotate_icon: bool = False) -> None
```

<a id="unreal.WDPGetCameraAnimationResult.show_touch_effect"></a>

#### show\_touch\_effect

```python
@property
def show_touch_effect() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WDPGetCameraAnimationResult.show_touch_effect"></a>

#### show\_touch\_effect

```python
@show_touch_effect.setter
def show_touch_effect(value: bool) -> None
```

<a id="unreal.WDPGetCameraAnimationResult.show_rotate_icon"></a>

#### show\_rotate\_icon

```python
@property
def show_rotate_icon() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WDPGetCameraAnimationResult.show_rotate_icon"></a>

#### show\_rotate\_icon

```python
@show_rotate_icon.setter
def show_rotate_icon(value: bool) -> None
```

<a id="unreal.WDPSetCameraAnimationParams"></a>