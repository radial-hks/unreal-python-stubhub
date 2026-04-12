## WDPGetCameraInfoResult Objects

```python
class WDPGetCameraInfoResult(ResultBase)
```

WDPGet Camera Info Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control_mode`` (str):  [Read-Write]
- ``field_of_view`` (float):  [Read-Write]
- ``location`` (Vector):  [Read-Write]
- ``location_limit`` (Array[Vector2D]):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``pitch_limit`` (Vector2D):  [Read-Write]
- ``rotation`` (CameraPresetRotator):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]
- ``view_distance_limit`` (Vector2D):  [Read-Write]
- ``yaw_limit`` (Vector2D):  [Read-Write]

<a id="unreal.WDPGetCameraInfoResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             location: Vector = [0.000000, 0.000000, 0.000000],
             rotation: CameraPresetRotator = [0.000000, 0.000000],
             location_limit: Array[Vector2D] = [],
             pitch_limit: Vector2D = [0.000000, 0.000000],
             yaw_limit: Vector2D = [0.000000, 0.000000],
             view_distance_limit: Vector2D = [0.000000, 0.000000],
             control_mode: str = "",
             field_of_view: float = 0.000000) -> None
```

<a id="unreal.WDPGetCameraInfoResult.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.WDPGetCameraInfoResult.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.WDPGetCameraInfoResult.rotation"></a>

#### rotation

```python
@property
def rotation() -> CameraPresetRotator
```

(CameraPresetRotator):  [Read-Write]

<a id="unreal.WDPGetCameraInfoResult.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: CameraPresetRotator) -> None
```

<a id="unreal.WDPGetCameraInfoResult.location_limit"></a>

#### location\_limit

```python
@property
def location_limit() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.WDPGetCameraInfoResult.location_limit"></a>

#### location\_limit

```python
@location_limit.setter
def location_limit(value: Array[Vector2D]) -> None
```

<a id="unreal.WDPGetCameraInfoResult.pitch_limit"></a>

#### pitch\_limit

```python
@property
def pitch_limit() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.WDPGetCameraInfoResult.pitch_limit"></a>

#### pitch\_limit

```python
@pitch_limit.setter
def pitch_limit(value: Vector2D) -> None
```

<a id="unreal.WDPGetCameraInfoResult.yaw_limit"></a>

#### yaw\_limit

```python
@property
def yaw_limit() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.WDPGetCameraInfoResult.yaw_limit"></a>

#### yaw\_limit

```python
@yaw_limit.setter
def yaw_limit(value: Vector2D) -> None
```

<a id="unreal.WDPGetCameraInfoResult.view_distance_limit"></a>

#### view\_distance\_limit

```python
@property
def view_distance_limit() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.WDPGetCameraInfoResult.view_distance_limit"></a>

#### view\_distance\_limit

```python
@view_distance_limit.setter
def view_distance_limit(value: Vector2D) -> None
```

<a id="unreal.WDPGetCameraInfoResult.control_mode"></a>

#### control\_mode

```python
@property
def control_mode() -> str
```

(str):  [Read-Write]

<a id="unreal.WDPGetCameraInfoResult.control_mode"></a>

#### control\_mode

```python
@control_mode.setter
def control_mode(value: str) -> None
```

<a id="unreal.WDPGetCameraInfoResult.field_of_view"></a>

#### field\_of\_view

```python
@property
def field_of_view() -> float
```

(float):  [Read-Write]

<a id="unreal.WDPGetCameraInfoResult.field_of_view"></a>

#### field\_of\_view

```python
@field_of_view.setter
def field_of_view(value: float) -> None
```

<a id="unreal.WDPUpdateCameraInfoParams"></a>