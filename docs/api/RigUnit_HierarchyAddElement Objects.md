## RigUnit_HierarchyAddElement Objects

```python
class RigUnit_HierarchyAddElement(RigUnit_DynamicHierarchyBaseMutable)
```

Rig Unit Hierarchy Add Element

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``item`` (RigElementKey):  [Read-Write] * The resulting item
- ``name`` (Name):  [Read-Write] * The name of the new element to add
- ``parent`` (RigElementKey):  [Read-Write] * The parent of the new element to add

<a id="unreal.RigUnit_HierarchyAddElement.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             parent: RigElementKey = [RigElementType.NONE, "None"],
             name: Name = "None",
             item: RigElementKey = [RigElementType.NONE, "None"]) -> None
```

<a id="unreal.RigUnit_HierarchyAddElement.parent"></a>

#### parent

```python
@property
def parent() -> RigElementKey
```

(RigElementKey):  [Read-Write] * The parent of the new element to add

<a id="unreal.RigUnit_HierarchyAddElement.parent"></a>

#### parent

```python
@parent.setter
def parent(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_HierarchyAddElement.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] * The name of the new element to add

<a id="unreal.RigUnit_HierarchyAddElement.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.RigUnit_HierarchyAddElement.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Only] * The resulting item

<a id="unreal.RigUnit_HierarchyAddBone"></a>