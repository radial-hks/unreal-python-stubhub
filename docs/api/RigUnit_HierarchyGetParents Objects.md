## RigUnit_HierarchyGetParents Objects

```python
class RigUnit_HierarchyGetParents(RigUnit_HierarchyBase)
```

Returns the item's parents

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Hierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child`` (RigElementKey):  [Read-Write]
- ``include_child`` (bool):  [Read-Write]
- ``parents`` (RigElementKeyCollection):  [Read-Write]
- ``reverse`` (bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetParents.__init__"></a>

#### __init__

```python
def __init__(child: RigElementKey = [RigElementType.NONE, "None"],
             include_child: bool = False,
             reverse: bool = False,
             parents: RigElementKeyCollection = [[]]) -> None
```

<a id="unreal.RigUnit_HierarchyGetParents.child"></a>

#### child

```python
@property
def child() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetParents.child"></a>

#### child

```python
@child.setter
def child(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_HierarchyGetParents.include_child"></a>

#### include_child

```python
@property
def include_child() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetParents.include_child"></a>

#### include_child

```python
@include_child.setter
def include_child(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyGetParents.reverse"></a>

#### reverse

```python
@property
def reverse() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetParents.reverse"></a>

#### reverse

```python
@reverse.setter
def reverse(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyGetParents.parents"></a>

#### parents

```python
@property
def parents() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Only]

<a id="unreal.RigUnit_HierarchyGetParentsItemArray"></a>