## AssetGuideline Objects

```python
class AssetGuideline(AssetUserData)
```

User data that can be attached to assets to check on load for guidlelines (plugins, project settings, etc).

This class intentionally does not accept FText arguments. The project using your bundled asset would need to have
your localization tables, and we currently do not support text table referencing.

**C++ Source:**

- **Module**: UnrealEd
- **File**: AssetGuideline.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guideline_name`` (Name):  [Read-Write] Name of this guideline, we will only check once per unique guideline name.
- ``plugins`` (Array[str]):  [Read-Write] Plugins to check for on load
- ``project_settings`` (Array[IniStringValue]):  [Read-Write] Project settings to check for on load. Look at your .ini's to populate this.

<a id="unreal.AssetImportTask"></a>