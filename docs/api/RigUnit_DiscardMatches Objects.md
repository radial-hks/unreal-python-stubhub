## RigUnit_DiscardMatches Objects

```python
class RigUnit_DiscardMatches(RigUnitMutable)
```

Discards matches during a connector event

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ConnectionCandidates.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``excluded`` (Array[RigElementKey]):  [Read-Write] The items being interacted on
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``message`` (str):  [Read-Write]

<a id="unreal.RigUnit_DiscardMatches.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             excluded: Array[RigElementKey] = [],
             message: str = "") -> None
```

<a id="unreal.RigUnit_DiscardMatches.excluded"></a>

#### excluded

```python
@property
def excluded() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Write] The items being interacted on

<a id="unreal.RigUnit_DiscardMatches.excluded"></a>

#### excluded

```python
@excluded.setter
def excluded(value: Array[RigElementKey]) -> None
```

<a id="unreal.RigUnit_DiscardMatches.message"></a>

#### message

```python
@property
def message() -> str
```

(str):  [Read-Write]

<a id="unreal.RigUnit_DiscardMatches.message"></a>

#### message

```python
@message.setter
def message(value: str) -> None
```

<a id="unreal.RigUnit_SetDefaultMatch"></a>