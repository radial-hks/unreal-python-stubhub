## RigUnit_SetIntAnimationChannelFromItem Objects

```python
class RigUnit_SetIntAnimationChannelFromItem(
        RigUnit_SetAnimationChannelBaseFromItem)
```

Set Int Channel is used to set a control's animation channel value

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ControlChannelFromItem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write]
- ``initial`` (bool):  [Read-Write] If set to true the initial value will be returned
- ``item`` (RigElementKey):  [Read-Write] The item representing the channel
- ``value`` (int32):  [Read-Write] The new value of the animation channel

<a id="unreal.RigUnit_SetIntAnimationChannelFromItem.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"],
             initial: bool = False,
             execute_context: ControlRigExecuteContext = [],
             value: int = 0) -> None
```

<a id="unreal.RigUnit_SetIntAnimationChannelFromItem.value"></a>

#### value

```python
@property
def value() -> int
```

(int32):  [Read-Write] The new value of the animation channel

<a id="unreal.RigUnit_SetIntAnimationChannelFromItem.value"></a>

#### value

```python
@value.setter
def value(value: int) -> None
```

<a id="unreal.RigUnit_SetVector2DAnimationChannelFromItem"></a>