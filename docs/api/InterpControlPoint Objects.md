## InterpControlPoint Objects

```python
class InterpControlPoint(StructBase)
```

Interp Control Point

**C++ Source:**

- **Module**: Engine
- **File**: InterpToMovementComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``position_control_point`` (Vector):  [Read-Write] The position of the point
- ``position_is_relative`` (bool):  [Read-Write] Is the location relative to the root components initial location

<a id="unreal.InterpControlPoint.__init__"></a>

#### __init__

```python
def __init__(position_control_point: Vector = [0.000000, 0.000000, 0.000000],
             position_is_relative: bool = False) -> None
```

<a id="unreal.InterpControlPoint.position_control_point"></a>

#### position_control_point

```python
@property
def position_control_point() -> Vector
```

(Vector):  [Read-Write] The position of the point

<a id="unreal.InterpControlPoint.position_control_point"></a>

#### position_control_point

```python
@position_control_point.setter
def position_control_point(value: Vector) -> None
```

<a id="unreal.InterpControlPoint.position_is_relative"></a>

#### position_is_relative

```python
@property
def position_is_relative() -> bool
```

(bool):  [Read-Write] Is the location relative to the root components initial location

<a id="unreal.InterpControlPoint.position_is_relative"></a>

#### position_is_relative

```python
@position_is_relative.setter
def position_is_relative(value: bool) -> None
```

<a id="unreal.DebugFloatHistory"></a>