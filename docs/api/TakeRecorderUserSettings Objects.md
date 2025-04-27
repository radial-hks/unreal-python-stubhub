## TakeRecorderUserSettings Objects

```python
class TakeRecorderUserSettings(Object)
```

Universal take recorder settings that apply to a whole take

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakeRecorder
- **File**: TakeRecorderSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``preset_save_dir`` (DirectoryPath):  [Read-Write] The default location in which to save take presets
- ``settings`` (TakeRecorderUserParameters):  [Read-Write] User settings that should be passed to a recorder instance

<a id="unreal.TakeRecorderUserSettings.settings"></a>

#### settings

```python
@property
def settings() -> TakeRecorderUserParameters
```

(TakeRecorderUserParameters):  [Read-Only] User settings that should be passed to a recorder instance

<a id="unreal.TakeRecorderProjectSettings"></a>