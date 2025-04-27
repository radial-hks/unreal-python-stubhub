## RigUnit_SetBoolAnimationChannel Objects

```python
class RigUnit_SetBoolAnimationChannel(RigUnit_SetAnimationChannelBase)
```

Set Bool Channel is used to set a control's animation channel value

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ControlChannel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel`` (Name):  [Read-Write] The name of the animation channel to retrieve the value for.
- ``control`` (Name):  [Read-Write] The name of the Control to retrieve the value for.
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write]
- ``initial`` (bool):  [Read-Write] If set to true the initial value will be returned
- ``value`` (bool):  [Read-Write] The new value of the animation channel

<a id="unreal.RigUnit_SetBoolAnimationChannel.__init__"></a>

#### __init__

```python
def __init__(control: Name = "None",
             channel: Name = "None",
             initial: bool = False,
             execute_context: ControlRigExecuteContext = [],
             value: bool = False) -> None
```

<a id="unreal.RigUnit_SetBoolAnimationChannel.value"></a>

#### value

```python
@property
def value() -> bool
```

(bool):  [Read-Write] The new value of the animation channel

<a id="unreal.RigUnit_SetBoolAnimationChannel.value"></a>

#### value

```python
@value.setter
def value(value: bool) -> None
```

<a id="unreal.RigUnit_SetFloatAnimationChannel"></a>