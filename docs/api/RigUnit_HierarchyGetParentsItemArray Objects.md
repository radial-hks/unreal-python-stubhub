## RigUnit_HierarchyGetParentsItemArray Objects

```python
class RigUnit_HierarchyGetParentsItemArray(RigUnit_HierarchyBase)
```

Returns the item's parents

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Hierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child`` (RigElementKey):  [Read-Write]
- ``default_parent`` (bool):  [Read-Write]
- ``include_child`` (bool):  [Read-Write]
- ``parents`` (Array[RigElementKey]):  [Read-Write]
- ``reverse`` (bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetParentsItemArray.__init__"></a>

#### __init__

```python
def __init__(child: RigElementKey = [RigElementType.NONE, "None"],
             include_child: bool = False,
             reverse: bool = False,
             default_parent: bool = False,
             parents: Array[RigElementKey] = []) -> None
```

<a id="unreal.RigUnit_HierarchyGetParentsItemArray.child"></a>

#### child

```python
@property
def child() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetParentsItemArray.child"></a>

#### child

```python
@child.setter
def child(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_HierarchyGetParentsItemArray.include_child"></a>

#### include_child

```python
@property
def include_child() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetParentsItemArray.include_child"></a>

#### include_child

```python
@include_child.setter
def include_child(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyGetParentsItemArray.reverse"></a>

#### reverse

```python
@property
def reverse() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetParentsItemArray.reverse"></a>

#### reverse

```python
@reverse.setter
def reverse(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyGetParentsItemArray.default_parent"></a>

#### default_parent

```python
@property
def default_parent() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetParentsItemArray.default_parent"></a>

#### default_parent

```python
@default_parent.setter
def default_parent(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyGetParentsItemArray.parents"></a>

#### parents

```python
@property
def parents() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only]

<a id="unreal.RigUnit_HierarchyGetChildren"></a>