## CameraRoamingFrameEventArgs Objects

```python
class CameraRoamingFrameEventArgs(EventArgsBase)
```

Camera Roaming Frame Event Args

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``camera_roam_eid`` (int64):  [Read-Write]
- ``frame_index`` (int32):  [Read-Write]
- ``location`` (Vector):  [Read-Write]
- ``progress_ratio`` (float):  [Read-Write]

<a id="unreal.CameraRoamingFrameEventArgs.__init__"></a>

#### \_\_init\_\_

```python
def __init__(camera_roam_eid: int = 0,
             frame_index: int = 0,
             location: Vector = [0.000000, 0.000000, 0.000000],
             progress_ratio: float = 0.000000) -> None
```

<a id="unreal.CameraRoamingFrameEventArgs.camera_roam_eid"></a>

#### camera\_roam\_eid

```python
@property
def camera_roam_eid() -> int
```

(int64):  [Read-Write]

<a id="unreal.CameraRoamingFrameEventArgs.camera_roam_eid"></a>

#### camera\_roam\_eid

```python
@camera_roam_eid.setter
def camera_roam_eid(value: int) -> None
```

<a id="unreal.CameraRoamingFrameEventArgs.frame_index"></a>

#### frame\_index

```python
@property
def frame_index() -> int
```

(int32):  [Read-Write]

<a id="unreal.CameraRoamingFrameEventArgs.frame_index"></a>

#### frame\_index

```python
@frame_index.setter
def frame_index(value: int) -> None
```

<a id="unreal.CameraRoamingFrameEventArgs.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.CameraRoamingFrameEventArgs.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.CameraRoamingFrameEventArgs.progress_ratio"></a>

#### progress\_ratio

```python
@property
def progress_ratio() -> float
```

(float):  [Read-Write]

<a id="unreal.CameraRoamingFrameEventArgs.progress_ratio"></a>

#### progress\_ratio

```python
@progress_ratio.setter
def progress_ratio(value: float) -> None
```

<a id="unreal.CameraPresetApplyParams"></a>