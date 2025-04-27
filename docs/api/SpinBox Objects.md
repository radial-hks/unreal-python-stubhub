## SpinBox Objects

```python
class SpinBox(Widget)
```

A numerical entry box that allows for direct entry of the number or allows the user to click and slide the number.

**C++ Source:**

- **Module**: UMG
- **File**: SpinBox.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``always_uses_delta_snap`` (bool):  [Read-Write] Whether this spin box should use the delta snapping logic for typed values - default false
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clear_keyboard_focus_on_commit`` (bool):  [Read-Write] Whether to remove the keyboard focus from the spin box when the value is committed
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``delta`` (float):  [Read-Write] The amount by which to change the spin box value as the slider moves.
- ``enable_slider`` (bool):  [Read-Write] Whether this spin box should have slider feature enabled
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``font`` (SlateFontInfo):  [Read-Write] Font color and opacity (overrides style)
- ``foreground_color`` (SlateColor):  [Read-Write]
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``justification`` (TextJustify):  [Read-Write] The justification the value text should appear as.
- ``keyboard_type`` (VirtualKeyboardType):  [Read-Write] If we're on a platform that requires a virtual keyboard, what kind of keyboard should this widget use?
- ``max_fractional_digits`` (int32):  [Read-Write] The maximum required fractional digits - default 6
- ``max_slider_value`` (float):  [Read-Write] The maximum allowable value that can be specified using the slider
- ``max_value`` (float):  [Read-Write] The maximum allowable value that can be manually entered into the spin box
- ``min_desired_width`` (float):  [Read-Write] The minimum width of the spin box
- ``min_fractional_digits`` (int32):  [Read-Write] The minimum required fractional digits - default 1
- ``min_slider_value`` (float):  [Read-Write] The minimum allowable value that can be specified using the slider
- ``min_value`` (float):  [Read-Write] The minimum allowable value that can be manually entered into the spin box
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_begin_slider_movement`` (OnSpinBoxBeginSliderMovement):  [Read-Write] Called right before the slider begins to move
- ``on_end_slider_movement`` (OnSpinBoxValueChangedEvent):  [Read-Write] Called right after the slider handle is released by the user
- ``on_value_changed`` (OnSpinBoxValueChangedEvent):  [Read-Write] Called when the value is changed interactively by the user
- ``on_value_committed`` (OnSpinBoxValueCommittedEvent):  [Read-Write] Called when the value is committed. Occurs when the user presses Enter or the text box loses focus.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``override_max_slider_value`` (bool):  [Read-Write] Whether the optional MaxSliderValue attribute of the widget is set
- ``override_max_value`` (bool):  [Read-Write] Whether the optional MaxValue attribute of the widget is set
- ``override_min_slider_value`` (bool):  [Read-Write] Whether the optional MinSliderValue attribute of the widget is set
- ``override_min_value`` (bool):  [Read-Write] Whether the optional MinValue attribute of the widget is set
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``select_all_text_on_commit`` (bool):  [Read-Write] Whether to select the text in the spin box when the value is committed
- ``slider_exponent`` (float):  [Read-Write] The exponent by which to increase the delta as the mouse moves. 1 is constant (never increases the delta).
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``value`` (float):  [Read-Write] Value stored in this spin box
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``widget_style`` (SpinBoxStyle):  [Read-Write] The Style

<a id="unreal.SpinBox.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write] Value stored in this spin box

<a id="unreal.SpinBox.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.SpinBox.widget_style"></a>

#### widget_style

```python
@property
def widget_style() -> SpinBoxStyle
```

(SpinBoxStyle):  [Read-Write] The Style

<a id="unreal.SpinBox.widget_style"></a>

#### widget_style

```python
@widget_style.setter
def widget_style(value: SpinBoxStyle) -> None
```

<a id="unreal.SpinBox.min_fractional_digits"></a>

#### min_fractional_digits

```python
@property
def min_fractional_digits() -> int
```

