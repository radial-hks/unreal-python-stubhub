## RigVMFunction_MathQuaternionFromEuler Objects

```python
class RigVMFunction_MathQuaternionFromEuler(RigVMFunction_MathQuaternionBase)
```

Makes a quaternion from euler values in degrees

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathQuaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``euler`` (Vector):  [Read-Write]
- ``result`` (Quat):  [Read-Write]
- ``rotation_order`` (EulerRotationOrder):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionFromEuler.__init__"></a>

#### __init__

```python
def __init__(euler: Vector = [0.000000, 0.000000, 0.000000],
             rotation_order: EulerRotationOrder = EulerRotationOrder.XYZ,
             result: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionFromEuler.euler"></a>

#### euler

```python
@property
def euler() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionFromEuler.euler"></a>

#### euler

```python
@euler.setter
def euler(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionFromEuler.rotation_order"></a>

#### rotation_order

```python
@property
def rotation_order() -> EulerRotationOrder
```

(EulerRotationOrder):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionFromEuler.rotation_order"></a>

#### rotation_order

```python
@rotation_order.setter
def rotation_order(value: EulerRotationOrder) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionFromEuler.result"></a>

#### result

```python
@property
def result() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_MathQuaternionFromEuler"></a>