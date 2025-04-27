## ToolMenuEntryScriptDataAdvanced Objects

```python
class ToolMenuEntryScriptDataAdvanced(StructBase)
```

Tool Menu Entry Script Data Advanced

**C++ Source:**

- **Module**: ToolMenus
- **File**: ToolMenuEntryScript.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entry_type`` (MultiBlockType):  [Read-Write]
- ``is_sub_menu`` (bool):  [Read-Write]
- ``open_sub_menu_on_click`` (bool):  [Read-Write]
- ``should_close_window_after_menu_selection`` (bool):  [Read-Write]
- ``simple_combo_box`` (bool):  [Read-Write]
- ``style_name_override`` (Name):  [Read-Write]
- ``tutorial_highlight`` (Name):  [Read-Write]
- ``user_interface_action_type`` (UserInterfaceActionType):  [Read-Write]

<a id="unreal.ToolMenuEntryScriptDataAdvanced.__init__"></a>

#### __init__

```python
def __init__(tutorial_highlight: Name = "None",
             entry_type: MultiBlockType = MultiBlockType.NONE,
             user_interface_action_type:
             UserInterfaceActionType = UserInterfaceActionType.NONE,
             style_name_override: Name = "None",
             is_sub_menu: bool = False,
             open_sub_menu_on_click: bool = False,
             should_close_window_after_menu_selection: bool = False,
             simple_combo_box: bool = False) -> None
```

<a id="unreal.ToolMenuEntryScriptDataAdvanced.tutorial_highlight"></a>

#### tutorial_highlight

```python
@property
def tutorial_highlight() -> Name
```

(Name):  [Read-Write]

<a id="unreal.ToolMenuEntryScriptDataAdvanced.tutorial_highlight"></a>

#### tutorial_highlight

```python
@tutorial_highlight.setter
def tutorial_highlight(value: Name) -> None
```

<a id="unreal.ToolMenuEntryScriptDataAdvanced.entry_type"></a>

#### entry_type

```python
@property
def entry_type() -> MultiBlockType
```

(MultiBlockType):  [Read-Write]

<a id="unreal.ToolMenuEntryScriptDataAdvanced.entry_type"></a>

#### entry_type

```python
@entry_type.setter
def entry_type(value: MultiBlockType) -> None
```

<a id="unreal.ToolMenuEntryScriptDataAdvanced.user_interface_action_type"></a>

#### user_interface_action_type

```python
@property
def user_interface_action_type() -> UserInterfaceActionType
```

(UserInterfaceActionType):  [Read-Write]

<a id="unreal.ToolMenuEntryScriptDataAdvanced.user_interface_action_type"></a>

#### user_interface_action_type

```python
@user_interface_action_type.setter
def user_interface_action_type(value: UserInterfaceActionType) -> None
```

<a id="unreal.ToolMenuEntryScriptDataAdvanced.style_name_override"></a>

#### style_name_override

```python
@property
def style_name_override() -> Name
```

(Name):  [Read-Write]

<a id="unreal.ToolMenuEntryScriptDataAdvanced.style_name_override"></a>

#### style_name_override

```python
@style_name_override.setter
def style_name_override(value: Name) -> None
```

<a id="unreal.ToolMenuEntryScriptDataAdvanced.is_sub_menu"></a>

#### is_sub_menu

```python
@property
def is_sub_menu() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ToolMenuEntryScriptDataAdvanced.is_sub_menu"></a>

#### is_sub_menu

```python
@is_sub_menu.setter
def is_sub_menu(value: bool) -> None
```

<a id="unreal.ToolMenuEntryScriptDataAdvanced.open_sub_menu_on_click"></a>

#### open_sub_menu_on_click

```python
@property
def open_sub_menu_on_click() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ToolMenuEntryScriptDataAdvanced.open_sub_menu_on_click"></a>

#### open_sub_menu_on_click

```python
@open_sub_menu_on_click.setter
def open_sub_menu_on_click(value: bool) -> None
```

<a id="unreal.ToolMenuEntryScriptDataAdvanced.should_close_window_after_menu_selection"></a>

#### should_close_window_after_menu_selection

```python
@property
def should_close_window_after_menu_selection() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ToolMenuEntryScriptDataAdvanced.should_close_window_after_menu_selection"></a>

#### should_close_window_after_menu_selection

```python
@should_close_window_after_menu_selection.setter
def should_close_window_after_menu_selection(value: bool) -> None
```

<a id="unreal.ToolMenuEntryScriptDataAdvanced.simple_combo_box"></a>

#### simple_combo_box

```python
@property
def simple_combo_box() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ToolMenuEntryScriptDataAdvanced.simple_combo_box"></a>

#### simple_combo_box

```python
@simple_combo_box.setter
def simple_combo_box(value: bool) -> None
```

<a id="unreal.ToolMenuEntryScriptData"></a>