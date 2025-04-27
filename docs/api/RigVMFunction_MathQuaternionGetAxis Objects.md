## RigVMFunction_MathQuaternionGetAxis Objects

```python
class RigVMFunction_MathQuaternionGetAxis(RigVMFunction_MathQuaternionBase)
```

Rotates a given vector by the quaternion

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathQuaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``axis`` (AxisType):  [Read-Write]
- ``quaternion`` (Quat):  [Read-Write]
- ``result`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionGetAxis.__init__"></a>

#### __init__

```python
def __init__(quaternion: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             axis: AxisType = AxisType.NONE,
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionGetAxis.quaternion"></a>

#### quaternion

```python
@property
def quaternion() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionGetAxis.quaternion"></a>

#### quaternion

```python
@quaternion.setter
def quaternion(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionGetAxis.axis"></a>

#### axis

```python
@property
def axis() -> AxisType
```

(AxisType):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionGetAxis.axis"></a>

#### axis

```python
@axis.setter
def axis(value: AxisType) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionGetAxis.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_MathQuaternionGetAxis"></a>