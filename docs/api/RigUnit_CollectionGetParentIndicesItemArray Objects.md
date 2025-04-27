## RigUnit_CollectionGetParentIndicesItemArray Objects

```python
class RigUnit_CollectionGetParentIndicesItemArray(RigUnit_CollectionBase)
```

Returns an array of relative parent indices for each item. Several options here
a) If an item has multiple parents the major parent (based on the weights) will be returned.
b) If an item has a parent that's not part of the collection INDEX_NONE will be returned.
c) If an item has a parent that's not part of the collection, but a grand parent is we'll use that index instead.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Collection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``items`` (Array[RigElementKey]):  [Read-Write]
- ``parent_indices`` (Array[int32]):  [Read-Write]

<a id="unreal.RigUnit_CollectionGetParentIndicesItemArray.__init__"></a>

#### __init__

```python
def __init__(items: Array[RigElementKey] = [],
             parent_indices: Array[int] = []) -> None
```

<a id="unreal.RigUnit_CollectionGetParentIndicesItemArray.items"></a>

#### items

```python
@property
def items() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Write]

<a id="unreal.RigUnit_CollectionGetParentIndicesItemArray.items"></a>

#### items

```python
@items.setter
def items(value: Array[RigElementKey]) -> None
```

<a id="unreal.RigUnit_CollectionGetParentIndicesItemArray.parent_indices"></a>

#### parent_indices

```python
@property
def parent_indices() -> Array[int]
```

(Array[int32]):  [Read-Only]

<a id="unreal.RigUnit_CollectionUnion"></a>