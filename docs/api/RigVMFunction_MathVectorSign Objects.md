## RigVMFunction_MathVectorSign Objects

```python
class RigVMFunction_MathVectorSign(RigVMFunction_MathVectorUnaryOp)
```

Returns the sign of the value (+1 for >= FVector(0.f, 0.f, 0.f), -1 for < 0.f) for each component

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathVector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (Vector):  [Read-Write]
- ``value`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorSign.__init__"></a>

#### __init__

```python
def __init__(value: Vector = [0.000000, 0.000000, 0.000000],
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_MathVectorSign"></a>