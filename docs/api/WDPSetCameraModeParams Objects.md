## WDPSetCameraModeParams Objects

```python
class WDPSetCameraModeParams(ParamsBase)
```

WDPSet Camera Mode Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control_mode`` (WdpCameraControlMode):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.WDPSetCameraModeParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        control_mode: WdpCameraControlMode = WdpCameraControlMode.RTS) -> None
```

<a id="unreal.WDPSetCameraModeParams.control_mode"></a>

#### control\_mode

```python
@property
def control_mode() -> WdpCameraControlMode
```

(WdpCameraControlMode):  [Read-Write]

<a id="unreal.WDPSetCameraModeParams.control_mode"></a>

#### control\_mode

```python
@control_mode.setter
def control_mode(value: WdpCameraControlMode) -> None
```

<a id="unreal.WDPSetCameraPoseParams"></a>