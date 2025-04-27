## RigVMFunction_MathQuaternionFromAxisAndAngle Objects

```python
class RigVMFunction_MathQuaternionFromAxisAndAngle(
        RigVMFunction_MathQuaternionBase)
```

Makes a quaternion from an axis and an angle in radians

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathQuaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angle`` (float):  [Read-Write]
- ``axis`` (Vector):  [Read-Write]
- ``result`` (Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionFromAxisAndAngle.__init__"></a>

#### __init__

```python
def __init__(axis: Vector = [0.000000, 0.000000, 0.000000],
             angle: float = 0.000000,
             result: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionFromAxisAndAngle.axis"></a>

#### axis

```python
@property
def axis() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionFromAxisAndAngle.axis"></a>

#### axis

```python
@axis.setter
def axis(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionFromAxisAndAngle.angle"></a>

#### angle

```python
@property
def angle() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionFromAxisAndAngle.angle"></a>

#### angle

```python
@angle.setter
def angle(value: float) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionFromAxisAndAngle.result"></a>

#### result

```python
@property
def result() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_MathQuaternionFromAxisAndAngle"></a>