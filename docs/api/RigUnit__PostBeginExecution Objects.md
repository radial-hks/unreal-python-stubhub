## RigUnit\_PostBeginExecution Objects

```python
class RigUnit_PostBeginExecution(RigUnit)
```

Event always executed after the forward solve

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_BeginExecution.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] The execution result

<a id="unreal.RigUnit_PostBeginExecution.__init__"></a>

#### \_\_init\_\_

```python
def __init__(execute_context: ControlRigExecuteContext = []) -> None
```

<a id="unreal.RigUnit_PostBeginExecution.execute_context"></a>

#### execute\_context

```python
@property
def execute_context() -> ControlRigExecuteContext
```

(ControlRigExecuteContext):  [Read-Only] The execution result

<a id="unreal.RigUnit_CollectionBase"></a>