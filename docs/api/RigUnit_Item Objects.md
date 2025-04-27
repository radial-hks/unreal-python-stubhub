## RigUnit_Item Objects

```python
class RigUnit_Item(RigUnit)
```

The Item node is used to share a specific item across the graph

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_BoneName.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``item`` (RigElementKey):  [Read-Write] The item

<a id="unreal.RigUnit_Item.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"]) -> None
```

<a id="unreal.RigUnit_Item.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] The item

<a id="unreal.RigUnit_Item.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_ItemArray"></a>