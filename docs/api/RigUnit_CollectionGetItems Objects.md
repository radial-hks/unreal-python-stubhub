## RigUnit_CollectionGetItems Objects

```python
class RigUnit_CollectionGetItems(RigUnit_CollectionBase)
```

Returns an array of items provided a collection

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Collection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collection`` (RigElementKeyCollection):  [Read-Write]
- ``items`` (Array[RigElementKey]):  [Read-Write]

<a id="unreal.RigUnit_CollectionGetItems.__init__"></a>

#### __init__

```python
def __init__(collection: RigElementKeyCollection = [[]],
             items: Array[RigElementKey] = []) -> None
```

<a id="unreal.RigUnit_CollectionGetItems.collection"></a>

#### collection

```python
@property
def collection() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Write]

<a id="unreal.RigUnit_CollectionGetItems.collection"></a>

#### collection

```python
@collection.setter
def collection(value: RigElementKeyCollection) -> None
```

<a id="unreal.RigUnit_CollectionGetItems.items"></a>

#### items

```python
@property
def items() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only]

<a id="unreal.RigUnit_CollectionGetParentIndices"></a>