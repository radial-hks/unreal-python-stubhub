## Synth2DSlider Objects

```python
class Synth2DSlider(Widget)
```

A simple widget that shows a sliding bar with a handle that allows you to control the value between 0..1.

* No Children

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: Synth2DSlider.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``indent_handle`` (bool):  [Read-Write] Whether the slidable area should be indented to fit the handle.
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_focusable`` (bool):  [Read-Write] Should the slider be focusable?
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``locked`` (bool):  [Read-Write] Whether the handle is interactive or fixed.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_controller_capture_begin`` (OnControllerCaptureBeginEventSynth2D):  [Read-Write] Invoked when the controller capture begins.
- ``on_controller_capture_end`` (OnControllerCaptureEndEventSynth2D):  [Read-Write] Invoked when the controller capture ends.
- ``on_mouse_capture_begin`` (OnMouseCaptureBeginEventSynth2D):  [Read-Write] Invoked when the mouse is pressed and a capture begins.
- ``on_mouse_capture_end`` (OnMouseCaptureEndEventSynth2D):  [Read-Write] Invoked when the mouse is released and a capture ends.
- ``on_value_changed_x`` (OnFloatValueChangedEventSynth2D):  [Read-Write] Called when the value is changed by slider or typing.
- ``on_value_changed_y`` (OnFloatValueChangedEventSynth2D):  [Read-Write] Called when the value is changed by slider or typing.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``slider_handle_color`` (LinearColor):  [Read-Write] The color to draw the slider handle in.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``step_size`` (float):  [Read-Write] The amount to adjust the value by, when using a controller or keyboard
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``value_x`` (float):  [Read-Write]
- ``value_y`` (float):  [Read-Write]
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``widget_style`` (Synth2DSliderStyle):  [Read-Write] The progress bar style

<a id="unreal.Synth2DSlider.widget_style"></a>

#### widget_style

```python
@property
def widget_style() -> Synth2DSliderStyle
```

(Synth2DSliderStyle):  [Read-Write] The progress bar style

<a id="unreal.Synth2DSlider.widget_style"></a>

#### widget_style

```python
@widget_style.setter
def widget_style(value: Synth2DSliderStyle) -> None
```

<a id="unreal.Synth2DSlider.slider_handle_color"></a>

#### slider_handle_color

```python
@property
def slider_handle_color() -> LinearColor
```

(LinearColor):  [Read-Only] The color to draw the slider handle in.

<a id="unreal.Synth2DSlider.indent_handle"></a>

#### indent_handle

```python
@property
def indent_handle() -> bool
```

(bool):  [Read-Only] Whether the slidable area should be indented to fit the handle.

<a id="unreal.Synth2DSlider.locked"></a>

#### locked

```python
@property
def locked() -> bool
```

(bool):  [Read-Only] Whether the handle is interactive or fixed.

<a id="unreal.Synth2DSlider.step_size"></a>

#### step_size

```python
@property
def step_size() -> float
```

(float):  [Read-Only] The amount to adjust the value by, when using a controller or keyboard

<a id="unreal.Synth2DSlider.is_focusable"></a>

#### is_focusable

```python
@property
def is_focusable() -> bool
```

(bool):  [Read-Only] Should the slider be focusable?

<a id="unreal.Synth2DSlider.on_mouse_capture_begin"></a>

#### on_mouse_capture_begin

```python
@property
def on_mouse_capture_begin() -> OnMouseCaptureBeginEventSynth2D
```

(OnMouseCaptureBeginEventSynth2D):  [Read-Write] Invoked when the mouse is pressed and a capture begins.

<a id="unreal.Synth2DSlider.on_mouse_capture_begin"></a>

#### on_mouse_capture_begin

```python
@on_mouse_capture_begin.setter
def on_mouse_capture_begin(value: OnMouseCaptureBeginEventSynth2D) -> None
```

<a id="unreal.Synth2DSlider.on_mouse_capture_end"></a>

#### on_mouse_capture_end

```python
@property
def on_mouse_capture_end() -> OnMouseCaptureEndEventSynth2D
```

