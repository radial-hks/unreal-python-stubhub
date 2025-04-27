## RigUnitMutable Objects

```python
class RigUnitMutable(RigUnit)
```

Base class for all rig units that can change data

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together

<a id="unreal.RigUnitMutable.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = []) -> None
```

<a id="unreal.RigUnitMutable.execute_context"></a>

#### execute_context

```python
@property
def execute_context() -> ControlRigExecuteContext
```

(ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together

<a id="unreal.RigUnitMutable.execute_context"></a>

#### execute_context

```python
@execute_context.setter
def execute_context(value: ControlRigExecuteContext) -> None
```

<a id="unreal.ControlRigExecuteContext"></a>