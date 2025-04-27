## RigVMFunction_ControlFlowBranch Objects

```python
class RigVMFunction_ControlFlowBranch(RigVMFunction_ControlFlowBase)
```

Executes either the True or False branch based on the condition

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_ControlFlow.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``completed`` (RigVMExecuteContext):  [Read-Write]
- ``condition`` (bool):  [Read-Write]
- ``execute_context`` (RigVMExecuteContext):  [Read-Write]
- ``false`` (RigVMExecuteContext):  [Read-Write]
- ``true`` (RigVMExecuteContext):  [Read-Write]

<a id="unreal.RigVMFunction_ControlFlowBranch.__init__"></a>

#### __init__

```python
def __init__(execute_context: RigVMExecuteContext = [],
             condition: bool = False,
             true: RigVMExecuteContext = [],
             false: RigVMExecuteContext = [],
             completed: RigVMExecuteContext = []) -> None
```

<a id="unreal.RigVMFunction_ControlFlowBranch.execute_context"></a>

#### execute_context

```python
@property
def execute_context() -> RigVMExecuteContext
```

(RigVMExecuteContext):  [Read-Write]

<a id="unreal.RigVMFunction_ControlFlowBranch.execute_context"></a>

#### execute_context

```python
@execute_context.setter
def execute_context(value: RigVMExecuteContext) -> None
```

<a id="unreal.RigVMFunction_ControlFlowBranch.condition"></a>

#### condition

```python
@property
def condition() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_ControlFlowBranch.condition"></a>

#### condition

```python
@condition.setter
def condition(value: bool) -> None
```

<a id="unreal.RigVMFunction_ControlFlowBranch.true"></a>

#### true

```python
@property
def true() -> RigVMExecuteContext
```

(RigVMExecuteContext):  [Read-Only]

<a id="unreal.RigVMFunction_ControlFlowBranch.false"></a>

#### false

```python
@property
def false() -> RigVMExecuteContext
```

(RigVMExecuteContext):  [Read-Only]

<a id="unreal.RigVMFunction_ControlFlowBranch.completed"></a>

#### completed

```python
@property
def completed() -> RigVMExecuteContext
```

(RigVMExecuteContext):  [Read-Only]

<a id="unreal.RigVMFunction_NameBase"></a>