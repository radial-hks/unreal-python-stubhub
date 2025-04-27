## ConsoleVariablesEditorFunctionLibrary Objects

```python
class ConsoleVariablesEditorFunctionLibrary(BlueprintFunctionLibrary)
```

An asset used to track collections of console variables that can be recalled and edited using the Console Variables Editor.

**C++ Source:**

- **Plugin**: ConsoleVariables
- **Module**: ConsoleVariablesEditor
- **File**: ConsoleVariablesEditorFunctionLibrary.h

<a id="unreal.ConsoleVariablesEditorFunctionLibrary.set_enable_multi_user_c_var_sync"></a>

#### set_enable_multi_user_c_var_sync

```python
@classmethod
def set_enable_multi_user_c_var_sync(cls, new_setting: bool) -> None
```

X.set_enable_multi_user_c_var_sync(new_setting) -> None
Enable or disable the Multi-user sync setting for the current instance of the editor.

Args:
    new_setting (bool):

<a id="unreal.ConsoleVariablesEditorFunctionLibrary.set_console_variable_by_name_string"></a>

#### set_console_variable_by_name_string

```python
@classmethod
def set_console_variable_by_name_string(cls, command_name: str,
                                        value: str) -> bool
```

X.set_console_variable_by_name_string(command_name, value) -> bool
Set a console variable value directly. Returns true if the console object exists.

Args:
    command_name (str): 
    value (str): 

Returns:
    bool:

<a id="unreal.ConsoleVariablesEditorFunctionLibrary.set_console_variable_by_name_int"></a>

#### set_console_variable_by_name_int

```python
@classmethod
def set_console_variable_by_name_int(cls, command_name: str,
                                     value: int) -> bool
```

X.set_console_variable_by_name_int(command_name, value) -> bool
Set a console variable value directly. Returns true if the console object exists.

Args:
    command_name (str): 
    value (int32): 

Returns:
    bool:

<a id="unreal.ConsoleVariablesEditorFunctionLibrary.set_console_variable_by_name_float"></a>

#### set_console_variable_by_name_float

```python
@classmethod
def set_console_variable_by_name_float(cls, command_name: str,
                                       value: float) -> bool
```

X.set_console_variable_by_name_float(command_name, value) -> bool
Set a console variable value directly. Returns true if the console object exists.

Args:
    command_name (str): 
    value (float): 

Returns:
    bool:

<a id="unreal.ConsoleVariablesEditorFunctionLibrary.set_console_variable_by_name_bool"></a>

#### set_console_variable_by_name_bool

```python
@classmethod
def set_console_variable_by_name_bool(cls, command_name: str,
                                      value: bool) -> bool
```

X.set_console_variable_by_name_bool(command_name, value) -> bool
Set a console variable value directly. Returns true if the console object exists.

Args:
    command_name (str): 
    value (bool): 

Returns:
    bool:

<a id="unreal.ConsoleVariablesEditorFunctionLibrary.remove_command_from_current_preset"></a>

#### remove_command_from_current_preset

```python
@classmethod
def remove_command_from_current_preset(cls, new_command: str) -> bool
```

X.remove_command_from_current_preset(new_command) -> bool
* Removes a command from the current preset if it exists in the saved data.
* The Asset will not be automatically saved.
*

Args:
    new_command (str): 

Returns:
    bool: true if successful.

<a id="unreal.ConsoleVariablesEditorFunctionLibrary.load_preset_into_console_variables_editor"></a>

#### load_preset_into_console_variables_editor

```python
@classmethod
def load_preset_into_console_variables_editor(
    cls,
    asset: ConsoleVariablesAsset,
    import_mode:
    ConsoleVariablesEditorPresetImportMode = ConsoleVariablesEditorPresetImportMode
    .ADD_TO_EXISTING
) -> None
```

X.load_preset_into_console_variables_editor(asset, import_mode=ConsoleVariablesEditorPresetImportMode.ADD_TO_EXISTING) -> None
Loads the given asset in the Console Variables Editor and sets all its variable values.

Args:
    asset (ConsoleVariablesAsset): 
    import_mode (ConsoleVariablesEditorPresetImportMode):

<a id="unreal.ConsoleVariablesEditorFunctionLibrary.get_list_of_commands_from_preset"></a>

#### get_list_of_commands_from_preset

```python
@classmethod
def get_list_of_commands_from_preset(
        cls, asset: ConsoleVariablesAsset) -> Optional[Array[str]]
```

X.get_list_of_commands_from_preset(asset) -> Array[str] or None
Return an array of strings containing the command names for each command found in the given preset.

Args:
    asset (ConsoleVariablesAsset): 

Returns:
    Array[str] or None: 

    out_command_list (Array[str]):

<a id="unreal.ConsoleVariablesEditorFunctionLibrary.get_enable_multi_user_c_var_sync"></a>

#### get_enable_multi_user_c_var_sync

```python
@classmethod
def get_enable_multi_user_c_var_sync(cls) -> bool
```

X.get_enable_multi_user_c_var_sync() -> bool
Return whether the Multi-user sync setting for the current instance of the editor is enabled.

Returns:
    bool:

<a id="unreal.ConsoleVariablesEditorFunctionLibrary.get_currently_loaded_preset"></a>

#### get_currently_loaded_preset

```python
@classmethod
def get_currently_loaded_preset(cls) -> ConsoleVariablesAsset
```

X.get_currently_loaded_preset() -> ConsoleVariablesAsset
Return the currently loaded list of variables in the Console Variables Editor.

Returns:
    ConsoleVariablesAsset:

<a id="unreal.ConsoleVariablesEditorFunctionLibrary.get_console_variable_string_value"></a>

#### get_console_variable_string_value

```python
@classmethod
def get_console_variable_string_value(cls, command_name: str) -> Optional[str]
```

X.get_console_variable_string_value(command_name) -> str or None
Get a console variable's string value directly. Returns true if the console object exists.

Args:
    command_name (str): 

Returns:
    str or None: 

    out_value (str):

<a id="unreal.ConsoleVariablesEditorFunctionLibrary.get_console_variable_source_by_name"></a>

#### get_console_variable_source_by_name

```python
@classmethod
def get_console_variable_source_by_name(cls,
                                        command_name: str) -> Optional[str]
```

X.get_console_variable_source_by_name(command_name) -> str or None
Set a console variable value directly. Returns true if the console object exists.

Args:
    command_name (str): 

Returns:
    str or None: 

    out_value (str):

<a id="unreal.ConsoleVariablesEditorFunctionLibrary.copy_current_list_to_asset"></a>

#### copy_current_list_to_asset

```python
@classmethod
def copy_current_list_to_asset(cls, asset: ConsoleVariablesAsset) -> bool
```

X.copy_current_list_to_asset(asset) -> bool
* Saves the current list in the Console Variables Editor to the given asset.
* The Asset will not be automatically saved.
*

Args:
    asset (ConsoleVariablesAsset): 

Returns:
    bool: true if successful.

<a id="unreal.ConsoleVariablesEditorFunctionLibrary.add_validated_command_to_current_preset"></a>

#### add_validated_command_to_current_preset

```python
@classmethod
def add_validated_command_to_current_preset(cls, new_command: str) -> bool
```

X.add_validated_command_to_current_preset(new_command) -> bool
* Adds a validated command to the current preset with its current value.
* The Asset will not be automatically saved.
*

Args:
    new_command (str): 

Returns:
    bool: true if successful.

<a id="unreal.ConcertCVarSynchronization"></a>