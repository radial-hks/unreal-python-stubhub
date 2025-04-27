## RigUnit_CollectionReverse Objects

```python
class RigUnit_CollectionReverse(RigUnit_CollectionBase)
```

Returns the collection in reverse order

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Collection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collection`` (RigElementKeyCollection):  [Read-Write]
- ``reversed`` (RigElementKeyCollection):  [Read-Write]

<a id="unreal.RigUnit_CollectionReverse.__init__"></a>

#### __init__

```python
def __init__(collection: RigElementKeyCollection = [[]],
             reversed: RigElementKeyCollection = [[]]) -> None
```

<a id="unreal.RigUnit_CollectionReverse.collection"></a>

#### collection

```python
@property
def collection() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Write]

<a id="unreal.RigUnit_CollectionReverse.collection"></a>

#### collection

```python
@collection.setter
def collection(value: RigElementKeyCollection) -> None
```

<a id="unreal.RigUnit_CollectionReverse.reversed"></a>

#### reversed

```python
@property
def reversed() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Only]

<a id="unreal.RigUnit_CollectionCount"></a>