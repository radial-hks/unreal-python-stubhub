## RigUnit_SetMultiControlFloat_Entry Objects

```python
class RigUnit_SetMultiControlFloat_Entry(StructBase)
```

Rig Unit Set Multi Control Float Entry

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control`` (Name):  [Read-Write] The name of the Control to set the transform for.
- ``float_value`` (float):  [Read-Write] The transform value to set for the given Control.

<a id="unreal.RigUnit_SetMultiControlFloat_Entry.__init__"></a>

#### __init__

```python
def __init__(control: Name = "None", float_value: float = 0.000000) -> None
```

<a id="unreal.RigUnit_SetMultiControlFloat_Entry.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to set the transform for.

<a id="unreal.RigUnit_SetMultiControlFloat_Entry.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_SetMultiControlFloat_Entry.float_value"></a>

#### float_value

```python
@property
def float_value() -> float
```

(float):  [Read-Write] The transform value to set for the given Control.

<a id="unreal.RigUnit_SetMultiControlFloat_Entry.float_value"></a>

#### float_value

```python
@float_value.setter
def float_value(value: float) -> None
```

<a id="unreal.RigUnit_SetMultiControlFloat"></a>