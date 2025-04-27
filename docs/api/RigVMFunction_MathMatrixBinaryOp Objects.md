## RigVMFunction_MathMatrixBinaryOp Objects

```python
class RigVMFunction_MathMatrixBinaryOp(RigVMFunction_MathMatrixBase)
```

Rig VMFunction Math Matrix Binary Op

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathMatrix.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (Matrix):  [Read-Write]
- ``b`` (Matrix):  [Read-Write]
- ``result`` (Matrix):  [Read-Write]

<a id="unreal.RigVMFunction_MathMatrixBinaryOp.__init__"></a>

#### __init__

```python
def __init__(
    a: Matrix = [[0.000000, 0.000000, 0.000000, 0.000000],
                 [0.000000, 0.000000, 0.000000, 0.000000],
                 [0.000000, 0.000000, 0.000000, 0.000000],
                 [0.000000, 0.000000, 0.000000, 0.000000]],
    b: Matrix = [[0.000000, 0.000000, 0.000000, 0.000000],
                 [0.000000, 0.000000, 0.000000, 0.000000],
                 [0.000000, 0.000000, 0.000000, 0.000000],
                 [0.000000, 0.000000, 0.000000, 0.000000]],
    result: Matrix = [[0.000000, 0.000000, 0.000000, 0.000000],
                      [0.000000, 0.000000, 0.000000, 0.000000],
                      [0.000000, 0.000000, 0.000000, 0.000000],
                      [0.000000, 0.000000, 0.000000, 0.000000]]
) -> None
```

<a id="unreal.RigVMFunction_MathMatrixBinaryOp.a"></a>

#### a

```python
@property
def a() -> Matrix
```

(Matrix):  [Read-Write]

<a id="unreal.RigVMFunction_MathMatrixBinaryOp.a"></a>

#### a

```python
@a.setter
def a(value: Matrix) -> None
```

<a id="unreal.RigVMFunction_MathMatrixBinaryOp.b"></a>

#### b

```python
@property
def b() -> Matrix
```

(Matrix):  [Read-Write]

<a id="unreal.RigVMFunction_MathMatrixBinaryOp.b"></a>

#### b

```python
@b.setter
def b(value: Matrix) -> None
```

<a id="unreal.RigVMFunction_MathMatrixBinaryOp.result"></a>

#### result

```python
@property
def result() -> Matrix
```

(Matrix):  [Read-Only]

<a id="unreal.RigUnit_MathMatrixBinaryOp"></a>