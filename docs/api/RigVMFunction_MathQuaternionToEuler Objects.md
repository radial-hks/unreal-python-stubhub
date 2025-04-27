## RigVMFunction_MathQuaternionToEuler Objects

```python
class RigVMFunction_MathQuaternionToEuler(RigVMFunction_MathQuaternionBase)
```

Retrieves the euler angles in degrees

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathQuaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (Vector):  [Read-Write]
- ``rotation_order`` (EulerRotationOrder):  [Read-Write]
- ``value`` (Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionToEuler.__init__"></a>

#### __init__

```python
def __init__(value: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             rotation_order: EulerRotationOrder = EulerRotationOrder.XYZ,
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionToEuler.value"></a>

#### value

```python
@property
def value() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionToEuler.value"></a>

#### value

```python
@value.setter
def value(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionToEuler.rotation_order"></a>

#### rotation_order

```python
@property
def rotation_order() -> EulerRotationOrder
```

(EulerRotationOrder):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionToEuler.rotation_order"></a>

#### rotation_order

```python
@rotation_order.setter
def rotation_order(value: EulerRotationOrder) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionToEuler.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_MathQuaternionToEuler"></a>