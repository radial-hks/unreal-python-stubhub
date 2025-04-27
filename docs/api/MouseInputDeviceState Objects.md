## MouseInputDeviceState Objects

```python
class MouseInputDeviceState(StructBase)
```

Current State of a physical Mouse device at a point in time.

**C++ Source:**

- **Module**: InteractiveToolsFramework
- **File**: InputState.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``delta2d`` (Vector2D):  [Read-Write] Change in 2D mouse position from last state event
- ``left`` (DeviceButtonState):  [Read-Write] State of the left mouse button
- ``middle`` (DeviceButtonState):  [Read-Write] State of the middle mouse button
- ``position2d`` (Vector2D):  [Read-Write] Current 2D position of the mouse, in application-defined coordinate system
- ``right`` (DeviceButtonState):  [Read-Write] State of the right mouse button
- ``wheel_delta`` (float):  [Read-Write] Change in 'ticks' of the mouse wheel since last state event
- ``world_ray`` (Ray):  [Read-Write] Ray into current 3D scene at current 2D mouse position

<a id="unreal.MouseInputDeviceState.__init__"></a>

#### __init__

```python
def __init__(
    left: DeviceButtonState = [[], False, False, False, False],
    middle: DeviceButtonState = [[], False, False, False, False],
    right: DeviceButtonState = [[], False, False, False, False],
    wheel_delta: float = 0.000000,
    position2d: Vector2D = [0.000000, 0.000000],
    delta2d: Vector2D = [0.000000, 0.000000],
    world_ray: Ray = [[0.000000, 0.000000, 0.000000],
                      [0.000000, 0.000000, 0.000000]]
) -> None
```

<a id="unreal.MouseInputDeviceState.left"></a>

#### left

```python
@property
def left() -> DeviceButtonState
```

(DeviceButtonState):  [Read-Write] State of the left mouse button

<a id="unreal.MouseInputDeviceState.left"></a>

#### left

```python
@left.setter
def left(value: DeviceButtonState) -> None
```

<a id="unreal.MouseInputDeviceState.middle"></a>

#### middle

```python
@property
def middle() -> DeviceButtonState
```

(DeviceButtonState):  [Read-Write] State of the middle mouse button

<a id="unreal.MouseInputDeviceState.middle"></a>

#### middle

```python
@middle.setter
def middle(value: DeviceButtonState) -> None
```

<a id="unreal.MouseInputDeviceState.right"></a>

#### right

```python
@property
def right() -> DeviceButtonState
```

(DeviceButtonState):  [Read-Write] State of the right mouse button

<a id="unreal.MouseInputDeviceState.right"></a>

#### right

```python
@right.setter
def right(value: DeviceButtonState) -> None
```

<a id="unreal.MouseInputDeviceState.wheel_delta"></a>

#### wheel_delta

```python
@property
def wheel_delta() -> float
```

(float):  [Read-Write] Change in 'ticks' of the mouse wheel since last state event

<a id="unreal.MouseInputDeviceState.wheel_delta"></a>

#### wheel_delta

```python
@wheel_delta.setter
def wheel_delta(value: float) -> None
```

<a id="unreal.MouseInputDeviceState.position2d"></a>

#### position2d

```python
@property
def position2d() -> Vector2D
```

(Vector2D):  [Read-Write] Current 2D position of the mouse, in application-defined coordinate system

<a id="unreal.MouseInputDeviceState.position2d"></a>

#### position2d

```python
@position2d.setter
def position2d(value: Vector2D) -> None
```

<a id="unreal.MouseInputDeviceState.delta2d"></a>

#### delta2d

```python
@property
def delta2d() -> Vector2D
```

(Vector2D):  [Read-Write] Change in 2D mouse position from last state event

<a id="unreal.MouseInputDeviceState.delta2d"></a>

#### delta2d

```python
@delta2d.setter
def delta2d(value: Vector2D) -> None
```

<a id="unreal.MouseInputDeviceState.world_ray"></a>

#### world_ray

```python
@property
def world_ray() -> Ray
```

(Ray):  [Read-Write] Ray into current 3D scene at current 2D mouse position

<a id="unreal.MouseInputDeviceState.world_ray"></a>

#### world_ray

```python
@world_ray.setter
def world_ray(value: Ray) -> None
```

<a id="unreal.InputDeviceState"></a>