## RigUnit_GetControlDrivenList Objects

```python
class RigUnit_GetControlDrivenList(RigUnit)
```

GetControlDrivenList is used to retrieve the list of affected controls of an indirect control

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlDrivenList.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control`` (Name):  [Read-Write] The name of the Control to get the list for
- ``driven`` (Array[RigElementKey]):  [Read-Write] The list of affected controls

<a id="unreal.RigUnit_GetControlDrivenList.__init__"></a>

#### __init__

```python
def __init__(control: Name = "None",
             driven: Array[RigElementKey] = []) -> None
```

<a id="unreal.RigUnit_GetControlDrivenList.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to get the list for

<a id="unreal.RigUnit_GetControlDrivenList.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_GetControlDrivenList.driven"></a>

#### driven

```python
@property
def driven() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only] The list of affected controls

<a id="unreal.RigUnit_SetControlDrivenList"></a>