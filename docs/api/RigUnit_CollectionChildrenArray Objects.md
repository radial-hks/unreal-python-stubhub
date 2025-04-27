## RigUnit_CollectionChildrenArray Objects

```python
class RigUnit_CollectionChildrenArray(RigUnit_CollectionBase)
```

Creates an item array based on the direct or recursive children
of a provided parent item. Returns an empty array for an invalid parent item.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Collection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_children`` (bool):  [Read-Write] When true, it will return all children, regardless of whether the parent is active or not.
  When false, will return only the children which are influenced by this parent
- ``include_parent`` (bool):  [Read-Write]
- ``items`` (Array[RigElementKey]):  [Read-Write]
- ``parent`` (RigElementKey):  [Read-Write]
- ``recursive`` (bool):  [Read-Write]
- ``type_to_search`` (RigElementType):  [Read-Write]

<a id="unreal.RigUnit_CollectionChildrenArray.__init__"></a>

#### __init__

```python
def __init__(parent: RigElementKey = [RigElementType.NONE, "None"],
             include_parent: bool = False,
             recursive: bool = False,
             default_children: bool = False,
             type_to_search: RigElementType = RigElementType.NONE,
             items: Array[RigElementKey] = []) -> None
```

<a id="unreal.RigUnit_CollectionChildrenArray.parent"></a>

#### parent

```python
@property
def parent() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_CollectionChildrenArray.parent"></a>

#### parent

```python
@parent.setter
def parent(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_CollectionChildrenArray.include_parent"></a>

#### include_parent

```python
@property
def include_parent() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_CollectionChildrenArray.include_parent"></a>

#### include_parent

```python
@include_parent.setter
def include_parent(value: bool) -> None
```

<a id="unreal.RigUnit_CollectionChildrenArray.recursive"></a>

#### recursive

```python
@property
def recursive() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_CollectionChildrenArray.recursive"></a>

#### recursive

```python
@recursive.setter
def recursive(value: bool) -> None
```

<a id="unreal.RigUnit_CollectionChildrenArray.default_children"></a>

#### default_children

```python
@property
def default_children() -> bool
```

(bool):  [Read-Write] When true, it will return all children, regardless of whether the parent is active or not.
When false, will return only the children which are influenced by this parent

<a id="unreal.RigUnit_CollectionChildrenArray.default_children"></a>

#### default_children

```python
@default_children.setter
def default_children(value: bool) -> None
```

<a id="unreal.RigUnit_CollectionChildrenArray.type_to_search"></a>

#### type_to_search

```python
@property
def type_to_search() -> RigElementType
```

(RigElementType):  [Read-Write]

<a id="unreal.RigUnit_CollectionChildrenArray.type_to_search"></a>

#### type_to_search

```python
@type_to_search.setter
def type_to_search(value: RigElementType) -> None
```

<a id="unreal.RigUnit_CollectionChildrenArray.items"></a>

#### items

```python
@property
def items() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only]

<a id="unreal.RigUnit_CollectionGetAll"></a>