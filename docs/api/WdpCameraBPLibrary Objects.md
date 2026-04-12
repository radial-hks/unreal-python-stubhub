## WdpCameraBPLibrary Objects

```python
class WdpCameraBPLibrary(BlueprintFunctionLibrary)
```

Wdp Camera BPLibrary

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpCameraBPLibrary.h

<a id="unreal.WdpCameraBPLibrary.un_possess_and_return"></a>

#### un\_possess\_and\_return

```python
@classmethod
def un_possess_and_return(cls,
                          world_context_object: Object,
                          duration: float = 0.000000,
                          index: int = 0) -> None
```

X.un_possess_and_return(world_context_object, duration=0.000000, index=0) -> None
取消并返回默认Pawn

Args:
    world_context_object (Object): 
    duration (float): 
    index (int32):

<a id="unreal.WdpCameraBPLibrary.toggle_following_actor"></a>

#### toggle\_following\_actor

```python
@classmethod
def toggle_following_actor(cls,
                           world_context_object: Object,
                           target_actor: Actor,
                           follow: bool = False) -> bool
```

X.toggle_following_actor(world_context_object, target_actor, follow=False) -> bool
切换相机Follow

Args:
    world_context_object (Object): 
    target_actor (Actor): 
    follow (bool): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.toggle_camera_self_auto_rotation"></a>

#### toggle\_camera\_self\_auto\_rotation

```python
@classmethod
def toggle_camera_self_auto_rotation(
        cls, world_context_object: Object, active: bool,
        settings: AutoSelfRotationSettings) -> bool
```

X.toggle_camera_self_auto_rotation(world_context_object, active, settings) -> bool
切换相机自身的自动旋转

Args:
    world_context_object (Object): 
    active (bool): 
    settings (AutoSelfRotationSettings): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.toggle_auto_rotation"></a>

#### toggle\_auto\_rotation

```python
@classmethod
def toggle_auto_rotation(cls, world_context_object: Object, active: bool,
                         auto_rotation_settings: AutoRotationSettings) -> bool
```

X.toggle_auto_rotation(world_context_object, active, auto_rotation_settings) -> bool
切换相机自动旋转

Args:
    world_context_object (Object): 
    active (bool): 
    auto_rotation_settings (AutoRotationSettings): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.toggle_auto_movement"></a>

#### toggle\_auto\_movement

```python
@classmethod
def toggle_auto_movement(cls, world_context_object: Object, active: bool,
                         auto_movement_settings: AutoMovementSettings) -> bool
```

X.toggle_auto_movement(world_context_object, active, auto_movement_settings) -> bool
切换相机自动位移

Args:
    world_context_object (Object): 
    active (bool): 
    auto_movement_settings (AutoMovementSettings): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.stop_following_actor"></a>

#### stop\_following\_actor

```python
@classmethod
def stop_following_actor(cls, world_context_object: Object) -> bool
```

X.stop_following_actor(world_context_object) -> bool
结束相机Follow

Args:
    world_context_object (Object): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.stop_all_camera_movement"></a>

#### stop\_all\_camera\_movement

```python
@classmethod
def stop_all_camera_movement(cls, world_context_object: Object) -> bool
```

X.stop_all_camera_movement(world_context_object) -> bool
停止所有相机运动

Args:
    world_context_object (Object): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.start_following_actor"></a>

#### start\_following\_actor

```python
@classmethod
def start_following_actor(
        cls,
        world_context_object: Object,
        target_actor: Actor,
        follow_mode: FollowingMode = FollowingMode.FM_TRACKING_LIGHT,
        duration: float = 1.200000) -> bool
```

X.start_following_actor(world_context_object, target_actor, follow_mode=FollowingMode.FM_TRACKING_LIGHT, duration=1.200000) -> bool
开始相机Follow动画

Args:
    world_context_object (Object): 
    target_actor (Actor): 
    follow_mode (FollowingMode): 
    duration (float): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.set_user_camera_settings"></a>

#### set\_user\_camera\_settings

```python
@classmethod
def set_user_camera_settings(cls, world_context_object: Object,
                             user_camera_settings: UserCameraSettings) -> bool
```

X.set_user_camera_settings(world_context_object, user_camera_settings) -> bool
设置用户相机参数

Args:
    world_context_object (Object): 
    user_camera_settings (UserCameraSettings): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.set_camera_limit_data"></a>

#### set\_camera\_limit\_data

