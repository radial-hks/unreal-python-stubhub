## AudioRadialSlider Objects

```python
class AudioRadialSlider(Widget)
```

An audio radial slider widget.

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioRadialSlider.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``center_background_color`` (LinearColor):  [Read-Write] The color to draw the widget background.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``hand_start_end_ratio`` (Vector2D):  [Read-Write] Start and end of the hand as a ratio to the slider radius (so 0.0 to 1.0 is from the slider center to the handle).
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_units_text_read_only`` (bool):  [Read-Write] Whether to set the units part of the text label read only.
- ``is_value_text_read_only`` (bool):  [Read-Write] Whether to set the value part of the text label read only.
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_value_changed`` (OnAudioRadialSliderValueChangedEvent):  [Read-Write] Called when the value is changed by slider or typing.
- ``output_range`` (Vector2D):  [Read-Write] Output range
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``show_label_only_on_hover`` (bool):  [Read-Write] If true, show text label only on hover; if false always show label.
- ``show_units_text`` (bool):  [Read-Write] Whether to show the units part of the text label.
- ``slider_bar_color`` (LinearColor):  [Read-Write] The color to draw the slider bar in.
- ``slider_progress_color`` (LinearColor):  [Read-Write] The color to draw the slider progress bar in.
- ``slider_thickness`` (float):  [Read-Write] The slider thickness.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``text_label_background_color`` (LinearColor):  [Read-Write] The color to draw the text label background.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``units_text`` (Text):  [Read-Write] The text label units
- ``value`` (float):  [Read-Write] The normalized linear (0 - 1) slider value position.
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``widget_layout`` (AudioRadialSliderLayout):  [Read-Write] The layout of the widget (position of text label).

<a id="unreal.AudioRadialSlider.on_value_changed"></a>

#### on_value_changed

```python
@property
def on_value_changed() -> OnAudioRadialSliderValueChangedEvent
```

(OnAudioRadialSliderValueChangedEvent):  [Read-Write] Called when the value is changed by slider or typing.

<a id="unreal.AudioRadialSlider.on_value_changed"></a>

#### on_value_changed

```python
@on_value_changed.setter
def on_value_changed(value: OnAudioRadialSliderValueChangedEvent) -> None
```

<a id="unreal.AudioRadialSlider.set_widget_layout"></a>

#### set_widget_layout

```python
def set_widget_layout(layout: AudioRadialSliderLayout) -> None
```

x.set_widget_layout(layout) -> None
Sets the widget layout

Args:
    layout (AudioRadialSliderLayout):

<a id="unreal.AudioRadialSlider.set_value_text_read_only"></a>

#### set_value_text_read_only

```python
def set_value_text_read_only(is_read_only: bool) -> None
```

x.set_value_text_read_only(is_read_only) -> None
Sets whether the value text is read only

Args:
    is_read_only (bool):

<a id="unreal.AudioRadialSlider.set_units_text_read_only"></a>

#### set_units_text_read_only

```python
def set_units_text_read_only(is_read_only: bool) -> None
```

x.set_units_text_read_only(is_read_only) -> None
Sets whether the units text is read only

Args:
    is_read_only (bool):

<a id="unreal.AudioRadialSlider.set_units_text"></a>

#### set_units_text

```python
def set_units_text(units: Text) -> None
```

x.set_units_text(units) -> None
Sets the units text

Args:
    units (Text):

<a id="unreal.AudioRadialSlider.set_text_label_background_color"></a>

#### set_text_label_background_color

```python
def set_text_label_background_color(color: SlateColor) -> None
```

x.set_text_label_background_color(color) -> None
Sets the label background color

Args:
    color (SlateColor):

<a id="unreal.AudioRadialSlider.set_slider_thickness"></a>

#### set_slider_thickness

```python
def set_slider_thickness(thickness: float) -> None
```

x.set_slider_thickness(thickness) -> None
Sets the slider thickness

Args:
    thickness (float):

<a id="unreal.AudioRadialSlider.set_slider_progress_color"></a>

#### set_slider_progress_color

```python
def set_slider_progress_color(value: LinearColor) -> None
```

x.set_slider_progress_color(value) -> None
Sets the slider progress color

Args:
    value (LinearColor):

<a id="unreal.AudioRadialSlider.set_slider_bar_color"></a>

#### set_slider_bar_color

```python
def set_slider_bar_color(value: LinearColor) -> None
```

x.set_slider_bar_color(value) -> None
Sets the slider bar color

Args:
    value (LinearColor):

<a id="unreal.AudioRadialSlider.set_show_units_text"></a>

#### set_show_units_text

```python
def set_show_units_text(show_units_text: bool) -> None
```

x.set_show_units_text(show_units_text) -> None
Sets whether to show the units text

Args:
    show_units_text (bool):

<a id="unreal.AudioRadialSlider.set_show_label_only_on_hover"></a>

#### set_show_label_only_on_hover

```python
def set_show_label_only_on_hover(show_label_only_on_hover: bool) -> None
```

x.set_show_label_only_on_hover(show_label_only_on_hover) -> None
If true, show text label only on hover; if false always show label.

Args:
    show_label_only_on_hover (bool):

<a id="unreal.AudioRadialSlider.set_output_range"></a>

#### set_output_range

```python
def set_output_range(output_range: Vector2D) -> None
```

x.set_output_range(output_range) -> None
Sets the output range

Args:
    output_range (Vector2D):

<a id="unreal.AudioRadialSlider.set_hand_start_end_ratio"></a>

#### set_hand_start_end_ratio

```python
def set_hand_start_end_ratio(hand_start_end_ratio: Vector2D) -> None
```

x.set_hand_start_end_ratio(hand_start_end_ratio) -> None
Sets the start and end of the hand as a ratio to the slider radius (so 0.0 to 1.0 is from the slider center to the handle).

Args:
    hand_start_end_ratio (Vector2D):

<a id="unreal.AudioRadialSlider.set_center_background_color"></a>

#### set_center_background_color

```python
def set_center_background_color(value: LinearColor) -> None
```

x.set_center_background_color(value) -> None
Sets the label background color

Args:
    value (LinearColor):

<a id="unreal.AudioRadialSlider.get_slider_value"></a>

#### get_slider_value

```python
def get_slider_value(output_value: float) -> float
```

x.get_slider_value(output_value) -> float
Get normalized linear (0 - 1) slider value from output based on internal lin to output mapping.

Args:
    output_value (float): 

Returns:
    float:

<a id="unreal.AudioRadialSlider.get_output_value"></a>

#### get_output_value

```python
def get_output_value(slider_value: float) -> float
```

x.get_output_value(slider_value) -> float
Get output value from normalized linear (0 - 1) based on internal lin to output mapping.

Args:
    slider_value (float): 

Returns:
    float:

<a id="unreal.AudioVolumeRadialSlider"></a>