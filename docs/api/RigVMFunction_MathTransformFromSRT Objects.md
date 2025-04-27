## RigVMFunction_MathTransformFromSRT Objects

```python
class RigVMFunction_MathTransformFromSRT(RigVMFunction_MathTransformBase)
```

Composes a Transform (and Euler Transform) from its components.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``euler_transform`` (EulerTransform):  [Read-Write]
- ``location`` (Vector):  [Read-Write]
- ``rotation`` (Vector):  [Read-Write]
- ``rotation_order`` (EulerRotationOrder):  [Read-Write]
- ``scale`` (Vector):  [Read-Write]
- ``transform`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformFromSRT.__init__"></a>

#### __init__

```python
def __init__(
    location: Vector = [0.000000, 0.000000, 0.000000],
    rotation: Vector = [0.000000, 0.000000, 0.000000],
    rotation_order: EulerRotationOrder = EulerRotationOrder.XYZ,
    scale: Vector = [0.000000, 0.000000, 0.000000],
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]],
    euler_transform: EulerTransform = [[0.000000, 0.000000, 0.000000],
                                       [0.000000, 0.000000, 0.000000],
                                       [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigVMFunction_MathTransformFromSRT.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformFromSRT.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathTransformFromSRT.rotation"></a>

#### rotation

```python
@property
def rotation() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformFromSRT.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathTransformFromSRT.rotation_order"></a>

#### rotation_order

```python
@property
def rotation_order() -> EulerRotationOrder
```

(EulerRotationOrder):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformFromSRT.rotation_order"></a>

#### rotation_order

```python
@rotation_order.setter
def rotation_order(value: EulerRotationOrder) -> None
```

<a id="unreal.RigVMFunction_MathTransformFromSRT.scale"></a>

#### scale

```python
@property
def scale() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformFromSRT.scale"></a>

#### scale

```python
@scale.setter
def scale(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathTransformFromSRT.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigVMFunction_MathTransformFromSRT.euler_transform"></a>

#### euler_transform

```python
@property
def euler_transform() -> EulerTransform
```

(EulerTransform):  [Read-Only]

<a id="unreal.RigUnit_MathTransformFromSRT"></a>