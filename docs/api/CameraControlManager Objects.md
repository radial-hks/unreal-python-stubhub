## CameraControlManager Objects

```python
class CameraControlManager(WorldSubsystem)
```

Camera Control Manager

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: CameraControlManager.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``camera_control_pitch_limit`` (Vector2D):  [Read-Write] ********************************************************// 旋转限制参数规范化控制
  // todo: 后续需要接入存档
- ``camera_control_yaw_limit`` (Vector2D):  [Read-Write]

<a id="unreal.CameraControlManager.camera_control_pitch_limit"></a>

#### camera\_control\_pitch\_limit

```python
@property
def camera_control_pitch_limit() -> Vector2D
```

(Vector2D):  [Read-Only] ********************************************************// 旋转限制参数规范化控制
// todo: 后续需要接入存档

<a id="unreal.CameraControlManager.camera_control_yaw_limit"></a>

#### camera\_control\_yaw\_limit

```python
@property
def camera_control_yaw_limit() -> Vector2D
```

(Vector2D):  [Read-Only]

<a id="unreal.CameraControlManager.world_to_screen_position"></a>

#### world\_to\_screen\_position

```python
def world_to_screen_position(world_position: Vector) -> Optional[Vector2D]
```

x.world_to_screen_position(world_position) -> Vector2D or None
根据世界位置计算对应屏幕位置

Args:
    world_position (Vector): 

Returns:
    Vector2D or None: 

    screen_position (Vector2D):

<a id="unreal.CameraControlManager.update_camera"></a>

#### update\_camera

```python
def update_camera(camera_info: CoreCameraData,
                  duration: float = 1.200000) -> bool
```

x.update_camera(camera_info, duration=1.200000) -> bool
更新相机信息

Args:
    camera_info (CoreCameraData): 
    duration (float): 

Returns:
    bool:

<a id="unreal.CameraControlManager.toggle_camera_rotate_around"></a>

#### toggle\_camera\_rotate\_around

```python
def toggle_camera_rotate_around(active: bool, clock_wise: bool,
                                speed: float) -> bool
```

x.toggle_camera_rotate_around(active, clock_wise, speed) -> bool
切换绕点旋转

Args:
    active (bool): 
    clock_wise (bool): 
    speed (float): 

Returns:
    bool:

<a id="unreal.CameraControlManager.toggle_camera_auto_rotate"></a>

#### toggle\_camera\_auto\_rotate

```python
def toggle_camera_auto_rotate(active: bool,
                              rotate_axis: Vector,
                              speed: float,
                              angle: float = 0.000000) -> bool
```

x.toggle_camera_auto_rotate(active, rotate_axis, speed, angle=0.000000) -> bool
切换自身自动旋转，Speed单位：度/s

Args:
    active (bool): 
    rotate_axis (Vector): 
    speed (float): 
    angle (float): 

Returns:
    bool:

<a id="unreal.CameraControlManager.toggle_camera_auto_movement"></a>

#### toggle\_camera\_auto\_movement

```python
def toggle_camera_auto_movement(active: bool, direction: Vector,
                                speed: float) -> bool
```

x.toggle_camera_auto_movement(active, direction, speed) -> bool
切换自动移动，Speed单位：m/s

Args:
    active (bool): 
    direction (Vector): 
    speed (float): 

Returns:
    bool:

<a id="unreal.CameraControlManager.stop_all_camera_movement"></a>

#### stop\_all\_camera\_movement

```python
def stop_all_camera_movement() -> bool
```

x.stop_all_camera_movement() -> bool
停止所有相机动画，包括移动、运动、旋转、自动移动

Returns:
    bool:

<a id="unreal.CameraControlManager.start_camera_auto_movement_distance"></a>

#### start\_camera\_auto\_movement\_distance

```python
def start_camera_auto_movement_distance(direction: Vector, distance: float,
                                        duration: float) -> bool
```

x.start_camera_auto_movement_distance(direction, distance, duration) -> bool
指定方向和距离以及时间来自动移动相机, distance(cm), duration(s)

Args:
    direction (Vector): 
    distance (double): 
    duration (float): 

Returns:
    bool:

<a id="unreal.CameraControlManager.set_control_mode"></a>

#### set\_control\_mode

```python
def set_control_mode(control_mode: str,
                     possess_duration: float = 2.000000) -> bool
```

x.set_control_mode(control_mode, possess_duration=2.000000) -> bool
Set Control Mode

Args:
    control_mode (str): 
    possess_duration (float): 

Returns:
    bool:

<a id="unreal.CameraControlManager.set_camera_speed"></a>

#### set\_camera\_speed

