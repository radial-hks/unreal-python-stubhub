## ToolMenuEntryScriptData Objects

```python
class ToolMenuEntryScriptData(StructBase)
```

Tool Menu Entry Script Data

**C++ Source:**

- **Module**: ToolMenus
- **File**: ToolMenuEntryScript.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``advanced`` (ToolMenuEntryScriptDataAdvanced):  [Read-Write]
- ``icon`` (ScriptSlateIcon):  [Read-Write]
- ``insert_position`` (ToolMenuInsert):  [Read-Write]
- ``label`` (Text):  [Read-Write]
- ``menu`` (Name):  [Read-Write]
- ``name`` (Name):  [Read-Write]
- ``owner_name`` (Name):  [Read-Write] Optional identifier used for unregistering a group of menu items
- ``section`` (Name):  [Read-Write]
- ``tool_tip`` (Text):  [Read-Write]

<a id="unreal.ToolMenuEntryScriptData.__init__"></a>

#### __init__

```python
def __init__(
    menu: Name = "None",
    section: Name = "None",
    name: Name = "None",
    label: Text = "",
    tool_tip: Text = "",
    icon: ScriptSlateIcon = ["None", "None", "None"],
    owner_name: Name = "None",
    insert_position: ToolMenuInsert = ["None", ToolMenuInsertType.DEFAULT],
    advanced: ToolMenuEntryScriptDataAdvanced = [
        "None", MultiBlockType.MENU_ENTRY, UserInterfaceActionType.BUTTON,
        "None", False, False, True, False
    ]
) -> None
```

<a id="unreal.ToolMenuEntryScriptData.menu"></a>

#### menu

```python
@property
def menu() -> Name
```

(Name):  [Read-Write]

<a id="unreal.ToolMenuEntryScriptData.menu"></a>

#### menu

```python
@menu.setter
def menu(value: Name) -> None
```

<a id="unreal.ToolMenuEntryScriptData.section"></a>

#### section

```python
@property
def section() -> Name
```

(Name):  [Read-Write]

<a id="unreal.ToolMenuEntryScriptData.section"></a>

#### section

```python
@section.setter
def section(value: Name) -> None
```

<a id="unreal.ToolMenuEntryScriptData.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.ToolMenuEntryScriptData.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.ToolMenuEntryScriptData.label"></a>

#### label

```python
@property
def label() -> Text
```

(Text):  [Read-Write]

<a id="unreal.ToolMenuEntryScriptData.label"></a>

#### label

```python
@label.setter
def label(value: Text) -> None
```

<a id="unreal.ToolMenuEntryScriptData.tool_tip"></a>

#### tool_tip

```python
@property
def tool_tip() -> Text
```

(Text):  [Read-Write]

<a id="unreal.ToolMenuEntryScriptData.tool_tip"></a>

#### tool_tip

```python
@tool_tip.setter
def tool_tip(value: Text) -> None
```

<a id="unreal.ToolMenuEntryScriptData.icon"></a>

#### icon

```python
@property
def icon() -> ScriptSlateIcon
```

(ScriptSlateIcon):  [Read-Write]

<a id="unreal.ToolMenuEntryScriptData.icon"></a>

#### icon

```python
@icon.setter
def icon(value: ScriptSlateIcon) -> None
```

<a id="unreal.ToolMenuEntryScriptData.owner_name"></a>

#### owner_name

```python
@property
def owner_name() -> Name
```

(Name):  [Read-Write] Optional identifier used for unregistering a group of menu items

<a id="unreal.ToolMenuEntryScriptData.owner_name"></a>

#### owner_name

```python
@owner_name.setter
def owner_name(value: Name) -> None
```

<a id="unreal.ToolMenuEntryScriptData.insert_position"></a>

#### insert_position

```python
@property
def insert_position() -> ToolMenuInsert
```

(ToolMenuInsert):  [Read-Write]

<a id="unreal.ToolMenuEntryScriptData.insert_position"></a>

#### insert_position

```python
@insert_position.setter
def insert_position(value: ToolMenuInsert) -> None
```

<a id="unreal.ToolMenuEntryScriptData.advanced"></a>

#### advanced

```python
@property
def advanced() -> ToolMenuEntryScriptDataAdvanced
```

(ToolMenuEntryScriptDataAdvanced):  [Read-Write]

<a id="unreal.ToolMenuEntryScriptData.advanced"></a>

#### advanced

```python
@advanced.setter
def advanced(value: ToolMenuEntryScriptDataAdvanced) -> None
```

<a id="unreal.ToolMenuSection"></a>