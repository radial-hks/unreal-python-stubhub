## RigUnit_InteractionExecution Objects

```python
class RigUnit_InteractionExecution(RigUnit)
```

Event for executing logic during an interaction

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_InteractionExecution.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] The execution result

<a id="unreal.RigUnit_InteractionExecution.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = []) -> None
```

<a id="unreal.RigUnit_InteractionExecution.execute_context"></a>

#### execute_context

```python
@property
def execute_context() -> ControlRigExecuteContext
```

(ControlRigExecuteContext):  [Read-Only] The execution result

<a id="unreal.RigUnit_InverseExecution"></a>