## RigUnit\_InverseExecution Objects

```python
class RigUnit_InverseExecution(RigUnit)
```

Event for driving elements based off the skeleton hierarchy

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_InverseExecution.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] The execution result

<a id="unreal.RigUnit_InverseExecution.__init__"></a>

#### \_\_init\_\_

```python
def __init__(execute_context: ControlRigExecuteContext = []) -> None
```

<a id="unreal.RigUnit_InverseExecution.execute_context"></a>

#### execute\_context

```python
@property
def execute_context() -> ControlRigExecuteContext
```

(ControlRigExecuteContext):  [Read-Only] The execution result

<a id="unreal.RigUnit_IsInteracting"></a>