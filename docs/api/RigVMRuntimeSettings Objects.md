## RigVMRuntimeSettings Objects

```python
class RigVMRuntimeSettings(StructBase)
```

Rig VMRuntime Settings

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMExecuteContext.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable_profiling`` (bool):  [Read-Write] When enabled records the timing of each instruction / node
  on each node and within the execution stack window.
  Keep in mind when looking at nodes in a function the duration
  represents the accumulated duration of all invocations
  of the function currently running.

  Note: This can only be used when in Debug Mode. Click the "Release" button
  in the top toolbar to switch to Debug mode.
- ``maximum_array_size`` (int32):  [Read-Write] The largest allowed size for arrays within the RigVM.
  Accessing or creating larger arrays will cause runtime errors in the rig.

<a id="unreal.RigVMRuntimeSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.RigVMPythonSettings"></a>