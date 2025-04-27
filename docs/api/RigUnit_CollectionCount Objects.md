## RigUnit_CollectionCount Objects

```python
class RigUnit_CollectionCount(RigUnit_CollectionBase)
```

Returns the number of elements in a collection

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Collection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collection`` (RigElementKeyCollection):  [Read-Write]
- ``count`` (int32):  [Read-Write]

<a id="unreal.RigUnit_CollectionCount.__init__"></a>

#### __init__

```python
def __init__(collection: RigElementKeyCollection = [[]],
             count: int = 0) -> None
```

<a id="unreal.RigUnit_CollectionCount.collection"></a>

#### collection

```python
@property
def collection() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Write]

<a id="unreal.RigUnit_CollectionCount.collection"></a>

#### collection

```python
@collection.setter
def collection(value: RigElementKeyCollection) -> None
```

<a id="unreal.RigUnit_CollectionCount.count"></a>

#### count

```python
@property
def count() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigUnit_CollectionItemAtIndex"></a>