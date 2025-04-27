## RigUnit_GetFloatAnimationChannelFromItem Objects

```python
class RigUnit_GetFloatAnimationChannelFromItem(
        RigUnit_GetAnimationChannelFromItemBase)
```

Get Float Channel is used to retrieve a control's animation channel value

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ControlChannelFromItem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``initial`` (bool):  [Read-Write] If set to true the initial value will be returned
- ``item`` (RigElementKey):  [Read-Write] The item representing the channel
- ``value`` (float):  [Read-Write] The current value of the animation channel

<a id="unreal.RigUnit_GetFloatAnimationChannelFromItem.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"],
             initial: bool = False,
             value: float = 0.000000) -> None
```

<a id="unreal.RigUnit_GetFloatAnimationChannelFromItem.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Only] The current value of the animation channel

<a id="unreal.RigUnit_GetIntAnimationChannelFromItem"></a>