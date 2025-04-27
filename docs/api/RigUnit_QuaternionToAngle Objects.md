## RigUnit_QuaternionToAngle Objects

```python
class RigUnit_QuaternionToAngle(RigUnit)
```

Rig Unit Quaternion to Angle

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Quaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angle`` (float):  [Read-Write]
- ``argument`` (Quat):  [Read-Write]
- ``axis`` (Vector):  [Read-Write]

<a id="unreal.RigUnit_QuaternionToAngle.__init__"></a>

#### __init__

```python
def __init__(axis: Vector = [0.000000, 0.000000, 0.000000],
             argument: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             angle: float = 0.000000) -> None
```

<a id="unreal.RigUnit_QuaternionToAngle.axis"></a>

#### axis

```python
@property
def axis() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_QuaternionToAngle.axis"></a>

#### axis

```python
@axis.setter
def axis(value: Vector) -> None
```

<a id="unreal.RigUnit_QuaternionToAngle.argument"></a>

#### argument

```python
@property
def argument() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigUnit_QuaternionToAngle.argument"></a>

#### argument

```python
@argument.setter
def argument(value: Quat) -> None
```

<a id="unreal.RigUnit_QuaternionToAngle.angle"></a>

#### angle

```python
@property
def angle() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_BinaryTransformOp"></a>