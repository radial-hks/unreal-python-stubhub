## MathRBFInterpolateQuatColor_Target Objects

```python
class MathRBFInterpolateQuatColor_Target(StructBase)
```

Math RBFInterpolate Quat Color Target

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathRBFInterpolate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``target`` (Quat):  [Read-Write]
- ``value`` (LinearColor):  [Read-Write]

<a id="unreal.MathRBFInterpolateQuatColor_Target.__init__"></a>

#### __init__

```python
def __init__(
        target: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
        value: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.MathRBFInterpolateQuatColor_Target.target"></a>

#### target

```python
@property
def target() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.MathRBFInterpolateQuatColor_Target.target"></a>

#### target

```python
@target.setter
def target(value: Quat) -> None
```

<a id="unreal.MathRBFInterpolateQuatColor_Target.value"></a>

#### value

```python
@property
def value() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.MathRBFInterpolateQuatColor_Target.value"></a>

#### value

```python
@value.setter
def value(value: LinearColor) -> None
```

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatColor"></a>