## ToolMenuSectionExtensions Objects

```python
class ToolMenuSectionExtensions(Object)
```

Tool Menu Section Extensions

**C++ Source:**

- **Module**: ToolMenus
- **File**: ToolMenusBlueprintLibrary.h

<a id="unreal.ToolMenuSectionExtensions.set_label"></a>

#### set_label

```python
@classmethod
def set_label(cls, section: ToolMenuSection, label: Text) -> ToolMenuSection
```

X.set_label(section, label) -> ToolMenuSection
Set Label

Args:
    section (ToolMenuSection): 
    label (Text): 

Returns:
    ToolMenuSection: 

    section (ToolMenuSection):

<a id="unreal.ToolMenuSectionExtensions.get_label"></a>

#### get_label

```python
@classmethod
def get_label(cls, section: ToolMenuSection) -> Text
```

X.get_label(section) -> Text
Get Label

Args:
    section (ToolMenuSection): 

Returns:
    Text:

<a id="unreal.ToolMenuSectionExtensions.add_entry_object"></a>

#### add_entry_object

```python
@classmethod
def add_entry_object(cls, section: ToolMenuSection,
                     object: ToolMenuEntryScript) -> ToolMenuSection
```

X.add_entry_object(section, object) -> ToolMenuSection
Add Entry Object

Args:
    section (ToolMenuSection): 
    object (ToolMenuEntryScript): 

Returns:
    ToolMenuSection: 

    section (ToolMenuSection):

<a id="unreal.ToolMenuSectionExtensions.add_entry"></a>

#### add_entry

```python
@classmethod
def add_entry(cls, section: ToolMenuSection,
              args: ToolMenuEntry) -> ToolMenuSection
```

X.add_entry(section, args) -> ToolMenuSection
Add Entry

Args:
    section (ToolMenuSection): 
    args (ToolMenuEntry): 

Returns:
    ToolMenuSection: 

    section (ToolMenuSection):

<a id="unreal.ToolMenuSectionDynamic"></a>