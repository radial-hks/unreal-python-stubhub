## AutoSelfRotationSettings Objects

```python
class AutoSelfRotationSettings(StructBase)
```

自身自动旋转的配置参数

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpDataSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_stop_when_user_input`` (bool):  [Read-Write] 用户开始操作时是否打断自动旋转
- ``duration`` (float):  [Read-Write] 旋转持续的时间
- ``rotate_value`` (Vector2D):  [Read-Write] 旋转的角度值(x=pitch, y=yaw)，速度模式时含义是每秒转动的角度，非速度模式时表示总旋转角度
- ``use_speed_mode`` (bool):  [Read-Write] 是速度模式还是角度模式(速度模式：输入速度一直运动；非速度模式：输入旋转的角度和用时，到目标后自动停止)

<a id="unreal.AutoSelfRotationSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(use_speed_mode: bool = False,
             rotate_value: Vector2D = [0.000000, 0.000000],
             duration: float = 0.000000,
             auto_stop_when_user_input: bool = False) -> None
```

<a id="unreal.AutoSelfRotationSettings.use_speed_mode"></a>

#### use\_speed\_mode

```python
@property
def use_speed_mode() -> bool
```

(bool):  [Read-Write] 是速度模式还是角度模式(速度模式：输入速度一直运动；非速度模式：输入旋转的角度和用时，到目标后自动停止)

<a id="unreal.AutoSelfRotationSettings.use_speed_mode"></a>

#### use\_speed\_mode

```python
@use_speed_mode.setter
def use_speed_mode(value: bool) -> None
```

<a id="unreal.AutoSelfRotationSettings.rotate_value"></a>

#### rotate\_value

```python
@property
def rotate_value() -> Vector2D
```

(Vector2D):  [Read-Write] 旋转的角度值(x=pitch, y=yaw)，速度模式时含义是每秒转动的角度，非速度模式时表示总旋转角度

<a id="unreal.AutoSelfRotationSettings.rotate_value"></a>

#### rotate\_value

```python
@rotate_value.setter
def rotate_value(value: Vector2D) -> None
```

<a id="unreal.AutoSelfRotationSettings.duration"></a>

#### duration

```python
@property
def duration() -> float
```

(float):  [Read-Write] 旋转持续的时间

<a id="unreal.AutoSelfRotationSettings.duration"></a>

#### duration

```python
@duration.setter
def duration(value: float) -> None
```

<a id="unreal.AutoSelfRotationSettings.auto_stop_when_user_input"></a>

#### auto\_stop\_when\_user\_input

```python
@property
def auto_stop_when_user_input() -> bool
```

(bool):  [Read-Write] 用户开始操作时是否打断自动旋转

<a id="unreal.AutoSelfRotationSettings.auto_stop_when_user_input"></a>

#### auto\_stop\_when\_user\_input

```python
@auto_stop_when_user_input.setter
def auto_stop_when_user_input(value: bool) -> None
```

<a id="unreal.AutoMovementSettings"></a>