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

#### \_\_init\_\_

```python
def __init__(
        dragged_element_keys: Array[RigElementKey] = [],
        target_element_key: RigElementKey = [RigElementType.NONE,
                                             "None"]) -> None
```

<a id="unreal.ControlRigRigHierarchyDragAndDropContext.dragged_element_keys"></a>

#### dragged\_element\_keys

```python
@property
def dragged_element_keys() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only]

<a id="unreal.ControlRigRigHierarchyDragAndDropContext.target_element_key"></a>

#### target\_element\_key

```python
@property
def target_element_key() -> RigElementKey
```

(RigElementKey):  [Read-Only]

<a id="unreal.ControlRigGraphNodeContextMenuContext"></a>