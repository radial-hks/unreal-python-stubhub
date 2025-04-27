## RigUnit_CollectionGetAll Objects

```python
class RigUnit_CollectionGetAll(RigUnit_CollectionBase)
```

Creates an item array for all elements given the filter.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Collection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``items`` (Array[RigElementKey]):  [Read-Write]
- ``type_to_search`` (RigElementType):  [Read-Write]

<a id="unreal.RigUnit_CollectionGetAll.__init__"></a>

#### __init__

```python
def __init__(type_to_search: RigElementType = RigElementType.NONE,
             items: Array[RigElementKey] = []) -> None
```

<a id="unreal.RigUnit_CollectionGetAll.type_to_search"></a>

#### type_to_search

```python
@property
def type_to_search() -> RigElementType
```

(RigElementType):  [Read-Write]

<a id="unreal.RigUnit_CollectionGetAll.type_to_search"></a>

#### type_to_search

```python
@type_to_search.setter
def type_to_search(value: RigElementType) -> None
```

<a id="unreal.RigUnit_CollectionGetAll.items"></a>

#### items

```python
@property
def items() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only]

<a id="unreal.RigUnit_CollectionReplaceItems"></a>