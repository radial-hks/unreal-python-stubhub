## ConsoleVariablesEditorPresetImportMode Objects

```python
class ConsoleVariablesEditorPresetImportMode(EnumBase)
```

EConsole Variables Editor Preset Import Mode

**C++ Source:**

- **Plugin**: ConsoleVariables
- **Module**: ConsoleVariablesEditor
- **File**: ConsoleVariablesEditorProjectSettings.h

<a id="unreal.ConsoleVariablesEditorPresetImportMode.ADD_TO_EXISTING"></a>

#### ADD_TO_EXISTING

0: Add the list of variables from the imported preset to the current preset, replacing the values of any overlapping
variables with the values from the imported preset.

<a id="unreal.ConsoleVariablesEditorPresetImportMode.REPLACE_EXISTING"></a>

#### REPLACE_EXISTING

1: Completely replace the list of variables in the current preset, resetting them to their default values and removing
them from the list before importing the new preset's variable list.

<a id="unreal.MovieGraphPathTracerDenoiserType"></a>