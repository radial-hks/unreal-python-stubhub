## RigVMFunction_MathQuaternionRotateVector Objects

```python
class RigVMFunction_MathQuaternionRotateVector(RigVMFunction_MathQuaternionBase
                                               )
```

Rotates a given vector by the quaternion

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathQuaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (Vector):  [Read-Write]
- ``transform`` (Quat):  [Read-Write]
- ``vector`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionRotateVector.__init__"></a>

#### __init__

```python
def __init__(transform: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             vector: Vector = [0.000000, 0.000000, 0.000000],
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionRotateVector.transform"></a>

#### transform

```python
@property
def transform() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionRotateVector.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionRotateVector.quaternion"></a>

#### quaternion

```python
@property
def quaternion() -> Quat
```

deprecated: 'quaternion' was renamed to 'transform'.

<a id="unreal.RigVMFunction_MathQuaternionRotateVector.quaternion"></a>

#### quaternion

```python
@quaternion.setter
def quaternion(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionRotateVector.vector"></a>

#### vector

```python
@property
def vector() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionRotateVector.vector"></a>

#### vector

```python
@vector.setter
def vector(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionRotateVector.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_MathQuaternionRotateVector"></a>