## RigVMFunction_Sequence Objects

```python
class RigVMFunction_Sequence(RigVMStruct)
```

Allows for a single execution pulse to trigger a series of events in order.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Sequence.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (RigVMExecuteContext):  [Read-Write] The execution result A
- ``b`` (RigVMExecuteContext):  [Read-Write] The execution result B
- ``execute_context`` (RigVMExecuteContext):  [Read-Write] The execution input

<a id="unreal.RigVMFunction_Sequence.__init__"></a>

#### __init__

```python
def __init__(execute_context: RigVMExecuteContext = [],
             a: RigVMExecuteContext = [],
             b: RigVMExecuteContext = []) -> None
```

<a id="unreal.RigVMFunction_Sequence.execute_context"></a>

#### execute_context

```python
@property
def execute_context() -> RigVMExecuteContext
```

(RigVMExecuteContext):  [Read-Write] The execution input

<a id="unreal.RigVMFunction_Sequence.execute_context"></a>

#### execute_context

```python
@execute_context.setter
def execute_context(value: RigVMExecuteContext) -> None
```

<a id="unreal.RigVMFunction_Sequence.a"></a>

#### a

```python
@property
def a() -> RigVMExecuteContext
```

(RigVMExecuteContext):  [Read-Only] The execution result A

<a id="unreal.RigVMFunction_Sequence.b"></a>

#### b

```python
@property
def b() -> RigVMExecuteContext
```

(RigVMExecuteContext):  [Read-Only] The execution result B

<a id="unreal.RigUnit_SequenceAggregate"></a>