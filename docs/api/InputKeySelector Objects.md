## InputKeySelector Objects

```python
class InputKeySelector(Widget)
```

A widget for selecting a single key or a single key with a modifier.

**C++ Source:**

- **Module**: UMG
- **File**: InputKeySelector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``allow_gamepad_keys`` (bool):  [Read-Write] When true gamepad keys are allowed in the input chord representing the selected key, otherwise they are ignored.
- ``allow_modifier_keys`` (bool):  [Read-Write] When true modifier keys such as control and alt are allowed in the
  input chord representing the selected key, if false modifier keys are ignored.
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``escape_keys`` (Array[Key]):  [Read-Write] When true gamepad keys are allowed in the input chord representing the selected key, otherwise they are ignored.
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``key_selection_text`` (Text):  [Read-Write] Sets the text which is displayed while selecting keys.
- ``margin`` (Margin):  [Read-Write] The amount of blank space around the text used to display the currently selected key.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``no_key_specified_text`` (Text):  [Read-Write] Sets the text to display when no key text is available or not selecting a key.
- ``on_is_selecting_key_changed`` (OnIsSelectingKeyChanged):  [Read-Write] Called whenever the key selection mode starts or stops.
- ``on_key_selected`` (OnKeySelected):  [Read-Write] Called whenever a new key is selected by the user.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``selected_key`` (InputChord):  [Read-Write] The currently selected key chord.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``text_style`` (TextBlockStyle):  [Read-Write] The button style used at runtime
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``widget_style`` (ButtonStyle):  [Read-Write] The button style used at runtime

<a id="unreal.InputKeySelector.widget_style"></a>

#### widget_style

```python
@property
def widget_style() -> ButtonStyle
```

(ButtonStyle):  [Read-Write] The button style used at runtime

<a id="unreal.InputKeySelector.widget_style"></a>

#### widget_style

```python
@widget_style.setter
def widget_style(value: ButtonStyle) -> None
```

<a id="unreal.InputKeySelector.text_style"></a>

#### text_style

```python
@property
def text_style() -> TextBlockStyle
```

(TextBlockStyle):  [Read-Write] The button style used at runtime

<a id="unreal.InputKeySelector.text_style"></a>

#### text_style

```python
@text_style.setter
def text_style(value: TextBlockStyle) -> None
```

<a id="unreal.InputKeySelector.selected_key"></a>

#### selected_key

```python
@property
def selected_key() -> InputChord
```

(InputChord):  [Read-Write] The currently selected key chord.

<a id="unreal.InputKeySelector.selected_key"></a>

#### selected_key

```python
@selected_key.setter
def selected_key(value: InputChord) -> None
```

<a id="unreal.InputKeySelector.margin"></a>

#### margin

```python
@property
def margin() -> Margin
```

(Margin):  [Read-Write] The amount of blank space around the text used to display the currently selected key.

<a id="unreal.InputKeySelector.margin"></a>

#### margin

```python
@margin.setter
def margin(value: Margin) -> None
```

<a id="unreal.InputKeySelector.key_selection_text"></a>

#### key_selection_text

```python
@property
def key_selection_text() -> Text
```

(Text):  [Read-Write] Sets the text which is displayed while selecting keys.

<a id="unreal.InputKeySelector.key_selection_text"></a>

#### key_selection_text

```python
@key_selection_text.setter
def key_selection_text(value: Text) -> None
```

<a id="unreal.InputKeySelector.no_key_specified_text"></a>

#### no_key_specified_text

```python
@property
def no_key_specified_text() -> Text
```

(Text):  [Read-Write] Sets the text to display when no key text is available or not selecting a key.

<a id="unreal.InputKeySelector.no_key_specified_text"></a>

#### no_key_specified_text

```python
@no_key_specified_text.setter
def no_key_specified_text(value: Text) -> None
```

<a id="unreal.InputKeySelector.allow_modifier_keys"></a>

#### allow_modifier_keys

```python
@property
def allow_modifier_keys() -> bool
```

(bool):  [Read-Write] When true modifier keys such as control and alt are allowed in the
input chord representing the selected key, if false modifier keys are ignored.

<a id="unreal.InputKeySelector.allow_modifier_keys"></a>

#### allow_modifier_keys

```python
@allow_modifier_keys.setter
def allow_modifier_keys(value: bool) -> None
```

<a id="unreal.InputKeySelector.allow_gamepad_keys"></a>

