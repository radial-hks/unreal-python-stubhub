## StateTreeEvent Objects

```python
class StateTreeEvent(StructBase)
```

StateTree event with payload.

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeModule
- **File**: StateTreeEvents.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``origin`` (Name):  [Read-Write] Optional info to describe who sent the event.
- ``payload`` (InstancedStruct):  [Read-Write] Optional payload for the event.
- ``tag`` (GameplayTag):  [Read-Write] Tag describing the event

<a id="unreal.StateTreeEvent.__init__"></a>

#### __init__

```python
def __init__(tag: GameplayTag = ["None"],
             payload: InstancedStruct = [],
             origin: Name = "None") -> None
```

<a id="unreal.StateTreeEvent.tag"></a>

#### tag

```python
@property
def tag() -> GameplayTag
```

(GameplayTag):  [Read-Write] Tag describing the event

<a id="unreal.StateTreeEvent.tag"></a>

#### tag

```python
@tag.setter
def tag(value: GameplayTag) -> None
```

<a id="unreal.StateTreeEvent.payload"></a>

#### payload

```python
@property
def payload() -> InstancedStruct
```

(InstancedStruct):  [Read-Write] Optional payload for the event.

<a id="unreal.StateTreeEvent.payload"></a>

#### payload

```python
@payload.setter
def payload(value: InstancedStruct) -> None
```

<a id="unreal.StateTreeEvent.origin"></a>

#### origin

```python
@property
def origin() -> Name
```

(Name):  [Read-Write] Optional info to describe who sent the event.

<a id="unreal.StateTreeEvent.origin"></a>

#### origin

```python
@origin.setter
def origin(value: Name) -> None
```

<a id="unreal.StateTreeIndex8"></a>