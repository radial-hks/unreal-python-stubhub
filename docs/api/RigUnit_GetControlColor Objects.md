## RigUnit_GetControlColor Objects

```python
class RigUnit_GetControlColor(RigUnit)
```

GetControlColor is used to retrieve the color of control

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlColor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write] The color of the control
- ``control`` (Name):  [Read-Write] The name of the Control to get the color for.

<a id="unreal.RigUnit_GetControlColor.__init__"></a>

#### __init__

```python
def __init__(
        control: Name = "None",
        color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_GetControlColor.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to get the color for.

<a id="unreal.RigUnit_GetControlColor.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_GetControlColor.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Only] The color of the control

<a id="unreal.RigUnit_SetControlColor"></a>