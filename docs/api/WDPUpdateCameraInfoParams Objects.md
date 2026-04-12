## WDPUpdateCameraInfoParams Objects

```python
class WDPUpdateCameraInfoParams(ParamsBase)
```

WDPUpdate Camera Info Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control_mode`` (WdpCameraControlMode):  [Read-Write]
- ``field_of_view`` (float):  [Read-Write]
- ``fly_time`` (float):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``location`` (Vector):  [Read-Write]
- ``location_limit`` (Array[Vector2D]):  [Read-Write]
- ``pitch_limit`` (Vector2D):  [Read-Write]
- ``rotation`` (CameraPresetRotator):  [Read-Write]
- ``view_distance_limit`` (Vector2D):  [Read-Write]
- ``yaw_limit`` (Vector2D):  [Read-Write]

<a id="unreal.WDPUpdateCameraInfoParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(location: Vector = [0.000000, 0.000000, 0.000000],
             rotation: CameraPresetRotator = [0.000000, 0.000000],
             location_limit: Array[Vector2D] = [],
             pitch_limit: Vector2D = [0.000000, 0.000000],
             yaw_limit: Vector2D = [0.000000, 0.000000],
             view_distance_limit: Vector2D = [0.000000, 0.000000],
             control_mode: WdpCameraControlMode = WdpCameraControlMode.RTS,
             field_of_view: float = 0.000000,
             fly_time: float = 0.000000) -> None
```

<a id="unreal.WDPUpdateCameraInfoParams.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.WDPUpdateCameraInfoParams.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.WDPUpdateCameraInfoParams.rotation"></a>

#### rotation

```python
@property
def rotation() -> CameraPresetRotator
```

(CameraPresetRotator):  [Read-Write]

<a id="unreal.WDPUpdateCameraInfoParams.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: CameraPresetRotator) -> None
```

<a id="unreal.WDPUpdateCameraInfoParams.location_limit"></a>

#### location\_limit

```python
@property
def location_limit() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.WDPUpdateCameraInfoParams.location_limit"></a>

#### location\_limit

```python
@location_limit.setter
def location_limit(value: Array[Vector2D]) -> None
```

<a id="unreal.WDPUpdateCameraInfoParams.pitch_limit"></a>

#### pitch\_limit

```python
@property
def pitch_limit() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.WDPUpdateCameraInfoParams.pitch_limit"></a>

#### pitch\_limit

```python
@pitch_limit.setter
def pitch_limit(value: Vector2D) -> None
```

<a id="unreal.WDPUpdateCameraInfoParams.yaw_limit"></a>

#### yaw\_limit

```python
@property
def yaw_limit() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.WDPUpdateCameraInfoParams.yaw_limit"></a>

#### yaw\_limit

```python
@yaw_limit.setter
def yaw_limit(value: Vector2D) -> None
```

<a id="unreal.WDPUpdateCameraInfoParams.view_distance_limit"></a>

#### view\_distance\_limit

```python
@property
def view_distance_limit() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.WDPUpdateCameraInfoParams.view_distance_limit"></a>

#### view\_distance\_limit

```python
@view_distance_limit.setter
def view_distance_limit(value: Vector2D) -> None
```

<a id="unreal.WDPUpdateCameraInfoParams.control_mode"></a>

#### control\_mode

```python
@property
def control_mode() -> WdpCameraControlMode
```

(WdpCameraControlMode):  [Read-Write]

<a id="unreal.WDPUpdateCameraInfoParams.control_mode"></a>

#### control\_mode

```python
@control_mode.setter
def control_mode(value: WdpCameraControlMode) -> None
```

<a id="unreal.WDPUpdateCameraInfoParams.field_of_view"></a>

#### field\_of\_view

```python
@property
def field_of_view() -> float
```

(float):  [Read-Write]

<a id="unreal.WDPUpdateCameraInfoParams.field_of_view"></a>

#### field\_of\_view

```python
@field_of_view.setter
def field_of_view(value: float) -> None
```

<a id="unreal.WDPUpdateCameraInfoParams.fly_time"></a>

#### fly\_time

```python
@property
def fly_time() -> float
```

(float):  [Read-Write]

<a id="unreal.WDPUpdateCameraInfoParams.fly_time"></a>

#### fly\_time

```python
@fly_time.setter
def fly_time(value: float) -> None
```

<a id="unreal.WDPCameraBaseTransformParams"></a>