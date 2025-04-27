## AudioMeter Objects

```python
class AudioMeter(Widget)
```

An audio meter widget.

Supports displaying a slower moving peak-hold value as well as the current meter value.

A clipping value is also displayed which shows a customizable color to indicate clipping.

Internal values are stored and interacted with as linear volume values.

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioMeter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``background_color`` (LinearColor):  [Read-Write] The color to draw the background.
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``meter_background_color`` (LinearColor):  [Read-Write] The color to draw the meter background.
- ``meter_channel_info`` (Array[MeterChannelInfo]):  [Read-Write] The current meter value to display.
- ``meter_clipping_color`` (LinearColor):  [Read-Write] The color to draw the meter clipping value.
- ``meter_peak_color`` (LinearColor):  [Read-Write] The color to draw the meter peak value.
- ``meter_scale_color`` (LinearColor):  [Read-Write] The color to draw the meter scale hashes.
- ``meter_scale_label_color`` (LinearColor):  [Read-Write] The color to draw the meter scale label.
- ``meter_value_color`` (LinearColor):  [Read-Write] The color to draw the meter value.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``orientation`` (Orientation):  [Read-Write] The slider's orientation.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``widget_style`` (AudioMeterStyle):  [Read-Write] The audio meter style

<a id="unreal.AudioMeter.widget_style"></a>

#### widget_style

```python
@property
def widget_style() -> AudioMeterStyle
```

(AudioMeterStyle):  [Read-Write] The audio meter style

<a id="unreal.AudioMeter.widget_style"></a>

#### widget_style

```python
@widget_style.setter
def widget_style(value: AudioMeterStyle) -> None
```

<a id="unreal.AudioMeter.orientation"></a>

#### orientation

```python
@property
def orientation() -> Orientation
```

(Orientation):  [Read-Only] The slider's orientation.

<a id="unreal.AudioMeter.background_color"></a>

#### background_color

```python
@property
def background_color() -> LinearColor
```

(LinearColor):  [Read-Only] The color to draw the background.

<a id="unreal.AudioMeter.meter_background_color"></a>

#### meter_background_color

```python
@property
def meter_background_color() -> LinearColor
```

(LinearColor):  [Read-Only] The color to draw the meter background.

<a id="unreal.AudioMeter.meter_value_color"></a>

#### meter_value_color

```python
@property
def meter_value_color() -> LinearColor
```

(LinearColor):  [Read-Only] The color to draw the meter value.

<a id="unreal.AudioMeter.meter_peak_color"></a>

#### meter_peak_color

```python
@property
def meter_peak_color() -> LinearColor
```

(LinearColor):  [Read-Only] The color to draw the meter peak value.

<a id="unreal.AudioMeter.meter_clipping_color"></a>

#### meter_clipping_color

```python
@property
def meter_clipping_color() -> LinearColor
```

(LinearColor):  [Read-Only] The color to draw the meter clipping value.

<a id="unreal.AudioMeter.meter_scale_color"></a>

#### meter_scale_color

```python
@property
def meter_scale_color() -> LinearColor
```

(LinearColor):  [Read-Only] The color to draw the meter scale hashes.

<a id="unreal.AudioMeter.meter_scale_label_color"></a>

#### meter_scale_label_color

```python
@property
def meter_scale_label_color() -> LinearColor
```

(LinearColor):  [Read-Only] The color to draw the meter scale label.

<a id="unreal.AudioMeter.set_meter_value_color"></a>

#### set_meter_value_color

```python
def set_meter_value_color(value: LinearColor) -> None
```

x.set_meter_value_color(value) -> None
Sets the meter value color

Args:
    value (LinearColor):

<a id="unreal.AudioMeter.set_meter_scale_label_color"></a>

#### set_meter_scale_label_color

```python
def set_meter_scale_label_color(value: LinearColor) -> None
```

x.set_meter_scale_label_color(value) -> None
Sets the meter scale color

Args:
    value (LinearColor):

<a id="unreal.AudioMeter.set_meter_scale_color"></a>

#### set_meter_scale_color

```python
def set_meter_scale_color(value: LinearColor) -> None
```

x.set_meter_scale_color(value) -> None
Sets the meter scale color

Args:
    value (LinearColor):

<a id="unreal.AudioMeter.set_meter_peak_color"></a>

#### set_meter_peak_color

```python
def set_meter_peak_color(value: LinearColor) -> None
```

x.set_meter_peak_color(value) -> None
Sets the meter peak color

Args:
    value (LinearColor):

<a id="unreal.AudioMeter.set_meter_clipping_color"></a>

#### set_meter_clipping_color

```python
def set_meter_clipping_color(value: LinearColor) -> None
```

x.set_meter_clipping_color(value) -> None
Sets the meter clipping color

Args:
    value (LinearColor):

<a id="unreal.AudioMeter.set_meter_channel_info"></a>

#### set_meter_channel_info

```python
def set_meter_channel_info(
        meter_channel_info: Array[MeterChannelInfo]) -> None
```

x.set_meter_channel_info(meter_channel_info) -> None
Sets the current meter values.

Args:
    meter_channel_info (Array[MeterChannelInfo]):

<a id="unreal.AudioMeter.set_meter_background_color"></a>

#### set_meter_background_color

```python
def set_meter_background_color(value: LinearColor) -> None
```

x.set_meter_background_color(value) -> None
Sets the meter background color

Args:
    value (LinearColor):

<a id="unreal.AudioMeter.set_background_color"></a>

#### set_background_color

```python
def set_background_color(value: LinearColor) -> None
```

x.set_background_color(value) -> None
Sets the background color

Args:
    value (LinearColor):

<a id="unreal.AudioMeter.get_meter_channel_info"></a>

#### get_meter_channel_info

```python
def get_meter_channel_info() -> Array[MeterChannelInfo]
```

x.get_meter_channel_info() -> Array[MeterChannelInfo]
Gets the current linear value of the meter.

Returns:
    Array[MeterChannelInfo]:

<a id="unreal.AudioOscilloscope"></a>