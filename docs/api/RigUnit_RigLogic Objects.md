## RigUnit_RigLogic Objects

```python
class RigUnit_RigLogic(RigUnitMutable)
```

RigLogic is used to translate control input curves into bone transforms and values for blend shape and
animated map multiplier curves

**C++ Source:**

- **Plugin**: RigLogic
- **Module**: RigLogicModule
- **File**: RigUnit_RigLogic.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together

<a id="unreal.RigUnit_RigLogic.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = []) -> None
```

<a id="unreal.TemplateSequenceBindingOverrideData"></a>