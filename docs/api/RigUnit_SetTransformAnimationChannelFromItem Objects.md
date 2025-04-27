## RigUnit_SetTransformAnimationChannelFromItem Objects

```python
class RigUnit_SetTransformAnimationChannelFromItem(
        RigUnit_SetAnimationChannelBaseFromItem)
```

Set Transform Channel is used to set a control's animation channel value

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ControlChannelFromItem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write]
- ``initial`` (bool):  [Read-Write] If set to true the initial value will be returned
- ``item`` (RigElementKey):  [Read-Write] The item representing the channel
- ``value`` (Transform):  [Read-Write] The new value of the animation channel

<a id="unreal.RigUnit_SetTransformAnimationChannelFromItem.__init__"></a>

#### __init__

```python
def __init__(
    item: RigElementKey = [RigElementType.NONE, "None"],
    initial: bool = False,
    execute_context: ControlRigExecuteContext = [],
    value: Transform = [[0.000000, 0.000000, 0.000000],
                        [-0.000000, 0.000000, 0.000000],
                        [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_SetTransformAnimationChannelFromItem.value"></a>

#### value

```python
@property
def value() -> Transform
```

(Transform):  [Read-Write] The new value of the animation channel

<a id="unreal.RigUnit_SetTransformAnimationChannelFromItem.value"></a>

#### value

```python
@value.setter
def value(value: Transform) -> None
```

<a id="unreal.RigUnit_CurveExists"></a>