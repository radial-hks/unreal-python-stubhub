## RigUnit_UnsetCurveValue Objects

```python
class RigUnit_UnsetCurveValue(RigUnitMutable)
```

UnsetCurveValue is used to perform a change in the curve container by invalidating a single Curve value.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_UnsetCurveValue.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``curve`` (Name):  [Read-Write] The name of the Curve to set the Value for.
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together

<a id="unreal.RigUnit_UnsetCurveValue.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             curve: Name = "None") -> None
```

<a id="unreal.RigUnit_UnsetCurveValue.curve"></a>

#### curve

```python
@property
def curve() -> Name
```

(Name):  [Read-Write] The name of the Curve to set the Value for.

<a id="unreal.RigUnit_UnsetCurveValue.curve"></a>

#### curve

```python
@curve.setter
def curve(value: Name) -> None
```

<a id="unreal.RigUnit_ToWorldSpace_Transform"></a>