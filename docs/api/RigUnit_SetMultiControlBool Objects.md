## RigUnit_SetMultiControlBool Objects

```python
class RigUnit_SetMultiControlBool(RigUnitMutable)
```

SetMultiControlBool is used to perform a change in the hierarchy by setting multiple controls' bool value.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entries`` (Array[RigUnit_SetMultiControlBool_Entry]):  [Read-Write] The array of control-Bool pairs to be processed
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together

<a id="unreal.RigUnit_SetMultiControlBool.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             entries: Array[RigUnit_SetMultiControlBool_Entry] = []) -> None
```

<a id="unreal.RigUnit_SetMultiControlBool.entries"></a>

#### entries

```python
@property
def entries() -> Array[RigUnit_SetMultiControlBool_Entry]
```

(Array[RigUnit_SetMultiControlBool_Entry]):  [Read-Write] The array of control-Bool pairs to be processed

<a id="unreal.RigUnit_SetMultiControlBool.entries"></a>

#### entries

```python
@entries.setter
def entries(value: Array[RigUnit_SetMultiControlBool_Entry]) -> None
```

<a id="unreal.RigUnit_SetControlFloat"></a>