## RigVMFunction_UserDefinedEvent Objects

```python
class RigVMFunction_UserDefinedEvent(RigVMStruct)
```

User Defined Event for running custom logic

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_UserDefinedEvent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``event_name`` (Name):  [Read-Only] True if the current interaction is a rotation
- ``execute_context`` (RigVMExecuteContext):  [Read-Write] The execution result

<a id="unreal.RigVMFunction_UserDefinedEvent.__init__"></a>

#### __init__

```python
def __init__(execute_context: RigVMExecuteContext = [],
             event_name: Name = "None") -> None
```

<a id="unreal.RigVMFunction_UserDefinedEvent.execute_context"></a>

#### execute_context

```python
@property
def execute_context() -> RigVMExecuteContext
```

(RigVMExecuteContext):  [Read-Only] The execution result

<a id="unreal.RigVMFunction_UserDefinedEvent.event_name"></a>

#### event_name

```python
@property
def event_name() -> Name
```

(Name):  [Read-Only] True if the current interaction is a rotation

<a id="unreal.RigUnit_UserDefinedEvent"></a>