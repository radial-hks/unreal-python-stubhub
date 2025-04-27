## ControlRigGraphNodeContextMenuContext Objects

```python
class ControlRigGraphNodeContextMenuContext(StructBase)
```

Control Rig Graph Node Context Menu Context

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRigEditor
- **File**: ControlRigContextMenuContext.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``graph`` (RigVMGraph):  [Read-Write] The graph associated with this context.
- ``node`` (RigVMNode):  [Read-Write] The node associated with this context.
- ``pin`` (RigVMPin):  [Read-Write] The pin associated with this context; may be NULL when over a node.

<a id="unreal.ControlRigGraphNodeContextMenuContext.__init__"></a>

#### __init__

```python
def __init__(graph: RigVMGraph = None,
             node: RigVMNode = None,
             pin: RigVMPin = None) -> None
```

<a id="unreal.ControlRigGraphNodeContextMenuContext.graph"></a>

#### graph

```python
@property
def graph() -> RigVMGraph
```

(RigVMGraph):  [Read-Only] The graph associated with this context.

<a id="unreal.ControlRigGraphNodeContextMenuContext.node"></a>

#### node

```python
@property
def node() -> RigVMNode
```

(RigVMNode):  [Read-Only] The node associated with this context.

<a id="unreal.ControlRigGraphNodeContextMenuContext.pin"></a>

#### pin

```python
@property
def pin() -> RigVMPin
```

(RigVMPin):  [Read-Only] The pin associated with this context; may be NULL when over a node.

<a id="unreal.ControlRigRigHierarchyToGraphDragAndDropContext"></a>