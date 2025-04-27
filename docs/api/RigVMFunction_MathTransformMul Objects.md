## RigVMFunction_MathTransformMul Objects

```python
class RigVMFunction_MathTransformMul(
        RigVMFunction_MathTransformBinaryAggregateOp)
```

Returns the product of the two values

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (Transform):  [Read-Write]
- ``b`` (Transform):  [Read-Write]
- ``result`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformMul.__init__"></a>

#### __init__

```python
def __init__(
    a: Transform = [[0.000000, 0.000000, 0.000000],
                    [-0.000000, 0.000000, 0.000000],
                    [1.000000, 1.000000, 1.000000]],
    b: Transform = [[0.000000, 0.000000, 0.000000],
                    [-0.000000, 0.000000, 0.000000],
                    [1.000000, 1.000000, 1.000000]],
    result: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_MathTransformMul"></a>