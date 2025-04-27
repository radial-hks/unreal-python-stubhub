## RigUnit_SetControlBool Objects

```python
class RigUnit_SetControlBool(RigUnitMutable)
```

SetControlBool is used to perform a change in the hierarchy by setting a single control's bool value.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bool_value`` (bool):  [Read-Write] The bool value to set for the given Control.
- ``control`` (Name):  [Read-Write] The name of the Control to set the bool for.
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together

<a id="unreal.RigUnit_SetControlBool.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             control: Name = "None",
             bool_value: bool = False) -> None
```

<a id="unreal.RigUnit_SetControlBool.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to set the bool for.

<a id="unreal.RigUnit_SetControlBool.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_SetControlBool.bool_value"></a>

#### bool_value

```python
@property
def bool_value() -> bool
```

(bool):  [Read-Write] The bool value to set for the given Control.

<a id="unreal.RigUnit_SetControlBool.bool_value"></a>

#### bool_value

```python
@bool_value.setter
def bool_value(value: bool) -> None
```

<a id="unreal.RigUnit_SetMultiControlBool_Entry"></a>