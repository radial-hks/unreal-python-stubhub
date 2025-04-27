## RigUnit_ItemArray Objects

```python
class RigUnit_ItemArray(RigUnit)
```

The Item Array node is used to share an array of items across the graph

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_BoneName.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``items`` (Array[RigElementKey]):  [Read-Write] The items

<a id="unreal.RigUnit_ItemArray.__init__"></a>

#### __init__

```python
def __init__(items: Array[RigElementKey] = []) -> None
```

<a id="unreal.RigUnit_ItemArray.items"></a>

#### items

```python
@property
def items() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Write] The items

<a id="unreal.RigUnit_ItemArray.items"></a>

#### items

```python
@items.setter
def items(value: Array[RigElementKey]) -> None
```

<a id="unreal.RigUnit_BoneName"></a>