## RigVMFunction_MathMatrixFromTransform Objects

```python
class RigVMFunction_MathMatrixFromTransform(RigVMFunction_MathMatrixBase)
```

Makes a matrix from a transform

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathMatrix.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (Matrix):  [Read-Write]
- ``transform`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathMatrixFromTransform.__init__"></a>

#### __init__

```python
def __init__(
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]],
    result: Matrix = [[0.000000, 0.000000, 0.000000, 0.000000],
                      [0.000000, 0.000000, 0.000000, 0.000000],
                      [0.000000, 0.000000, 0.000000, 0.000000],
                      [0.000000, 0.000000, 0.000000, 0.000000]]
) -> None
```

<a id="unreal.RigVMFunction_MathMatrixFromTransform.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathMatrixFromTransform.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigVMFunction_MathMatrixFromTransform.result"></a>

#### result

```python
@property
def result() -> Matrix
```

(Matrix):  [Read-Only]

<a id="unreal.RigUnit_MathMatrixFromTransform"></a>