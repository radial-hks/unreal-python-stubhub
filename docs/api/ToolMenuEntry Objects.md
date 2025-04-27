## ToolMenuEntry Objects

```python
class ToolMenuEntry(StructBase)
```

Represents entries in menus such as buttons, checkboxes, and sub-menus.

Many entries are created for you via the methods of FToolMenuSection, such as FToolMenuSection::AddMenuEntry.

**C++ Source:**

- **Module**: ToolMenus
- **File**: ToolMenuEntry.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``insert_position`` (ToolMenuInsert):  [Read-Write]
- ``name`` (Name):  [Read-Write]
- ``owner`` (ToolMenuOwner):  [Read-Write]
- ``script_object`` (ToolMenuEntryScript):  [Read-Write]
- ``should_close_window_after_menu_selection`` (bool):  [Read-Write]
- ``style_name_override`` (Name):  [Read-Write]
- ``tutorial_highlight_name`` (Name):  [Read-Write]
- ``type`` (MultiBlockType):  [Read-Write]
- ``user_interface_action_type`` (UserInterfaceActionType):  [Read-Write]

<a id="unreal.ToolMenuEntry.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             owner: ToolMenuOwner = ["None"],
             type: MultiBlockType = MultiBlockType.NONE,
             user_interface_action_type:
             UserInterfaceActionType = UserInterfaceActionType.NONE,
             tutorial_highlight_name: Name = "None",
             insert_position: ToolMenuInsert = [
                 "None", ToolMenuInsertType.DEFAULT
             ],
             should_close_window_after_menu_selection: bool = False,
             script_object: ToolMenuEntryScript = None,
             style_name_override: Name = "None") -> None
```

<a id="unreal.ToolMenuEntry.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.ToolMenuEntry.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.ToolMenuEntry.owner"></a>

#### owner

```python
@property
def owner() -> ToolMenuOwner
```

(ToolMenuOwner):  [Read-Write]

<a id="unreal.ToolMenuEntry.owner"></a>

#### owner

```python
@owner.setter
def owner(value: ToolMenuOwner) -> None
```

<a id="unreal.ToolMenuEntry.type"></a>

#### type

```python
@property
def type() -> MultiBlockType
```

(MultiBlockType):  [Read-Write]

<a id="unreal.ToolMenuEntry.type"></a>

#### type

```python
@type.setter
def type(value: MultiBlockType) -> None
```

<a id="unreal.ToolMenuEntry.user_interface_action_type"></a>

#### user_interface_action_type

```python
@property
def user_interface_action_type() -> UserInterfaceActionType
```

(UserInterfaceActionType):  [Read-Write]

<a id="unreal.ToolMenuEntry.user_interface_action_type"></a>

#### user_interface_action_type

```python
@user_interface_action_type.setter
def user_interface_action_type(value: UserInterfaceActionType) -> None
```

<a id="unreal.ToolMenuEntry.tutorial_highlight_name"></a>

#### tutorial_highlight_name

```python
@property
def tutorial_highlight_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.ToolMenuEntry.tutorial_highlight_name"></a>

#### tutorial_highlight_name

```python
@tutorial_highlight_name.setter
def tutorial_highlight_name(value: Name) -> None
```

<a id="unreal.ToolMenuEntry.insert_position"></a>

#### insert_position

```python
@property
def insert_position() -> ToolMenuInsert
```

(ToolMenuInsert):  [Read-Write]

<a id="unreal.ToolMenuEntry.insert_position"></a>

#### insert_position

```python
@insert_position.setter
def insert_position(value: ToolMenuInsert) -> None
```

<a id="unreal.ToolMenuEntry.should_close_window_after_menu_selection"></a>

#### should_close_window_after_menu_selection

```python
@property
def should_close_window_after_menu_selection() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ToolMenuEntry.should_close_window_after_menu_selection"></a>

#### should_close_window_after_menu_selection

```python
@should_close_window_after_menu_selection.setter
def should_close_window_after_menu_selection(value: bool) -> None
```

<a id="unreal.ToolMenuEntry.script_object"></a>

#### script_object

```python
@property
def script_object() -> ToolMenuEntryScript
```

(ToolMenuEntryScript):  [Read-Write]

<a id="unreal.ToolMenuEntry.script_object"></a>

#### script_object

```python
@script_object.setter
def script_object(value: ToolMenuEntryScript) -> None
```

<a id="unreal.ToolMenuEntry.style_name_override"></a>

#### style_name_override

```python
@property
def style_name_override() -> Name
```

(Name):  [Read-Write]

<a id="unreal.ToolMenuEntry.style_name_override"></a>

#### style_name_override

```python
@style_name_override.setter
def style_name_override(value: Name) -> None
```

<a id="unreal.ToolMenuEntry.set_tool_tip"></a>

#### set_tool_tip

```python
def set_tool_tip(tool_tip: Text) -> None
```

x.set_tool_tip(tool_tip) -> None
Set Tool Tip

Args:
    tool_tip (Text):

<a id="unreal.ToolMenuEntry.set_string_command"></a>

#### set_string_command

```python
def set_string_command(type: ToolMenuStringCommandType, custom_type: Name,
                       string: str) -> None
```

x.set_string_command(type, custom_type, string) -> None
Set String Command

Args:
    type (ToolMenuStringCommandType): 
    custom_type (Name): 
    string (str):

<a id="unreal.ToolMenuEntry.set_label"></a>

#### set_label

```python
def set_label(label: Text) -> None
```

x.set_label(label) -> None
Set Label

Args:
    label (Text):

<a id="unreal.ToolMenuEntry.set_icon"></a>

#### set_icon

```python
def set_icon(style_set_name: Name,
             style_name: Name = "None",
             small_style_name: Name = "None") -> None
```

x.set_icon(style_set_name, style_name="None", small_style_name="None") -> None
Set Icon

Args:
    style_set_name (Name): 
    style_name (Name): 
    small_style_name (Name):

<a id="unreal.ToolMenuEntry.get_tool_tip"></a>

#### get_tool_tip

```python
def get_tool_tip() -> Text
```

x.get_tool_tip() -> Text
Get Tool Tip

Returns:
    Text:

<a id="unreal.ToolMenuEntry.get_label"></a>

#### get_label

```python
def get_label() -> Text
```

x.get_label() -> Text
Get Label

Returns:
    Text:

<a id="unreal.ScriptSlateIcon"></a>