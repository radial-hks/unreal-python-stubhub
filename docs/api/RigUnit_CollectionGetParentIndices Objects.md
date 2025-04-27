## RigUnit_CollectionGetParentIndices Objects

```python
class RigUnit_CollectionGetParentIndices(RigUnit_CollectionBase)
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

- ``collection`` (RigElementKeyCollection):  [Read-Write]
- ``parent_indices`` (Array[int32]):  [Read-Write]

<a id="unreal.RigUnit_CollectionGetParentIndices.__init__"></a>

#### __init__

```python
def __init__(collection: RigElementKeyCollection = [[]],
             parent_indices: Array[int] = []) -> None
```

<a id="unreal.RigUnit_CollectionGetParentIndices.collection"></a>

#### collection

```python
@property
def collection() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Write]

<a id="unreal.RigUnit_CollectionGetParentIndices.collection"></a>

#### collection

```python
@collection.setter
def collection(value: RigElementKeyCollection) -> None
```

<a id="unreal.RigUnit_CollectionGetParentIndices.parent_indices"></a>

#### parent_indices

```python
@property
def parent_indices() -> Array[int]
```

(Array[int32]):  [Read-Only]

<a id="unreal.RigUnit_CollectionGetParentIndicesItemArray"></a>