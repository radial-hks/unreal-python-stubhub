## RigUnit_SetCurveValue Objects

```python
class RigUnit_SetCurveValue(RigUnitMutable)
```

SetCurveValue is used to perform a change in the curve container by setting a single Curve value.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetCurveValue.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``curve`` (Name):  [Read-Write] The name of the Curve to set the Value for.
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``value`` (float):  [Read-Write] The value to set for the given Curve.

<a id="unreal.RigUnit_SetCurveValue.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             curve: Name = "None",
             value: float = 0.000000) -> None
```

<a id="unreal.RigUnit_SetCurveValue.curve"></a>

#### curve

```python
@property
def curve() -> Name
```

(Name):  [Read-Write] The name of the Curve to set the Value for.

<a id="unreal.RigUnit_SetCurveValue.curve"></a>

#### curve

```python
@curve.setter
def curve(value: Name) -> None
```

<a id="unreal.RigUnit_SetCurveValue.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write] The value to set for the given Curve.

<a id="unreal.RigUnit_SetCurveValue.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.RigUnit_SetRelativeBoneTransform"></a>