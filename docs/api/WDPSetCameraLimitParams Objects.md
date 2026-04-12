## WDPSetCameraLimitParams Objects

```python
class WDPSetCameraLimitParams(ParamsBase)
```

WDPSet Camera Limit Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``location_limit`` (Array[Vector2D]):  [Read-Write]
- ``pitch_limit`` (Vector2D):  [Read-Write]
- ``view_distance_limit`` (Vector2D):  [Read-Write]
- ``yaw_limit`` (Vector2D):  [Read-Write]

<a id="unreal.WDPSetCameraLimitParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(location_limit: Array[Vector2D] = [],
             pitch_limit: Vector2D = [0.000000, 0.000000],
             yaw_limit: Vector2D = [0.000000, 0.000000],
             view_distance_limit: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.WDPSetCameraLimitParams.location_limit"></a>

#### location\_limit

```python
@property
def location_limit() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.WDPSetCameraLimitParams.location_limit"></a>

#### location\_limit

```python
@location_limit.setter
def location_limit(value: Array[Vector2D]) -> None
```

<a id="unreal.WDPSetCameraLimitParams.pitch_limit"></a>

#### pitch\_limit

```python
@property
def pitch_limit() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.WDPSetCameraLimitParams.pitch_limit"></a>

#### pitch\_limit

```python
@pitch_limit.setter
def pitch_limit(value: Vector2D) -> None
```

<a id="unreal.WDPSetCameraLimitParams.yaw_limit"></a>

#### yaw\_limit

```python
@property
def yaw_limit() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.WDPSetCameraLimitParams.yaw_limit"></a>

#### yaw\_limit

```python
@yaw_limit.setter
def yaw_limit(value: Vector2D) -> None
```

<a id="unreal.WDPSetCameraLimitParams.view_distance_limit"></a>

#### view\_distance\_limit

```python
@property
def view_distance_limit() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.WDPSetCameraLimitParams.view_distance_limit"></a>

#### view\_distance\_limit

```python
@view_distance_limit.setter
def view_distance_limit(value: Vector2D) -> None
```

<a id="unreal.WDPGetCameraLimitResult"></a>