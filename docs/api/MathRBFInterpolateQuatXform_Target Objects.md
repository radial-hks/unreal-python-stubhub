## MathRBFInterpolateQuatXform_Target Objects

```python
class MathRBFInterpolateQuatXform_Target(StructBase)
```

Math RBFInterpolate Quat Xform Target

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathRBFInterpolate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``target`` (Quat):  [Read-Write]
- ``value`` (Transform):  [Read-Write]

<a id="unreal.MathRBFInterpolateQuatXform_Target.__init__"></a>

#### __init__

```python
def __init__(
    target: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
    value: Transform = [[0.000000, 0.000000, 0.000000],
                        [-0.000000, 0.000000, 0.000000],
                        [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.MathRBFInterpolateQuatXform_Target.target"></a>

#### target

```python
@property
def target() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.MathRBFInterpolateQuatXform_Target.target"></a>

#### target

```python
@target.setter
def target(value: Quat) -> None
```

<a id="unreal.MathRBFInterpolateQuatXform_Target.value"></a>

#### value

```python
@property
def value() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.MathRBFInterpolateQuatXform_Target.value"></a>

#### value

```python
@value.setter
def value(value: Transform) -> None
```

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatXform"></a>