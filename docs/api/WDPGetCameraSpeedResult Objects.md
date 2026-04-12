## WDPGetCameraSpeedResult Objects

```python
class WDPGetCameraSpeedResult(ResultBase)
```

WDPGet Camera Speed Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable_dynamic_speed`` (bool):  [Read-Write]
- ``key_movement_base_speed`` (float):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``rotation_pitch_speed_scale`` (float):  [Read-Write]
- ``rotation_yaw_speed_scale`` (float):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]
- ``zoom_speed_scale`` (float):  [Read-Write]

<a id="unreal.WDPGetCameraSpeedResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             rotation_yaw_speed_scale: float = 0.000000,
             rotation_pitch_speed_scale: float = 0.000000,
             zoom_speed_scale: float = 0.000000,
             key_movement_base_speed: float = 0.000000,
             enable_dynamic_speed: bool = False) -> None
```

<a id="unreal.WDPGetCameraSpeedResult.rotation_yaw_speed_scale"></a>

#### rotation\_yaw\_speed\_scale

```python
@property
def rotation_yaw_speed_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.WDPGetCameraSpeedResult.rotation_yaw_speed_scale"></a>

#### rotation\_yaw\_speed\_scale

```python
@rotation_yaw_speed_scale.setter
def rotation_yaw_speed_scale(value: float) -> None
```

<a id="unreal.WDPGetCameraSpeedResult.rotation_pitch_speed_scale"></a>

#### rotation\_pitch\_speed\_scale

```python
@property
def rotation_pitch_speed_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.WDPGetCameraSpeedResult.rotation_pitch_speed_scale"></a>

#### rotation\_pitch\_speed\_scale

```python
@rotation_pitch_speed_scale.setter
def rotation_pitch_speed_scale(value: float) -> None
```

<a id="unreal.WDPGetCameraSpeedResult.zoom_speed_scale"></a>

#### zoom\_speed\_scale

```python
@property
def zoom_speed_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.WDPGetCameraSpeedResult.zoom_speed_scale"></a>

#### zoom\_speed\_scale

```python
@zoom_speed_scale.setter
def zoom_speed_scale(value: float) -> None
```

<a id="unreal.WDPGetCameraSpeedResult.key_movement_base_speed"></a>

#### key\_movement\_base\_speed

```python
@property
def key_movement_base_speed() -> float
```

(float):  [Read-Write]

<a id="unreal.WDPGetCameraSpeedResult.key_movement_base_speed"></a>

#### key\_movement\_base\_speed

```python
@key_movement_base_speed.setter
def key_movement_base_speed(value: float) -> None
```

<a id="unreal.WDPGetCameraSpeedResult.enable_dynamic_speed"></a>

#### enable\_dynamic\_speed

```python
@property
def enable_dynamic_speed() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WDPGetCameraSpeedResult.enable_dynamic_speed"></a>

#### enable\_dynamic\_speed

```python
@enable_dynamic_speed.setter
def enable_dynamic_speed(value: bool) -> None
```

<a id="unreal.WDPSetCameraSpeedParams"></a>