## ToolMenu Objects

```python
class ToolMenu(ToolMenuBase)
```

Represents a menu in the ToolMenus system.

An instance of this class is returned by basic APIs such as UToolMenus::RegisterMenu and UToolMenus::ExtendMenu.

**C++ Source:**

- **Module**: ToolMenus
- **File**: ToolMenu.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``close_self_only`` (bool):  [Read-Write]
- ``menu_name`` (Name):  [Read-Write]
- ``menu_owner`` (ToolMenuOwner):  [Read-Write]
- ``menu_parent`` (Name):  [Read-Write]
- ``menu_type`` (MultiBoxType):  [Read-Write]
- ``prevent_customization`` (bool):  [Read-Write] Prevent menu from being customized
- ``searchable`` (bool):  [Read-Write]
- ``should_close_window_after_menu_selection`` (bool):  [Read-Write]
- ``style_name`` (Name):  [Read-Write]
- ``tool_bar_force_small_icons`` (bool):  [Read-Write]
- ``tool_bar_is_focusable`` (bool):  [Read-Write]
- ``tutorial_highlight_name`` (Name):  [Read-Write]

<a id="unreal.ToolMenu.menu_name"></a>

#### menu_name

```python
@property
def menu_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.ToolMenu.menu_name"></a>

#### menu_name

```python
@menu_name.setter
def menu_name(value: Name) -> None
```

<a id="unreal.ToolMenu.menu_parent"></a>

#### menu_parent

```python
@property
def menu_parent() -> Name
```

(Name):  [Read-Write]

<a id="unreal.ToolMenu.menu_parent"></a>

#### menu_parent

```python
@menu_parent.setter
def menu_parent(value: Name) -> None
```

<a id="unreal.ToolMenu.style_name"></a>

#### style_name

```python
@property
def style_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.ToolMenu.style_name"></a>

#### style_name

```python
@style_name.setter
def style_name(value: Name) -> None
```

<a id="unreal.ToolMenu.tutorial_highlight_name"></a>

#### tutorial_highlight_name

```python
@property
def tutorial_highlight_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.ToolMenu.tutorial_highlight_name"></a>

#### tutorial_highlight_name

```python
@tutorial_highlight_name.setter
def tutorial_highlight_name(value: Name) -> None
```

<a id="unreal.ToolMenu.menu_type"></a>

#### menu_type

```python
@property
def menu_type() -> MultiBoxType
```

(MultiBoxType):  [Read-Write]

<a id="unreal.ToolMenu.menu_type"></a>

#### menu_type

```python
@menu_type.setter
def menu_type(value: MultiBoxType) -> None
```

<a id="unreal.ToolMenu.should_close_window_after_menu_selection"></a>

#### should_close_window_after_menu_selection

```python
@property
def should_close_window_after_menu_selection() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ToolMenu.should_close_window_after_menu_selection"></a>

#### should_close_window_after_menu_selection

```python
@should_close_window_after_menu_selection.setter
def should_close_window_after_menu_selection(value: bool) -> None
```

<a id="unreal.ToolMenu.close_self_only"></a>

#### close_self_only

```python
@property
def close_self_only() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ToolMenu.close_self_only"></a>

#### close_self_only

```python
@close_self_only.setter
def close_self_only(value: bool) -> None
```

<a id="unreal.ToolMenu.searchable"></a>

#### searchable

```python
@property
def searchable() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ToolMenu.searchable"></a>

#### searchable

```python
@searchable.setter
def searchable(value: bool) -> None
```

<a id="unreal.ToolMenu.tool_bar_is_focusable"></a>

#### tool_bar_is_focusable

```python
@property
def tool_bar_is_focusable() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ToolMenu.tool_bar_is_focusable"></a>

#### tool_bar_is_focusable

```python
@tool_bar_is_focusable.setter
def tool_bar_is_focusable(value: bool) -> None
```

<a id="unreal.ToolMenu.tool_bar_force_small_icons"></a>

#### tool_bar_force_small_icons

```python
@property
def tool_bar_force_small_icons() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ToolMenu.tool_bar_force_small_icons"></a>

#### tool_bar_force_small_icons

```python
@tool_bar_force_small_icons.setter
def tool_bar_force_small_icons(value: bool) -> None
```

<a id="unreal.ToolMenu.prevent_customization"></a>

#### prevent_customization

```python
@property
def prevent_customization() -> bool
```

(bool):  [Read-Write] Prevent menu from being customized

<a id="unreal.ToolMenu.prevent_customization"></a>

#### prevent_customization

```python
@prevent_customization.setter
def prevent_customization(value: bool) -> None
```

<a id="unreal.ToolMenu.menu_owner"></a>

#### menu_owner

```python
@property
def menu_owner() -> ToolMenuOwner
```

(ToolMenuOwner):  [Read-Write]

<a id="unreal.ToolMenu.menu_owner"></a>

#### menu_owner

```python
@menu_owner.setter
def menu_owner(value: ToolMenuOwner) -> None
```

<a id="unreal.ToolMenu.init_menu"></a>

#### init_menu

```python
def init_menu(owner: ToolMenuOwner,
              name: Name,
              parent: Name = "None",
              type: MultiBoxType = MultiBoxType.MENU) -> None
```

x.init_menu(owner, name, parent="None", type=MultiBoxType.MENU) -> None
Init Menu

Args:
    owner (ToolMenuOwner): 
    name (Name): 
    parent (Name): 
    type (MultiBoxType):

<a id="unreal.ToolMenu.add_sub_menu"></a>

#### add_sub_menu

```python
def add_sub_menu(owner: Name,
                 section_name: Name,
                 name: Name,
                 label: Text,
                 tool_tip: Text = "") -> ToolMenu
```

x.add_sub_menu(owner, section_name, name, label, tool_tip="") -> ToolMenu
Add Sub Menu Script

Args:
    owner (Name): 
    section_name (Name): 
    name (Name): 
    label (Text): 
    tool_tip (Text): 

Returns:
    ToolMenu:

<a id="unreal.ToolMenu.add_section"></a>

#### add_section

```python
def add_section(
        section_name: Name,
        label: Text = "",
        insert_name: Name = "None",
        insert_type: ToolMenuInsertType = ToolMenuInsertType.DEFAULT) -> None
```

x.add_section(section_name, label="", insert_name="None", insert_type=ToolMenuInsertType.DEFAULT) -> None
Add Section Script

Args:
    section_name (Name): 
    label (Text): 
    insert_name (Name): 
    insert_type (ToolMenuInsertType):

<a id="unreal.ToolMenu.add_menu_entry_object"></a>

#### add_menu_entry_object

```python
def add_menu_entry_object(object: ToolMenuEntryScript) -> None
```

x.add_menu_entry_object(object) -> None
Add Menu Entry Object

Args:
    object (ToolMenuEntryScript):

<a id="unreal.ToolMenu.add_menu_entry"></a>

#### add_menu_entry

```python
def add_menu_entry(section_name: Name, args: ToolMenuEntry) -> None
```

x.add_menu_entry(section_name, args) -> None
Add Menu Entry

Args:
    section_name (Name): 
    args (ToolMenuEntry):

<a id="unreal.ToolMenu.add_dynamic_section"></a>

#### add_dynamic_section

```python
def add_dynamic_section(section_name: Name,
                        object: ToolMenuSectionDynamic) -> None
```

x.add_dynamic_section(section_name, object) -> None
Add Dynamic Section Script

Args:
    section_name (Name): 
    object (ToolMenuSectionDynamic):

<a id="unreal.ToolMenuContextBase"></a>