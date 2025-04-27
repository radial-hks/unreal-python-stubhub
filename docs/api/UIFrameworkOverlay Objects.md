## UIFrameworkOverlay Objects

```python
class UIFrameworkOverlay(UIFrameworkWidget)
```

UIFramework Overlay

**C++ Source:**

- **Plugin**: UIFramework
- **Module**: UIFramework
- **File**: UIFOverlay.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_enabled`` (bool):  [Read-Write]
- ``visibility`` (SlateVisibility):  [Read-Write]
- ``widget_class`` (Class):  [Read-Write]

<a id="unreal.UIFrameworkOverlay.remove_widget"></a>

#### remove_widget

```python
def remove_widget(widget: UIFrameworkWidget) -> None
```

x.remove_widget(widget) -> None
Remove Widget

Args:
    widget (UIFrameworkWidget):

<a id="unreal.UIFrameworkOverlay.add_widget"></a>

#### add_widget

```python
def add_widget(widget: UIFrameworkOverlaySlot) -> None
```

x.add_widget(widget) -> None
Add Widget

Args:
    widget (UIFrameworkOverlaySlot):

<a id="unreal.UIFrameworkStackBox"></a>