## RigUnit_GetCandidates Objects

```python
class RigUnit_GetCandidates(RigUnit)
```

Returns the connection candidates for one connector

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ConnectionCandidates.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``candidates`` (Array[RigElementKey]):  [Read-Write] The items being interacted on
- ``connector`` (RigElementKey):  [Read-Write] The connector being resolved

<a id="unreal.RigUnit_GetCandidates.__init__"></a>

#### __init__

```python
def __init__(connector: RigElementKey = [RigElementType.NONE, "None"],
             candidates: Array[RigElementKey] = []) -> None
```

<a id="unreal.RigUnit_GetCandidates.connector"></a>

#### connector

```python
@property
def connector() -> RigElementKey
```

(RigElementKey):  [Read-Only] The connector being resolved

<a id="unreal.RigUnit_GetCandidates.candidates"></a>

#### candidates

```python
@property
def candidates() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only] The items being interacted on

<a id="unreal.RigUnit_DiscardMatches"></a>