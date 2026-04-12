## FollowCameraSettings Objects

```python
class FollowCameraSettings(StructBase)
```

Follow 模式的相机配置

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpDataSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_resore_time`` (float):  [Read-Write] 当不操作相机时，自动回正的时间，0代表禁止操作相机，小于0代表不回正
- ``default_distance`` (double):  [Read-Write] 初始距离
- ``default_fov`` (float):  [Read-Write] 初始FOV
- ``default_rotation`` (Rotator):  [Read-Write] 初始旋转
- ``distance_limit`` (Vector2D):  [Read-Write] 距离限制
- ``pivot_location`` (Vector):  [Read-Write] 旋转轴心
- ``rotation_lag_speed`` (float):  [Read-Write] 旋转的lag速度
- ``use_relative_rotation`` (bool):  [Read-Write] 旋转是否为Relative

<a id="unreal.FollowCameraSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(pivot_location: Vector = [0.000000, 0.000000, 0.000000],
             default_rotation: Rotator = [0.000000, 0.000000, 0.000000],
             use_relative_rotation: bool = False,
             rotation_lag_speed: float = 0.000000,
             default_distance: float = 0.000000,
             distance_limit: Vector2D = [0.000000, 0.000000],
             default_fov: float = 0.000000,
             auto_resore_time: float = 0.000000) -> None
```

<a id="unreal.FollowCameraSettings.pivot_location"></a>

#### pivot\_location

```python
@property
def pivot_location() -> Vector
```

(Vector):  [Read-Write] 旋转轴心

<a id="unreal.FollowCameraSettings.pivot_location"></a>

#### pivot\_location

```python
@pivot_location.setter
def pivot_location(value: Vector) -> None
```

<a id="unreal.FollowCameraSettings.default_rotation"></a>

#### default\_rotation

```python
@property
def default_rotation() -> Rotator
```

(Rotator):  [Read-Write] 初始旋转

<a id="unreal.FollowCameraSettings.default_rotation"></a>

#### default\_rotation

```python
@default_rotation.setter
def default_rotation(value: Rotator) -> None
```

<a id="unreal.FollowCameraSettings.use_relative_rotation"></a>

#### use\_relative\_rotation

```python
@property
def use_relative_rotation() -> bool
```

(bool):  [Read-Write] 旋转是否为Relative

<a id="unreal.FollowCameraSettings.use_relative_rotation"></a>

#### use\_relative\_rotation

```python
@use_relative_rotation.setter
def use_relative_rotation(value: bool) -> None
```

<a id="unreal.FollowCameraSettings.rotation_lag_speed"></a>

#### rotation\_lag\_speed

```python
@property
def rotation_lag_speed() -> float
```

(float):  [Read-Write] 旋转的lag速度

<a id="unreal.FollowCameraSettings.rotation_lag_speed"></a>

#### rotation\_lag\_speed

```python
@rotation_lag_speed.setter
def rotation_lag_speed(value: float) -> None
```

<a id="unreal.FollowCameraSettings.default_distance"></a>

#### default\_distance

```python
@property
def default_distance() -> float
```

(double):  [Read-Write] 初始距离

<a id="unreal.FollowCameraSettings.default_distance"></a>

#### default\_distance

```python
@default_distance.setter
def default_distance(value: float) -> None
```

<a id="unreal.FollowCameraSettings.distance_limit"></a>

#### distance\_limit

```python
@property
def distance_limit() -> Vector2D
```

(Vector2D):  [Read-Write] 距离限制

<a id="unreal.FollowCameraSettings.distance_limit"></a>

#### distance\_limit

```python
@distance_limit.setter
def distance_limit(value: Vector2D) -> None
```

<a id="unreal.FollowCameraSettings.default_fov"></a>

#### default\_fov

```python
@property
def default_fov() -> float
```

(float):  [Read-Write] 初始FOV

<a id="unreal.FollowCameraSettings.default_fov"></a>

#### default\_fov

```python
@default_fov.setter
def default_fov(value: float) -> None
```

<a id="unreal.FollowCameraSettings.auto_resore_time"></a>

#### auto\_resore\_time

```python
@property
def auto_resore_time() -> float
```

(float):  [Read-Write] 当不操作相机时，自动回正的时间，0代表禁止操作相机，小于0代表不回正

<a id="unreal.FollowCameraSettings.auto_resore_time"></a>

#### auto\_resore\_time

```python
@auto_resore_time.setter
def auto_resore_time(value: float) -> None
```

<a id="unreal.WdpShapeChangedPointInfo"></a>