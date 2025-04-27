## RigVMFunction_MathTransformUnaryOp Objects

```python
class RigVMFunction_MathTransformUnaryOp(RigVMFunction_MathTransformBase)
```

Rig VMFunction Math Transform Unary Op

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (Transform):  [Read-Write]
- ``value`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformUnaryOp.__init__"></a>

#### __init__

```python
def __init__(
    value: Transform = [[0.000000, 0.000000, 0.000000],
                        [-0.000000, 0.000000, 0.000000],
                        [1.000000, 1.000000, 1.000000]],
    result: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigVMFunction_MathTransformUnaryOp.value"></a>

#### value

```python
@property
def value() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformUnaryOp.value"></a>

#### value

```python
@value.setter
def value(value: Transform) -> None
```

<a id="unreal.RigVMFunction_MathTransformUnaryOp.result"></a>

#### result

```python
@property
def result() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_MathTransformUnaryOp"></a>