```python
@classmethod
def set_camera_limit_data(cls, world_context_object: Object,
                          rotation_limit: CameraRotationLimitationData,
                          zoom_limit: CameraZoomLimitationData) -> bool
```

X.set_camera_limit_data(world_context_object, rotation_limit, zoom_limit) -> bool
更新相机的限制数据 旋转和缩放

Args:
    world_context_object (Object): 
    rotation_limit (CameraRotationLimitationData): 
    zoom_limit (CameraZoomLimitationData): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.set_camera_collision_data"></a>

#### set\_camera\_collision\_data

```python
@classmethod
def set_camera_collision_data(cls, world_context_object: Object,
                              collision_data: CameraCollisionData) -> bool
```

X.set_camera_collision_data(world_context_object, collision_data) -> bool
更新相机的碰撞数据

Args:
    world_context_object (Object): 
    collision_data (CameraCollisionData): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.remote_input_zoom_key_value_update"></a>

#### remote\_input\_zoom\_key\_value\_update

```python
@classmethod
def remote_input_zoom_key_value_update(cls, world_context_object: Object,
                                       value: float) -> bool
```

X.remote_input_zoom_key_value_update(world_context_object, value) -> bool
遥控缩放输入 更新，大于0 = ZoomOut， 小于0 = ZoomIn

Args:
    world_context_object (Object): 
    value (float): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.remote_input_toggle_zoom_key_pressed_released"></a>

#### remote\_input\_toggle\_zoom\_key\_pressed\_released

```python
@classmethod
def remote_input_toggle_zoom_key_pressed_released(cls,
                                                  world_context_object: Object,
                                                  is_pressed: bool = False
                                                  ) -> bool
```

X.remote_input_toggle_zoom_key_pressed_released(world_context_object, is_pressed=False) -> bool
遥控缩放输入 开始 结束

Args:
    world_context_object (Object): 
    is_pressed (bool): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.remote_input_toggle_rotate_key_pressed_released"></a>

#### remote\_input\_toggle\_rotate\_key\_pressed\_released

```python
@classmethod
def remote_input_toggle_rotate_key_pressed_released(
        cls, world_context_object: Object, is_pressed: bool = False) -> bool
```

X.remote_input_toggle_rotate_key_pressed_released(world_context_object, is_pressed=False) -> bool
遥控旋转输入 开始 结束

Args:
    world_context_object (Object): 
    is_pressed (bool): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.remote_input_rotate_key_value_update"></a>

#### remote\_input\_rotate\_key\_value\_update

```python
@classmethod
def remote_input_rotate_key_value_update(cls, world_context_object: Object,
                                         value: Vector2D) -> bool
```

X.remote_input_rotate_key_value_update(world_context_object, value) -> bool
遥控旋转输入 更新， X = Yaw Y = Pitch

Args:
    world_context_object (Object): 
    value (Vector2D): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.remote_input_movement_value_update"></a>

#### remote\_input\_movement\_value\_update

```python
@classmethod
def remote_input_movement_value_update(cls, world_context_object: Object,
                                       value: Vector) -> bool
```

X.remote_input_movement_value_update(world_context_object, value) -> bool
遥控操作移动输入 X = Forward, Y = Right, Z = Up

Args:
    world_context_object (Object): 
    value (Vector): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.possess_to_new_pawn"></a>

#### possess\_to\_new\_pawn

```python
@classmethod
def possess_to_new_pawn(cls,
                        world_context_object: Object,
                        new_pawn: Pawn,
                        duration: float = 0.000000,
                        index: int = 0) -> None
```

X.possess_to_new_pawn(world_context_object, new_pawn, duration=0.000000, index=0) -> None
切换控制到新的Pawn

Args:
    world_context_object (Object): 
    new_pawn (Pawn): 
    duration (float): 
    index (int32):

<a id="unreal.WdpCameraBPLibrary.get_wdp_player_pawn"></a>

#### get\_wdp\_player\_pawn

```python
@classmethod
def get_wdp_player_pawn(cls,
                        world_context_object: Object,
                        index: int = 0) -> WdpBasePawn
```

X.get_wdp_player_pawn(world_context_object, index=0) -> WdpBasePawn
获取WdpPawn的引用

Args:
    world_context_object (Object): 
    index (int32): 

Returns:
    WdpBasePawn:

<a id="unreal.WdpCameraBPLibrary.get_wdp_player_controller"></a>

