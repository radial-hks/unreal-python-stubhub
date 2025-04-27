## EditableText Objects

```python
class EditableText(Widget)
```

Editable text box widget

**C++ Source:**

- **Module**: UMG
- **File**: EditableText.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``allow_context_menu`` (bool):  [Read-Write] Whether the context menu can be opened
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clear_keyboard_focus_on_commit`` (bool):  [Read-Write] Whether to clear keyboard focus when pressing enter to commit changes
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``hint_text`` (Text):  [Read-Write] Hint text that appears when there is no text in the text box
- ``is_caret_moved_when_gain_focus`` (bool):  [Read-Write] When set to true the caret is moved when gaining focus
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_password`` (bool):  [Read-Write] Sets whether this text box is for storing a password
- ``is_read_only`` (bool):  [Read-Write] Sets whether this text box can actually be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``justification`` (TextJustify):  [Read-Write] How the text should be aligned with the margin.
- ``keyboard_type`` (VirtualKeyboardType):  [Read-Write] If we're on a platform that requires a virtual keyboard, what kind of keyboard should this widget use?
- ``minimum_desired_width`` (float):  [Read-Write] The minimum desired Width for the text
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_text_changed`` (OnEditableTextChangedEvent):  [Read-Write] Called whenever the text is changed programmatically or interactively by the user
- ``on_text_committed`` (OnEditableTextCommittedEvent):  [Read-Write] Called whenever the text is committed.  This happens when the user presses enter or the text box loses focus.
- ``overflow_policy`` (TextOverflowPolicy):  [Read-Write] Sets what happens to text that is clipped and doesn't fit within the clip rect for this widget
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``revert_text_on_escape`` (bool):  [Read-Write] Whether to allow the user to back out of changes when they press the escape key
- ``select_all_text_on_commit`` (bool):  [Read-Write] Whether to select all text when pressing enter to commit changes
- ``select_all_text_when_focused`` (bool):  [Read-Write] Whether to select all text when the user clicks to give focus on the widget
- ``shaped_text_options`` (ShapedTextOptions):  [Read-Write] Controls how the text within this widget should be shaped.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``text`` (Text):  [Read-Write] The text content for this editable text box widget
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``virtual_keyboard_dismiss_action`` (VirtualKeyboardDismissAction):  [Read-Write] What action should be taken when the virtual keyboard is dismissed?
- ``virtual_keyboard_options`` (VirtualKeyboardOptions):  [Read-Write] Additional options for the virtual keyboard
- ``virtual_keyboard_trigger`` (VirtualKeyboardTrigger):  [Read-Write]
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``widget_style`` (EditableTextStyle):  [Read-Write] The style

<a id="unreal.EditableText.text"></a>

#### text

```python
@property
def text() -> Text
```

(Text):  [Read-Write] The text content for this editable text box widget

<a id="unreal.EditableText.text"></a>

#### text

```python
@text.setter
def text(value: Text) -> None
```

<a id="unreal.EditableText.hint_text"></a>

#### hint_text

```python
@property
def hint_text() -> Text
```

(Text):  [Read-Write] Hint text that appears when there is no text in the text box

<a id="unreal.EditableText.hint_text"></a>

#### hint_text

```python
@hint_text.setter
def hint_text(value: Text) -> None
```

<a id="unreal.EditableText.widget_style"></a>

#### widget_style

```python
@property
def widget_style() -> EditableTextStyle
```

(EditableTextStyle):  [Read-Write] The style

<a id="unreal.EditableText.widget_style"></a>

#### widget_style

```python
@widget_style.setter
def widget_style(value: EditableTextStyle) -> None
```

<a id="unreal.EditableText.is_read_only"></a>

#### is_read_only

```python
@property
def is_read_only() -> bool
```

(bool):  [Read-Write] Sets whether this text box can actually be modified interactively by the user

<a id="unreal.EditableText.is_read_only"></a>

#### is_read_only

```python
@is_read_only.setter
def is_read_only(value: bool) -> None
```

<a id="unreal.EditableText.is_password"></a>

#### is_password

