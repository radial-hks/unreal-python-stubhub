## RigUnit_ConnectorExecution Objects

```python
class RigUnit_ConnectorExecution(RigUnit)
```

Event for filtering connection candidates

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ConnectorExecution.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] The execution result

<a id="unreal.RigUnit_ConnectorExecution.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = []) -> None
```

<a id="unreal.RigUnit_ConnectorExecution.execute_context"></a>

#### execute_context

```python
@property
def execute_context() -> ControlRigExecuteContext
```

(ControlRigExecuteContext):  [Read-Only] The execution result

<a id="unreal.RigUnit_PointSimulation_DebugSettings"></a>