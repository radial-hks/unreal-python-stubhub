## ActorModifierCoreInsertOperation Objects

```python
class ActorModifierCoreInsertOperation(StructBase)
```

Actor Modifier Core Insert Operation

**C++ Source:**

- **Plugin**: ActorModifierCore
- **Module**: ActorModifierCore
- **File**: ActorModifierCoreLibraryDefs.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``insert_position`` (ActorModifierCoreStackPosition):  [Read-Write]
- ``insert_position_context`` (ActorModifierCoreBase):  [Read-Write]
- ``modifier_class`` (type(Class)):  [Read-Write]

<a id="unreal.ActorModifierCoreInsertOperation.__init__"></a>

#### __init__

```python
def __init__(
        modifier_class: Class = None,
        insert_position:
    ActorModifierCoreStackPosition = ActorModifierCoreStackPosition.BEFORE,
        insert_position_context: ActorModifierCoreBase = None) -> None
```

<a id="unreal.ActorModifierCoreInsertOperation.modifier_class"></a>

#### modifier_class

```python
@property
def modifier_class() -> Class
```

(type(Class)):  [Read-Write]

<a id="unreal.ActorModifierCoreInsertOperation.modifier_class"></a>

#### modifier_class

```python
@modifier_class.setter
def modifier_class(value: Class) -> None
```

<a id="unreal.ActorModifierCoreInsertOperation.insert_position"></a>

#### insert_position

```python
@property
def insert_position() -> ActorModifierCoreStackPosition
```

(ActorModifierCoreStackPosition):  [Read-Write]

<a id="unreal.ActorModifierCoreInsertOperation.insert_position"></a>

#### insert_position

```python
@insert_position.setter
def insert_position(value: ActorModifierCoreStackPosition) -> None
```

<a id="unreal.ActorModifierCoreInsertOperation.insert_position_context"></a>

#### insert_position_context

```python
@property
def insert_position_context() -> ActorModifierCoreBase
```

(ActorModifierCoreBase):  [Read-Write]

<a id="unreal.ActorModifierCoreInsertOperation.insert_position_context"></a>

#### insert_position_context

```python
@insert_position_context.setter
def insert_position_context(value: ActorModifierCoreBase) -> None
```

<a id="unreal.ActorModifierCoreCloneOperation"></a>