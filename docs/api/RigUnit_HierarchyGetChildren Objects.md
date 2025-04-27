## RigUnit_HierarchyGetChildren Objects

```python
class RigUnit_HierarchyGetChildren(RigUnit_HierarchyBase)
```

Returns the item's children

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Hierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``children`` (RigElementKeyCollection):  [Read-Write]
- ``include_parent`` (bool):  [Read-Write]
- ``parent`` (RigElementKey):  [Read-Write]
- ``recursive`` (bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetChildren.__init__"></a>

#### __init__

```python
def __init__(parent: RigElementKey = [RigElementType.NONE, "None"],
             include_parent: bool = False,
             recursive: bool = False,
             children: RigElementKeyCollection = [[]]) -> None
```

<a id="unreal.RigUnit_HierarchyGetChildren.parent"></a>

#### parent

```python
@property
def parent() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetChildren.parent"></a>

#### parent

```python
@parent.setter
def parent(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_HierarchyGetChildren.include_parent"></a>

#### include_parent

```python
@property
def include_parent() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetChildren.include_parent"></a>

#### include_parent

```python
@include_parent.setter
def include_parent(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyGetChildren.recursive"></a>

#### recursive

```python
@property
def recursive() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetChildren.recursive"></a>

#### recursive

```python
@recursive.setter
def recursive(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyGetChildren.children"></a>

#### children

```python
@property
def children() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Only]

<a id="unreal.RigUnit_HierarchyGetSiblings"></a>