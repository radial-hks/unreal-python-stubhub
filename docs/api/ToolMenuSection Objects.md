## ToolMenuSection Objects

```python
class ToolMenuSection(StructBase)
```

Tool Menu Section

**C++ Source:**

- **Module**: ToolMenus
- **File**: ToolMenuSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blocks`` (Array[ToolMenuEntry]):  [Read-Write]
- ``context`` (ToolMenuContext):  [Read-Write]
- ``insert_position`` (ToolMenuInsert):  [Read-Write]
- ``name`` (Name):  [Read-Write]
- ``owner`` (ToolMenuOwner):  [Read-Write]
- ``tool_menu_section_dynamic`` (ToolMenuSectionDynamic):  [Read-Write]

<a id="unreal.ToolMenuSection.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             owner: ToolMenuOwner = ["None"],
             blocks: Array[ToolMenuEntry] = [],
             insert_position: ToolMenuInsert = [
                 "None", ToolMenuInsertType.DEFAULT
             ],
             context: ToolMenuContext = [],
             tool_menu_section_dynamic: ToolMenuSectionDynamic = None) -> None
```

<a id="unreal.ToolMenuSection.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.ToolMenuSection.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.ToolMenuSection.owner"></a>

#### owner

```python
@property
def owner() -> ToolMenuOwner
```

(ToolMenuOwner):  [Read-Write]

<a id="unreal.ToolMenuSection.owner"></a>

#### owner

```python
@owner.setter
def owner(value: ToolMenuOwner) -> None
```

<a id="unreal.ToolMenuSection.blocks"></a>

#### blocks

```python
@property
def blocks() -> Array[ToolMenuEntry]
```

(Array[ToolMenuEntry]):  [Read-Write]

<a id="unreal.ToolMenuSection.blocks"></a>

#### blocks

```python
@blocks.setter
def blocks(value: Array[ToolMenuEntry]) -> None
```

<a id="unreal.ToolMenuSection.insert_position"></a>

#### insert_position

```python
@property
def insert_position() -> ToolMenuInsert
```

(ToolMenuInsert):  [Read-Write]

<a id="unreal.ToolMenuSection.insert_position"></a>

#### insert_position

```python
@insert_position.setter
def insert_position(value: ToolMenuInsert) -> None
```

<a id="unreal.ToolMenuSection.context"></a>

#### context

```python
@property
def context() -> ToolMenuContext
```

(ToolMenuContext):  [Read-Write]

<a id="unreal.ToolMenuSection.context"></a>

#### context

```python
@context.setter
def context(value: ToolMenuContext) -> None
```

<a id="unreal.ToolMenuSection.tool_menu_section_dynamic"></a>

#### tool_menu_section_dynamic

```python
@property
def tool_menu_section_dynamic() -> ToolMenuSectionDynamic
```

(ToolMenuSectionDynamic):  [Read-Write]

<a id="unreal.ToolMenuSection.tool_menu_section_dynamic"></a>

#### tool_menu_section_dynamic

```python
@tool_menu_section_dynamic.setter
def tool_menu_section_dynamic(value: ToolMenuSectionDynamic) -> None
```

<a id="unreal.ToolMenuSection.set_label"></a>

#### set_label

```python
def set_label(label: Text) -> None
```

x.set_label(label) -> None
Set Label

Args:
    label (Text):

<a id="unreal.ToolMenuSection.get_label"></a>

#### get_label

```python
def get_label() -> Text
```

x.get_label() -> Text
Get Label

Returns:
    Text:

<a id="unreal.ToolMenuSection.add_entry_object"></a>

#### add_entry_object

```python
def add_entry_object(object: ToolMenuEntryScript) -> None
```

x.add_entry_object(object) -> None
Add Entry Object

Args:
    object (ToolMenuEntryScript):

<a id="unreal.ToolMenuSection.add_entry"></a>

#### add_entry

```python
def add_entry(args: ToolMenuEntry) -> None
```

x.add_entry(args) -> None
Add Entry

Args:
    args (ToolMenuEntry):

<a id="unreal.InterchangePipelinePropertyStatePerContext"></a>