```python
def set_camera_speed(speed_data: WDPCameraSpeedData) -> bool
```

x.set_camera_speed(speed_data) -> bool
设置相机速度

Args:
    speed_data (WDPCameraSpeedData): 

Returns:
    bool:

<a id="unreal.CameraControlManager.set_camera_preset_data"></a>

#### set\_camera\_preset\_data

```python
def set_camera_preset_data(camera_location: Vector,
                           rotation: Rotator = [
                               0.000000, -30.000000, 0.000000
                           ],
                           pitch_limit: Vector2D = [-89.000000, 0.000000],
                           yaw_limit: Vector2D = [-179.999000, 179.999000],
                           distance_limit: Vector2D = [
                               0.000000, 10000000.000000
                           ],
                           fov: float = 90.000000,
                           control_mode: Name = "RTS",
                           duration: float = 0.500000) -> bool
```

x.set_camera_preset_data(camera_location, rotation=[0.000000, -30.000000, 0.000000], pitch_limit=[-89.000000, 0.000000], yaw_limit=[-179.999000, 179.999000], distance_limit=[0.000000, 10000000.000000], fov=90.000000, control_mode="RTS", duration=0.500000) -> bool
设置相机数据

Args:
    camera_location (Vector): 
    rotation (Rotator): 
    pitch_limit (Vector2D): 
    yaw_limit (Vector2D): 
    distance_limit (Vector2D): 
    fov (float): 
    control_mode (Name): 
    duration (float): 

Returns:
    bool:

<a id="unreal.CameraControlManager.set_camera_limit"></a>

#### set\_camera\_limit

```python
def set_camera_limit(limit_data: WDPCameraLimitData) -> bool
```

x.set_camera_limit(limit_data) -> bool
Set Camera Limit

Args:
    limit_data (WDPCameraLimitData): 

Returns:
    bool:

<a id="unreal.CameraControlManager.set_camera_control_enabled"></a>

#### set\_camera\_control\_enabled

```python
def set_camera_control_enabled(enabled: bool) -> None
```

x.set_camera_control_enabled(enabled) -> None
通过Feature切换相机操作功能开启关闭

Args:
    enabled (bool):

<a id="unreal.CameraControlManager.set_camera_animation"></a>

#### set\_camera\_animation

```python
def set_camera_animation(animation_data: WDPCameraAnimationData) -> bool
```

x.set_camera_animation(animation_data) -> bool
Set Camera Animation

Args:
    animation_data (WDPCameraAnimationData): 

Returns:
    bool:

<a id="unreal.CameraControlManager.screen_to_world_position"></a>

#### screen\_to\_world\_position

```python
def screen_to_world_position(
        screen_position: Vector2D) -> Optional[Tuple[Vector, Vector]]
```

x.screen_to_world_position(screen_position) -> (out_position=Vector, out_direction=Vector) or None
根据屏幕位置反算世界位置

Args:
    screen_position (Vector2D): 

Returns:
    tuple or None: 

    out_position (Vector): 

    out_direction (Vector):

<a id="unreal.CameraControlManager.remote_update_camera_zoom"></a>

#### remote\_update\_camera\_zoom

```python
def remote_update_camera_zoom(step: float) -> bool
```

x.remote_update_camera_zoom(step) -> bool
遥控缩放，大于0：ZoomOut，小于0：ZoomIn

Args:
    step (float): 

Returns:
    bool:

<a id="unreal.CameraControlManager.remote_update_camera_rotate"></a>

#### remote\_update\_camera\_rotate

```python
def remote_update_camera_rotate(rotate_direction: WdpCameraRotateDir,
                                step: float) -> bool
```

x.remote_update_camera_rotate(rotate_direction, step) -> bool
Remote Update Camera Rotate

Args:
    rotate_direction (WdpCameraRotateDir): 
    step (float): 

Returns:
    bool:

<a id="unreal.CameraControlManager.remote_toggle_camera_zoom"></a>

#### remote\_toggle\_camera\_zoom

```python
def remote_toggle_camera_zoom(start: bool = True) -> bool
```

x.remote_toggle_camera_zoom(start=True) -> bool
Remote Toggle Camera Zoom

Args:
    start (bool): 

Returns:
    bool:

<a id="unreal.CameraControlManager.remote_toggle_camera_self_rotate"></a>

#### remote\_toggle\_camera\_self\_rotate

```python
def remote_toggle_camera_self_rotate(pressed: bool = False) -> bool
```

x.remote_toggle_camera_self_rotate(pressed=False) -> bool
遥控相机的自身旋转开关

Args:
    pressed (bool): 

Returns:
    bool:

<a id="unreal.CameraControlManager.remote_toggle_camera_rotate"></a>

