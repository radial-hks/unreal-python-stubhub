## ActorModifierCoreMoveOperation Objects

```python
class ActorModifierCoreMoveOperation(StructBase)
```

Actor Modifier Core Move Operation

**C++ Source:**

- **Plugin**: ActorModifierCore
- **Module**: ActorModifierCore
- **File**: ActorModifierCoreLibraryDefs.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``move_modifier`` (ActorModifierCoreBase):  [Read-Write]
- ``move_position`` (ActorModifierCoreStackPosition):  [Read-Write]
- ``move_position_context`` (ActorModifierCoreBase):  [Read-Write]

<a id="unreal.ActorModifierCoreMoveOperation.__init__"></a>

#### __init__

```python
def __init__(
        move_modifier: ActorModifierCoreBase = None,
        move_position:
    ActorModifierCoreStackPosition = ActorModifierCoreStackPosition.BEFORE,
        move_position_context: ActorModifierCoreBase = None) -> None
```

<a id="unreal.ActorModifierCoreMoveOperation.move_modifier"></a>

#### move_modifier

```python
@property
def move_modifier() -> ActorModifierCoreBase
```

(ActorModifierCoreBase):  [Read-Write]

<a id="unreal.ActorModifierCoreMoveOperation.move_modifier"></a>

#### move_modifier

```python
@move_modifier.setter
def move_modifier(value: ActorModifierCoreBase) -> None
```

<a id="unreal.ActorModifierCoreMoveOperation.move_position"></a>

#### move_position

```python
@property
def move_position() -> ActorModifierCoreStackPosition
```

(ActorModifierCoreStackPosition):  [Read-Write]

<a id="unreal.ActorModifierCoreMoveOperation.move_position"></a>

#### move_position

```python
@move_position.setter
def move_position(value: ActorModifierCoreStackPosition) -> None
```

<a id="unreal.ActorModifierCoreMoveOperation.move_position_context"></a>

#### move_position_context

```python
@property
def move_position_context() -> ActorModifierCoreBase
```

(ActorModifierCoreBase):  [Read-Write]

<a id="unreal.ActorModifierCoreMoveOperation.move_position_context"></a>

#### move_position_context

```python
@move_position_context.setter
def move_position_context(value: ActorModifierCoreBase) -> None
```

<a id="unreal.ActorModifierCoreRemoveOperation"></a>