(int32):  [Read-Write] The minimum required fractional digits - default 1

<a id="unreal.SpinBox.min_fractional_digits"></a>

#### min_fractional_digits

```python
@min_fractional_digits.setter
def min_fractional_digits(value: int) -> None
```

<a id="unreal.SpinBox.max_fractional_digits"></a>

#### max_fractional_digits

```python
@property
def max_fractional_digits() -> int
```

(int32):  [Read-Write] The maximum required fractional digits - default 6

<a id="unreal.SpinBox.max_fractional_digits"></a>

#### max_fractional_digits

```python
@max_fractional_digits.setter
def max_fractional_digits(value: int) -> None
```

<a id="unreal.SpinBox.always_uses_delta_snap"></a>

#### always_uses_delta_snap

```python
@property
def always_uses_delta_snap() -> bool
```

(bool):  [Read-Write] Whether this spin box should use the delta snapping logic for typed values - default false

<a id="unreal.SpinBox.always_uses_delta_snap"></a>

#### always_uses_delta_snap

```python
@always_uses_delta_snap.setter
def always_uses_delta_snap(value: bool) -> None
```

<a id="unreal.SpinBox.enable_slider"></a>

#### enable_slider

```python
@property
def enable_slider() -> bool
```

(bool):  [Read-Write] Whether this spin box should have slider feature enabled

<a id="unreal.SpinBox.enable_slider"></a>

#### enable_slider

```python
@enable_slider.setter
def enable_slider(value: bool) -> None
```

<a id="unreal.SpinBox.delta"></a>

#### delta

```python
@property
def delta() -> float
```

(float):  [Read-Write] The amount by which to change the spin box value as the slider moves.

<a id="unreal.SpinBox.delta"></a>

#### delta

```python
@delta.setter
def delta(value: float) -> None
```

<a id="unreal.SpinBox.slider_exponent"></a>

#### slider_exponent

```python
@property
def slider_exponent() -> float
```

(float):  [Read-Write] The exponent by which to increase the delta as the mouse moves. 1 is constant (never increases the delta).

<a id="unreal.SpinBox.slider_exponent"></a>

#### slider_exponent

```python
@slider_exponent.setter
def slider_exponent(value: float) -> None
```

<a id="unreal.SpinBox.font"></a>

#### font

```python
@property
def font() -> SlateFontInfo
```

(SlateFontInfo):  [Read-Write] Font color and opacity (overrides style)

<a id="unreal.SpinBox.font"></a>

#### font

```python
@font.setter
def font(value: SlateFontInfo) -> None
```

<a id="unreal.SpinBox.justification"></a>

#### justification

```python
@property
def justification() -> TextJustify
```

(TextJustify):  [Read-Write] The justification the value text should appear as.

<a id="unreal.SpinBox.justification"></a>

#### justification

```python
@justification.setter
def justification(value: TextJustify) -> None
```

<a id="unreal.SpinBox.min_desired_width"></a>

#### min_desired_width

```python
@property
def min_desired_width() -> float
```

(float):  [Read-Write] The minimum width of the spin box

<a id="unreal.SpinBox.min_desired_width"></a>

#### min_desired_width

```python
@min_desired_width.setter
def min_desired_width(value: float) -> None
```

<a id="unreal.SpinBox.clear_keyboard_focus_on_commit"></a>

#### clear_keyboard_focus_on_commit

```python
@property
def clear_keyboard_focus_on_commit() -> bool
```

(bool):  [Read-Write] Whether to remove the keyboard focus from the spin box when the value is committed

<a id="unreal.SpinBox.clear_keyboard_focus_on_commit"></a>

#### clear_keyboard_focus_on_commit

```python
@clear_keyboard_focus_on_commit.setter
def clear_keyboard_focus_on_commit(value: bool) -> None
```

<a id="unreal.SpinBox.select_all_text_on_commit"></a>

#### select_all_text_on_commit