#### allow_gamepad_keys

```python
@property
def allow_gamepad_keys() -> bool
```

(bool):  [Read-Write] When true gamepad keys are allowed in the input chord representing the selected key, otherwise they are ignored.

<a id="unreal.InputKeySelector.allow_gamepad_keys"></a>

#### allow_gamepad_keys

```python
@allow_gamepad_keys.setter
def allow_gamepad_keys(value: bool) -> None
```

<a id="unreal.InputKeySelector.escape_keys"></a>

#### escape_keys

```python
@property
def escape_keys() -> Array[Key]
```

(Array[Key]):  [Read-Only] When true gamepad keys are allowed in the input chord representing the selected key, otherwise they are ignored.

<a id="unreal.InputKeySelector.on_key_selected"></a>

#### on_key_selected

```python
@property
def on_key_selected() -> OnKeySelected
```

(OnKeySelected):  [Read-Write] Called whenever a new key is selected by the user.

<a id="unreal.InputKeySelector.on_key_selected"></a>

#### on_key_selected

```python
@on_key_selected.setter
def on_key_selected(value: OnKeySelected) -> None
```

<a id="unreal.InputKeySelector.on_is_selecting_key_changed"></a>

#### on_is_selecting_key_changed

```python
@property
def on_is_selecting_key_changed() -> OnIsSelectingKeyChanged
```

(OnIsSelectingKeyChanged):  [Read-Write] Called whenever the key selection mode starts or stops.

<a id="unreal.InputKeySelector.on_is_selecting_key_changed"></a>

#### on_is_selecting_key_changed

```python
@on_is_selecting_key_changed.setter
def on_is_selecting_key_changed(value: OnIsSelectingKeyChanged) -> None
```

<a id="unreal.InputKeySelector.set_text_block_visibility"></a>

#### set_text_block_visibility

```python
def set_text_block_visibility(visibility: SlateVisibility) -> None
```

x.set_text_block_visibility(visibility) -> None
Sets the visibility of the text block.

Args:
    visibility (SlateVisibility):

<a id="unreal.InputKeySelector.set_selected_key"></a>

#### set_selected_key

```python
def set_selected_key(selected_key: InputChord) -> None
```

x.set_selected_key(selected_key) -> None
Sets the currently selected key.

Args:
    selected_key (InputChord):

<a id="unreal.InputKeySelector.set_no_key_specified_text"></a>

#### set_no_key_specified_text

```python
def set_no_key_specified_text(no_key_specified_text: Text) -> None
```

x.set_no_key_specified_text(no_key_specified_text) -> None
Sets the text to display when no key text is available or not selecting a key.

Args:
    no_key_specified_text (Text):

<a id="unreal.InputKeySelector.set_key_selection_text"></a>

#### set_key_selection_text

```python
def set_key_selection_text(key_selection_text: Text) -> None
```

x.set_key_selection_text(key_selection_text) -> None
Sets the text which is displayed while selecting keys.

Args:
    key_selection_text (Text):

<a id="unreal.InputKeySelector.set_escape_keys"></a>

#### set_escape_keys

```python
def set_escape_keys(keys: Array[Key]) -> None
```

x.set_escape_keys(keys) -> None
Sets escape keys.

Args:
    keys (Array[Key]):

<a id="unreal.InputKeySelector.set_allow_modifier_keys"></a>

#### set_allow_modifier_keys

```python
def set_allow_modifier_keys(allow_modifier_keys: bool) -> None
```

x.set_allow_modifier_keys(allow_modifier_keys) -> None
Sets whether or not modifier keys are allowed in the selected key.

Args:
    allow_modifier_keys (bool):

<a id="unreal.InputKeySelector.set_allow_gamepad_keys"></a>

#### set_allow_gamepad_keys

```python
def set_allow_gamepad_keys(allow_gamepad_keys: bool) -> None
```

x.set_allow_gamepad_keys(allow_gamepad_keys) -> None
Sets whether or not gamepad keys are allowed in the selected key.

Args:
    allow_gamepad_keys (bool):

<a id="unreal.InputKeySelector.get_is_selecting_key"></a>

#### get_is_selecting_key

```python
def get_is_selecting_key() -> bool
```

x.get_is_selecting_key() -> bool
Returns true if the widget is currently selecting a key, otherwise returns false.

Returns:
    bool:

<a id="unreal.InvalidationBox"></a>