## RemoteControlEntity Objects

```python
class RemoteControlEntity(StructBase)
```

Base class for exposed objects, properties, functions etc...

**C++ Source:**

- **Plugin**: RemoteControl
- **Module**: RemoteControl
- **File**: RemoteControlEntity.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``id`` (Guid):  [Read-Only] Unique identifier for this entity
- ``label`` (Name):  [Read-Only] This exposed entity's alias.
- ``owner`` (RemoteControlPreset):  [Read-Write] The preset that owns this entity.

<a id="unreal.RemoteControlEntity.__init__"></a>

#### __init__

```python
def __init__(owner: RemoteControlPreset = None,
             label: Name = "None",
             id: Guid = []) -> None
```

<a id="unreal.RemoteControlEntity.owner"></a>

#### owner

```python
@property
def owner() -> RemoteControlPreset
```

(RemoteControlPreset):  [Read-Only] The preset that owns this entity.

<a id="unreal.RemoteControlEntity.label"></a>

#### label

```python
@property
def label() -> Name
```

(Name):  [Read-Only] This exposed entity's alias.

<a id="unreal.RemoteControlEntity.id"></a>

#### id

```python
@property
def id() -> Guid
```

(Guid):  [Read-Only] Unique identifier for this entity

<a id="unreal.RemoteControlActor"></a>