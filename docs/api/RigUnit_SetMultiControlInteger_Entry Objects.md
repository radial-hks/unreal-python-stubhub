## RigUnit_SetMultiControlInteger_Entry Objects

```python
class RigUnit_SetMultiControlInteger_Entry(StructBase)
```

Rig Unit Set Multi Control Integer Entry

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control`` (Name):  [Read-Write] The name of the Control to set the transform for.
- ``integer_value`` (int32):  [Read-Write] The transform value to set for the given Control.

<a id="unreal.RigUnit_SetMultiControlInteger_Entry.__init__"></a>

#### __init__

```python
def __init__(control: Name = "None", integer_value: int = 0) -> None
```

<a id="unreal.RigUnit_SetMultiControlInteger_Entry.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to set the transform for.

<a id="unreal.RigUnit_SetMultiControlInteger_Entry.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_SetMultiControlInteger_Entry.integer_value"></a>

#### integer_value

```python
@property
def integer_value() -> int
```

(int32):  [Read-Write] The transform value to set for the given Control.

<a id="unreal.RigUnit_SetMultiControlInteger_Entry.integer_value"></a>

#### integer_value

```python
@integer_value.setter
def integer_value(value: int) -> None
```

<a id="unreal.RigUnit_SetMultiControlInteger"></a>