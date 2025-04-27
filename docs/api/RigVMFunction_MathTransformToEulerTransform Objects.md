## RigVMFunction_MathTransformToEulerTransform Objects

```python
class RigVMFunction_MathTransformToEulerTransform(
        RigVMFunction_MathTransformBase)
```

Retrieves a euler based transform from a quaternion based transform

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (EulerTransform):  [Read-Write]
- ``value`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformToEulerTransform.__init__"></a>

#### __init__

```python
def __init__(
    value: Transform = [[0.000000, 0.000000, 0.000000],
                        [-0.000000, 0.000000, 0.000000],
                        [1.000000, 1.000000, 1.000000]],
    result: EulerTransform = [[0.000000, 0.000000, 0.000000],
                              [0.000000, 0.000000, 0.000000],
                              [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigVMFunction_MathTransformToEulerTransform.value"></a>

#### value

```python
@property
def value() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformToEulerTransform.value"></a>

#### value

```python
@value.setter
def value(value: Transform) -> None
```

<a id="unreal.RigVMFunction_MathTransformToEulerTransform.result"></a>

#### result

```python
@property
def result() -> EulerTransform
```

(EulerTransform):  [Read-Only]

<a id="unreal.RigUnit_MathTransformToEulerTransform"></a>