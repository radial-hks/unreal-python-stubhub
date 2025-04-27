## RigUnit_SetAnimationChannelBase Objects

```python
class RigUnit_SetAnimationChannelBase(RigUnit_GetAnimationChannelBase)
```

Set Animation Channel is used to change a control's animation channel value

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ControlChannel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel`` (Name):  [Read-Write] The name of the animation channel to retrieve the value for.
- ``control`` (Name):  [Read-Write] The name of the Control to retrieve the value for.
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write]
- ``initial`` (bool):  [Read-Write] If set to true the initial value will be returned

<a id="unreal.RigUnit_SetAnimationChannelBase.__init__"></a>

#### __init__

```python
def __init__(control: Name = "None",
             channel: Name = "None",
             initial: bool = False,
             execute_context: ControlRigExecuteContext = []) -> None
```

<a id="unreal.RigUnit_SetAnimationChannelBase.execute_context"></a>

#### execute_context

```python
@property
def execute_context() -> ControlRigExecuteContext
```

(ControlRigExecuteContext):  [Read-Write]

<a id="unreal.RigUnit_SetAnimationChannelBase.execute_context"></a>

#### execute_context

```python
@execute_context.setter
def execute_context(value: ControlRigExecuteContext) -> None
```

<a id="unreal.RigUnit_SetBoolAnimationChannel"></a>