#### get\_wdp\_player\_controller

```python
@classmethod
def get_wdp_player_controller(cls,
                              world_context_object: Object,
                              index: int = 0) -> WdpPlayerController
```

X.get_wdp_player_controller(world_context_object, index=0) -> WdpPlayerController
获取WdpPlayerController的引用

Args:
    world_context_object (Object): 
    index (int32): 

Returns:
    WdpPlayerController:

<a id="unreal.WdpCameraBPLibrary.get_user_camera_settings"></a>

#### get\_user\_camera\_settings

```python
@classmethod
def get_user_camera_settings(
        cls, world_context_object: Object) -> Optional[UserCameraSettings]
```

X.get_user_camera_settings(world_context_object) -> UserCameraSettings or None
获取用户设置的相机参数

Args:
    world_context_object (Object): 

Returns:
    UserCameraSettings or None: 

    user_camera_settings (UserCameraSettings):

<a id="unreal.WdpCameraBPLibrary.get_current_camera_data"></a>

#### get\_current\_camera\_data

```python
@classmethod
def get_current_camera_data(
        cls, world_context_object: Object) -> Optional[AllCameraData]
```

X.get_current_camera_data(world_context_object) -> AllCameraData or None
获取全部的相机数据

Args:
    world_context_object (Object): 

Returns:
    AllCameraData or None: 

    all_camera_data (AllCameraData):

<a id="unreal.WdpCameraBPLibrary.get_camera_limit_data"></a>

#### get\_camera\_limit\_data

```python
@classmethod
def get_camera_limit_data(
    cls, world_context_object: Object
) -> Optional[Tuple[CameraRotationLimitationData, CameraZoomLimitationData]]
```

X.get_camera_limit_data(world_context_object) -> (rotation_limit=CameraRotationLimitationData, zoom_limit=CameraZoomLimitationData) or None
获取相机的限制数据，旋转和缩放的限制

Args:
    world_context_object (Object): 

Returns:
    tuple or None: 

    rotation_limit (CameraRotationLimitationData): 

    zoom_limit (CameraZoomLimitationData):

<a id="unreal.WdpCameraBPLibrary.get_camera_core_data"></a>

#### get\_camera\_core\_data

```python
@classmethod
def get_camera_core_data(
        cls, world_context_object: Object) -> Optional[CoreCameraData]
```

X.get_camera_core_data(world_context_object) -> CoreCameraData or None
获取相机的核心数据，位置旋转和缩放，如果不包含Interface则返回CameraManager的数据

Args:
    world_context_object (Object): 

Returns:
    CoreCameraData or None: 

    core_camera_data (CoreCameraData):

<a id="unreal.WdpCameraBPLibrary.get_camera_collision_data"></a>

#### get\_camera\_collision\_data

```python
@classmethod
def get_camera_collision_data(
        cls, world_context_object: Object) -> Optional[CameraCollisionData]
```

X.get_camera_collision_data(world_context_object) -> CameraCollisionData or None
获取相机的碰撞设置数据

Args:
    world_context_object (Object): 

Returns:
    CameraCollisionData or None: 

    collision_data (CameraCollisionData):

<a id="unreal.WdpCameraBPLibrary.find_camera_preset_by_index"></a>

#### find\_camera\_preset\_by\_index

```python
@classmethod
def find_camera_preset_by_index(cls, world_context_object: Object,
                                tag: GameplayTag,
                                index: int) -> Optional[WdpCameraPresetActor]
```

X.find_camera_preset_by_index(world_context_object, tag, index) -> WdpCameraPresetActor or None
通过Tag和Index查找对应的WdpCameraPreset

Args:
    world_context_object (Object): 
    tag (GameplayTag): 
    index (int32): 

Returns:
    WdpCameraPresetActor or None: 

    camera_preset (WdpCameraPresetActor):

<a id="unreal.WdpCameraBPLibrary.convert_core_camera_data_to_world_space"></a>

#### convert\_core\_camera\_data\_to\_world\_space

```python
@classmethod
def convert_core_camera_data_to_world_space(
        cls, world_context_object: Object,
        core_camera_data_surface_space: CoreCameraData) -> CoreCameraData
```

X.convert_core_camera_data_to_world_space(world_context_object, core_camera_data_surface_space) -> CoreCameraData
将CoreCameraData从球面空间转换为世界空间 需要放置WorldOriginAnchor

