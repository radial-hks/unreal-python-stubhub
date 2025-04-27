## RigUnit_SetControlDrivenList Objects

```python
class RigUnit_SetControlDrivenList(RigUnitMutable)
```

SetControlDrivenList is used to change the list of affected controls of an indirect control

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlDrivenList.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control`` (Name):  [Read-Write] The name of the Control to set the list for
- ``driven`` (Array[RigElementKey]):  [Read-Write] The list of affected controls
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together

<a id="unreal.RigUnit_SetControlDrivenList.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             control: Name = "None",
             driven: Array[RigElementKey] = []) -> None
```

<a id="unreal.RigUnit_SetControlDrivenList.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to set the list for

<a id="unreal.RigUnit_SetControlDrivenList.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_SetControlDrivenList.driven"></a>

#### driven

```python
@property
def driven() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Write] The list of affected controls

<a id="unreal.RigUnit_SetControlDrivenList.driven"></a>

#### driven

```python
@driven.setter
def driven(value: Array[RigElementKey]) -> None
```

<a id="unreal.RigUnit_SetControlOffset"></a>