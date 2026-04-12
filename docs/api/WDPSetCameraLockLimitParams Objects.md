## WDPSetCameraLockLimitParams Objects

```python
class WDPSetCameraLockLimitParams(ParamsBase)
```

WDPSet Camera Lock Limit Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``location_limit`` (float):  [Read-Write]
- ``pitch_limit`` (float):  [Read-Write]
- ``view_distance_limit`` (float):  [Read-Write]
- ``yaw_limit`` (float):  [Read-Write]

<a id="unreal.WDPSetCameraLockLimitParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(location_limit: float = 0.000000,
             pitch_limit: float = 0.000000,
             yaw_limit: float = 0.000000,
             view_distance_limit: float = 0.000000) -> None
```

<a id="unreal.WDPSetCameraLockLimitParams.location_limit"></a>

#### location\_limit

```python
@property
def location_limit() -> float
```

(float):  [Read-Write]

<a id="unreal.WDPSetCameraLockLimitParams.location_limit"></a>

#### location\_limit

```python
@location_limit.setter
def location_limit(value: float) -> None
```

<a id="unreal.WDPSetCameraLockLimitParams.pitch_limit"></a>

#### pitch\_limit

```python
@property
def pitch_limit() -> float
```

(float):  [Read-Write]

<a id="unreal.WDPSetCameraLockLimitParams.pitch_limit"></a>

#### pitch\_limit

```python
@pitch_limit.setter
def pitch_limit(value: float) -> None
```

<a id="unreal.WDPSetCameraLockLimitParams.yaw_limit"></a>

#### yaw\_limit

```python
@property
def yaw_limit() -> float
```

(float):  [Read-Write]

<a id="unreal.WDPSetCameraLockLimitParams.yaw_limit"></a>

#### yaw\_limit

```python
@yaw_limit.setter
def yaw_limit(value: float) -> None
```

<a id="unreal.WDPSetCameraLockLimitParams.view_distance_limit"></a>

#### view\_distance\_limit

```python
@property
def view_distance_limit() -> float
```

(float):  [Read-Write]

<a id="unreal.WDPSetCameraLockLimitParams.view_distance_limit"></a>

#### view\_distance\_limit

```python
@view_distance_limit.setter
def view_distance_limit(value: float) -> None
```

<a id="unreal.WDPResetCameraLimitParams"></a>