(OnMouseCaptureEndEventSynth2D):  [Read-Write] Invoked when the mouse is released and a capture ends.

<a id="unreal.Synth2DSlider.on_mouse_capture_end"></a>

#### on_mouse_capture_end

```python
@on_mouse_capture_end.setter
def on_mouse_capture_end(value: OnMouseCaptureEndEventSynth2D) -> None
```

<a id="unreal.Synth2DSlider.on_controller_capture_begin"></a>

#### on_controller_capture_begin

```python
@property
def on_controller_capture_begin() -> OnControllerCaptureBeginEventSynth2D
```

(OnControllerCaptureBeginEventSynth2D):  [Read-Write] Invoked when the controller capture begins.

<a id="unreal.Synth2DSlider.on_controller_capture_begin"></a>

#### on_controller_capture_begin

```python
@on_controller_capture_begin.setter
def on_controller_capture_begin(
        value: OnControllerCaptureBeginEventSynth2D) -> None
```

<a id="unreal.Synth2DSlider.on_controller_capture_end"></a>

#### on_controller_capture_end

```python
@property
def on_controller_capture_end() -> OnControllerCaptureEndEventSynth2D
```

(OnControllerCaptureEndEventSynth2D):  [Read-Write] Invoked when the controller capture ends.

<a id="unreal.Synth2DSlider.on_controller_capture_end"></a>

#### on_controller_capture_end

```python
@on_controller_capture_end.setter
def on_controller_capture_end(
        value: OnControllerCaptureEndEventSynth2D) -> None
```

<a id="unreal.Synth2DSlider.on_value_changed_x"></a>

#### on_value_changed_x

```python
@property
def on_value_changed_x() -> OnFloatValueChangedEventSynth2D
```

(OnFloatValueChangedEventSynth2D):  [Read-Write] Called when the value is changed by slider or typing.

<a id="unreal.Synth2DSlider.on_value_changed_x"></a>

#### on_value_changed_x

```python
@on_value_changed_x.setter
def on_value_changed_x(value: OnFloatValueChangedEventSynth2D) -> None
```

<a id="unreal.Synth2DSlider.on_value_changed_y"></a>

#### on_value_changed_y

```python
@property
def on_value_changed_y() -> OnFloatValueChangedEventSynth2D
```

(OnFloatValueChangedEventSynth2D):  [Read-Write] Called when the value is changed by slider or typing.

<a id="unreal.Synth2DSlider.on_value_changed_y"></a>

#### on_value_changed_y

```python
@on_value_changed_y.setter
def on_value_changed_y(value: OnFloatValueChangedEventSynth2D) -> None
```

<a id="unreal.Synth2DSlider.set_value"></a>

#### set_value

```python
def set_value(value: Vector2D) -> None
```

x.set_value(value) -> None
Sets the current value of the slider.

Args:
    value (Vector2D):

<a id="unreal.Synth2DSlider.set_step_size"></a>

#### set_step_size

```python
def set_step_size(value: float) -> None
```

x.set_step_size(value) -> None
Sets the amount to adjust the value by, when using a controller or keyboard

Args:
    value (float):

<a id="unreal.Synth2DSlider.set_slider_handle_color"></a>

#### set_slider_handle_color

```python
def set_slider_handle_color(value: LinearColor) -> None
```

x.set_slider_handle_color(value) -> None
Sets the color of the handle bar

Args:
    value (LinearColor):

<a id="unreal.Synth2DSlider.set_locked"></a>

#### set_locked

```python
def set_locked(value: bool) -> None
```

x.set_locked(value) -> None
Sets the handle to be interactive or fixed

Args:
    value (bool):

<a id="unreal.Synth2DSlider.set_indent_handle"></a>

#### set_indent_handle

```python
def set_indent_handle(value: bool) -> None
```

x.set_indent_handle(value) -> None
Sets if the slidable area should be indented to fit the handle

Args:
    value (bool):

<a id="unreal.Synth2DSlider.get_value"></a>

#### get_value

```python
def get_value() -> Vector2D
```

x.get_value() -> Vector2D
Gets the current value of the slider.

Returns:
    Vector2D:

<a id="unreal.SynthKnob"></a>