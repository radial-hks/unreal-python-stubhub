## ToolMenuEntryScript Objects

```python
class ToolMenuEntryScript(Object)
```

Tool Menu Entry Script

**C++ Source:**

- **Module**: ToolMenus
- **File**: ToolMenuEntryScript.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data`` (ToolMenuEntryScriptData):  [Read-Write]

<a id="unreal.ToolMenuEntryScript.data"></a>

#### data

```python
@property
def data() -> ToolMenuEntryScriptData
```

(ToolMenuEntryScriptData):  [Read-Write]

<a id="unreal.ToolMenuEntryScript.data"></a>

#### data

```python
@data.setter
def data(value: ToolMenuEntryScriptData) -> None
```

<a id="unreal.ToolMenuEntryScript.register_menu_entry"></a>

#### register_menu_entry

```python
def register_menu_entry() -> None
```

x.register_menu_entry() -> None
Register Menu Entry

<a id="unreal.ToolMenuEntryScript.is_visible"></a>

#### is_visible

```python
def is_visible(context: ToolMenuContext) -> bool
```

x.is_visible(context) -> bool
Is Visible

Args:
    context (ToolMenuContext): 

Returns:
    bool:

<a id="unreal.ToolMenuEntryScript.init_entry"></a>

#### init_entry

```python
def init_entry(owner_name: Name,
               menu: Name,
               section: Name,
               name: Name,
               label: Text = "",
               tool_tip: Text = "") -> None
```

x.init_entry(owner_name, menu, section, name, label="", tool_tip="") -> None
Init Entry

Args:
    owner_name (Name): 
    menu (Name): 
    section (Name): 
    name (Name): 
    label (Text): 
    tool_tip (Text):

<a id="unreal.ToolMenuEntryScript.get_tool_tip"></a>

#### get_tool_tip

```python
def get_tool_tip(context: ToolMenuContext) -> Text
```

x.get_tool_tip(context) -> Text
Get Tool Tip

Args:
    context (ToolMenuContext): 

Returns:
    Text:

<a id="unreal.ToolMenuEntryScript.get_label"></a>

#### get_label

```python
def get_label(context: ToolMenuContext) -> Text
```

x.get_label(context) -> Text
Get Label

Args:
    context (ToolMenuContext): 

Returns:
    Text:

<a id="unreal.ToolMenuEntryScript.get_icon"></a>

#### get_icon

```python
def get_icon(context: ToolMenuContext) -> ScriptSlateIcon
```

x.get_icon(context) -> ScriptSlateIcon
Get Icon

Args:
    context (ToolMenuContext): 

Returns:
    ScriptSlateIcon:

<a id="unreal.ToolMenuEntryScript.get_check_state"></a>

#### get_check_state

```python
def get_check_state(context: ToolMenuContext) -> CheckBoxState
```

x.get_check_state(context) -> CheckBoxState
Get Check State

Args:
    context (ToolMenuContext): 

Returns:
    CheckBoxState:

<a id="unreal.ToolMenuEntryScript.execute"></a>

#### execute

```python
def execute(context: ToolMenuContext) -> None
```

x.execute(context) -> None
Execute

Args:
    context (ToolMenuContext):

<a id="unreal.ToolMenuEntryScript.construct_menu_entry"></a>

#### construct_menu_entry

```python
def construct_menu_entry(menu: ToolMenu, section_name: Name,
                         context: ToolMenuContext) -> None
```

x.construct_menu_entry(menu, section_name, context) -> None
Construct Menu Entry

Args:
    menu (ToolMenu): 
    section_name (Name): 
    context (ToolMenuContext):

<a id="unreal.ToolMenuEntryScript.can_execute"></a>

#### can_execute

```python
def can_execute(context: ToolMenuContext) -> bool
```

x.can_execute(context) -> bool
Can Execute

Args:
    context (ToolMenuContext): 

Returns:
    bool:

<a id="unreal.ToolMenuProfileContext"></a>