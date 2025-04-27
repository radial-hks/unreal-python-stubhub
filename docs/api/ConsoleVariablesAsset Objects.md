## ConsoleVariablesAsset Objects

```python
class ConsoleVariablesAsset(Object)
```

An asset used to track collections of console variables that can be recalled and edited using the Console Variables Editor.

**C++ Source:**

- **Plugin**: ConsoleVariables
- **Module**: ConsoleVariablesEditorRuntime
- **File**: ConsoleVariablesAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``variable_collection_description`` (str):  [Read-Write] User defined description of the variable collection

<a id="unreal.ConsoleVariablesAsset.variable_collection_description"></a>

#### variable_collection_description

```python
@property
def variable_collection_description() -> str
```

(str):  [Read-Only] User defined description of the variable collection

<a id="unreal.ConsoleVariablesAsset.set_variable_collection_description"></a>

#### set_variable_collection_description

```python
def set_variable_collection_description(
        variable_collection_description: str) -> None
```

x.set_variable_collection_description(variable_collection_description) -> None
Sets a description for this variable collection.

Args:
    variable_collection_description (str):

<a id="unreal.ConsoleVariablesAsset.replace_saved_commands"></a>

#### replace_saved_commands

```python
def replace_saved_commands(
        replacement: Array[ConsoleVariablesEditorAssetSaveData]) -> None
```

x.replace_saved_commands(replacement) -> None
Completely replaces the saved data with new saved data

Args:
    replacement (Array[ConsoleVariablesEditorAssetSaveData]):

<a id="unreal.ConsoleVariablesAsset.remove_console_variable"></a>

#### remove_console_variable

```python
def remove_console_variable(command_string: str) -> bool
```

x.remove_console_variable(command_string) -> bool
Returns true if the element was found and successfully removed.

Args:
    command_string (str): 

Returns:
    bool:

<a id="unreal.ConsoleVariablesAsset.get_variable_collection_description"></a>

#### get_variable_collection_description

```python
def get_variable_collection_description() -> str
```

x.get_variable_collection_description() -> str
Get Variable Collection Description

Returns:
    str:

<a id="unreal.ConsoleVariablesAsset.get_saved_commands_count"></a>

#### get_saved_commands_count

```python
def get_saved_commands_count() -> int
```

x.get_saved_commands_count() -> int32
Returns how many console variables are serialized in this asset

Returns:
    int32:

<a id="unreal.ConsoleVariablesAsset.get_saved_commands_as_string_array"></a>

#### get_saved_commands_as_string_array

```python
def get_saved_commands_as_string_array(
        only_include_checked: bool = False) -> Array[str]
```

x.get_saved_commands_as_string_array(only_include_checked=False) -> Array[str]
Returns the saved list of console variables as an array of FString.

Args:
    only_include_checked (bool): If true, only commands and variables with a Checked checkstate in the Console Variables Editor UI will be included. Otherwise, all will be included.

Returns:
    Array[str]:

<a id="unreal.ConsoleVariablesAsset.get_saved_commands_as_comma_separated_string"></a>

#### get_saved_commands_as_comma_separated_string

```python
def get_saved_commands_as_comma_separated_string(
        only_include_checked: bool = False) -> str
```

x.get_saved_commands_as_comma_separated_string(only_include_checked=False) -> str
Returns the saved list of console variables as a concatenated comma-separated string. Useful for passing commands and variables to a command line.

Args:
    only_include_checked (bool): If true, only commands and variables with a Checked checkstate in the Console Variables Editor UI will be included. Otherwise, all will be included.

Returns:
    str:

<a id="unreal.ConsoleVariablesAsset.get_saved_commands"></a>

#### get_saved_commands

```python
def get_saved_commands() -> Array[ConsoleVariablesEditorAssetSaveData]
```

x.get_saved_commands() -> Array[ConsoleVariablesEditorAssetSaveData]
Returns the saved list of console variable information such as the variable name, the type and the value of the variable at the time the asset was saved.

Returns:
    Array[ConsoleVariablesEditorAssetSaveData]:

<a id="unreal.ConsoleVariablesAsset.find_saved_data_by_command_string"></a>

#### find_saved_data_by_command_string

```python
def find_saved_data_by_command_string(
    command_string: str,
    search_case: SearchCase = SearchCase.IGNORE_CASE
) -> Optional[ConsoleVariablesEditorAssetSaveData]
```

x.find_saved_data_by_command_string(command_string, search_case=SearchCase.IGNORE_CASE) -> ConsoleVariablesEditorAssetSaveData or None
Outputs the FConsoleVariablesEditorAssetSaveData matching InCommand. Returns whether a match was found. Case sensitive.

Args:
    command_string (str): 
    search_case (SearchCase): 

Returns:
    ConsoleVariablesEditorAssetSaveData or None: 

    out_value (ConsoleVariablesEditorAssetSaveData):

<a id="unreal.ConsoleVariablesAsset.execute_saved_commands"></a>

#### execute_saved_commands

```python
def execute_saved_commands(world_context_object: Object,
                           only_include_checked: bool = False) -> None
```

x.execute_saved_commands(world_context_object, only_include_checked=False) -> None
Executes all saved commands in this asset, optionally only including those with a Checked checkstate in the UI.

Args:
    world_context_object (Object): 
    only_include_checked (bool): If true, only commands and variables with a Checked checkstate in the Console Variables Editor UI will be included. Otherwise, all will be included.

<a id="unreal.ConsoleVariablesAsset.copy_from"></a>

#### copy_from

```python
def copy_from(asset_to_copy: ConsoleVariablesAsset) -> None
```

x.copy_from(asset_to_copy) -> None
Copy list of variables from input asset to this asset

Args:
    asset_to_copy (ConsoleVariablesAsset):

<a id="unreal.ConsoleVariablesAsset.add_or_set_console_object_saved_data"></a>

#### add_or_set_console_object_saved_data

```python
def add_or_set_console_object_saved_data(
        data: ConsoleVariablesEditorAssetSaveData) -> None
```

x.add_or_set_console_object_saved_data(data) -> None
Set the value of a saved console variable if the name matches; add a new console variable to the list if a match is not found.

Args:
    data (ConsoleVariablesEditorAssetSaveData):

<a id="unreal.ConsoleVariablesAsset.add_from"></a>

#### add_from

```python
def add_from(asset_to_copy: ConsoleVariablesAsset) -> None
```

x.add_from(asset_to_copy) -> None
Add list of variables from input asset to this asset's list

Args:
    asset_to_copy (ConsoleVariablesAsset):

<a id="unreal.ConsoleVariablesEditorFactory"></a>