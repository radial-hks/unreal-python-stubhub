## UIFrameworkUserWidget Objects

```python
class UIFrameworkUserWidget(UIFrameworkWidget)
```

UIFramework User Widget

**C++ Source:**

- **Plugin**: UIFramework
- **Module**: UIFramework
- **File**: UIFUserWidget.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_enabled`` (bool):  [Read-Write]
- ``visibility`` (SlateVisibility):  [Read-Write]
- ``widget_class`` (Class):  [Read-Write]

<a id="unreal.UIFrameworkUserWidget.set_widget_class"></a>

#### set_widget_class

```python
def set_widget_class(value: Class) -> None
```

x.set_widget_class(value) -> None
Set Widget Class

Args:
    value (Class):

<a id="unreal.UIFrameworkUserWidget.set_named_slot"></a>

#### set_named_slot

```python
def set_named_slot(slot_name: Name, widget: UIFrameworkWidget) -> None
```

x.set_named_slot(slot_name, widget) -> None
Set Named Slot

Args:
    slot_name (Name): 
    widget (UIFrameworkWidget):

<a id="unreal.UIFrameworkUserWidget.get_named_slot"></a>

#### get_named_slot

```python
def get_named_slot(slot_name: Name) -> UIFrameworkWidget
```

x.get_named_slot(slot_name) -> UIFrameworkWidget
Get Named Slot

Args:
    slot_name (Name): 

Returns:
    UIFrameworkWidget:

<a id="unreal.EditorConfigBase"></a>