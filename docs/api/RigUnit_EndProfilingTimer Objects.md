## RigUnit_EndProfilingTimer Objects

```python
class RigUnit_EndProfilingTimer(RigVMFunction_DebugBaseMutable)
```

Ends an existing profiling timer for debugging, used in conjunction with Start Profiling Timer

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ProfilingBracket.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (RigVMExecuteContext):  [Read-Write] * This property is used to chain multiple mutable nodes together
- ``number_of_measurements`` (int32):  [Read-Only]
- ``prefix`` (str):  [Read-Only]

<a id="unreal.RigUnit_EndProfilingTimer.__init__"></a>

#### __init__

```python
def __init__(execute_context: RigVMExecuteContext = [],
             number_of_measurements: int = 0,
             prefix: str = "") -> None
```

<a id="unreal.RigUnit_EndProfilingTimer.number_of_measurements"></a>

#### number_of_measurements

```python
@property
def number_of_measurements() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigUnit_EndProfilingTimer.prefix"></a>

#### prefix

```python
@property
def prefix() -> str
```

(str):  [Read-Only]

<a id="unreal.RigUnit_VisualDebugVector"></a>