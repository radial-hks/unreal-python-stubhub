## RigUnit_SetControlFloat Objects

```python
class RigUnit_SetControlFloat(RigUnitMutable)
```

SetControlFloat is used to perform a change in the hierarchy by setting a single control's float value.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control`` (Name):  [Read-Write] The name of the Control to set the transform for.
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``float_value`` (float):  [Read-Write] The transform value to set for the given Control.
- ``weight`` (float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_SetControlFloat.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             control: Name = "None",
             weight: float = 0.000000,
             float_value: float = 0.000000) -> None
```

<a id="unreal.RigUnit_SetControlFloat.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to set the transform for.

<a id="unreal.RigUnit_SetControlFloat.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_SetControlFloat.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_SetControlFloat.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_SetControlFloat.float_value"></a>

#### float_value

```python
@property
def float_value() -> float
```

(float):  [Read-Write] The transform value to set for the given Control.

<a id="unreal.RigUnit_SetControlFloat.float_value"></a>

#### float_value

```python
@float_value.setter
def float_value(value: float) -> None
```

<a id="unreal.RigUnit_SetMultiControlFloat_Entry"></a>