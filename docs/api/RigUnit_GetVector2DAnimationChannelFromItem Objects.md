## RigUnit_GetVector2DAnimationChannelFromItem Objects

```python
class RigUnit_GetVector2DAnimationChannelFromItem(
        RigUnit_GetAnimationChannelFromItemBase)
```

Get Vector2D Channel is used to retrieve a control's animation channel value

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ControlChannelFromItem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``initial`` (bool):  [Read-Write] If set to true the initial value will be returned
- ``item`` (RigElementKey):  [Read-Write] The item representing the channel
- ``value`` (Vector2D):  [Read-Write] The current value of the animation channel

<a id="unreal.RigUnit_GetVector2DAnimationChannelFromItem.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"],
             initial: bool = False,
             value: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_GetVector2DAnimationChannelFromItem.value"></a>

#### value

```python
@property
def value() -> Vector2D
```

(Vector2D):  [Read-Only] The current value of the animation channel

<a id="unreal.RigUnit_GetVectorAnimationChannelFromItem"></a>