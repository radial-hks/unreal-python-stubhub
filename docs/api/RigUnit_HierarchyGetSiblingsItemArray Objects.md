## RigUnit_HierarchyGetSiblingsItemArray Objects

```python
class RigUnit_HierarchyGetSiblingsItemArray(RigUnit_HierarchyBase)
```

Returns the item's siblings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Hierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_siblings`` (bool):  [Read-Write] When true, it will return all siblings, regardless of whether the parent is active or not.
  When false, will return only the siblings which are influenced by the same parent
- ``include_item`` (bool):  [Read-Write]
- ``item`` (RigElementKey):  [Read-Write]
- ``siblings`` (Array[RigElementKey]):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetSiblingsItemArray.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"],
             include_item: bool = False,
             default_siblings: bool = False,
             siblings: Array[RigElementKey] = []) -> None
```

<a id="unreal.RigUnit_HierarchyGetSiblingsItemArray.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetSiblingsItemArray.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_HierarchyGetSiblingsItemArray.include_item"></a>

#### include_item

```python
@property
def include_item() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetSiblingsItemArray.include_item"></a>

#### include_item

```python
@include_item.setter
def include_item(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyGetSiblingsItemArray.default_siblings"></a>

#### default_siblings

```python
@property
def default_siblings() -> bool
```

(bool):  [Read-Write] When true, it will return all siblings, regardless of whether the parent is active or not.
When false, will return only the siblings which are influenced by the same parent

<a id="unreal.RigUnit_HierarchyGetSiblingsItemArray.default_siblings"></a>

#### default_siblings

```python
@default_siblings.setter
def default_siblings(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyGetSiblingsItemArray.siblings"></a>

#### siblings

```python
@property
def siblings() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only]

<a id="unreal.RigUnit_HierarchyGetChainItemArray"></a>