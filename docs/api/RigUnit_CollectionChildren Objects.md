## RigUnit_CollectionChildren Objects

```python
class RigUnit_CollectionChildren(RigUnit_CollectionBase)
```

Creates a collection based on the direct or recursive children
of a provided parent item. Returns an empty collection for an invalid parent item.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Collection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collection`` (RigElementKeyCollection):  [Read-Write]
- ``include_parent`` (bool):  [Read-Write]
- ``parent`` (RigElementKey):  [Read-Write]
- ``recursive`` (bool):  [Read-Write]
- ``type_to_search`` (RigElementType):  [Read-Write]

<a id="unreal.RigUnit_CollectionChildren.__init__"></a>

#### __init__

```python
def __init__(parent: RigElementKey = [RigElementType.NONE, "None"],
             include_parent: bool = False,
             recursive: bool = False,
             type_to_search: RigElementType = RigElementType.NONE,
             collection: RigElementKeyCollection = [[]]) -> None
```

<a id="unreal.RigUnit_CollectionChildren.parent"></a>

#### parent

```python
@property
def parent() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_CollectionChildren.parent"></a>

#### parent

```python
@parent.setter
def parent(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_CollectionChildren.include_parent"></a>

#### include_parent

```python
@property
def include_parent() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_CollectionChildren.include_parent"></a>

#### include_parent

```python
@include_parent.setter
def include_parent(value: bool) -> None
```

<a id="unreal.RigUnit_CollectionChildren.recursive"></a>

#### recursive

```python
@property
def recursive() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_CollectionChildren.recursive"></a>

#### recursive

```python
@recursive.setter
def recursive(value: bool) -> None
```

<a id="unreal.RigUnit_CollectionChildren.type_to_search"></a>

#### type_to_search

```python
@property
def type_to_search() -> RigElementType
```

(RigElementType):  [Read-Write]

<a id="unreal.RigUnit_CollectionChildren.type_to_search"></a>

#### type_to_search

```python
@type_to_search.setter
def type_to_search(value: RigElementType) -> None
```

<a id="unreal.RigUnit_CollectionChildren.collection"></a>

#### collection

```python
@property
def collection() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Only]

<a id="unreal.RigUnit_CollectionChildrenArray"></a>