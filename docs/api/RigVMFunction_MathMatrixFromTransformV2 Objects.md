## RigVMFunction_MathMatrixFromTransformV2 Objects

```python
class RigVMFunction_MathMatrixFromTransformV2(RigVMFunction_MathMatrixBase)
```

Makes a matrix from a transform

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathMatrix.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (Matrix):  [Read-Write]
- ``value`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathMatrixFromTransformV2.__init__"></a>

#### __init__

```python
def __init__(
    value: Transform = [[0.000000, 0.000000, 0.000000],
                        [-0.000000, 0.000000, 0.000000],
                        [1.000000, 1.000000, 1.000000]],
    result: Matrix = [[0.000000, 0.000000, 0.000000, 0.000000],
                      [0.000000, 0.000000, 0.000000, 0.000000],
                      [0.000000, 0.000000, 0.000000, 0.000000],
                      [0.000000, 0.000000, 0.000000, 0.000000]]
) -> None
```

<a id="unreal.RigVMFunction_MathMatrixFromTransformV2.value"></a>

#### value

```python
@property
def value() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathMatrixFromTransformV2.value"></a>

#### value

```python
@value.setter
def value(value: Transform) -> None
```

<a id="unreal.RigVMFunction_MathMatrixFromTransformV2.result"></a>

#### result

```python
@property
def result() -> Matrix
```

(Matrix):  [Read-Only]

<a id="unreal.RigUnit_MathMatrixFromTransformV2"></a>