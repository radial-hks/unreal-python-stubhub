## RigUnit_HierarchyRemoveElement Objects

```python
class RigUnit_HierarchyRemoveElement(RigUnit_DynamicHierarchyBaseMutable)
```

Removes an element from the hierarchy
Note: This node only runs as part of the construction event.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``item`` (RigElementKey):  [Read-Write] * The item to remove
- ``success`` (bool):  [Read-Write] * True if the element has been removed successfuly

<a id="unreal.RigUnit_HierarchyRemoveElement.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             item: RigElementKey = [RigElementType.NONE, "None"],
             success: bool = False) -> None
```

<a id="unreal.RigUnit_HierarchyRemoveElement.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] * The item to remove

<a id="unreal.RigUnit_HierarchyRemoveElement.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_HierarchyRemoveElement.success"></a>

#### success

```python
@property
def success() -> bool
```

(bool):  [Read-Only] * True if the element has been removed successfuly

<a id="unreal.RigUnit_HierarchyAddElement"></a>