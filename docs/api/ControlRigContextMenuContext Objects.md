## ControlRigContextMenuContext Objects

```python
class ControlRigContextMenuContext(Object)
```

Control Rig Context Menu Context

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRigEditor
- **File**: ControlRigContextMenuContext.h

<a id="unreal.ControlRigContextMenuContext.is_alt_down"></a>

#### is_alt_down

```python
def is_alt_down() -> bool
```

x.is_alt_down() -> bool
Returns true if either alt key is down

Returns:
    bool:

<a id="unreal.ControlRigContextMenuContext.get_rig_hierarchy_to_graph_drag_and_drop_context"></a>

#### get_rig_hierarchy_to_graph_drag_and_drop_context

```python
def get_rig_hierarchy_to_graph_drag_and_drop_context(
) -> ControlRigRigHierarchyToGraphDragAndDropContext
```

x.get_rig_hierarchy_to_graph_drag_and_drop_context() -> ControlRigRigHierarchyToGraphDragAndDropContext
Returns context for the menu that shows up when drag and drop from Rig Hierarchy to the Rig Graph

Returns:
    ControlRigRigHierarchyToGraphDragAndDropContext:

<a id="unreal.ControlRigContextMenuContext.get_rig_hierarchy_drag_and_drop_context"></a>

#### get_rig_hierarchy_drag_and_drop_context

```python
def get_rig_hierarchy_drag_and_drop_context(
) -> ControlRigRigHierarchyDragAndDropContext
```

x.get_rig_hierarchy_drag_and_drop_context() -> ControlRigRigHierarchyDragAndDropContext
Returns context for a drag & drop action that contains source and target element keys

Returns:
    ControlRigRigHierarchyDragAndDropContext:

<a id="unreal.ControlRigContextMenuContext.get_graph_node_context_menu_context"></a>

#### get_graph_node_context_menu_context

```python
def get_graph_node_context_menu_context(
) -> ControlRigGraphNodeContextMenuContext
```

x.get_graph_node_context_menu_context() -> ControlRigGraphNodeContextMenuContext
Returns context for graph node context menu

Returns:
    ControlRigGraphNodeContextMenuContext:

<a id="unreal.ControlRigContextMenuContext.get_control_rig_blueprint"></a>

#### get_control_rig_blueprint

```python
def get_control_rig_blueprint() -> ControlRigBlueprint
```

x.get_control_rig_blueprint() -> ControlRigBlueprint
Get the control rig blueprint that we are editing

Returns:
    ControlRigBlueprint:

<a id="unreal.ControlRigContextMenuContext.get_control_rig"></a>

#### get_control_rig

```python
def get_control_rig() -> ControlRig
```

x.get_control_rig() -> ControlRig
Get the active control rig instance in the viewport

Returns:
    ControlRig:

<a id="unreal.ControlRigSkeletalMeshComponent"></a>