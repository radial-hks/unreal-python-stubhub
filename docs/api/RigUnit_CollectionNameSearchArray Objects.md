## RigUnit_CollectionNameSearchArray Objects

```python
class RigUnit_CollectionNameSearchArray(RigUnit_CollectionBase)
```

Creates an item array based on a name search.
The name search is case sensitive.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Collection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``items`` (Array[RigElementKey]):  [Read-Write]
- ``partial_name`` (Name):  [Read-Write]
- ``type_to_search`` (RigElementType):  [Read-Write]

<a id="unreal.RigUnit_CollectionNameSearchArray.__init__"></a>

#### __init__

```python
def __init__(partial_name: Name = "None",
             type_to_search: RigElementType = RigElementType.NONE,
             items: Array[RigElementKey] = []) -> None
```

<a id="unreal.RigUnit_CollectionNameSearchArray.partial_name"></a>

#### partial_name

```python
@property
def partial_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigUnit_CollectionNameSearchArray.partial_name"></a>

#### partial_name

```python
@partial_name.setter
def partial_name(value: Name) -> None
```

<a id="unreal.RigUnit_CollectionNameSearchArray.type_to_search"></a>

#### type_to_search

```python
@property
def type_to_search() -> RigElementType
```

(RigElementType):  [Read-Write]

<a id="unreal.RigUnit_CollectionNameSearchArray.type_to_search"></a>

#### type_to_search

```python
@type_to_search.setter
def type_to_search(value: RigElementType) -> None
```

<a id="unreal.RigUnit_CollectionNameSearchArray.items"></a>

#### items

```python
@property
def items() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only]

<a id="unreal.RigUnit_CollectionChildren"></a>