Args:
    world_context_object (Object): 
    core_camera_data_surface_space (CoreCameraData): 

Returns:
    CoreCameraData:

<a id="unreal.WdpCameraBPLibrary.convert_core_camera_data_to_surface_space"></a>

#### convert\_core\_camera\_data\_to\_surface\_space

```python
@classmethod
def convert_core_camera_data_to_surface_space(
        cls, world_context_object: Object,
        core_camera_data_world_space: CoreCameraData) -> CoreCameraData
```

X.convert_core_camera_data_to_surface_space(world_context_object, core_camera_data_world_space) -> CoreCameraData
将CoreCameraData转换为球面空间 需要放置WorldOriginAnchor

Args:
    world_context_object (Object): 
    core_camera_data_world_space (CoreCameraData): 

Returns:
    CoreCameraData:

<a id="unreal.WdpCameraBPLibrary.change_camera_standard"></a>

#### change\_camera\_standard

```python
@classmethod
def change_camera_standard(cls,
                           world_context_object: Object,
                           target_camera_data: AllCameraData,
                           settings: TravelAnimationSettings,
                           duration: float = 1.200000) -> bool
```

X.change_camera_standard(world_context_object, target_camera_data, settings, duration=1.200000) -> bool
标准相机切换命令，执行全部相机变更操作

Args:
    world_context_object (Object): 
    target_camera_data (AllCameraData): 
    settings (TravelAnimationSettings): 
    duration (float): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.change_camera_preset_data_api"></a>

#### change\_camera\_preset\_data\_api

```python
@classmethod
def change_camera_preset_data_api(cls,
                                  world_context_object: Object,
                                  camera_location: Vector,
                                  camera_rotation: Rotator,
                                  pitch_limit: Vector2D = [
                                      -89.000000, 0.000000
                                  ],
                                  yaw_limit: Vector2D = [
                                      -179.999000, 179.999000
                                  ],
                                  distance_limit: Vector2D = [
                                      0.000000, 10000000.000000
                                  ],
                                  fov: float = 90.000000,
                                  control_mode: Name = "RTS",
                                  duration: float = 1.200000) -> bool
```

X.change_camera_preset_data_api(world_context_object, camera_location, camera_rotation, pitch_limit=[-89.000000, 0.000000], yaw_limit=[-179.999000, 179.999000], distance_limit=[0.000000, 10000000.000000], fov=90.000000, control_mode="RTS", duration=1.200000) -> bool
设置一个相机预设，只给API用，这个设置其实会造成问题不过先实现了再说

Args:
    world_context_object (Object): 
    camera_location (Vector): 
    camera_rotation (Rotator): 
    pitch_limit (Vector2D): 
    yaw_limit (Vector2D): 
    distance_limit (Vector2D): 
    fov (float): 
    control_mode (Name): 
    duration (float): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.change_camera_look_at"></a>

#### change\_camera\_look\_at

```python
@classmethod
def change_camera_look_at(cls,
                          world_context_object: Object,
                          target: Vector,
                          settings: TravelAnimationSettings,
                          change_distance: bool = False,
                          distance: float = 1000.000000,
                          override_pitch: bool = False,
                          pitch: float = -45.000000,
                          duration: float = 1.200000) -> bool
```

X.change_camera_look_at(world_context_object, target, settings, change_distance=False, distance=1000.000000, override_pitch=False, pitch=-45.000000, duration=1.200000) -> bool
相机看向一个点

Args:
    world_context_object (Object): 
    target (Vector): 
    settings (TravelAnimationSettings): 
    change_distance (bool): 
    distance (double): 
    override_pitch (bool): 
    pitch (float): 
    duration (float): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.change_camera_index"></a>

#### change\_camera\_index

```python
@classmethod
def change_camera_index(cls,
                        world_context_object: Object,
                        tag: GameplayTag,
                        index: int,
                        settings: TravelAnimationSettings,
                        duration: float = 1.200000) -> bool
```

X.change_camera_index(world_context_object, tag, index, settings, duration=1.200000) -> bool
通用的相机预设命令，通过WdpCameraPreset配置相机参数，如果没找到相机会返回false

Args:
    world_context_object (Object): 
    tag (GameplayTag): 
    index (int32): 
    settings (TravelAnimationSettings): 
    duration (float): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.change_camera_focus_to_point_with_rotation"></a>

#### change\_camera\_focus\_to\_point\_with\_rotation

