## RigUnit_SetAnimationChannelBaseFromItem Objects

```python
class RigUnit_SetAnimationChannelBaseFromItem(
        RigUnit_GetAnimationChannelFromItemBase)
```

Set Animation Channel is used to change a control's animation channel value

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ControlChannelFromItem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write]
- ``initial`` (bool):  [Read-Write] If set to true the initial value will be returned
- ``item`` (RigElementKey):  [Read-Write] The item representing the channel

<a id="unreal.RigUnit_SetAnimationChannelBaseFromItem.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"],
             initial: bool = False,
             execute_context: ControlRigExecuteContext = []) -> None
```

<a id="unreal.RigUnit_SetAnimationChannelBaseFromItem.execute_context"></a>

#### execute_context

```python
@property
def execute_context() -> ControlRigExecuteContext
```

(ControlRigExecuteContext):  [Read-Write]

<a id="unreal.RigUnit_SetAnimationChannelBaseFromItem.execute_context"></a>

#### execute_context

```python
@execute_context.setter
def execute_context(value: ControlRigExecuteContext) -> None
```

<a id="unreal.RigUnit_SetBoolAnimationChannelFromItem"></a>