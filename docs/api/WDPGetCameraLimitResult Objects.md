## WDPGetCameraLimitResult Objects

```python
class WDPGetCameraLimitResult(ResultBase)
```

WDPGet Camera Limit Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``location_limit`` (Array[Vector2D]):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``pitch_limit`` (Vector2D):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]
- ``view_distance_limit`` (Vector2D):  [Read-Write]
- ``yaw_limit`` (Vector2D):  [Read-Write]

<a id="unreal.WDPGetCameraLimitResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             location_limit: Array[Vector2D] = [],
             pitch_limit: Vector2D = [0.000000, 0.000000],
             yaw_limit: Vector2D = [0.000000, 0.000000],
             view_distance_limit: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.WDPGetCameraLimitResult.location_limit"></a>

#### location\_limit

```python
@property
def location_limit() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.WDPGetCameraLimitResult.location_limit"></a>

#### location\_limit

```python
@location_limit.setter
def location_limit(value: Array[Vector2D]) -> None
```

<a id="unreal.WDPGetCameraLimitResult.pitch_limit"></a>

#### pitch\_limit

```python
@property
def pitch_limit() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.WDPGetCameraLimitResult.pitch_limit"></a>

#### pitch\_limit

```python
@pitch_limit.setter
def pitch_limit(value: Vector2D) -> None
```

<a id="unreal.WDPGetCameraLimitResult.yaw_limit"></a>

#### yaw\_limit

```python
@property
def yaw_limit() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.WDPGetCameraLimitResult.yaw_limit"></a>

#### yaw\_limit

```python
@yaw_limit.setter
def yaw_limit(value: Vector2D) -> None
```

<a id="unreal.WDPGetCameraLimitResult.view_distance_limit"></a>

#### view\_distance\_limit

```python
@property
def view_distance_limit() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.WDPGetCameraLimitResult.view_distance_limit"></a>

#### view\_distance\_limit

```python
@view_distance_limit.setter
def view_distance_limit(value: Vector2D) -> None
```

<a id="unreal.WDPSetCameraLockLimitParams"></a>