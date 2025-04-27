## RigVMFunction_MathQuaternionToAxisAndAngle Objects

```python
class RigVMFunction_MathQuaternionToAxisAndAngle(
        RigVMFunction_MathQuaternionBase)
```

Retrieves the axis and angle of a quaternion in radians

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathQuaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angle`` (float):  [Read-Write]
- ``axis`` (Vector):  [Read-Write]
- ``value`` (Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionToAxisAndAngle.__init__"></a>

#### __init__

```python
def __init__(value: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             axis: Vector = [0.000000, 0.000000, 0.000000],
             angle: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionToAxisAndAngle.value"></a>

#### value

```python
@property
def value() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionToAxisAndAngle.value"></a>

#### value

```python
@value.setter
def value(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionToAxisAndAngle.axis"></a>

#### axis

```python
@property
def axis() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathQuaternionToAxisAndAngle.angle"></a>

#### angle

```python
@property
def angle() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_MathQuaternionToAxisAndAngle"></a>