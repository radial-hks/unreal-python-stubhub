## RigVMFunction_IsHostBeingDebugged Objects

```python
class RigVMFunction_IsHostBeingDebugged(RigVMStruct)
```

Returns true if a graph is run with its asset editor open. This is editor only - in shipping it always returns false.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Context.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (bool):  [Read-Write] True if the graph is currently open in the asset editor

<a id="unreal.RigVMFunction_IsHostBeingDebugged.__init__"></a>

#### __init__

```python
def __init__(result: bool = False) -> None
```

<a id="unreal.RigVMFunction_IsHostBeingDebugged.result"></a>

#### result

```python
@property
def result() -> bool
```

(bool):  [Read-Only] True if the graph is currently open in the asset editor

<a id="unreal.RigVMExecuteContext"></a>