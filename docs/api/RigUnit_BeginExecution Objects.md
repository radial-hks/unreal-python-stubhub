## RigUnit_BeginExecution Objects

```python
class RigUnit_BeginExecution(RigUnit)
```

Event for driving the skeleton hierarchy with variables and rig elements

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_BeginExecution.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] The execution result

<a id="unreal.RigUnit_BeginExecution.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = []) -> None
```

<a id="unreal.RigUnit_BeginExecution.execute_context"></a>

#### execute_context

```python
@property
def execute_context() -> ControlRigExecuteContext
```

(ControlRigExecuteContext):  [Read-Only] The execution result

<a id="unreal.RigUnit_PreBeginExecution"></a>