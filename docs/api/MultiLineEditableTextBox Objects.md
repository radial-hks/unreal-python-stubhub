## MultiLineEditableTextBox Objects

```python
class MultiLineEditableTextBox(TextLayoutWidget)
```

Allows a user to enter multiple lines of text

**C++ Source:**

- **Module**: UMG
- **File**: MultiLineEditableTextBox.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``allow_context_menu`` (bool):  [Read-Write] Whether the context menu can be opened
- ``apply_line_height_to_bottom_line`` (bool):  [Read-Write] Whether to leave extra space below the last line due to line height.
- ``auto_wrap_text`` (bool):  [Read-Write] True if we're wrapping text automatically based on the computed horizontal space for this widget.
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``hint_text`` (Text):  [Read-Write] Hint text that appears when there is no text in the text box
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_read_only`` (bool):  [Read-Write] Sets the Text as Readonly to prevent it from being modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``justification`` (TextJustify):  [Read-Write] How the text should be aligned with the margin.
- ``line_height_percentage`` (float):  [Read-Write] The amount to scale each lines height by.
- ``margin`` (Margin):  [Read-Write] The amount of blank space left around the edges of text area.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_text_changed`` (OnMultiLineEditableTextBoxChangedEvent):  [Read-Write] Called whenever the text is changed programmatically or interactively by the user
- ``on_text_committed`` (OnMultiLineEditableTextBoxCommittedEvent):  [Read-Write] Called whenever the text is committed.  This happens when the user presses enter or the text box loses focus.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``shaped_text_options`` (ShapedTextOptions):  [Read-Write] Controls how the text within this widget should be shaped.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``text`` (Text):  [Read-Write] The text content for this editable text box widget
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``virtual_keyboard_dismiss_action`` (VirtualKeyboardDismissAction):  [Read-Write] What action should be taken when the virtual keyboard is dismissed?
- ``virtual_keyboard_options`` (VirtualKeyboardOptions):  [Read-Write] Additional options to be used by the virtual keyboard summoned from this widget
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``widget_style`` (EditableTextBoxStyle):  [Read-Write] The style
- ``wrap_text_at`` (float):  [Read-Write] Whether text wraps onto a new line when it's length exceeds this width; if this value is zero or negative, no wrapping occurs.
- ``wrapping_policy`` (TextWrappingPolicy):  [Read-Write] The wrapping policy to use.

<a id="unreal.MultiLineEditableTextBox.text"></a>

#### text

```python
@property
def text() -> Text
```

(Text):  [Read-Write] The text content for this editable text box widget

<a id="unreal.MultiLineEditableTextBox.text"></a>

#### text

```python
@text.setter
def text(value: Text) -> None
```

<a id="unreal.MultiLineEditableTextBox.hint_text"></a>

#### hint_text

```python
@property
def hint_text() -> Text
```

(Text):  [Read-Write] Hint text that appears when there is no text in the text box

<a id="unreal.MultiLineEditableTextBox.hint_text"></a>

#### hint_text

```python
@hint_text.setter
def hint_text(value: Text) -> None
```

<a id="unreal.MultiLineEditableTextBox.widget_style"></a>

#### widget_style

```python
@property
def widget_style() -> EditableTextBoxStyle
```

(EditableTextBoxStyle):  [Read-Write] The style

<a id="unreal.MultiLineEditableTextBox.widget_style"></a>

#### widget_style

```python
@widget_style.setter
def widget_style(value: EditableTextBoxStyle) -> None
```

<a id="unreal.MultiLineEditableTextBox.is_read_only"></a>

#### is_read_only

```python
@property
def is_read_only() -> bool
```

(bool):  [Read-Write] Sets the Text as Readonly to prevent it from being modified interactively by the user

<a id="unreal.MultiLineEditableTextBox.is_read_only"></a>

#### is_read_only

```python
@is_read_only.setter
def is_read_only(value: bool) -> None
```

<a id="unreal.MultiLineEditableTextBox.on_text_changed"></a>

#### on_text_changed

```python
@property
def on_text_changed() -> OnMultiLineEditableTextBoxChangedEvent
```

(OnMultiLineEditableTextBoxChangedEvent):  [Read-Write] Called whenever the text is changed programmatically or interactively by the user

<a id="unreal.MultiLineEditableTextBox.on_text_changed"></a>

#### on_text_changed

```python
@on_text_changed.setter
def on_text_changed(value: OnMultiLineEditableTextBoxChangedEvent) -> None
```

<a id="unreal.MultiLineEditableTextBox.on_text_committed"></a>

#### on_text_committed

```python
@property
def on_text_committed() -> OnMultiLineEditableTextBoxCommittedEvent
```

(OnMultiLineEditableTextBoxCommittedEvent):  [Read-Write] Called whenever the text is committed.  This happens when the user presses enter or the text box loses focus.

<a id="unreal.MultiLineEditableTextBox.on_text_committed"></a>

#### on_text_committed

```python
@on_text_committed.setter
def on_text_committed(value: OnMultiLineEditableTextBoxCommittedEvent) -> None
```

<a id="unreal.MultiLineEditableTextBox.set_text_style"></a>

#### set_text_style

```python
def set_text_style(text_style: TextBlockStyle) -> None
```

x.set_text_style(text_style) -> None
Set Text Style

Args:
    text_style (TextBlockStyle):

<a id="unreal.MultiLineEditableTextBox.set_text"></a>

#### set_text

```python
def set_text(text: Text) -> None
```

x.set_text(text) -> None
Directly sets the widget text.
Warning: This will wipe any binding created for the Text property!

Args:
    text (Text): The text to assign to the widget

<a id="unreal.MultiLineEditableTextBox.set_is_read_only"></a>

#### set_is_read_only

```python
def set_is_read_only(read_only: bool) -> None
```

x.set_is_read_only(read_only) -> None
Sets the Text as Readonly to prevent it from being modified interactively by the user

Args:
    read_only (bool):

<a id="unreal.MultiLineEditableTextBox.set_hint_text"></a>

#### set_hint_text

```python
def set_hint_text(hint_text: Text) -> None
```

x.set_hint_text(hint_text) -> None
Sets the Hint text that appears when there is no text in the text box

Args:
    hint_text (Text): The text that appears when there is no text in the text box

<a id="unreal.MultiLineEditableTextBox.set_foreground_color"></a>

#### set_foreground_color

```python
def set_foreground_color(color: LinearColor) -> None
```

x.set_foreground_color(color) -> None
Set Foreground Color

Args:
    color (LinearColor):

<a id="unreal.MultiLineEditableTextBox.set_error"></a>

#### set_error

```python
def set_error(error: Text) -> None
```

x.set_error(error) -> None
Set Error

Args:
    error (Text):

<a id="unreal.MultiLineEditableTextBox.get_text"></a>

#### get_text

```python
def get_text() -> Text
```

x.get_text() -> Text
Gets the widget text

Returns:
    Text: The widget text

<a id="unreal.MultiLineEditableTextBox.get_hint_text"></a>

#### get_hint_text

```python
def get_hint_text() -> Text
```

x.get_hint_text() -> Text
Returns the Hint text that appears when there is no text in the text box

Returns:
    Text:

<a id="unreal.NamedSlot"></a>