```python
@property
def is_password() -> bool
```

(bool):  [Read-Write] Sets whether this text box is for storing a password

<a id="unreal.EditableText.is_password"></a>

#### is_password

```python
@is_password.setter
def is_password(value: bool) -> None
```

<a id="unreal.EditableText.minimum_desired_width"></a>

#### minimum_desired_width

```python
@property
def minimum_desired_width() -> float
```

(float):  [Read-Write] The minimum desired Width for the text

<a id="unreal.EditableText.minimum_desired_width"></a>

#### minimum_desired_width

```python
@minimum_desired_width.setter
def minimum_desired_width(value: float) -> None
```

<a id="unreal.EditableText.is_caret_moved_when_gain_focus"></a>

#### is_caret_moved_when_gain_focus

```python
@property
def is_caret_moved_when_gain_focus() -> bool
```

(bool):  [Read-Write] When set to true the caret is moved when gaining focus

<a id="unreal.EditableText.is_caret_moved_when_gain_focus"></a>

#### is_caret_moved_when_gain_focus

```python
@is_caret_moved_when_gain_focus.setter
def is_caret_moved_when_gain_focus(value: bool) -> None
```

<a id="unreal.EditableText.select_all_text_when_focused"></a>

#### select_all_text_when_focused

```python
@property
def select_all_text_when_focused() -> bool
```

(bool):  [Read-Write] Whether to select all text when the user clicks to give focus on the widget

<a id="unreal.EditableText.select_all_text_when_focused"></a>

#### select_all_text_when_focused

```python
@select_all_text_when_focused.setter
def select_all_text_when_focused(value: bool) -> None
```

<a id="unreal.EditableText.revert_text_on_escape"></a>

#### revert_text_on_escape

```python
@property
def revert_text_on_escape() -> bool
```

(bool):  [Read-Write] Whether to allow the user to back out of changes when they press the escape key

<a id="unreal.EditableText.revert_text_on_escape"></a>

#### revert_text_on_escape

```python
@revert_text_on_escape.setter
def revert_text_on_escape(value: bool) -> None
```

<a id="unreal.EditableText.clear_keyboard_focus_on_commit"></a>

#### clear_keyboard_focus_on_commit

```python
@property
def clear_keyboard_focus_on_commit() -> bool
```

(bool):  [Read-Write] Whether to clear keyboard focus when pressing enter to commit changes

<a id="unreal.EditableText.clear_keyboard_focus_on_commit"></a>

#### clear_keyboard_focus_on_commit

```python
@clear_keyboard_focus_on_commit.setter
def clear_keyboard_focus_on_commit(value: bool) -> None
```

<a id="unreal.EditableText.select_all_text_on_commit"></a>

#### select_all_text_on_commit

```python
@property
def select_all_text_on_commit() -> bool
```

(bool):  [Read-Write] Whether to select all text when pressing enter to commit changes

<a id="unreal.EditableText.select_all_text_on_commit"></a>

#### select_all_text_on_commit

```python
@select_all_text_on_commit.setter
def select_all_text_on_commit(value: bool) -> None
```

<a id="unreal.EditableText.justification"></a>

#### justification

```python
@property
def justification() -> TextJustify
```

(TextJustify):  [Read-Write] How the text should be aligned with the margin.

<a id="unreal.EditableText.justification"></a>

#### justification

```python
@justification.setter
def justification(value: TextJustify) -> None
```

<a id="unreal.EditableText.overflow_policy"></a>

#### overflow_policy

```python
@property
def overflow_policy() -> TextOverflowPolicy
```

(TextOverflowPolicy):  [Read-Write] Sets what happens to text that is clipped and doesn't fit within the clip rect for this widget

<a id="unreal.EditableText.overflow_policy"></a>

#### overflow_policy

```python
@overflow_policy.setter
def overflow_policy(value: TextOverflowPolicy) -> None
```

<a id="unreal.EditableText.shaped_text_options"></a>

#### shaped_text_options

```python
@property
def shaped_text_options() -> ShapedTextOptions
```

