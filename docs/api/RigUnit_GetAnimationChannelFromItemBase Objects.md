## RigUnit_GetAnimationChannelFromItemBase Objects

```python
class RigUnit_GetAnimationChannelFromItemBase(RigUnit)
```

Get Animation Channel is used to retrieve a control's animation channel value

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ControlChannelFromItem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``initial`` (bool):  [Read-Write] If set to true the initial value will be returned
- ``item`` (RigElementKey):  [Read-Write] The item representing the channel

<a id="unreal.RigUnit_GetAnimationChannelFromItemBase.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"],
             initial: bool = False) -> None
```

<a id="unreal.RigUnit_GetAnimationChannelFromItemBase.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] The item representing the channel

<a id="unreal.RigUnit_GetAnimationChannelFromItemBase.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_GetAnimationChannelFromItemBase.initial"></a>

#### initial

```python
@property
def initial() -> bool
```

(bool):  [Read-Write] If set to true the initial value will be returned

<a id="unreal.RigUnit_GetAnimationChannelFromItemBase.initial"></a>

#### initial

```python
@initial.setter
def initial(value: bool) -> None
```

<a id="unreal.RigUnit_GetBoolAnimationChannelFromItem"></a>