```python
@property
def select_all_text_on_commit() -> bool
```

(bool):  [Read-Write] Whether to select the text in the spin box when the value is committed

<a id="unreal.SpinBox.select_all_text_on_commit"></a>

#### select_all_text_on_commit

```python
@select_all_text_on_commit.setter
def select_all_text_on_commit(value: bool) -> None
```

<a id="unreal.SpinBox.foreground_color"></a>

#### foreground_color

```python
@property
def foreground_color() -> SlateColor
```

(SlateColor):  [Read-Write]

<a id="unreal.SpinBox.foreground_color"></a>

#### foreground_color

```python
@foreground_color.setter
def foreground_color(value: SlateColor) -> None
```

<a id="unreal.SpinBox.on_value_changed"></a>

#### on_value_changed

```python
@property
def on_value_changed() -> OnSpinBoxValueChangedEvent
```

(OnSpinBoxValueChangedEvent):  [Read-Write] Called when the value is changed interactively by the user

<a id="unreal.SpinBox.on_value_changed"></a>

#### on_value_changed

```python
@on_value_changed.setter
def on_value_changed(value: OnSpinBoxValueChangedEvent) -> None
```

<a id="unreal.SpinBox.on_value_committed"></a>

#### on_value_committed

```python
@property
def on_value_committed() -> OnSpinBoxValueCommittedEvent
```

(OnSpinBoxValueCommittedEvent):  [Read-Write] Called when the value is committed. Occurs when the user presses Enter or the text box loses focus.

<a id="unreal.SpinBox.on_value_committed"></a>

#### on_value_committed

```python
@on_value_committed.setter
def on_value_committed(value: OnSpinBoxValueCommittedEvent) -> None
```

<a id="unreal.SpinBox.on_begin_slider_movement"></a>

#### on_begin_slider_movement

```python
@property
def on_begin_slider_movement() -> OnSpinBoxBeginSliderMovement
```

(OnSpinBoxBeginSliderMovement):  [Read-Write] Called right before the slider begins to move

<a id="unreal.SpinBox.on_begin_slider_movement"></a>

#### on_begin_slider_movement

```python
@on_begin_slider_movement.setter
def on_begin_slider_movement(value: OnSpinBoxBeginSliderMovement) -> None
```

<a id="unreal.SpinBox.on_end_slider_movement"></a>

#### on_end_slider_movement

```python
@property
def on_end_slider_movement() -> OnSpinBoxValueChangedEvent
```

(OnSpinBoxValueChangedEvent):  [Read-Write] Called right after the slider handle is released by the user

<a id="unreal.SpinBox.on_end_slider_movement"></a>

#### on_end_slider_movement

```python
@on_end_slider_movement.setter
def on_end_slider_movement(value: OnSpinBoxValueChangedEvent) -> None
```

<a id="unreal.SpinBox.min_value"></a>

#### min_value

```python
@property
def min_value() -> float
```

(float):  [Read-Write] The minimum allowable value that can be manually entered into the spin box

<a id="unreal.SpinBox.min_value"></a>

#### min_value

```python
@min_value.setter
def min_value(value: float) -> None
```

<a id="unreal.SpinBox.max_value"></a>

#### max_value

```python
@property
def max_value() -> float
```

(float):  [Read-Write] The maximum allowable value that can be manually entered into the spin box

<a id="unreal.SpinBox.max_value"></a>

#### max_value

```python
@max_value.setter
def max_value(value: float) -> None
```

<a id="unreal.SpinBox.min_slider_value"></a>

#### min_slider_value

```python
@property
def min_slider_value() -> float
```

(float):  [Read-Write] The minimum allowable value that can be specified using the slider

<a id="unreal.SpinBox.min_slider_value"></a>

#### min_slider_value

```python
@min_slider_value.setter
def min_slider_value(value: float) -> None
```

<a id="unreal.SpinBox.max_slider_value"></a>

#### max_slider_value

```python
@property
def max_slider_value() -> float
```

