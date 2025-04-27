## UIFrameworkStackBox Objects

```python
class UIFrameworkStackBox(UIFrameworkWidget)
```

UIFramework Stack Box

**C++ Source:**

- **Plugin**: UIFramework
- **Module**: UIFramework
- **File**: UIFStackBox.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_enabled`` (bool):  [Read-Write]
- ``orientation`` (Orientation):  [Read-Write] The orientation of the stack box.
- ``visibility`` (SlateVisibility):  [Read-Write]
- ``widget_class`` (Class):  [Read-Write]

<a id="unreal.UIFrameworkStackBox.orientation"></a>

#### orientation

```python
@property
def orientation() -> Orientation
```

(Orientation):  [Read-Write] The orientation of the stack box.

<a id="unreal.UIFrameworkStackBox.orientation"></a>

#### orientation

```python
@orientation.setter
def orientation(value: Orientation) -> None
```

<a id="unreal.UIFrameworkStackBox.remove_widget"></a>

#### remove_widget

```python
def remove_widget(widget: UIFrameworkWidget) -> None
```

x.remove_widget(widget) -> None
Remove Widget

Args:
    widget (UIFrameworkWidget):

<a id="unreal.UIFrameworkStackBox.add_widget"></a>

#### add_widget

```python
def add_widget(widget: UIFrameworkStackBoxSlot) -> None
```

x.add_widget(widget) -> None
Add Widget

Args:
    widget (UIFrameworkStackBoxSlot):

<a id="unreal.UIFrameworkTextBase"></a>