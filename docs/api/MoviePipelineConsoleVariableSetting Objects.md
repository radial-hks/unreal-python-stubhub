## MoviePipelineConsoleVariableSetting Objects

```python
class MoviePipelineConsoleVariableSetting(MoviePipelineSetting)
```

Movie Pipeline Console Variable Setting

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineSettings
- **File**: MoviePipelineConsoleVariableSetting.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``console_variable_presets`` (Array[MovieSceneConsoleVariableTrackInterface]):  [Read-Write] An array of presets from the Console Variables Editor. The preset cvars will be applied (in the order they are
  specified) before any of the cvars in "Console Variables". In other words, cvars in "Console Variables" will
  take precedence over the cvars coming from these presets.
- ``end_console_commands`` (Array[str]):  [Read-Write] An array of console commands to execute when this shot is finished. Used to restore changes made by
  StartConsoleCommands.
- ``start_console_commands`` (Array[str]):  [Read-Write] An array of console commands to execute when this shot is started. If you need to restore the value
  after the shot, add a matching entry in the EndConsoleCommands array. Because they are commands
  and not values we cannot save the preivous value automatically.

<a id="unreal.MoviePipelineConsoleVariableSetting.console_variable_presets"></a>

#### console_variable_presets

```python
@property
def console_variable_presets(
) -> Array[MovieSceneConsoleVariableTrackInterface]
```

(Array[MovieSceneConsoleVariableTrackInterface]):  [Read-Write] An array of presets from the Console Variables Editor. The preset cvars will be applied (in the order they are
specified) before any of the cvars in "Console Variables". In other words, cvars in "Console Variables" will
take precedence over the cvars coming from these presets.

<a id="unreal.MoviePipelineConsoleVariableSetting.console_variable_presets"></a>

#### console_variable_presets

```python
@console_variable_presets.setter
def console_variable_presets(
        value: Array[MovieSceneConsoleVariableTrackInterface]) -> None
```

<a id="unreal.MoviePipelineConsoleVariableSetting.start_console_commands"></a>

#### start_console_commands

```python
@property
def start_console_commands() -> Array[str]
```

(Array[str]):  [Read-Write] An array of console commands to execute when this shot is started. If you need to restore the value
after the shot, add a matching entry in the EndConsoleCommands array. Because they are commands
and not values we cannot save the preivous value automatically.

<a id="unreal.MoviePipelineConsoleVariableSetting.start_console_commands"></a>

#### start_console_commands

```python
@start_console_commands.setter
def start_console_commands(value: Array[str]) -> None
```

<a id="unreal.MoviePipelineConsoleVariableSetting.end_console_commands"></a>

#### end_console_commands

```python
@property
def end_console_commands() -> Array[str]
```

(Array[str]):  [Read-Write] An array of console commands to execute when this shot is finished. Used to restore changes made by
StartConsoleCommands.

<a id="unreal.MoviePipelineConsoleVariableSetting.end_console_commands"></a>

#### end_console_commands

```python
@end_console_commands.setter
def end_console_commands(value: Array[str]) -> None
```

<a id="unreal.MoviePipelineConsoleVariableSetting.update_console_variable_enable_state"></a>

#### update_console_variable_enable_state

```python
def update_console_variable_enable_state(name: str, is_enabled: bool) -> bool
```

x.update_console_variable_enable_state(name, is_enabled) -> bool
Updates the enable state of the console variable override with the provided name. If there are duplicate cvars
with the same name, the last one with the provided name will be updated. Returns true if the operation was
successful, else false.

Args:
    name (str): 
    is_enabled (bool): 

Returns:
    bool:

<a id="unreal.MoviePipelineConsoleVariableSetting.remove_console_variable"></a>

#### remove_console_variable

```python
def remove_console_variable(name: str,
                            remove_all_instances: bool = False) -> bool
```

x.remove_console_variable(name, remove_all_instances=False) -> bool
Removes the console variable override with the specified name. If more than one with the same name exists, the
last one will be removed. Returns true if at least one console variable was removed, else false.

Args:
    name (str): 
    remove_all_instances (bool): Remove all console variables overrides with the given name (not just the last one)

Returns:
    bool:

<a id="unreal.MoviePipelineConsoleVariableSetting.get_console_variables"></a>

#### get_console_variables

```python
def get_console_variables() -> Array[MoviePipelineConsoleVariableEntry]
```

x.get_console_variables() -> Array[MoviePipelineConsoleVariableEntry]
Gets a copy of all console variable overrides. These are not meant to be changed; use the mutator methods if
console variables need to be updated.

Returns:
    Array[MoviePipelineConsoleVariableEntry]:

<a id="unreal.MoviePipelineConsoleVariableSetting.add_or_update_console_variable"></a>

#### add_or_update_console_variable

```python
def add_or_update_console_variable(name: str, value: float) -> bool
```

x.add_or_update_console_variable(name, value) -> bool
Adds a console variable override with the given name and value if one does not already exist. If the console
variable with the given name already exists, its value will be updated (the last one will be updated if there are
duplicates with the same name). Returns true if the operation was successful, else false.
see: AddConsoleVariable()

Args:
    name (str): 
    value (float): 

Returns:
    bool:

<a id="unreal.MoviePipelineConsoleVariableSetting.add_console_variable"></a>

#### add_console_variable

```python
def add_console_variable(name: str, value: float) -> bool
```

x.add_console_variable(name, value) -> bool
Adds a console variable override with the given name and value, and will add a duplicate if one with the provided
name already exists. Returns true if the operation was successful, else false.
see: AddOrUpdateConsoleVariable()

Args:
    name (str): 
    value (float): 

Returns:
    bool:

<a id="unreal.MoviePipelineWidgetRenderer"></a>