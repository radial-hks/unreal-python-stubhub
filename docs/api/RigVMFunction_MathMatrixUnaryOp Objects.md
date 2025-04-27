## RigVMFunction_MathMatrixUnaryOp Objects

```python
class RigVMFunction_MathMatrixUnaryOp(RigVMFunction_MathMatrixBase)
```

Rig VMFunction Math Matrix Unary Op

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathMatrix.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (Matrix):  [Read-Write]
- ``value`` (Matrix):  [Read-Write]

<a id="unreal.RigVMFunction_MathMatrixUnaryOp.__init__"></a>

#### __init__

```python
def __init__(
    value: Matrix = [[0.000000, 0.000000, 0.000000, 0.000000],
                     [0.000000, 0.000000, 0.000000, 0.000000],
                     [0.000000, 0.000000, 0.000000, 0.000000],
                     [0.000000, 0.000000, 0.000000, 0.000000]],
    result: Matrix = [[0.000000, 0.000000, 0.000000, 0.000000],
                      [0.000000, 0.000000, 0.000000, 0.000000],
                      [0.000000, 0.000000, 0.000000, 0.000000],
                      [0.000000, 0.000000, 0.000000, 0.000000]]
) -> None
```

<a id="unreal.RigVMFunction_MathMatrixUnaryOp.value"></a>

#### value

```python
@property
def value() -> Matrix
```

(Matrix):  [Read-Write]

<a id="unreal.RigVMFunction_MathMatrixUnaryOp.value"></a>

#### value

```python
@value.setter
def value(value: Matrix) -> None
```

<a id="unreal.RigVMFunction_MathMatrixUnaryOp.result"></a>

#### result

```python
@property
def result() -> Matrix
```

(Matrix):  [Read-Only]

<a id="unreal.RigUnit_MathMatrixUnaryOp"></a>