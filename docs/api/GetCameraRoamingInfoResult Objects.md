## GetCameraRoamingInfoResult Objects

```python
class GetCameraRoamingInfoResult(ResultBase)
```

Get Camera Roaming Info Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``progress_ratio`` (float):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.GetCameraRoamingInfoResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             progress_ratio: float = 0.000000) -> None
```

<a id="unreal.GetCameraRoamingInfoResult.progress_ratio"></a>

#### progress\_ratio

```python
@property
def progress_ratio() -> float
```

(float):  [Read-Write]

<a id="unreal.GetCameraRoamingInfoResult.progress_ratio"></a>

#### progress\_ratio

```python
@progress_ratio.setter
def progress_ratio(value: float) -> None
```

<a id="unreal.CameraRoamingFrameEventArgs"></a>