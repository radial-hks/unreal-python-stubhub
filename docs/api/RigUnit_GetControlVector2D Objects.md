## RigUnit_GetControlVector2D Objects

```python
class RigUnit_GetControlVector2D(RigUnit)
```

GetControlVector2D is used to retrieve a single Vector2D from a hierarchy.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_GetControlTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control`` (Name):  [Read-Write] The name of the Control to retrieve the Vector2D for.
- ``maximum`` (Vector2D):  [Read-Write] The maximum value of the control.
- ``minimum`` (Vector2D):  [Read-Write] The minimum value of the control.
- ``vector`` (Vector2D):  [Read-Write] The current value of the control.

<a id="unreal.RigUnit_GetControlVector2D.__init__"></a>

#### __init__

```python
def __init__(control: Name = "None",
             vector: Vector2D = [0.000000, 0.000000],
             minimum: Vector2D = [0.000000, 0.000000],
             maximum: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_GetControlVector2D.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to retrieve the Vector2D for.

<a id="unreal.RigUnit_GetControlVector2D.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_GetControlVector2D.vector"></a>

#### vector

```python
@property
def vector() -> Vector2D
```

(Vector2D):  [Read-Only] The current value of the control.

<a id="unreal.RigUnit_GetControlVector2D.minimum"></a>

#### minimum

```python
@property
def minimum() -> Vector2D
```

(Vector2D):  [Read-Only] The minimum value of the control.

<a id="unreal.RigUnit_GetControlVector2D.maximum"></a>

#### maximum

```python
@property
def maximum() -> Vector2D
```

(Vector2D):  [Read-Only] The maximum value of the control.

<a id="unreal.RigUnit_GetControlVector"></a>