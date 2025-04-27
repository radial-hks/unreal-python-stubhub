## RigUnit_CollectionItems Objects

```python
class RigUnit_CollectionItems(RigUnit_CollectionBase)
```

Returns a collection provided a specific array of items.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Collection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_duplicates`` (bool):  [Read-Write]
- ``collection`` (RigElementKeyCollection):  [Read-Write]
- ``items`` (Array[RigElementKey]):  [Read-Write]

<a id="unreal.RigUnit_CollectionItems.__init__"></a>

#### __init__

```python
def __init__(items: Array[RigElementKey] = [],
             allow_duplicates: bool = False,
             collection: RigElementKeyCollection = [[]]) -> None
```

<a id="unreal.RigUnit_CollectionItems.items"></a>

#### items

```python
@property
def items() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Write]

<a id="unreal.RigUnit_CollectionItems.items"></a>

#### items

```python
@items.setter
def items(value: Array[RigElementKey]) -> None
```

<a id="unreal.RigUnit_CollectionItems.allow_duplicates"></a>

#### allow_duplicates

```python
@property
def allow_duplicates() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_CollectionItems.allow_duplicates"></a>

#### allow_duplicates

```python
@allow_duplicates.setter
def allow_duplicates(value: bool) -> None
```

<a id="unreal.RigUnit_CollectionItems.collection"></a>

#### collection

```python
@property
def collection() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Only]

<a id="unreal.RigUnit_CollectionGetItems"></a>