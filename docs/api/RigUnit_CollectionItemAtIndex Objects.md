## RigUnit_CollectionItemAtIndex Objects

```python
class RigUnit_CollectionItemAtIndex(RigUnit_CollectionBase)
```

Returns a single item within a collection by index

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Collection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collection`` (RigElementKeyCollection):  [Read-Write]
- ``index`` (int32):  [Read-Write]
- ``item`` (RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_CollectionItemAtIndex.__init__"></a>

#### __init__

```python
def __init__(collection: RigElementKeyCollection = [[]],
             index: int = 0,
             item: RigElementKey = [RigElementType.NONE, "None"]) -> None
```

<a id="unreal.RigUnit_CollectionItemAtIndex.collection"></a>

#### collection

```python
@property
def collection() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Write]

<a id="unreal.RigUnit_CollectionItemAtIndex.collection"></a>

#### collection

```python
@collection.setter
def collection(value: RigElementKeyCollection) -> None
```

<a id="unreal.RigUnit_CollectionItemAtIndex.index"></a>

#### index

```python
@property
def index() -> int
```

(int32):  [Read-Write]

<a id="unreal.RigUnit_CollectionItemAtIndex.index"></a>

#### index

```python
@index.setter
def index(value: int) -> None
```

<a id="unreal.RigUnit_CollectionItemAtIndex.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Only]

<a id="unreal.RigUnit_CollectionLoop"></a>