## RigUnit_CollectionNameSearch Objects

```python
class RigUnit_CollectionNameSearch(RigUnit_CollectionBase)
```

Creates a collection based on a name search.
The name search is case sensitive.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Collection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collection`` (RigElementKeyCollection):  [Read-Write]
- ``partial_name`` (Name):  [Read-Write]
- ``type_to_search`` (RigElementType):  [Read-Write]

<a id="unreal.RigUnit_CollectionNameSearch.__init__"></a>

#### __init__

```python
def __init__(partial_name: Name = "None",
             type_to_search: RigElementType = RigElementType.NONE,
             collection: RigElementKeyCollection = [[]]) -> None
```

<a id="unreal.RigUnit_CollectionNameSearch.partial_name"></a>

#### partial_name

```python
@property
def partial_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigUnit_CollectionNameSearch.partial_name"></a>

#### partial_name

```python
@partial_name.setter
def partial_name(value: Name) -> None
```

<a id="unreal.RigUnit_CollectionNameSearch.type_to_search"></a>

#### type_to_search

```python
@property
def type_to_search() -> RigElementType
```

(RigElementType):  [Read-Write]

<a id="unreal.RigUnit_CollectionNameSearch.type_to_search"></a>

#### type_to_search

```python
@type_to_search.setter
def type_to_search(value: RigElementType) -> None
```

<a id="unreal.RigUnit_CollectionNameSearch.collection"></a>

#### collection

```python
@property
def collection() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Only]

<a id="unreal.RigUnit_CollectionNameSearchArray"></a>