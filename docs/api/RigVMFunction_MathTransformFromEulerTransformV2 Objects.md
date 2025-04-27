## RigVMFunction_MathTransformFromEulerTransformV2 Objects

```python
class RigVMFunction_MathTransformFromEulerTransformV2(
        RigVMFunction_MathTransformBase)
```

Makes a quaternion based transform from a euler based transform

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (Transform):  [Read-Write]
- ``value`` (EulerTransform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformFromEulerTransformV2.__init__"></a>

#### __init__

```python
def __init__(
    value: EulerTransform = [[0.000000, 0.000000, 0.000000],
                             [0.000000, 0.000000, 0.000000],
                             [1.000000, 1.000000, 1.000000]],
    result: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigVMFunction_MathTransformFromEulerTransformV2.value"></a>

#### value

```python
@property
def value() -> EulerTransform
```

(EulerTransform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformFromEulerTransformV2.value"></a>

#### value

```python
@value.setter
def value(value: EulerTransform) -> None
```

<a id="unreal.RigVMFunction_MathTransformFromEulerTransformV2.result"></a>

#### result

```python
@property
def result() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_MathTransformFromEulerTransformV2"></a>