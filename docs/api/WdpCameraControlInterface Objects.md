## WdpCameraControlInterface Objects

```python
class WdpCameraControlInterface(Interface)
```

Wdp Camera Control Interface

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpCameraControlInterface.h

<a id="unreal.WdpCameraControlInterface.bpi_toggle_camera_self_auto_rotation"></a>

#### bpi\_toggle\_camera\_self\_auto\_rotation

```python
def bpi_toggle_camera_self_auto_rotation(
        active: bool, settings: AutoSelfRotationSettings) -> bool
```

x.bpi_toggle_camera_self_auto_rotation(active, settings) -> bool
切换相机自身自动旋转

Args:
    active (bool): 
    settings (AutoSelfRotationSettings): 

Returns:
    bool:

<a id="unreal.WdpCameraControlInterface.bpi_toggle_camera_auto_rotation"></a>

#### bpi\_toggle\_camera\_auto\_rotation

```python
def bpi_toggle_camera_auto_rotation(active: bool,
                                    settings: AutoRotationSettings) -> bool
```

x.bpi_toggle_camera_auto_rotation(active, settings) -> bool
切换自动旋转

Args:
    active (bool): 
    settings (AutoRotationSettings): 

Returns:
    bool:

<a id="unreal.WdpCameraControlInterface.bpi_toggle_camera_auto_movement"></a>

#### bpi\_toggle\_camera\_auto\_movement

```python
def bpi_toggle_camera_auto_movement(active: bool,
                                    settings: AutoMovementSettings) -> bool
```

x.bpi_toggle_camera_auto_movement(active, settings) -> bool
切换自动移动

Args:
    active (bool): 
    settings (AutoMovementSettings): 

Returns:
    bool:

<a id="unreal.WdpCameraControlInterface.bpi_stop_all_camera_animation"></a>

#### bpi\_stop\_all\_camera\_animation

```python
def bpi_stop_all_camera_animation() -> None
```

x.bpi_stop_all_camera_animation() -> None
停止所有相机移动

<a id="unreal.WdpCameraControlInterface.bpi_set_user_camera_settings"></a>

#### bpi\_set\_user\_camera\_settings

```python
def bpi_set_user_camera_settings(
        user_camera_settings: UserCameraSettings) -> bool
```

x.bpi_set_user_camera_settings(user_camera_settings) -> bool
设置用户自定义相机数据

Args:
    user_camera_settings (UserCameraSettings): 

Returns:
    bool:

<a id="unreal.WdpCameraControlInterface.bpi_set_camera_limit_info"></a>

#### bpi\_set\_camera\_limit\_info

```python
def bpi_set_camera_limit_info(rotation_limit: CameraRotationLimitationData,
                              zoom_limit: CameraZoomLimitationData) -> bool
```

x.bpi_set_camera_limit_info(rotation_limit, zoom_limit) -> bool
设置相机的限制数据

Args:
    rotation_limit (CameraRotationLimitationData): 
    zoom_limit (CameraZoomLimitationData): 

Returns:
    bool:

<a id="unreal.WdpCameraControlInterface.bpi_set_camera_collision_info"></a>

#### bpi\_set\_camera\_collision\_info

```python
def bpi_set_camera_collision_info(collision_data: CameraCollisionData) -> bool
```

x.bpi_set_camera_collision_info(collision_data) -> bool
设置相机的碰撞数据

Args:
    collision_data (CameraCollisionData): 

Returns:
    bool:

<a id="unreal.WdpCameraControlInterface.bpi_play_camera_core_data"></a>

#### bpi\_play\_camera\_core\_data

```python
def bpi_play_camera_core_data(core_camera_data: CoreCameraData,
                              settings: TravelAnimationSettings,
                              duration: float = 1.200000) -> None
```

x.bpi_play_camera_core_data(core_camera_data, settings, duration=1.200000) -> None
执行简单的相机运动动画接口

Args:
    core_camera_data (CoreCameraData): 
    settings (TravelAnimationSettings): 
    duration (float):

<a id="unreal.WdpCameraControlInterface.bpi_get_user_camera_settings"></a>

#### bpi\_get\_user\_camera\_settings

```python
def bpi_get_user_camera_settings() -> Optional[UserCameraSettings]
```

x.bpi_get_user_camera_settings() -> UserCameraSettings or None
获取用户设置的相机数据

Returns:
    UserCameraSettings or None: 

    user_camera_settings (UserCameraSettings):

<a id="unreal.WdpCameraControlInterface.bpi_get_current_camera_data"></a>

#### bpi\_get\_current\_camera\_data

```python
def bpi_get_current_camera_data() -> Optional[AllCameraData]
```

x.bpi_get_current_camera_data() -> AllCameraData or None
获取全部的相机数据结构体

Returns:
    AllCameraData or None: 

    all_camera_data (AllCameraData):

<a id="unreal.WdpCameraControlInterface.bpi_change_camera_standard"></a>

#### bpi\_change\_camera\_standard

```python
def bpi_change_camera_standard(camera_data: AllCameraData,
                               settings: TravelAnimationSettings,
                               duration: float = 1.200000) -> None
```

x.bpi_change_camera_standard(camera_data, settings, duration=1.200000) -> None
执行标准相机动画

Args:
    camera_data (AllCameraData): 
    settings (TravelAnimationSettings): 
    duration (float):

<a id="unreal.WdpCameraPresetActor"></a>