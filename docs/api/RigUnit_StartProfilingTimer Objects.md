## RigUnit_StartProfilingTimer Objects

```python
class RigUnit_StartProfilingTimer(RigVMFunction_DebugBaseMutable)
```

Starts a profiling timer for debugging, used in conjunction with End Profiling Timer

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ProfilingBracket.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (RigVMExecuteContext):  [Read-Write] * This property is used to chain multiple mutable nodes together

<a id="unreal.RigUnit_StartProfilingTimer.__init__"></a>

#### __init__

```python
def __init__(execute_context: RigVMExecuteContext = []) -> None
```

<a id="unreal.RigUnit_EndProfilingTimer"></a>