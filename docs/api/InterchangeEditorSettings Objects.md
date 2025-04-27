## InterchangeEditorSettings Objects

```python
class InterchangeEditorSettings(DeveloperSettings)
```

Interchange Editor Settings

**C++ Source:**

- **Module**: InterchangeEngine
- **File**: InterchangeProjectSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``show_import_dialog_at_reimport`` (bool):  [Read-Write] If enabled, the import option dialog will show when interchange re-import.
- ``used_group_name`` (Name):  [Read-Write] If enabled, the import option dialog will show when interchange re-import.
- ``used_group_uid`` (Guid):  [Read-Write]

<a id="unreal.InterchangeEditorSettings.set_used_group_name"></a>

#### set_used_group_name

```python
def set_used_group_name(used_group_name: Name) -> None
```

x.set_used_group_name(used_group_name) -> None
Set Used Group Name

Args:
    used_group_name (Name):

<a id="unreal.InterchangeEditorSettings.get_used_group_name"></a>

#### get_used_group_name

```python
def get_used_group_name() -> Name
```

x.get_used_group_name() -> Name
Get Used Group Name

Returns:
    Name:

<a id="unreal.InterchangePythonPipelineBase"></a>