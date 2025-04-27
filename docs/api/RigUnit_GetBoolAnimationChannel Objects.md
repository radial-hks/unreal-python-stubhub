## RigUnit_GetBoolAnimationChannel Objects

```python
class RigUnit_GetBoolAnimationChannel(RigUnit_GetAnimationChannelBase)
```

Get Bool Channel is used to retrieve a control's animation channel value

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ControlChannel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel`` (Name):  [Read-Write] The name of the animation channel to retrieve the value for.
- ``control`` (Name):  [Read-Write] The name of the Control to retrieve the value for.
- ``initial`` (bool):  [Read-Write] If set to true the initial value will be returned
- ``value`` (bool):  [Read-Write] The current value of the animation channel

<a id="unreal.RigUnit_GetBoolAnimationChannel.__init__"></a>

#### __init__

```python
def __init__(control: Name = "None",
             channel: Name = "None",
             initial: bool = False,
             value: bool = False) -> None
```

<a id="unreal.RigUnit_GetBoolAnimationChannel.value"></a>

#### value

```python
@property
def value() -> bool
```

(bool):  [Read-Only] The current value of the animation channel

<a id="unreal.RigUnit_GetFloatAnimationChannel"></a>