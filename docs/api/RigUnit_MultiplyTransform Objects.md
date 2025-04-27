## RigUnit_MultiplyTransform Objects

```python
class RigUnit_MultiplyTransform(RigUnit_BinaryTransformOp)
```

Rig Unit Multiply Transform

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Transform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``argument0`` (Transform):  [Read-Write]
- ``argument1`` (Transform):  [Read-Write]
- ``result`` (Transform):  [Read-Write]

<a id="unreal.RigUnit_MultiplyTransform.__init__"></a>

#### __init__

```python
def __init__(
    argument0: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]],
    argument1: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]],
    result: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_GetRelativeTransform"></a>