## WDPResetCameraPoseParams Objects

```python
class WDPResetCameraPoseParams(ParamsBase)
```

WDPReset Camera Pose Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``fly_time`` (float):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``state`` (WdpResetCameraPoseState):  [Read-Write]

<a id="unreal.WDPResetCameraPoseParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(state: WdpResetCameraPoseState = WdpResetCameraPoseState.DEFAULT,
             fly_time: float = 0.000000) -> None
```

<a id="unreal.WDPResetCameraPoseParams.state"></a>

#### state

```python
@property
def state() -> WdpResetCameraPoseState
```

(WdpResetCameraPoseState):  [Read-Write]

<a id="unreal.WDPResetCameraPoseParams.state"></a>

#### state

```python
@state.setter
def state(value: WdpResetCameraPoseState) -> None
```

<a id="unreal.WDPResetCameraPoseParams.fly_time"></a>

#### fly\_time

```python
@property
def fly_time() -> float
```

(float):  [Read-Write]

<a id="unreal.WDPResetCameraPoseParams.fly_time"></a>

#### fly\_time

```python
@fly_time.setter
def fly_time(value: float) -> None
```

<a id="unreal.WDPGetCameraPoseResult"></a>