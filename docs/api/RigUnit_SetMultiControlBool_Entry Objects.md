## RigUnit_SetMultiControlBool_Entry Objects

```python
class RigUnit_SetMultiControlBool_Entry(StructBase)
```

Rig Unit Set Multi Control Bool Entry

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bool_value`` (bool):  [Read-Write] The bool value to set for the given Control.
- ``control`` (Name):  [Read-Write] The name of the Control to set the transform for.

<a id="unreal.RigUnit_SetMultiControlBool_Entry.__init__"></a>

#### __init__

```python
def __init__(control: Name = "None", bool_value: bool = False) -> None
```

<a id="unreal.RigUnit_SetMultiControlBool_Entry.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to set the transform for.

<a id="unreal.RigUnit_SetMultiControlBool_Entry.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_SetMultiControlBool_Entry.bool_value"></a>

#### bool_value

```python
@property
def bool_value() -> bool
```

(bool):  [Read-Write] The bool value to set for the given Control.

<a id="unreal.RigUnit_SetMultiControlBool_Entry.bool_value"></a>

#### bool_value

```python
@bool_value.setter
def bool_value(value: bool) -> None
```

<a id="unreal.RigUnit_SetMultiControlBool"></a>