## RigUnit_SequenceExecution Objects

```python
class RigUnit_SequenceExecution(RigUnit)
```

Allows for a single execution pulse to trigger a series of events in order.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SequenceExecution.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (ControlRigExecuteContext):  [Read-Write] The execution result A
- ``b`` (ControlRigExecuteContext):  [Read-Write] The execution result B
- ``c`` (ControlRigExecuteContext):  [Read-Write] The execution result C
- ``d`` (ControlRigExecuteContext):  [Read-Write] The execution result D
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] The execution input

<a id="unreal.RigUnit_SequenceExecution.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             a: ControlRigExecuteContext = [],
             b: ControlRigExecuteContext = [],
             c: ControlRigExecuteContext = [],
             d: ControlRigExecuteContext = []) -> None
```

<a id="unreal.RigUnit_SequenceExecution.execute_context"></a>

#### execute_context

```python
@property
def execute_context() -> ControlRigExecuteContext
```

(ControlRigExecuteContext):  [Read-Write] The execution input

<a id="unreal.RigUnit_SequenceExecution.execute_context"></a>

#### execute_context

```python
@execute_context.setter
def execute_context(value: ControlRigExecuteContext) -> None
```

<a id="unreal.RigUnit_SequenceExecution.a"></a>

#### a

```python
@property
def a() -> ControlRigExecuteContext
```

(ControlRigExecuteContext):  [Read-Only] The execution result A

<a id="unreal.RigUnit_SequenceExecution.b"></a>

#### b

```python
@property
def b() -> ControlRigExecuteContext
```

(ControlRigExecuteContext):  [Read-Only] The execution result B

<a id="unreal.RigUnit_SequenceExecution.c"></a>

#### c

```python
@property
def c() -> ControlRigExecuteContext
```

(ControlRigExecuteContext):  [Read-Only] The execution result C

<a id="unreal.RigUnit_SequenceExecution.d"></a>

#### d

```python
@property
def d() -> ControlRigExecuteContext
```

(ControlRigExecuteContext):  [Read-Only] The execution result D

<a id="unreal.RigUnit_AddBoneTransform"></a>