```python
@classmethod
def change_camera_focus_to_point_with_rotation(
        cls,
        world_context_object: Object,
        target_location: Vector,
        target_rotation: Rotator,
        settings: TravelAnimationSettings,
        distance: float = 5000.000000,
        duration: float = 0.500000) -> bool
```

X.change_camera_focus_to_point_with_rotation(world_context_object, target_location, target_rotation, settings, distance=5000.000000, duration=0.500000) -> bool
相机聚焦到一个点，目标点和距离，并使用自定义旋转

Args:
    world_context_object (Object): 
    target_location (Vector): 
    target_rotation (Rotator): 
    settings (TravelAnimationSettings): 
    distance (double): 
    duration (float): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.change_camera_focus_to_points"></a>

#### change\_camera\_focus\_to\_points

```python
@classmethod
def change_camera_focus_to_points(cls,
                                  world_context_object: Object,
                                  target_locations: Array[Vector],
                                  settings: TravelAnimationSettings,
                                  scale: float = 1.000000,
                                  min_distance: float = 5000.000000,
                                  duration: float = 0.500000) -> bool
```

X.change_camera_focus_to_points(world_context_object, target_locations, settings, scale=1.000000, min_distance=5000.000000, duration=0.500000) -> bool
相机聚焦到多个点，根据点自动计算Bounds，保持当前旋转

Args:
    world_context_object (Object): 
    target_locations (Array[Vector]): 
    settings (TravelAnimationSettings): 
    scale (float): 
    min_distance (double): 
    duration (float): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.change_camera_focus_to_point"></a>

#### change\_camera\_focus\_to\_point

```python
@classmethod
def change_camera_focus_to_point(cls,
                                 world_context_object: Object,
                                 target_location: Vector,
                                 settings: TravelAnimationSettings,
                                 distance: float = 5000.000000,
                                 duration: float = 0.500000) -> bool
```

X.change_camera_focus_to_point(world_context_object, target_location, settings, distance=5000.000000, duration=0.500000) -> bool
相机聚焦到一个点，目标点和距离，保持当前旋转

Args:
    world_context_object (Object): 
    target_location (Vector): 
    settings (TravelAnimationSettings): 
    distance (double): 
    duration (float): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.change_camera_core_data"></a>

#### change\_camera\_core\_data

```python
@classmethod
def change_camera_core_data(cls,
                            world_context_object: Object,
                            target_core_camera_data: CoreCameraData,
                            settings: TravelAnimationSettings,
                            duration: float = 1.200000) -> bool
```

X.change_camera_core_data(world_context_object, target_core_camera_data, settings, duration=1.200000) -> bool
简单的相机FlyTo命令，位置、旋转和时长

Args:
    world_context_object (Object): 
    target_core_camera_data (CoreCameraData): 
    settings (TravelAnimationSettings): 
    duration (float): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.change_camera_auto_rotate_around_pivot"></a>

#### change\_camera\_auto\_rotate\_around\_pivot

```python
@classmethod
def change_camera_auto_rotate_around_pivot(cls,
                                           world_context_object: Object,
                                           target: Vector,
                                           settings: AutoRotationSettings,
                                           change_distance: bool = False,
                                           distance: float = 1000.000000,
                                           override_pitch: bool = False,
                                           pitch: float = -45.000000,
                                           duration: float = 1.200000) -> bool
```

X.change_camera_auto_rotate_around_pivot(world_context_object, target, settings, change_distance=False, distance=1000.000000, override_pitch=False, pitch=-45.000000, duration=1.200000) -> bool
绕一个固定点旋转，并且相机会朝向这个点

Args:
    world_context_object (Object): 
    target (Vector): 
    settings (AutoRotationSettings): 
    change_distance (bool): 
    distance (double): 
    override_pitch (bool): 
    pitch (float): 
    duration (float): 

Returns:
    bool:

<a id="unreal.WdpCameraBPLibrary.calc_look_at_info_to_camera_data"></a>

#### calc\_look\_at\_info\_to\_camera\_data

```python
@classmethod
def calc_look_at_info_to_camera_data(
        cls, target: Vector, current_location: Vector, use_distance: bool,
        distance: float, rotate_limit: CameraRotationLimitationData,
        override_pitch: bool, pitch: float) -> Tuple[Vector, Rotator]
```

