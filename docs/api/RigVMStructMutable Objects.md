## RigVMStructMutable Objects

```python
class RigVMStructMutable(RigVMStruct)
```

The base mutable class for all RigVM enabled structs.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMStruct.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (RigVMExecuteContext):  [Read-Write] * This property is used to chain multiple mutable nodes together

<a id="unreal.RigVMStructMutable.__init__"></a>

#### __init__

```python
def __init__(execute_context: RigVMExecuteContext = []) -> None
```

<a id="unreal.RigVMStructMutable.execute_context"></a>

#### execute_context

```python
@property
def execute_context() -> RigVMExecuteContext
```

(RigVMExecuteContext):  [Read-Write] * This property is used to chain multiple mutable nodes together

<a id="unreal.RigVMStructMutable.execute_context"></a>

#### execute_context

```python
@execute_context.setter
def execute_context(value: RigVMExecuteContext) -> None
```

<a id="unreal.RigVMFunction_DebugBaseMutable"></a>