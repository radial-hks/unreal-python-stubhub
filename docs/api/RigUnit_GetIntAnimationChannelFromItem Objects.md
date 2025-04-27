## RigUnit_GetIntAnimationChannelFromItem Objects

```python
class RigUnit_GetIntAnimationChannelFromItem(
        RigUnit_GetAnimationChannelFromItemBase)
```

Get Int Channel is used to retrieve a control's animation channel value

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ControlChannelFromItem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``initial`` (bool):  [Read-Write] If set to true the initial value will be returned
- ``item`` (RigElementKey):  [Read-Write] The item representing the channel
- ``value`` (int32):  [Read-Write] The current value of the animation channel

<a id="unreal.RigUnit_GetIntAnimationChannelFromItem.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"],
             initial: bool = False,
             value: int = 0) -> None
```

<a id="unreal.RigUnit_GetIntAnimationChannelFromItem.value"></a>

#### value

```python
@property
def value() -> int
```

(int32):  [Read-Only] The current value of the animation channel

<a id="unreal.RigUnit_GetVector2DAnimationChannelFromItem"></a>