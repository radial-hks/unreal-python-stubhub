## ControlRigRigHierarchyDragAndDropContext Objects

```python
class ControlRigRigHierarchyDragAndDropContext(StructBase)
```

Control Rig Rig Hierarchy Drag and Drop Context

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRigEditor
- **File**: ControlRigContextMenuContext.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dragged_element_keys`` (Array[RigElementKey]):  [Read-Write]
- ``target_element_key`` (RigElementKey):  [Read-Write]

<a id="unreal.ControlRigRigHierarchyDragAndDropContext.__init__"></a>

#### __init__

```python
def __init__(
        dragged_element_keys: Array[RigElementKey] = [],
        target_element_key: RigElementKey = [RigElementType.NONE,
                                             "None"]) -> None
```

<a id="unreal.ControlRigRigHierarchyDragAndDropContext.dragged_element_keys"></a>

#### dragged_element_keys

```python
@property
def dragged_element_keys() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only]

<a id="unreal.ControlRigRigHierarchyDragAndDropContext.target_element_key"></a>

#### target_element_key

```python
@property
def target_element_key() -> RigElementKey
```

(RigElementKey):  [Read-Only]

<a id="unreal.ControlRigGraphNodeContextMenuContext"></a>