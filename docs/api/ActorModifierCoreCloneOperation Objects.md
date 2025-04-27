## ActorModifierCoreCloneOperation Objects

```python
class ActorModifierCoreCloneOperation(StructBase)
```

Actor Modifier Core Clone Operation

**C++ Source:**

- **Plugin**: ActorModifierCore
- **Module**: ActorModifierCore
- **File**: ActorModifierCoreLibraryDefs.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``clone_modifier`` (ActorModifierCoreBase):  [Read-Write]
- ``clone_position`` (ActorModifierCoreStackPosition):  [Read-Write]
- ``clone_position_context`` (ActorModifierCoreBase):  [Read-Write]

<a id="unreal.ActorModifierCoreCloneOperation.__init__"></a>

#### __init__

```python
def __init__(
        clone_modifier: ActorModifierCoreBase = None,
        clone_position:
    ActorModifierCoreStackPosition = ActorModifierCoreStackPosition.BEFORE,
        clone_position_context: ActorModifierCoreBase = None) -> None
```

<a id="unreal.ActorModifierCoreCloneOperation.clone_modifier"></a>

#### clone_modifier

```python
@property
def clone_modifier() -> ActorModifierCoreBase
```

(ActorModifierCoreBase):  [Read-Write]

<a id="unreal.ActorModifierCoreCloneOperation.clone_modifier"></a>

#### clone_modifier

```python
@clone_modifier.setter
def clone_modifier(value: ActorModifierCoreBase) -> None
```

<a id="unreal.ActorModifierCoreCloneOperation.clone_position"></a>

#### clone_position

```python
@property
def clone_position() -> ActorModifierCoreStackPosition
```

(ActorModifierCoreStackPosition):  [Read-Write]

<a id="unreal.ActorModifierCoreCloneOperation.clone_position"></a>

#### clone_position

```python
@clone_position.setter
def clone_position(value: ActorModifierCoreStackPosition) -> None
```

<a id="unreal.ActorModifierCoreCloneOperation.clone_position_context"></a>

#### clone_position_context

```python
@property
def clone_position_context() -> ActorModifierCoreBase
```

(ActorModifierCoreBase):  [Read-Write]

<a id="unreal.ActorModifierCoreCloneOperation.clone_position_context"></a>

#### clone_position_context

```python
@clone_position_context.setter
def clone_position_context(value: ActorModifierCoreBase) -> None
```

<a id="unreal.ActorModifierCoreMoveOperation"></a>