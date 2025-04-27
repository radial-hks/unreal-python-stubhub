## RigUnit_GetControlBool Objects

```python
class RigUnit_GetControlBool(RigUnit)
```

GetControlBool is used to retrieve a single Bool from a hierarchy.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_GetControlTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bool_value`` (bool):  [Read-Write] The current bool of the given bone - or identity in case it wasn't found.
- ``control`` (Name):  [Read-Write] The name of the Control to retrieve the bool for.

<a id="unreal.RigUnit_GetControlBool.__init__"></a>

#### __init__

```python
def __init__(control: Name = "None", bool_value: bool = False) -> None
```

<a id="unreal.RigUnit_GetControlBool.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to retrieve the bool for.

<a id="unreal.RigUnit_GetControlBool.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_GetControlBool.bool_value"></a>

#### bool_value

```python
@property
def bool_value() -> bool
```

(bool):  [Read-Only] The current bool of the given bone - or identity in case it wasn't found.

<a id="unreal.RigUnit_GetControlFloat"></a>