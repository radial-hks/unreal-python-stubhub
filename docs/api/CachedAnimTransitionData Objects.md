## CachedAnimTransitionData Objects

```python
class CachedAnimTransitionData(StructBase)
```

Cached Anim Transition Data

**C++ Source:**

- **Module**: Engine
- **File**: CachedAnimData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``from_state_name`` (Name):  [Read-Write] Name of From State to Cache
- ``state_machine_name`` (Name):  [Read-Write] Name of StateMachine State is in
- ``to_state_name`` (Name):  [Read-Write] Name of To State to Cache

<a id="unreal.CachedAnimTransitionData.__init__"></a>

#### __init__

```python
def __init__(state_machine_name: Name = "None",
             from_state_name: Name = "None",
             to_state_name: Name = "None") -> None
```

<a id="unreal.CachedAnimTransitionData.state_machine_name"></a>

#### state_machine_name

```python
@property
def state_machine_name() -> Name
```

(Name):  [Read-Only] Name of StateMachine State is in

<a id="unreal.CachedAnimTransitionData.from_state_name"></a>

#### from_state_name

```python
@property
def from_state_name() -> Name
```

(Name):  [Read-Only] Name of From State to Cache

<a id="unreal.CachedAnimTransitionData.to_state_name"></a>

#### to_state_name

```python
@property
def to_state_name() -> Name
```

(Name):  [Read-Only] Name of To State to Cache

<a id="unreal.NamedCurveValue"></a>