X.calc_look_at_info_to_camera_data(target, current_location, use_distance, distance, rotate_limit, override_pitch, pitch) -> (out_camera_location=Vector, out_camera_rotation=Rotator)
LookAt参数转换为相机参数

Args:
    target (Vector): 
    current_location (Vector): 
    use_distance (bool): 
    distance (double): 
    rotate_limit (CameraRotationLimitationData): 
    override_pitch (bool): 
    pitch (float): 

Returns:
    tuple: 

    out_camera_location (Vector): 

    out_camera_rotation (Rotator):

<a id="unreal.WdpCameraBPLibrary.calc_lon_lat_alt_to_world_location_rotation"></a>

#### calc\_lon\_lat\_alt\_to\_world\_location\_rotation

```python
@classmethod
def calc_lon_lat_alt_to_world_location_rotation(
        cls, world_context_object: Object, lon: float, lat: float, alt: float,
        local_rotation: Rotator) -> Optional[Tuple[Vector, Rotator]]
```

X.calc_lon_lat_alt_to_world_location_rotation(world_context_object, lon, lat, alt, local_rotation) -> (out_location=Vector, out_rotation=Rotator) or None
将经纬度和高度换算成引擎坐标的位置和旋转 高度单位为米 需要放置WorldOriginAnchor

Args:
    world_context_object (Object): 
    lon (double): 
    lat (double): 
    alt (double): 
    local_rotation (Rotator): 

Returns:
    tuple or None: 

    out_location (Vector): 

    out_rotation (Rotator):

<a id="unreal.WdpCameraBPLibrary.calc_lon_lat_alt_to_core_camera_data"></a>

#### calc\_lon\_lat\_alt\_to\_core\_camera\_data

```python
@classmethod
def calc_lon_lat_alt_to_core_camera_data(
    cls,
    world_context_object: Object,
    lon: float,
    lat: float,
    alt: float,
    keep_rotation: bool,
    surface_rotation: Rotator = [0.000000, -45.000000, 0.000000]
) -> Optional[CoreCameraData]
```

X.calc_lon_lat_alt_to_core_camera_data(world_context_object, lon, lat, alt, keep_rotation, surface_rotation=[0.000000, -45.000000, 0.000000]) -> CoreCameraData or None
根据经纬度高度和球面空间旋转 计算相机目标数据 高度单位为米 需要放置WorldOriginAnchor

Args:
    world_context_object (Object): 
    lon (double): 
    lat (double): 
    alt (double): 
    keep_rotation (bool): 
    surface_rotation (Rotator): 

Returns:
    CoreCameraData or None: 

    out_camer_data (CoreCameraData):

<a id="unreal.WdpCameraBPLibrary.calc_focus_to_lon_lat_alt_to_camera_data"></a>

#### calc\_focus\_to\_lon\_lat\_alt\_to\_camera\_data

```python
@classmethod
def calc_focus_to_lon_lat_alt_to_camera_data(
    cls,
    world_context_object: Object,
    lon: float,
    lat: float,
    alt: float,
    keep_rotation: bool,
    distance: float = 1000.000000,
    surface_rotation: Rotator = [0.000000, -45.000000, 0.000000]
) -> Optional[CoreCameraData]
```

X.calc_focus_to_lon_lat_alt_to_camera_data(world_context_object, lon, lat, alt, keep_rotation, distance=1000.000000, surface_rotation=[0.000000, -45.000000, 0.000000]) -> CoreCameraData or None
根据目标点的经纬高 距离 和目标的空间旋转 计算目标相机数据 高度单位为米 需要放置WorldOriginAnchor

Args:
    world_context_object (Object): 
    lon (double): 
    lat (double): 
    alt (double): 
    keep_rotation (bool): 
    distance (double): 
    surface_rotation (Rotator): 

Returns:
    CoreCameraData or None: 

    out_camer_data (CoreCameraData):

<a id="unreal.WdpCameraBPLibrary.calc_focus_info_to_camera_data"></a>

#### calc\_focus\_info\_to\_camera\_data

```python
@classmethod
def calc_focus_info_to_camera_data(cls, target: Vector, distance: float,
                                   rotation: Rotator) -> Vector
```

X.calc_focus_info_to_camera_data(target, distance, rotation) -> Vector
相机Focus参数转换为相机参数

Args:
    target (Vector): 
    distance (double): 
    rotation (Rotator): 

Returns:
    Vector: 

    out_camera_location (Vector):

<a id="unreal.WdpCameraControlInterface"></a>