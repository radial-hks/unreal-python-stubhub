## WDPResetCameraLimitParams Objects

```python
class WDPResetCameraLimitParams(ParamsBase)
```

WDPReset Camera Limit Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``state`` (WdpResetCameraLimitState):  [Read-Write]

<a id="unreal.WDPResetCameraLimitParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    state: WdpResetCameraLimitState = WdpResetCameraLimitState.DEFAULT
) -> None
```

<a id="unreal.WDPResetCameraLimitParams.state"></a>

#### state

```python
@property
def state() -> WdpResetCameraLimitState
```

(WdpResetCameraLimitState):  [Read-Write]

<a id="unreal.WDPResetCameraLimitParams.state"></a>

#### state

```python
@state.setter
def state(value: WdpResetCameraLimitState) -> None
```

<a id="unreal.WDPGetCameraSpeedResult"></a>