## RemoteControlActor Objects

```python
class RemoteControlActor(RemoteControlEntity)
```

Represents an actor exposed in the panel.

**C++ Source:**

- **Plugin**: RemoteControl
- **Module**: RemoteControl
- **File**: RemoteControlActor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``id`` (Guid):  [Read-Only] Unique identifier for this entity
- ``label`` (Name):  [Read-Only] This exposed entity's alias.
- ``owner`` (RemoteControlPreset):  [Read-Write] The preset that owns this entity.
- ``path`` (SoftObjectPath):  [Read-Write] Path to the exposed object.

<a id="unreal.RemoteControlActor.__init__"></a>

#### __init__

```python
def __init__(owner: RemoteControlPreset = None,
             label: Name = "None",
             id: Guid = [],
             path: SoftObjectPath = [""]) -> None
```

<a id="unreal.RemoteControlActor.path"></a>

#### path

```python
@property
def path() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Only] Path to the exposed object.

<a id="unreal.RemoteControlField"></a>