## RigVMFunction_MathTransformFromEulerTransform Objects

```python
class RigVMFunction_MathTransformFromEulerTransform(
        RigVMFunction_MathTransformBase)
```

Makes a quaternion based transform from a euler based transform

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``euler_transform`` (EulerTransform):  [Read-Write]
- ``result`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformFromEulerTransform.__init__"></a>

#### __init__

```python
def __init__(
    euler_transform: EulerTransform = [[0.000000, 0.000000, 0.000000],
                                       [0.000000, 0.000000, 0.000000],
                                       [1.000000, 1.000000, 1.000000]],
    result: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigVMFunction_MathTransformFromEulerTransform.euler_transform"></a>

#### euler_transform

```python
@property
def euler_transform() -> EulerTransform
```

(EulerTransform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformFromEulerTransform.euler_transform"></a>

#### euler_transform

```python
@euler_transform.setter
def euler_transform(value: EulerTransform) -> None
```

<a id="unreal.RigVMFunction_MathTransformFromEulerTransform.result"></a>

#### result

```python
@property
def result() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_MathTransformFromEulerTransform"></a>