## RigVMFunction_MathMatrixToTransform Objects

```python
class RigVMFunction_MathMatrixToTransform(RigVMFunction_MathMatrixBase)
```

Makes a transform from a matrix

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathMatrix.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (Transform):  [Read-Write]
- ``value`` (Matrix):  [Read-Write]

<a id="unreal.RigVMFunction_MathMatrixToTransform.__init__"></a>

#### __init__

```python
def __init__(
    value: Matrix = [[0.000000, 0.000000, 0.000000, 0.000000],
                     [0.000000, 0.000000, 0.000000, 0.000000],
                     [0.000000, 0.000000, 0.000000, 0.000000],
                     [0.000000, 0.000000, 0.000000, 0.000000]],
    result: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigVMFunction_MathMatrixToTransform.value"></a>

#### value

```python
@property
def value() -> Matrix
```

(Matrix):  [Read-Write]

<a id="unreal.RigVMFunction_MathMatrixToTransform.value"></a>

#### value

```python
@value.setter
def value(value: Matrix) -> None
```

<a id="unreal.RigVMFunction_MathMatrixToTransform.result"></a>

#### result

```python
@property
def result() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_MathMatrixToTransform"></a>