(ShapedTextOptions):  [Read-Only] Controls how the text within this widget should be shaped.

<a id="unreal.EditableText.on_text_changed"></a>

#### on_text_changed

```python
@property
def on_text_changed() -> OnEditableTextChangedEvent
```

(OnEditableTextChangedEvent):  [Read-Write] Called whenever the text is changed programmatically or interactively by the user

<a id="unreal.EditableText.on_text_changed"></a>

#### on_text_changed

```python
@on_text_changed.setter
def on_text_changed(value: OnEditableTextChangedEvent) -> None
```

<a id="unreal.EditableText.on_text_committed"></a>

#### on_text_committed

```python
@property
def on_text_committed() -> OnEditableTextCommittedEvent
```

(OnEditableTextCommittedEvent):  [Read-Write] Called whenever the text is committed.  This happens when the user presses enter or the text box loses focus.

<a id="unreal.EditableText.on_text_committed"></a>

#### on_text_committed

```python
@on_text_committed.setter
def on_text_committed(value: OnEditableTextCommittedEvent) -> None
```

<a id="unreal.EditableText.set_text"></a>

#### set_text

```python
def set_text(text: Text) -> None
```

x.set_text(text) -> None
Directly sets the widget text.
Warning: This will wipe any binding created for the Text property!

Args:
    text (Text): The text to assign to the widget

<a id="unreal.EditableText.set_minimum_desired_width"></a>

#### set_minimum_desired_width

```python
def set_minimum_desired_width(min_desired_width: float) -> None
```

x.set_minimum_desired_width(min_desired_width) -> None
Set the minimum desired width for this text box

Args:
    min_desired_width (float): new minimum desired width

<a id="unreal.EditableText.set_is_read_only"></a>

#### set_is_read_only

```python
def set_is_read_only(inb_is_ready_only: bool) -> None
```

x.set_is_read_only(inb_is_ready_only) -> None
Set Is Read Only

Args:
    inb_is_ready_only (bool):

<a id="unreal.EditableText.set_is_password"></a>

#### set_is_password

```python
def set_is_password(inb_is_password: bool) -> None
```

x.set_is_password(inb_is_password) -> None
Set Is Password

Args:
    inb_is_password (bool):

<a id="unreal.EditableText.set_hint_text"></a>

#### set_hint_text

```python
def set_hint_text(hint_text: Text) -> None
```

x.set_hint_text(hint_text) -> None
Set Hint Text

Args:
    hint_text (Text):

<a id="unreal.EditableText.set_font_outline_material"></a>

#### set_font_outline_material

```python
def set_font_outline_material(material: MaterialInterface) -> None
```

x.set_font_outline_material(material) -> None
Set Font Outline Material

Args:
    material (MaterialInterface):

<a id="unreal.EditableText.set_font_material"></a>

#### set_font_material

```python
def set_font_material(material: MaterialInterface) -> None
```

x.set_font_material(material) -> None
Set Font Material

Args:
    material (MaterialInterface):

<a id="unreal.EditableText.set_font"></a>

#### set_font

```python
def set_font(font_info: SlateFontInfo) -> None
```

x.set_font(font_info) -> None
Set Font

Args:
    font_info (SlateFontInfo):

<a id="unreal.EditableText.get_text"></a>

#### get_text

```python
def get_text() -> Text
```

x.get_text() -> Text
Gets the widget text

Returns:
    Text: The widget text

<a id="unreal.EditableText.get_justification"></a>

#### get_justification

```python
def get_justification() -> TextJustify
```

x.get_justification() -> TextJustify
Get Justification

Returns:
    TextJustify:

<a id="unreal.EditableText.get_hint_text"></a>

#### get_hint_text

```python
def get_hint_text() -> Text
```

x.get_hint_text() -> Text
Gets the Hint text that appears when there is no text in the text box

Returns:
    Text:

<a id="unreal.EditableText.get_font"></a>

#### get_font

```python
def get_font() -> SlateFontInfo
```

x.get_font() -> SlateFontInfo
Get Font

Returns:
    SlateFontInfo:

<a id="unreal.EditableTextBox"></a>