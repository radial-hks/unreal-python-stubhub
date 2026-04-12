## WDPCameraRoamParams Objects

```python
class WDPCameraRoamParams(ParamsBase)
```

WDPCamera Roam Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``camera_roam_eid`` (int64):  [Read-Write]
- ``enable_rotating_on_pause`` (bool):  [Read-Write]
- ``enable_zooming_on_pause`` (bool):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``progress_ratio`` (float):  [Read-Write]
- ``reverse`` (bool):  [Read-Write]
- ``speed_ratio`` (float):  [Read-Write]
- ``state`` (WdpCameraRoamState):  [Read-Write]

<a id="unreal.WDPCameraRoamParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(camera_roam_eid: int = 0,
             state: WdpCameraRoamState = WdpCameraRoamState.PLAY,
             progress_ratio: float = 0.000000,
             speed_ratio: float = 0.000000,
             reverse: bool = False,
             enable_rotating_on_pause: bool = False,
             enable_zooming_on_pause: bool = False) -> None
```

<a id="unreal.WDPCameraRoamParams.camera_roam_eid"></a>

#### camera\_roam\_eid

```python
@property
def camera_roam_eid() -> int
```

(int64):  [Read-Write]

<a id="unreal.WDPCameraRoamParams.camera_roam_eid"></a>

#### camera\_roam\_eid

```python
@camera_roam_eid.setter
def camera_roam_eid(value: int) -> None
```

<a id="unreal.WDPCameraRoamParams.state"></a>

#### state

```python
@property
def state() -> WdpCameraRoamState
```

(WdpCameraRoamState):  [Read-Write]

<a id="unreal.WDPCameraRoamParams.state"></a>

#### state

```python
@state.setter
def state(value: WdpCameraRoamState) -> None
```

<a id="unreal.WDPCameraRoamParams.progress_ratio"></a>

#### progress\_ratio

```python
@property
def progress_ratio() -> float
```

(float):  [Read-Write]

<a id="unreal.WDPCameraRoamParams.progress_ratio"></a>

#### progress\_ratio

```python
@progress_ratio.setter
def progress_ratio(value: float) -> None
```

<a id="unreal.WDPCameraRoamParams.speed_ratio"></a>

#### speed\_ratio

```python
@property
def speed_ratio() -> float
```

(float):  [Read-Write]

<a id="unreal.WDPCameraRoamParams.speed_ratio"></a>

#### speed\_ratio

```python
@speed_ratio.setter
def speed_ratio(value: float) -> None
```

<a id="unreal.WDPCameraRoamParams.reverse"></a>

#### reverse

```python
@property
def reverse() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WDPCameraRoamParams.reverse"></a>

#### reverse

```python
@reverse.setter
def reverse(value: bool) -> None
```

<a id="unreal.WDPCameraRoamParams.enable_rotating_on_pause"></a>

#### enable\_rotating\_on\_pause

```python
@property
def enable_rotating_on_pause() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WDPCameraRoamParams.enable_rotating_on_pause"></a>

#### enable\_rotating\_on\_pause

```python
@enable_rotating_on_pause.setter
def enable_rotating_on_pause(value: bool) -> None
```

<a id="unreal.WDPCameraRoamParams.enable_zooming_on_pause"></a>

#### enable\_zooming\_on\_pause

```python
@property
def enable_zooming_on_pause() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WDPCameraRoamParams.enable_zooming_on_pause"></a>

#### enable\_zooming\_on\_pause

```python
@enable_zooming_on_pause.setter
def enable_zooming_on_pause(value: bool) -> None
```

<a id="unreal.GetCameraRoamingInfoParams"></a>