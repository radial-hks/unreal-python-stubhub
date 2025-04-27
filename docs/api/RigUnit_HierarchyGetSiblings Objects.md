## RigUnit_HierarchyGetSiblings Objects

```python
class RigUnit_HierarchyGetSiblings(RigUnit_HierarchyBase)
```

Returns the item's siblings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Hierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``include_item`` (bool):  [Read-Write]
- ``item`` (RigElementKey):  [Read-Write]
- ``siblings`` (RigElementKeyCollection):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetSiblings.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"],
             include_item: bool = False,
             siblings: RigElementKeyCollection = [[]]) -> None
```

<a id="unreal.RigUnit_HierarchyGetSiblings.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetSiblings.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_HierarchyGetSiblings.include_item"></a>

#### include_item

```python
@property
def include_item() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetSiblings.include_item"></a>

#### include_item

```python
@include_item.setter
def include_item(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyGetSiblings.siblings"></a>

#### siblings

```python
@property
def siblings() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Only]

<a id="unreal.RigUnit_HierarchyGetSiblingsItemArray"></a>