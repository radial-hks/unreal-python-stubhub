## RemoteControlField Objects

```python
class RemoteControlField(RemoteControlEntity)
```

Represents a property or function that has been exposed to remote control.

**C++ Source:**

- **Plugin**: RemoteControl
- **Module**: RemoteControl
- **File**: RemoteControlField.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``field_name`` (Name):  [Read-Only] The exposed field's name.
- ``field_type`` (ExposedFieldType):  [Read-Only] The field's type.
- ``id`` (Guid):  [Read-Only] Unique identifier for this entity
- ``label`` (Name):  [Read-Only] This exposed entity's alias.
- ``owner`` (RemoteControlPreset):  [Read-Write] The preset that owns this entity.
- ``property_id`` (Name):  [Read-Only] The exposed field's identifier.

<a id="unreal.RemoteControlField.__init__"></a>

#### __init__

```python
def __init__(owner: RemoteControlPreset = None,
             label: Name = "None",
             id: Guid = [],
             field_type: ExposedFieldType = ExposedFieldType.INVALID,
             field_name: Name = "None",
             property_id: Name = "None") -> None
```

<a id="unreal.RemoteControlField.field_type"></a>

#### field_type

```python
@property
def field_type() -> ExposedFieldType
```

(ExposedFieldType):  [Read-Only] The field's type.

<a id="unreal.RemoteControlField.field_name"></a>

#### field_name

```python
@property
def field_name() -> Name
```

(Name):  [Read-Only] The exposed field's name.

<a id="unreal.RemoteControlField.property_id"></a>

#### property_id

```python
@property
def property_id() -> Name
```

(Name):  [Read-Only] The exposed field's identifier.

<a id="unreal.RemoteControlProperty"></a>