#### remote\_toggle\_camera\_rotate

```python
def remote_toggle_camera_rotate(start: bool = False) -> bool
```

x.remote_toggle_camera_rotate(start=False) -> bool
Remote Toggle Camera Rotate

Args:
    start (bool): 

Returns:
    bool:

<a id="unreal.CameraControlManager.remote_camera_move"></a>

#### remote\_camera\_move

```python
def remote_camera_move(move_direction: WDPDirection, step: float) -> bool
```

x.remote_camera_move(move_direction, step) -> bool
遥控输入

Args:
    move_direction (WDPDirection): 
    step (float): 

Returns:
    bool:

<a id="unreal.CameraControlManager.notify_camera_motion_start"></a>

#### notify\_camera\_motion\_start

```python
def notify_camera_motion_start(e_reason: CameraMotionReason,
                               eids: Array[str]) -> None
```

x.notify_camera_motion_start(e_reason, eids) -> None
Notify Camera Motion Start

Args:
    e_reason (CameraMotionReason): 
    eids (Array[str]):

<a id="unreal.CameraControlManager.notify_camera_motion_end"></a>

#### notify\_camera\_motion\_end

```python
def notify_camera_motion_end() -> None
```

x.notify_camera_motion_end() -> None
Notify Camera Motion End

<a id="unreal.CameraControlManager.get_control_mode"></a>

#### get\_control\_mode

```python
def get_control_mode() -> str
```

x.get_control_mode() -> str
Get Control Mode

Returns:
    str:

<a id="unreal.CameraControlManager.get_camera_speed"></a>

#### get\_camera\_speed

```python
def get_camera_speed() -> Optional[WDPCameraSpeedData]
```

x.get_camera_speed() -> WDPCameraSpeedData or None
获得相机速度

Returns:
    WDPCameraSpeedData or None: 

    speed_data (WDPCameraSpeedData):

<a id="unreal.CameraControlManager.get_camera_limit"></a>

#### get\_camera\_limit

```python
def get_camera_limit() -> Optional[WDPCameraLimitData]
```

x.get_camera_limit() -> WDPCameraLimitData or None
Get Camera Limit

Returns:
    WDPCameraLimitData or None: 

    limit_data (WDPCameraLimitData):

<a id="unreal.CameraControlManager.get_camera_info"></a>

#### get\_camera\_info

```python
def get_camera_info() -> Optional[WDPCameraInfo]
```

x.get_camera_info() -> WDPCameraInfo or None
获取相机信息

Returns:
    WDPCameraInfo or None: 

    camera_info (WDPCameraInfo):

<a id="unreal.CameraControlManager.get_camera_animation"></a>

#### get\_camera\_animation

```python
def get_camera_animation() -> Optional[WDPCameraAnimationData]
```

x.get_camera_animation() -> WDPCameraAnimationData or None
获得相机动画

Returns:
    WDPCameraAnimationData or None: 

    animation_data (WDPCameraAnimationData):

<a id="unreal.CameraControlManager.focus_to_position"></a>

#### focus\_to\_position

```python
def focus_to_position(target_location: Vector,
                      target_rotation: Rotator,
                      distance: float = 5000.000000,
                      duration: float = 0.500000) -> bool
```

x.focus_to_position(target_location, target_rotation, distance=5000.000000, duration=0.500000) -> bool
聚焦到某个位置，带旋转

Args:
    target_location (Vector): 
    target_rotation (Rotator): 
    distance (float): 
    duration (float): 

Returns:
    bool:

<a id="unreal.CameraControlManager.focus_to_point"></a>

#### focus\_to\_point

```python
def focus_to_point(target_location: Vector,
                   distance: float = 5000.000000,
                   default_duration: float = 0.500000) -> bool
```

x.focus_to_point(target_location, distance=5000.000000, default_duration=0.500000) -> bool
DefaultDuration暂时先默认0.5s，对于Focus来说速度快一些比较友好

Args:
    target_location (Vector): 
    distance (float): 
    default_duration (float): 

Returns:
    bool:

<a id="unreal.CameraControlManager.enable_camera_control_features"></a>

#### enable\_camera\_control\_features

```python
def enable_camera_control_features(features: int) -> None
```

x.enable_camera_control_features(features) -> None
开启所选的相机功能

Args:
    features (int32):

<a id="unreal.CameraControlManager.disable_camera_control_features"></a>

#### disable\_camera\_control\_features

```python
def disable_camera_control_features(features: int) -> None
```

x.disable_camera_control_features(features) -> None
禁用所选的相机功能

Args:
    features (int32):

<a id="unreal.FollowActorInterface"></a>