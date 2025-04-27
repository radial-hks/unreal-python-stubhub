## StateTreeEditorNode Objects

```python
class StateTreeEditorNode(StructBase)
```

Base for Evaluator, Task and Condition nodes.

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeEditorModule
- **File**: StateTreeEditorNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``expression_indent`` (uint8):  [Read-Write]
- ``expression_operand`` (StateTreeExpressionOperand):  [Read-Write]
- ``id`` (Guid):  [Read-Write]
- ``instance`` (InstancedStruct):  [Read-Write]
- ``instance_object`` (Object):  [Read-Write]
- ``node`` (InstancedStruct):  [Read-Write]

<a id="unreal.StateTreeEditorNode.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.StateTreeItem"></a>