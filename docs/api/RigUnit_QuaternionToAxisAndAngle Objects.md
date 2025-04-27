## RigUnit_QuaternionToAxisAndAngle Objects

```python
class RigUnit_QuaternionToAxisAndAngle(RigUnit)
```

Rig Unit Quaternion to Axis and Angle

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Quaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angle`` (float):  [Read-Write]
- ``argument`` (Quat):  [Read-Write]
- ``axis`` (Vector):  [Read-Write]

<a id="unreal.RigUnit_QuaternionToAxisAndAngle.__init__"></a>

#### __init__

```python
def __init__(argument: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             axis: Vector = [0.000000, 0.000000, 0.000000],
             angle: float = 0.000000) -> None
```

<a id="unreal.RigUnit_QuaternionToAxisAndAngle.argument"></a>

#### argument

```python
@property
def argument() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigUnit_QuaternionToAxisAndAngle.argument"></a>

#### argument

```python
@argument.setter
def argument(value: Quat) -> None
```

<a id="unreal.RigUnit_QuaternionToAxisAndAngle.axis"></a>

#### axis

```python
@property
def axis() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_QuaternionToAxisAndAngle.angle"></a>

#### angle

```python
@property
def angle() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_QuaternionFromAxisAndAngle"></a>