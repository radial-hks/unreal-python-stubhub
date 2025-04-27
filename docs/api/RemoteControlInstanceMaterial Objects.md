## RemoteControlInstanceMaterial Objects

```python
class RemoteControlInstanceMaterial(RemoteControlProperty)
```

Represents a material instance property that has been exposed to remote control.

**C++ Source:**

- **Plugin**: RemoteControl
- **Module**: RemoteControl
- **File**: RemoteControlInstanceMaterial.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``field_name`` (Name):  [Read-Only] The exposed field's name.
- ``field_type`` (ExposedFieldType):  [Read-Only] The field's type.
- ``id`` (Guid):  [Read-Only] Unique identifier for this entity
- ``label`` (Name):  [Read-Only] This exposed entity's alias.
- ``owner`` (RemoteControlPreset):  [Read-Write] The preset that owns this entity.
- ``property_id`` (Name):  [Read-Only] The exposed field's identifier.

<a id="unreal.RemoteControlInstanceMaterial.__init__"></a>

#### __init__

```python
def __init__(owner: RemoteControlPreset = None,
             label: Name = "None",
             id: Guid = [],
             field_type: ExposedFieldType = ExposedFieldType.INVALID,
             field_name: Name = "None",
             property_id: Name = "None") -> None
```

<a id="unreal.RemoteControlInterceptionFunctionParamStruct"></a>