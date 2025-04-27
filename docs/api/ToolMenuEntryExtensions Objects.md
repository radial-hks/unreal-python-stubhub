## ToolMenuEntryExtensions Objects

```python
class ToolMenuEntryExtensions(Object)
```

Tool Menu Entry Extensions

**C++ Source:**

- **Module**: ToolMenus
- **File**: ToolMenusBlueprintLibrary.h

<a id="unreal.ToolMenuEntryExtensions.set_tool_tip"></a>

#### set_tool_tip

```python
@classmethod
def set_tool_tip(cls, target: ToolMenuEntry, tool_tip: Text) -> ToolMenuEntry
```

X.set_tool_tip(target, tool_tip) -> ToolMenuEntry
Set Tool Tip

Args:
    target (ToolMenuEntry): 
    tool_tip (Text): 

Returns:
    ToolMenuEntry: 

    target (ToolMenuEntry):

<a id="unreal.ToolMenuEntryExtensions.set_string_command"></a>

#### set_string_command

```python
@classmethod
def set_string_command(cls, target: ToolMenuEntry,
                       type: ToolMenuStringCommandType, custom_type: Name,
                       string: str) -> ToolMenuEntry
```

X.set_string_command(target, type, custom_type, string) -> ToolMenuEntry
Set String Command

Args:
    target (ToolMenuEntry): 
    type (ToolMenuStringCommandType): 
    custom_type (Name): 
    string (str): 

Returns:
    ToolMenuEntry: 

    target (ToolMenuEntry):

<a id="unreal.ToolMenuEntryExtensions.set_label"></a>

#### set_label

```python
@classmethod
def set_label(cls, target: ToolMenuEntry, label: Text) -> ToolMenuEntry
```

X.set_label(target, label) -> ToolMenuEntry
Set Label

Args:
    target (ToolMenuEntry): 
    label (Text): 

Returns:
    ToolMenuEntry: 

    target (ToolMenuEntry):

<a id="unreal.ToolMenuEntryExtensions.set_icon"></a>

#### set_icon

```python
@classmethod
def set_icon(cls,
             target: ToolMenuEntry,
             style_set_name: Name,
             style_name: Name = "None",
             small_style_name: Name = "None") -> ToolMenuEntry
```

X.set_icon(target, style_set_name, style_name="None", small_style_name="None") -> ToolMenuEntry
Set Icon

Args:
    target (ToolMenuEntry): 
    style_set_name (Name): 
    style_name (Name): 
    small_style_name (Name): 

Returns:
    ToolMenuEntry: 

    target (ToolMenuEntry):

<a id="unreal.ToolMenuEntryExtensions.init_menu_entry"></a>

#### init_menu_entry

```python
@classmethod
def init_menu_entry(cls, owner: Name, name: Name, label: Text, tool_tip: Text,
                    command_type: ToolMenuStringCommandType,
                    custom_command_type: Name,
                    command_string: str) -> ToolMenuEntry
```

X.init_menu_entry(owner, name, label, tool_tip, command_type, custom_command_type, command_string) -> ToolMenuEntry
Init Menu Entry

Args:
    owner (Name): 
    name (Name): 
    label (Text): 
    tool_tip (Text): 
    command_type (ToolMenuStringCommandType): 
    custom_command_type (Name): 
    command_string (str): 

Returns:
    ToolMenuEntry:

<a id="unreal.ToolMenuEntryExtensions.get_tool_tip"></a>

#### get_tool_tip

```python
@classmethod
def get_tool_tip(cls, target: ToolMenuEntry) -> Text
```

X.get_tool_tip(target) -> Text
Get Tool Tip

Args:
    target (ToolMenuEntry): 

Returns:
    Text:

<a id="unreal.ToolMenuEntryExtensions.get_label"></a>

#### get_label

```python
@classmethod
def get_label(cls, target: ToolMenuEntry) -> Text
```

X.get_label(target) -> Text
Get Label

Args:
    target (ToolMenuEntry): 

Returns:
    Text:

<a id="unreal.ToolMenuSectionExtensions"></a>