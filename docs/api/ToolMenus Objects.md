## ToolMenus Objects

```python
class ToolMenus(Object)
```

Tool Menus

**C++ Source:**

- **Module**: ToolMenus
- **File**: ToolMenus.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``customized_menus`` (Array[CustomizedToolMenu]):  [Read-Write]
- ``menu_profiles`` (Map[Name, ToolMenuProfileMap]):  [Read-Write] MenuName
- ``menu_substitutions_during_generate`` (Map[Name, Name]):  [Read-Write] Allow substituting one menu for another during generate but not during find or extend

<a id="unreal.ToolMenus.unregister_owner_by_name"></a>

#### unregister_owner_by_name

```python
def unregister_owner_by_name(owner_name: Name) -> None
```

x.unregister_owner_by_name(owner_name) -> None
Removes all entries that were registered under a specific owner name

Args:
    owner_name (Name):

<a id="unreal.ToolMenus.set_section_position"></a>

#### set_section_position

```python
def set_section_position(menu_name: Name, section_name: Name,
                         other_section_name: Name,
                         position_type: ToolMenuInsertType) -> None
```

x.set_section_position(menu_name, section_name, other_section_name, position_type) -> None
Sets where to insert a section into a menu when generating relative to other section names.

Args:
    menu_name (Name): 
    section_name (Name): 
    other_section_name (Name): 
    position_type (ToolMenuInsertType):

<a id="unreal.ToolMenus.set_section_label"></a>

#### set_section_label

```python
def set_section_label(menu_name: Name, section_name: Name,
                      label: Text) -> None
```

x.set_section_label(menu_name, section_name, label) -> None
Sets a section's displayed label text.

Args:
    menu_name (Name): 
    section_name (Name): 
    label (Text):

<a id="unreal.ToolMenus.remove_section"></a>

#### remove_section

```python
def remove_section(menu_name: Name, section: Name) -> None
```

x.remove_section(menu_name, section) -> None
Removes a section from a given menu

Args:
    menu_name (Name): 
    section (Name):

<a id="unreal.ToolMenus.remove_menu"></a>

#### remove_menu

```python
def remove_menu(menu_name: Name) -> None
```

x.remove_menu(menu_name) -> None
Unregisters a menu by name

Args:
    menu_name (Name):

<a id="unreal.ToolMenus.remove_entry"></a>

#### remove_entry

```python
def remove_entry(menu_name: Name, section: Name, name: Name) -> None
```

x.remove_entry(menu_name, section, name) -> None
Removes a menu entry from a given menu and section

Args:
    menu_name (Name): 
    section (Name): 
    name (Name):

<a id="unreal.ToolMenus.register_menu"></a>

#### register_menu

```python
def register_menu(name: Name,
                  parent: Name = "None",
                  type: MultiBoxType = MultiBoxType.MENU,
                  warn_if_already_registered: bool = True) -> ToolMenu
```

x.register_menu(name, parent="None", type=MultiBoxType.MENU, warn_if_already_registered=True) -> ToolMenu
Registers a menu by name

Args:
    name (Name): 
    parent (Name): Optional name of a menu to layer on top of.
    type (MultiBoxType): Type of menu that will be generated such as: ToolBar, VerticalToolBar, etc..
    warn_if_already_registered (bool): Display warning if already registered

Returns:
    ToolMenu: ToolMenu        Menu object

<a id="unreal.ToolMenus.refresh_menu_widget"></a>

#### refresh_menu_widget

```python
def refresh_menu_widget(name: Name) -> bool
```

x.refresh_menu_widget(name) -> bool
Rebuilds all widgets generated from a specific menu.

Args:
    name (Name): 

Returns:
    bool:

<a id="unreal.ToolMenus.refresh_all_widgets"></a>

#### refresh_all_widgets

```python
def refresh_all_widgets() -> None
```

x.refresh_all_widgets() -> None
Rebuilds all currently generated widgets next tick.

<a id="unreal.ToolMenus.is_menu_registered"></a>

#### is_menu_registered

```python
def is_menu_registered(name: Name) -> bool
```

x.is_menu_registered(name) -> bool
Determines if a menu has already been registered.

Args:
    name (Name): Name of the menu to find.

Returns:
    bool: bool    True if menu has already been registered.

<a id="unreal.ToolMenus.get"></a>

#### get

```python
@classmethod
def get(cls) -> ToolMenus
```

X.get() -> ToolMenus
Get

Returns:
    ToolMenus:

<a id="unreal.ToolMenus.find_menu"></a>

#### find_menu

```python
def find_menu(name: Name) -> ToolMenu
```

x.find_menu(name) -> ToolMenu
Finds an existing menu that has been registered or extended.

Args:
    name (Name): Name of the menu to find.

Returns:
    ToolMenu: ToolMenu        Menu object. Returns null if not found.

<a id="unreal.ToolMenus.find_context"></a>

#### find_context

```python
@classmethod
def find_context(cls, context: ToolMenuContext, class_: Class) -> Object
```

X.find_context(context, class_) -> Object
Finds a context object of a given class if it exists

Args:
    context (ToolMenuContext): 
    class_ (type(Class)): 

Returns:
    Object:

<a id="unreal.ToolMenus.extend_menu"></a>

#### extend_menu

```python
def extend_menu(name: Name) -> ToolMenu
```

x.extend_menu(name) -> ToolMenu
Extends a menu without registering the menu or claiming ownership of it. Ok to call even if menu does not exist yet.

Args:
    name (Name): Name of the menu to extend

Returns:
    ToolMenu: ToolMenu        Menu object

<a id="unreal.ToolMenus.add_menu_entry_object"></a>

#### add_menu_entry_object

```python
@classmethod
def add_menu_entry_object(cls, menu_entry_object: ToolMenuEntryScript) -> bool
```

X.add_menu_entry_object(menu_entry_object) -> bool
Registers menu entry object from blueprint/script

Args:
    menu_entry_object (ToolMenuEntryScript): 

Returns:
    bool:

<a id="unreal.ToolMenuContextExtensions"></a>