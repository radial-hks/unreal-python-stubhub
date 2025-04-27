## RigUnit_HierarchyGetParent Objects

```python
class RigUnit_HierarchyGetParent(RigUnit_HierarchyBase)
```

Returns the item's parent

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Hierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child`` (RigElementKey):  [Read-Write]
- ``default_parent`` (bool):  [Read-Write] When true, it will return the default parent, regardless of whether the parent incluences the element or not
- ``parent`` (RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetParent.__init__"></a>

#### __init__

```python
def __init__(child: RigElementKey = [RigElementType.NONE, "None"],
             default_parent: bool = False,
             parent: RigElementKey = [RigElementType.NONE, "None"]) -> None
```

<a id="unreal.RigUnit_HierarchyGetParent.child"></a>

#### child

```python
@property
def child() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetParent.child"></a>

#### child

```python
@child.setter
def child(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_HierarchyGetParent.default_parent"></a>

#### default_parent

```python
@property
def default_parent() -> bool
```

(bool):  [Read-Write] When true, it will return the default parent, regardless of whether the parent incluences the element or not

<a id="unreal.RigUnit_HierarchyGetParent.default_parent"></a>

#### default_parent

```python
@default_parent.setter
def default_parent(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyGetParent.parent"></a>

#### parent

```python
@property
def parent() -> RigElementKey
```

(RigElementKey):  [Read-Only]

<a id="unreal.RigUnit_HierarchyGetParents"></a>