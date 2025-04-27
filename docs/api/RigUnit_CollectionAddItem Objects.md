## RigUnit_CollectionAddItem Objects

```python
class RigUnit_CollectionAddItem(RigUnit_CollectionBase)
```

Adds an element to an existing collection

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Collection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collection`` (RigElementKeyCollection):  [Read-Write]
- ``item`` (RigElementKey):  [Read-Write]
- ``result`` (RigElementKeyCollection):  [Read-Write]

<a id="unreal.RigUnit_CollectionAddItem.__init__"></a>

#### __init__

```python
def __init__(collection: RigElementKeyCollection = [[]],
             item: RigElementKey = [RigElementType.NONE, "None"],
             result: RigElementKeyCollection = [[]]) -> None
```

<a id="unreal.RigUnit_CollectionAddItem.collection"></a>

#### collection

```python
@property
def collection() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Write]

<a id="unreal.RigUnit_CollectionAddItem.collection"></a>

#### collection

```python
@collection.setter
def collection(value: RigElementKeyCollection) -> None
```

<a id="unreal.RigUnit_CollectionAddItem.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_CollectionAddItem.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_CollectionAddItem.result"></a>

#### result

```python
@property
def result() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Only]

<a id="unreal.RigUnit_DynamicHierarchyBase"></a>