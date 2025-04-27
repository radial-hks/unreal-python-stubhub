## AudioOscilloscope Objects

```python
class AudioOscilloscope(Widget)
```

An oscilloscope UMG widget.

Supports displaying waveforms from incoming audio samples.

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioOscilloscopeUMG.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``amplitude_grid_labels_unit`` (YAxisLabelsUnit):  [Read-Write] Define the amplitude grid labels unit.
- ``analysis_period_ms`` (float):  [Read-Write] The analysis period in milliseconds.
- ``audio_bus`` (AudioBus):  [Read-Write] The audio bus used to obtain audio samples for the oscilloscope
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``channel_to_analyze`` (int32):  [Read-Write] The channel to analyze with the oscilloscope (only available if PanelLayoutType is set to "Advanced").
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
- ``max_time_window_ms`` (float):  [Read-Write] The max time window in milliseconds.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``oscilloscope_style`` (AudioOscilloscopePanelStyle):  [Read-Write] The oscilloscope panel style
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``panel_layout_type`` (AudioPanelLayoutType):  [Read-Write] Show/Hide advanced panel layout.
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``show_amplitude_grid`` (bool):  [Read-Write] Show/Hide the amplitude grid.
- ``show_amplitude_labels`` (bool):  [Read-Write] Show/Hide the amplitude labels.
- ``show_time_grid`` (bool):  [Read-Write] Show/Hide the time grid.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``time_grid_labels_unit`` (XAxisLabelsUnit):  [Read-Write] Define the time grid labels unit.
- ``time_window_ms`` (float):  [Read-Write] The time window in milliseconds.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``trigger_mode`` (AudioOscilloscopeTriggerMode):  [Read-Write] The trigger detection behavior.
- ``trigger_threshold`` (float):  [Read-Write] The trigger threshold position in the Y axis.
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.AudioOscilloscope.oscilloscope_style"></a>

#### oscilloscope_style

```python
@property
def oscilloscope_style() -> AudioOscilloscopePanelStyle
```

(AudioOscilloscopePanelStyle):  [Read-Only] The oscilloscope panel style

<a id="unreal.AudioOscilloscope.audio_bus"></a>

#### audio_bus

```python
@property
def audio_bus() -> AudioBus
```

(AudioBus):  [Read-Only] The audio bus used to obtain audio samples for the oscilloscope

<a id="unreal.AudioOscilloscope.max_time_window_ms"></a>

#### max_time_window_ms

```python
@property
def max_time_window_ms() -> float
```

(float):  [Read-Only] The max time window in milliseconds.

<a id="unreal.AudioOscilloscope.time_window_ms"></a>

#### time_window_ms

```python
@property
def time_window_ms() -> float
```

(float):  [Read-Only] The time window in milliseconds.

<a id="unreal.AudioOscilloscope.analysis_period_ms"></a>

#### analysis_period_ms

```python
@property
def analysis_period_ms() -> float
```

(float):  [Read-Only] The analysis period in milliseconds.

<a id="unreal.AudioOscilloscope.show_time_grid"></a>

#### show_time_grid

```python
@property
def show_time_grid() -> bool
```

(bool):  [Read-Only] Show/Hide the time grid.

<a id="unreal.AudioOscilloscope.time_grid_labels_unit"></a>

#### time_grid_labels_unit

```python
@property
def time_grid_labels_unit() -> XAxisLabelsUnit
```

(XAxisLabelsUnit):  [Read-Only] Define the time grid labels unit.

<a id="unreal.AudioOscilloscope.show_amplitude_grid"></a>

#### show_amplitude_grid

```python
@property
def show_amplitude_grid() -> bool
```

(bool):  [Read-Only] Show/Hide the amplitude grid.

<a id="unreal.AudioOscilloscope.show_amplitude_labels"></a>

#### show_amplitude_labels

```python
@property
def show_amplitude_labels() -> bool
```

(bool):  [Read-Only] Show/Hide the amplitude labels.

<a id="unreal.AudioOscilloscope.amplitude_grid_labels_unit"></a>

#### amplitude_grid_labels_unit

```python
@property
def amplitude_grid_labels_unit() -> YAxisLabelsUnit
```

(YAxisLabelsUnit):  [Read-Only] Define the amplitude grid labels unit.

<a id="unreal.AudioOscilloscope.trigger_mode"></a>

#### trigger_mode

```python
@property
def trigger_mode() -> AudioOscilloscopeTriggerMode
```

(AudioOscilloscopeTriggerMode):  [Read-Only] The trigger detection behavior.

<a id="unreal.AudioOscilloscope.trigger_threshold"></a>

#### trigger_threshold

```python
@property
def trigger_threshold() -> float
```

(float):  [Read-Only] The trigger threshold position in the Y axis.

<a id="unreal.AudioOscilloscope.panel_layout_type"></a>

#### panel_layout_type

```python
@property
def panel_layout_type() -> AudioPanelLayoutType
```

(AudioPanelLayoutType):  [Read-Only] Show/Hide advanced panel layout.

<a id="unreal.AudioOscilloscope.channel_to_analyze"></a>

#### channel_to_analyze

```python
@property
def channel_to_analyze() -> int
```

(int32):  [Read-Only] The channel to analyze with the oscilloscope (only available if PanelLayoutType is set to "Advanced").

<a id="unreal.AudioOscilloscope.stop_processing"></a>

#### stop_processing

```python
def stop_processing() -> None
```

x.stop_processing() -> None
Stops the oscilloscope processing.

<a id="unreal.AudioOscilloscope.start_processing"></a>

#### start_processing

```python
def start_processing() -> None
```

x.start_processing() -> None
Starts the oscilloscope processing.

<a id="unreal.AudioRadialSlider"></a>