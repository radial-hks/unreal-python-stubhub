## WdpCameraControlAPI Objects

```python
class WdpCameraControlAPI(StandardApiClassBase)
```

Wdp Camera Control API

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPI.h

<a id="unreal.WdpCameraControlAPI.update_camera"></a>

#### update\_camera

```python
def update_camera(params: WDPUpdateCameraInfoParams) -> Optional[ResultBase]
```

x.update_camera(params) -> ResultBase or None
Update Camera

Args:
    params (WDPUpdateCameraInfoParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.toggle_camera_self_rotate"></a>

#### toggle\_camera\_self\_rotate

```python
def toggle_camera_self_rotate(
        params: ToggleCameraSelfRotateParams) -> Optional[ResultBase]
```

x.toggle_camera_self_rotate(params) -> ResultBase or None
Toggle Camera Self Rotate

Args:
    params (ToggleCameraSelfRotateParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.stop_camera_step_update"></a>

#### stop\_camera\_step\_update

```python
def stop_camera_step_update(params: ParamsBase) -> Optional[ResultBase]
```

x.stop_camera_step_update(params) -> ResultBase or None
Stop Camera Step Update

Args:
    params (ParamsBase): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.set_camera_speed"></a>

#### set\_camera\_speed

```python
def set_camera_speed(params: WDPSetCameraSpeedParams) -> Optional[ResultBase]
```

x.set_camera_speed(params) -> ResultBase or None
Set Camera Speed

Args:
    params (WDPSetCameraSpeedParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.set_camera_pose"></a>

#### set\_camera\_pose

```python
def set_camera_pose(params: WDPSetCameraPoseParams) -> Optional[ResultBase]
```

x.set_camera_pose(params) -> ResultBase or None
Set Camera Pose

Args:
    params (WDPSetCameraPoseParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.set_camera_mode"></a>

#### set\_camera\_mode

```python
def set_camera_mode(params: WDPSetCameraModeParams) -> Optional[ResultBase]
```

x.set_camera_mode(params) -> ResultBase or None
获取当前镜头信息

Args:
    params (WDPSetCameraModeParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.set_camera_lock_limit"></a>

#### set\_camera\_lock\_limit

```python
def set_camera_lock_limit(
        params: WDPSetCameraLockLimitParams) -> Optional[ResultBase]
```

x.set_camera_lock_limit(params) -> ResultBase or None
Set Camera Lock Limit

Args:
    params (WDPSetCameraLockLimitParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.set_camera_limit"></a>

#### set\_camera\_limit

```python
def set_camera_limit(params: WDPSetCameraLimitParams) -> Optional[ResultBase]
```

x.set_camera_limit(params) -> ResultBase or None
Set Camera Limit

Args:
    params (WDPSetCameraLimitParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.set_camera_animation"></a>

#### set\_camera\_animation

```python
def set_camera_animation(
        params: WDPSetCameraAnimationParams) -> Optional[ResultBase]
```

x.set_camera_animation(params) -> ResultBase or None
Set Camera Animation

Args:
    params (WDPSetCameraAnimationParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.reset_camera_pose"></a>

#### reset\_camera\_pose

```python
def reset_camera_pose(
        params: WDPResetCameraPoseParams) -> Optional[ResultBase]
```

x.reset_camera_pose(params) -> ResultBase or None
Reset Camera Pose

Args:
    params (WDPResetCameraPoseParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.reset_camera_limit"></a>

#### reset\_camera\_limit

```python
def reset_camera_limit(
        params: WDPResetCameraLimitParams) -> Optional[ResultBase]
```

x.reset_camera_limit(params) -> ResultBase or None
Reset Camera Limit

Args:
    params (WDPResetCameraLimitParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.play_camera_roam"></a>

#### play\_camera\_roam

```python
def play_camera_roam(params: WDPCameraRoamParams) -> Optional[ResultBase]
```

x.play_camera_roam(params) -> ResultBase or None
**********************************************停止相机运动*********************************************************// 镜头范围

Args:
    params (WDPCameraRoamParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.get_camera_speed"></a>

#### get\_camera\_speed

```python
def get_camera_speed(params: ParamsBase) -> Optional[WDPGetCameraSpeedResult]
```

x.get_camera_speed(params) -> WDPGetCameraSpeedResult or None
Get Camera Speed

Args:
    params (ParamsBase): 

Returns:
    WDPGetCameraSpeedResult or None: 

    out_result (WDPGetCameraSpeedResult):

<a id="unreal.WdpCameraControlAPI.get_camera_roaming_info"></a>

#### get\_camera\_roaming\_info

```python
def get_camera_roaming_info(
    params: GetCameraRoamingInfoParams
) -> Optional[GetCameraRoamingInfoResult]
```

x.get_camera_roaming_info(params) -> GetCameraRoamingInfoResult or None
Get Camera Roaming Info

Args:
    params (GetCameraRoamingInfoParams): 

Returns:
    GetCameraRoamingInfoResult or None: 

    out_result (GetCameraRoamingInfoResult):

<a id="unreal.WdpCameraControlAPI.get_camera_pose"></a>

#### get\_camera\_pose

```python
def get_camera_pose(params: ParamsBase) -> Optional[WDPGetCameraPoseResult]
```

x.get_camera_pose(params) -> WDPGetCameraPoseResult or None
Get Camera Pose

Args:
    params (ParamsBase): 

Returns:
    WDPGetCameraPoseResult or None: 

    out_result (WDPGetCameraPoseResult):

<a id="unreal.WdpCameraControlAPI.get_camera_limit"></a>

#### get\_camera\_limit

```python
def get_camera_limit(params: ParamsBase) -> Optional[WDPGetCameraLimitResult]
```

x.get_camera_limit(params) -> WDPGetCameraLimitResult or None
Get Camera Limit

Args:
    params (ParamsBase): 

Returns:
    WDPGetCameraLimitResult or None: 

    out_result (WDPGetCameraLimitResult):

<a id="unreal.WdpCameraControlAPI.get_camera_info"></a>

#### get\_camera\_info

```python
def get_camera_info(params: ParamsBase) -> Optional[WDPGetCameraInfoResult]
```

x.get_camera_info(params) -> WDPGetCameraInfoResult or None
Get Camera Info

Args:
    params (ParamsBase): 

Returns:
    WDPGetCameraInfoResult or None: 

    out_result (WDPGetCameraInfoResult):

<a id="unreal.WdpCameraControlAPI.get_camera_animation"></a>

#### get\_camera\_animation

```python
def get_camera_animation(
        params: ParamsBase) -> Optional[WDPGetCameraAnimationResult]
```

x.get_camera_animation(params) -> WDPGetCameraAnimationResult or None
Get Camera Animation

Args:
    params (ParamsBase): 

Returns:
    WDPGetCameraAnimationResult or None: 

    out_result (WDPGetCameraAnimationResult):

<a id="unreal.WdpCameraControlAPI.follow_entity"></a>

#### follow\_entity

```python
def follow_entity(params: WDPFollowEntityParams) -> Optional[ResultBase]
```

x.follow_entity(params) -> ResultBase or None
**********************************************镜头自定义动画行为****************************************************************// 跟踪实体

Args:
    params (WDPFollowEntityParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.focus_to_position"></a>

#### focus\_to\_position

```python
def focus_to_position(params: WDPFocusPositionParams) -> Optional[ResultBase]
```

x.focus_to_position(params) -> ResultBase or None
***************************************Focus********************************************************

Args:
    params (WDPFocusPositionParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.focus_to_nodes"></a>

#### focus\_to\_nodes

```python
def focus_to_nodes(params: WDPFocusNodesParams) -> Optional[ResultBase]
```

x.focus_to_nodes(params) -> ResultBase or None
Focus to Nodes

Args:
    params (WDPFocusNodesParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.focus_to_entities"></a>

#### focus\_to\_entities

```python
def focus_to_entities(params: WDPFocusEntitiesParams) -> Optional[ResultBase]
```

x.focus_to_entities(params) -> ResultBase or None
Focus to Entities

Args:
    params (WDPFocusEntitiesParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.focus_to_box"></a>

#### focus\_to\_box

```python
def focus_to_box(params: WDPFocusBoxParams) -> Optional[ResultBase]
```

x.focus_to_box(params) -> ResultBase or None
Focus to Box

Args:
    params (WDPFocusBoxParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.focus_to_all_entities"></a>

#### focus\_to\_all\_entities

```python
def focus_to_all_entities(
        params: WdpFocusToAllEntitiesParams) -> Optional[ResultBase]
```

x.focus_to_all_entities(params) -> ResultBase or None
Focus to All Entities

Args:
    params (WdpFocusToAllEntitiesParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.camera_stop"></a>

#### camera\_stop

```python
def camera_stop(params: ParamsBase) -> Optional[ResultBase]
```

x.camera_stop(params) -> ResultBase or None
**********************************************停止相机运动*********************************************************// 镜头范围

Args:
    params (ParamsBase): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.camera_step_zoom"></a>

#### camera\_step\_zoom

```python
def camera_step_zoom(params: CameraStepZoomParams) -> Optional[ResultBase]
```

x.camera_step_zoom(params) -> ResultBase or None
Camera Step Zoom

Args:
    params (CameraStepZoomParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.camera_step_rotate"></a>

#### camera\_step\_rotate

```python
def camera_step_rotate(params: CameraStepRotateParams) -> Optional[ResultBase]
```

x.camera_step_rotate(params) -> ResultBase or None
Camera Step Rotate

Args:
    params (CameraStepRotateParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.camera_step_move"></a>

#### camera\_step\_move

```python
def camera_step_move(params: CameraStepMoveParams) -> Optional[ResultBase]
```

x.camera_step_move(params) -> ResultBase or None
*****************************************镜头单步移动旋转缩放******************************************************

Args:
    params (CameraStepMoveParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.camera_rotate"></a>

#### camera\_rotate

```python
def camera_rotate(
        params: WDPCameraRotateTransformParams) -> Optional[ResultBase]
```

x.camera_rotate(params) -> ResultBase or None
镜头基础旋转行为

Args:
    params (WDPCameraRotateTransformParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.camera_move"></a>

#### camera\_move

```python
def camera_move(params: WDPCameraMoveTransformParams) -> Optional[ResultBase]
```

x.camera_move(params) -> ResultBase or None
*****************************************镜头基础移动和旋转******************************************************// 镜头基础移动行为

Args:
    params (WDPCameraMoveTransformParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.camera_around"></a>

#### camera\_around

```python
def camera_around(params: WDPCameraAroundParams) -> Optional[ResultBase]
```

x.camera_around(params) -> ResultBase or None
镜头绕场景中心旋转行为

Args:
    params (WDPCameraAroundParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCameraControlAPI.apply_camera_preset"></a>

#### apply\_camera\_preset

```python
def apply_camera_preset(
        params: CameraPresetApplyParams) -> Optional[ResultBase]
```

x.apply_camera_preset(params) -> ResultBase or None
Apply Camera Preset

Args:
    params (CameraPresetApplyParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpCoordAideAPI"></a>