## RigVMFunction_MathTransformBinaryAggregateOp Objects

```python
class RigVMFunction_MathTransformBinaryAggregateOp(
        RigVMFunction_MathTransformBase)
```

Rig VMFunction Math Transform Binary Aggregate Op

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (Transform):  [Read-Write]
- ``b`` (Transform):  [Read-Write]
- ``result`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformBinaryAggregateOp.__init__"></a>

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

<a id="unreal.RigVMFunction_MathTransformBinaryAggregateOp.a"></a>

#### a

```python
@property
def a() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformBinaryAggregateOp.a"></a>

#### a

```python
@a.setter
def a(value: Transform) -> None
```

<a id="unreal.RigVMFunction_MathTransformBinaryAggregateOp.b"></a>

#### b

```python
@property
def b() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformBinaryAggregateOp.b"></a>

#### b

```python
@b.setter
def b(value: Transform) -> None
```

<a id="unreal.RigVMFunction_MathTransformBinaryAggregateOp.result"></a>

#### result

```python
@property
def result() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_MathTransformBinaryAggregateOp"></a>