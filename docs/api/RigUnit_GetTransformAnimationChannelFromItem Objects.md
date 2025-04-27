## RigUnit_GetTransformAnimationChannelFromItem Objects

```python
class RigUnit_GetTransformAnimationChannelFromItem(
        RigUnit_GetAnimationChannelFromItemBase)
```

Get Transform Channel is used to retrieve a control's animation channel value

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ControlChannelFromItem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``initial`` (bool):  [Read-Write] If set to true the initial value will be returned
- ``item`` (RigElementKey):  [Read-Write] The item representing the channel
- ``value`` (Transform):  [Read-Write] The current value of the animation channel

<a id="unreal.RigUnit_GetTransformAnimationChannelFromItem.__init__"></a>

#### __init__

```python
def __init__(
    item: RigElementKey = [RigElementType.NONE, "None"],
    initial: bool = False,
    value: Transform = [[0.000000, 0.000000, 0.000000],
                        [-0.000000, 0.000000, 0.000000],
                        [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_GetTransformAnimationChannelFromItem.value"></a>

#### value

```python
@property
def value() -> Transform
```

(Transform):  [Read-Only] The current value of the animation channel

<a id="unreal.RigUnit_SetAnimationChannelBaseFromItem"></a>