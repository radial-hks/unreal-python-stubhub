## AutoMovementSettings Objects

```python
class AutoMovementSettings(StructBase)
```

自动位移的配置参数

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpDataSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_stop_when_user_input`` (bool):  [Read-Write] 当用户开始操作时是否自动打断自动位移
- ``move_direction`` (Vector):  [Read-Write] 移动的方向
- ``move_distance`` (double):  [Read-Write] 距离模式时，移动的距离, 单位：cm
- ``move_duration`` (float):  [Read-Write] 距离模式时，移动的时长
- ``speed`` (double):  [Read-Write] 速度模式移动的速度，单位：m/s
- ``use_speed_mode`` (bool):  [Read-Write] 是否为速度模(速度模式：输入一个速度持续运动；非速度模式：输入运动的距离和用时，到目标后自动停止)

<a id="unreal.AutoMovementSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(use_speed_mode: bool = False,
             move_direction: Vector = [0.000000, 0.000000, 0.000000],
             speed: float = 0.000000,
             move_duration: float = 0.000000,
             move_distance: float = 0.000000,
             auto_stop_when_user_input: bool = False) -> None
```

<a id="unreal.AutoMovementSettings.use_speed_mode"></a>

#### use\_speed\_mode

```python
@property
def use_speed_mode() -> bool
```

(bool):  [Read-Write] 是否为速度模(速度模式：输入一个速度持续运动；非速度模式：输入运动的距离和用时，到目标后自动停止)

<a id="unreal.AutoMovementSettings.use_speed_mode"></a>

#### use\_speed\_mode

```python
@use_speed_mode.setter
def use_speed_mode(value: bool) -> None
```

<a id="unreal.AutoMovementSettings.move_direction"></a>

#### move\_direction

```python
@property
def move_direction() -> Vector
```

(Vector):  [Read-Write] 移动的方向

<a id="unreal.AutoMovementSettings.move_direction"></a>

#### move\_direction

```python
@move_direction.setter
def move_direction(value: Vector) -> None
```

<a id="unreal.AutoMovementSettings.speed"></a>

#### speed

```python
@property
def speed() -> float
```

(double):  [Read-Write] 速度模式移动的速度，单位：m/s

<a id="unreal.AutoMovementSettings.speed"></a>

#### speed

```python
@speed.setter
def speed(value: float) -> None
```

<a id="unreal.AutoMovementSettings.move_duration"></a>

#### move\_duration

```python
@property
def move_duration() -> float
```

(float):  [Read-Write] 距离模式时，移动的时长

<a id="unreal.AutoMovementSettings.move_duration"></a>

#### move\_duration

```python
@move_duration.setter
def move_duration(value: float) -> None
```

<a id="unreal.AutoMovementSettings.move_distance"></a>

#### move\_distance

```python
@property
def move_distance() -> float
```

(double):  [Read-Write] 距离模式时，移动的距离, 单位：cm

<a id="unreal.AutoMovementSettings.move_distance"></a>

#### move\_distance

```python
@move_distance.setter
def move_distance(value: float) -> None
```

<a id="unreal.AutoMovementSettings.auto_stop_when_user_input"></a>

#### auto\_stop\_when\_user\_input

```python
@property
def auto_stop_when_user_input() -> bool
```

(bool):  [Read-Write] 当用户开始操作时是否自动打断自动位移

<a id="unreal.AutoMovementSettings.auto_stop_when_user_input"></a>

#### auto\_stop\_when\_user\_input

```python
@auto_stop_when_user_input.setter
def auto_stop_when_user_input(value: bool) -> None
```

<a id="unreal.AutoRotationSettings"></a>