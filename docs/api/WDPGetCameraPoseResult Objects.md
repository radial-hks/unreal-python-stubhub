## WDPGetCameraPoseResult Objects

```python
class WDPGetCameraPoseResult(ResultBase)
```

WDPGet Camera Pose Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``location`` (Vector):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``rotation`` (CameraPresetRotator):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.WDPGetCameraPoseResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             location: Vector = [0.000000, 0.000000, 0.000000],
             rotation: CameraPresetRotator = [0.000000, 0.000000]) -> None
```

<a id="unreal.WDPGetCameraPoseResult.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.WDPGetCameraPoseResult.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.WDPGetCameraPoseResult.rotation"></a>

#### rotation

```python
@property
def rotation() -> CameraPresetRotator
```

(CameraPresetRotator):  [Read-Write]

<a id="unreal.WDPGetCameraPoseResult.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: CameraPresetRotator) -> None
```

<a id="unreal.WDPSetCameraLimitParams"></a>