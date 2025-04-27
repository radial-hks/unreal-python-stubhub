## RigUnit_SetDefaultMatch Objects

```python
class RigUnit_SetDefaultMatch(RigUnitMutable)
```

Set default match during a connector event

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ConnectionCandidates.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default`` (RigElementKey):  [Read-Write] The items being interacted on
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together

<a id="unreal.RigUnit_SetDefaultMatch.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             default: RigElementKey = [RigElementType.NONE, "None"]) -> None
```

<a id="unreal.RigUnit_SetDefaultMatch.default"></a>

#### default

```python
@property
def default() -> RigElementKey
```

(RigElementKey):  [Read-Write] The items being interacted on

<a id="unreal.RigUnit_SetDefaultMatch.default"></a>

#### default

```python
@default.setter
def default(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_ConnectorExecution"></a>