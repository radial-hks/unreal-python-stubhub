## AutoRotationSettings Objects

```python
class AutoRotationSettings(StructBase)
```

自动旋转的配置参数

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpDataSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_stop_when_user_input`` (bool):  [Read-Write] 用户开始操作时是否打断自动旋转
- ``duration`` (float):  [Read-Write] 旋转一圈的时间
- ``enable_zoom_input_when_rotate`` (bool):  [Read-Write] 自动旋转时是否允许缩放操作（如果允许则缩放不会打断旋转）
- ``loop_count`` (int32):  [Read-Write] 转几圈，小于等于0代表无限
- ``rotate_direction`` (AutoCameraRotateDirection):  [Read-Write] 自动旋转的方向，自动、顺时针、逆时针，如果为自动则根据当前角度自动选择方向

<a id="unreal.AutoRotationSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        rotate_direction: AutoCameraRotateDirection = AutoCameraRotateDirection
    .ACR_AUTO,
        duration: float = 0.000000,
        loop_count: int = 0,
        auto_stop_when_user_input: bool = False,
        enable_zoom_input_when_rotate: bool = False) -> None
```

<a id="unreal.AutoRotationSettings.rotate_direction"></a>

#### rotate\_direction

```python
@property
def rotate_direction() -> AutoCameraRotateDirection
```

(AutoCameraRotateDirection):  [Read-Write] 自动旋转的方向，自动、顺时针、逆时针，如果为自动则根据当前角度自动选择方向

<a id="unreal.AutoRotationSettings.rotate_direction"></a>

#### rotate\_direction

```python
@rotate_direction.setter
def rotate_direction(value: AutoCameraRotateDirection) -> None
```

<a id="unreal.AutoRotationSettings.duration"></a>

#### duration

```python
@property
def duration() -> float
```

(float):  [Read-Write] 旋转一圈的时间

<a id="unreal.AutoRotationSettings.duration"></a>

#### duration

```python
@duration.setter
def duration(value: float) -> None
```

<a id="unreal.AutoRotationSettings.loop_count"></a>

#### loop\_count

```python
@property
def loop_count() -> int
```

(int32):  [Read-Write] 转几圈，小于等于0代表无限

<a id="unreal.AutoRotationSettings.loop_count"></a>

#### loop\_count

```python
@loop_count.setter
def loop_count(value: int) -> None
```

<a id="unreal.AutoRotationSettings.auto_stop_when_user_input"></a>

#### auto\_stop\_when\_user\_input

```python
@property
def auto_stop_when_user_input() -> bool
```

(bool):  [Read-Write] 用户开始操作时是否打断自动旋转

<a id="unreal.AutoRotationSettings.auto_stop_when_user_input"></a>

#### auto\_stop\_when\_user\_input

```python
@auto_stop_when_user_input.setter
def auto_stop_when_user_input(value: bool) -> None
```

<a id="unreal.AutoRotationSettings.enable_zoom_input_when_rotate"></a>

#### enable\_zoom\_input\_when\_rotate

```python
@property
def enable_zoom_input_when_rotate() -> bool
```

(bool):  [Read-Write] 自动旋转时是否允许缩放操作（如果允许则缩放不会打断旋转）

<a id="unreal.AutoRotationSettings.enable_zoom_input_when_rotate"></a>

#### enable\_zoom\_input\_when\_rotate

```python
@enable_zoom_input_when_rotate.setter
def enable_zoom_input_when_rotate(value: bool) -> None
```

<a id="unreal.UserCameraSettings"></a>