(float):  [Read-Write] The maximum allowable value that can be specified using the slider

<a id="unreal.SpinBox.max_slider_value"></a>

#### max_slider_value

```python
@max_slider_value.setter
def max_slider_value(value: float) -> None
```

<a id="unreal.SpinBox.set_value"></a>

#### set_value

```python
def set_value(new_value: float) -> None
```

x.set_value(new_value) -> None
Set the value of the spin box.

Args:
    new_value (float):

<a id="unreal.SpinBox.set_min_value"></a>

#### set_min_value

```python
def set_min_value(new_value: float) -> None
```

x.set_min_value(new_value) -> None
Set the minimum value that can be manually set in the spin box.

Args:
    new_value (float):

<a id="unreal.SpinBox.set_min_slider_value"></a>

#### set_min_slider_value

```python
def set_min_slider_value(new_value: float) -> None
```

x.set_min_slider_value(new_value) -> None
Set the minimum value that can be specified using the slider.

Args:
    new_value (float):

<a id="unreal.SpinBox.set_max_value"></a>

#### set_max_value

```python
def set_max_value(new_value: float) -> None
```

x.set_max_value(new_value) -> None
Set the maximum value that can be manually set in the spin box.

Args:
    new_value (float):

<a id="unreal.SpinBox.set_max_slider_value"></a>

#### set_max_slider_value

```python
def set_max_slider_value(new_value: float) -> None
```

x.set_max_slider_value(new_value) -> None
Set the maximum value that can be specified using the slider.

Args:
    new_value (float):

<a id="unreal.SpinBox.set_foreground_color"></a>

#### set_foreground_color

```python
def set_foreground_color(foreground_color: SlateColor) -> None
```

x.set_foreground_color(foreground_color) -> None
Set Foreground Color

Args:
    foreground_color (SlateColor):

<a id="unreal.SpinBox.get_value"></a>

#### get_value

```python
def get_value() -> float
```

x.get_value() -> float
Get the current value of the spin box.

Returns:
    float:

<a id="unreal.SpinBox.get_min_value"></a>

#### get_min_value

```python
def get_min_value() -> float
```

x.get_min_value() -> float
Get the current minimum value that can be manually set in the spin box.

Returns:
    float:

<a id="unreal.SpinBox.get_min_slider_value"></a>

#### get_min_slider_value

```python
def get_min_slider_value() -> float
```

x.get_min_slider_value() -> float
Get the current minimum value that can be specified using the slider.

Returns:
    float:

<a id="unreal.SpinBox.get_max_value"></a>

#### get_max_value

```python
def get_max_value() -> float
```

x.get_max_value() -> float
Get the current maximum value that can be manually set in the spin box.

Returns:
    float:

<a id="unreal.SpinBox.get_max_slider_value"></a>

#### get_max_slider_value

```python
def get_max_slider_value() -> float
```

x.get_max_slider_value() -> float
Get the current maximum value that can be specified using the slider.

Returns:
    float:

<a id="unreal.SpinBox.clear_min_value"></a>

#### clear_min_value

```python
def clear_min_value() -> None
```

x.clear_min_value() -> None
Clear the minimum value that can be manually set in the spin box.

<a id="unreal.SpinBox.clear_min_slider_value"></a>

#### clear_min_slider_value

```python
def clear_min_slider_value() -> None
```

x.clear_min_slider_value() -> None
Clear the minimum value that can be specified using the slider.

<a id="unreal.SpinBox.clear_max_value"></a>

#### clear_max_value

```python
def clear_max_value() -> None
```

x.clear_max_value() -> None
Clear the maximum value that can be manually set in the spin box.

<a id="unreal.SpinBox.clear_max_slider_value"></a>

#### clear_max_slider_value

```python
def clear_max_slider_value() -> None
```

x.clear_max_slider_value() -> None
Clear the maximum value that can be specified using the slider.

<a id="unreal.StackBox"></a>