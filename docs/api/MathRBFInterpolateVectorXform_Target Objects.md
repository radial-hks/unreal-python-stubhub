## MathRBFInterpolateVectorXform_Target Objects

```python
class MathRBFInterpolateVectorXform_Target(StructBase)
```

Math RBFInterpolate Vector Xform Target

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathRBFInterpolate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``target`` (Vector):  [Read-Write]
- ``value`` (Transform):  [Read-Write]

<a id="unreal.MathRBFInterpolateVectorXform_Target.__init__"></a>

#### __init__

```python
def __init__(
    target: Vector = [0.000000, 0.000000, 0.000000],
    value: Transform = [[0.000000, 0.000000, 0.000000],
                        [-0.000000, 0.000000, 0.000000],
                        [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.MathRBFInterpolateVectorXform_Target.target"></a>

#### target

```python
@property
def target() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.MathRBFInterpolateVectorXform_Target.target"></a>

#### target

```python
@target.setter
def target(value: Vector) -> None
```

<a id="unreal.MathRBFInterpolateVectorXform_Target.value"></a>

#### value

```python
@property
def value() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.MathRBFInterpolateVectorXform_Target.value"></a>

#### value

```python
@value.setter
def value(value: Transform) -> None
```

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorXform"></a>