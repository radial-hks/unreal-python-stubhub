## UserCameraSettings Objects

```python
class UserCameraSettings(StructBase)
```

用户可配置的相机操作参数

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpDataSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``boost_scale`` (float):  [Read-Write] 按住Shift冲刺时的倍率
- ``decrease_scale`` (float):  [Read-Write] 按住Ctrl减速时的倍率
- ``enable_dynamic_speed`` (bool):  [Read-Write] 是否启用动态按键速度，相机的速度和高度相关
- ``invert_x`` (bool):  [Read-Write] 反转X轴
- ``invert_y`` (bool):  [Read-Write] 反转Y轴
- ``key_movement_base_speed`` (float):  [Read-Write] 基础的按键移动的速度(m/s)
- ``rotation_pitch_speed_scale`` (float):  [Read-Write] 相机的垂直Pitch方向里旋转速度倍率
- ``rotation_yaw_speed_scale`` (float):  [Read-Write] 相机的水平Yaw方向里旋转速度倍率
- ``show_rotate_icon`` (bool):  [Read-Write] 是否显示旋转时的图标
- ``show_touch_effect`` (bool):  [Read-Write] 是否显示点击时的屏幕特效
- ``zoom_speed_scale`` (float):  [Read-Write] 缩放速度倍率

<a id="unreal.UserCameraSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(rotation_yaw_speed_scale: float = 0.000000,
             rotation_pitch_speed_scale: float = 0.000000,
             zoom_speed_scale: float = 0.000000,
             enable_dynamic_speed: bool = False,
             key_movement_base_speed: float = 0.000000,
             invert_x: bool = False,
             invert_y: bool = False,
             boost_scale: float = 0.000000,
             decrease_scale: float = 0.000000,
             show_touch_effect: bool = False,
             show_rotate_icon: bool = False) -> None
```

<a id="unreal.UserCameraSettings.rotation_yaw_speed_scale"></a>

#### rotation\_yaw\_speed\_scale

```python
@property
def rotation_yaw_speed_scale() -> float
```

(float):  [Read-Write] 相机的水平Yaw方向里旋转速度倍率

<a id="unreal.UserCameraSettings.rotation_yaw_speed_scale"></a>

#### rotation\_yaw\_speed\_scale

```python
@rotation_yaw_speed_scale.setter
def rotation_yaw_speed_scale(value: float) -> None
```

<a id="unreal.UserCameraSettings.rotation_pitch_speed_scale"></a>

#### rotation\_pitch\_speed\_scale

```python
@property
def rotation_pitch_speed_scale() -> float
```

(float):  [Read-Write] 相机的垂直Pitch方向里旋转速度倍率

<a id="unreal.UserCameraSettings.rotation_pitch_speed_scale"></a>

#### rotation\_pitch\_speed\_scale

```python
@rotation_pitch_speed_scale.setter
def rotation_pitch_speed_scale(value: float) -> None
```

<a id="unreal.UserCameraSettings.zoom_speed_scale"></a>

#### zoom\_speed\_scale

```python
@property
def zoom_speed_scale() -> float
```

(float):  [Read-Write] 缩放速度倍率

<a id="unreal.UserCameraSettings.zoom_speed_scale"></a>

#### zoom\_speed\_scale

```python
@zoom_speed_scale.setter
def zoom_speed_scale(value: float) -> None
```

<a id="unreal.UserCameraSettings.enable_dynamic_speed"></a>

#### enable\_dynamic\_speed

```python
@property
def enable_dynamic_speed() -> bool
```

(bool):  [Read-Write] 是否启用动态按键速度，相机的速度和高度相关

<a id="unreal.UserCameraSettings.enable_dynamic_speed"></a>

#### enable\_dynamic\_speed

```python
@enable_dynamic_speed.setter
def enable_dynamic_speed(value: bool) -> None
```

<a id="unreal.UserCameraSettings.key_movement_base_speed"></a>

#### key\_movement\_base\_speed

```python
@property
def key_movement_base_speed() -> float
```

(float):  [Read-Write] 基础的按键移动的速度(m/s)

<a id="unreal.UserCameraSettings.key_movement_base_speed"></a>

#### key\_movement\_base\_speed

```python
@key_movement_base_speed.setter
def key_movement_base_speed(value: float) -> None
```

<a id="unreal.UserCameraSettings.invert_x"></a>

#### invert\_x

```python
@property
def invert_x() -> bool
```

(bool):  [Read-Write] 反转X轴

<a id="unreal.UserCameraSettings.invert_x"></a>

#### invert\_x

```python
@invert_x.setter
def invert_x(value: bool) -> None
```

<a id="unreal.UserCameraSettings.invert_y"></a>

#### invert\_y

```python
@property
def invert_y() -> bool
```

(bool):  [Read-Write] 反转Y轴

<a id="unreal.UserCameraSettings.invert_y"></a>

#### invert\_y

```python
@invert_y.setter
def invert_y(value: bool) -> None
```

<a id="unreal.UserCameraSettings.boost_scale"></a>

#### boost\_scale

```python
@property
def boost_scale() -> float
```

(float):  [Read-Write] 按住Shift冲刺时的倍率

<a id="unreal.UserCameraSettings.boost_scale"></a>

#### boost\_scale

```python
@boost_scale.setter
def boost_scale(value: float) -> None
```

<a id="unreal.UserCameraSettings.decrease_scale"></a>

#### decrease\_scale

```python
@property
def decrease_scale() -> float
```

(float):  [Read-Write] 按住Ctrl减速时的倍率

<a id="unreal.UserCameraSettings.decrease_scale"></a>

#### decrease\_scale

```python
@decrease_scale.setter
def decrease_scale(value: float) -> None
```

<a id="unreal.UserCameraSettings.show_touch_effect"></a>

#### show\_touch\_effect

```python
@property
def show_touch_effect() -> bool
```

(bool):  [Read-Write] 是否显示点击时的屏幕特效

<a id="unreal.UserCameraSettings.show_touch_effect"></a>

#### show\_touch\_effect

```python
@show_touch_effect.setter
def show_touch_effect(value: bool) -> None
```

<a id="unreal.UserCameraSettings.show_rotate_icon"></a>

#### show\_rotate\_icon

```python
@property
def show_rotate_icon() -> bool
```

(bool):  [Read-Write] 是否显示旋转时的图标

<a id="unreal.UserCameraSettings.show_rotate_icon"></a>

#### show\_rotate\_icon

```python
@show_rotate_icon.setter
def show_rotate_icon(value: bool) -> None
```

<a id="unreal.RuntimeCameraData"></a>