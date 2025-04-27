## RadialSlider Objects

```python
class RadialSlider(Widget)
```

A simple widget that shows a sliding bar with a handle that allows you to control the value between 0..1.

* No Children

**C++ Source:**

- **Module**: AdvancedWidgets
- **File**: RadialSlider.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``angular_offset`` (float):  [Read-Write] Rotates radial slider by arbitrary offset to support full gamut of configurations.
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``center_background_color`` (LinearColor):  [Read-Write] The color to draw the center background in.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``custom_default_value`` (float):  [Read-Write] The value where the slider should draw it's progress bar from, independent of direction
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``hand_start_end_ratio`` (Vector2D):  [Read-Write] Start and end of the hand as a ratio to the slider radius (so 0.0 to 1.0 is from the slider center to the handle).
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_focusable`` (bool):  [Read-Write] Should the slider be focusable?
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``locked`` (bool):  [Read-Write] Whether the handle is interactive or fixed.
- ``mouse_uses_step`` (bool):  [Read-Write] Sets new value if mouse position is greater/less than half the step size.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_controller_capture_begin`` (OnControllerCaptureBeginEvent):  [Read-Write] Invoked when the controller capture begins.
- ``on_controller_capture_end`` (OnControllerCaptureEndEvent):  [Read-Write] Invoked when the controller capture ends.
- ``on_mouse_capture_begin`` (OnMouseCaptureBeginEvent):  [Read-Write] Invoked when the mouse is pressed and a capture begins.
- ``on_mouse_capture_end`` (OnMouseCaptureEndEvent):  [Read-Write] Invoked when the mouse is released and a capture ends.
- ``on_value_changed`` (OnFloatValueChangedEvent):  [Read-Write] Called when the value is changed by slider or typing.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``requires_controller_lock`` (bool):  [Read-Write] Sets whether we have to lock input to change the slider value.
- ``show_slider_hand`` (bool):  [Read-Write] Whether to show the slider hand.
- ``show_slider_handle`` (bool):  [Read-Write] Whether to show the slider handle (thumb).
- ``slider_bar_color`` (LinearColor):  [Read-Write] The color to draw the slider bar in.
- ``slider_handle_color`` (LinearColor):  [Read-Write] The color to draw the slider handle in.
- ``slider_handle_end_angle`` (float):  [Read-Write] The angle at which the Slider Handle will end.
- ``slider_handle_start_angle`` (float):  [Read-Write] The angle at which the Slider Handle will start.
- ``slider_progress_color`` (LinearColor):  [Read-Write] The color to draw the completed progress of the slider bar in.
- ``slider_range`` (RuntimeFloatCurve):  [Read-Write] A curve that defines how the slider should be sampled. Default is linear.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``step_size`` (float):  [Read-Write] The amount to adjust the value by, when using a controller or keyboard
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``use_custom_default_value`` (bool):  [Read-Write] Whether the slider should draw it's progress bar from a custom value on the slider
- ``use_vertical_drag`` (bool):  [Read-Write] Whether the value is changed when dragging vertically as opposed to along the radial curve.
- ``value`` (float):  [Read-Write] The slider value to display.
- ``value_tags`` (Array[float]):  [Read-Write] Adds text tags to the radial slider at the value's position.
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``widget_style`` (SliderStyle):  [Read-Write] The progress bar style

<a id="unreal.RadialSlider.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write] The slider value to display.

<a id="unreal.RadialSlider.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.RadialSlider.slider_range"></a>

#### slider_range

```python
@property
def slider_range() -> RuntimeFloatCurve
```

(RuntimeFloatCurve):  [Read-Only] A curve that defines how the slider should be sampled. Default is linear.

<a id="unreal.RadialSlider.value_tags"></a>

#### value_tags

```python
@property
def value_tags() -> Array[float]
```

(Array[float]):  [Read-Only] Adds text tags to the radial slider at the value's position.

<a id="unreal.RadialSlider.slider_handle_start_angle"></a>

#### slider_handle_start_angle

```python
@property
def slider_handle_start_angle() -> float
```

(float):  [Read-Only] The angle at which the Slider Handle will start.

<a id="unreal.RadialSlider.slider_handle_end_angle"></a>

#### slider_handle_end_angle

```python
@property
def slider_handle_end_angle() -> float
```

(float):  [Read-Only] The angle at which the Slider Handle will end.

<a id="unreal.RadialSlider.angular_offset"></a>

#### angular_offset

```python
@property
def angular_offset() -> float
```

(float):  [Read-Only] Rotates radial slider by arbitrary offset to support full gamut of configurations.

<a id="unreal.RadialSlider.hand_start_end_ratio"></a>

#### hand_start_end_ratio

```python
@property
def hand_start_end_ratio() -> Vector2D
```

(Vector2D):  [Read-Only] Start and end of the hand as a ratio to the slider radius (so 0.0 to 1.0 is from the slider center to the handle).

<a id="unreal.RadialSlider.widget_style"></a>

#### widget_style

```python
@property
def widget_style() -> SliderStyle
```

(SliderStyle):  [Read-Write] The progress bar style

<a id="unreal.RadialSlider.widget_style"></a>

#### widget_style

```python
@widget_style.setter
def widget_style(value: SliderStyle) -> None
```

<a id="unreal.RadialSlider.slider_bar_color"></a>

#### slider_bar_color

```python
@property
def slider_bar_color() -> LinearColor
```

(LinearColor):  [Read-Only] The color to draw the slider bar in.

<a id="unreal.RadialSlider.slider_progress_color"></a>

#### slider_progress_color

```python
@property
def slider_progress_color() -> LinearColor
```

(LinearColor):  [Read-Only] The color to draw the completed progress of the slider bar in.

<a id="unreal.RadialSlider.slider_handle_color"></a>

#### slider_handle_color

```python
@property
def slider_handle_color() -> LinearColor
```

(LinearColor):  [Read-Only] The color to draw the slider handle in.

<a id="unreal.RadialSlider.center_background_color"></a>

#### center_background_color

```python
@property
def center_background_color() -> LinearColor
```

(LinearColor):  [Read-Only] The color to draw the center background in.

<a id="unreal.RadialSlider.locked"></a>

#### locked

```python
@property
def locked() -> bool
```

(bool):  [Read-Only] Whether the handle is interactive or fixed.

<a id="unreal.RadialSlider.mouse_uses_step"></a>

#### mouse_uses_step

```python
@property
def mouse_uses_step() -> bool
```

(bool):  [Read-Only] Sets new value if mouse position is greater/less than half the step size.

<a id="unreal.RadialSlider.requires_controller_lock"></a>

#### requires_controller_lock

```python
@property
def requires_controller_lock() -> bool
```

(bool):  [Read-Only] Sets whether we have to lock input to change the slider value.

<a id="unreal.RadialSlider.step_size"></a>

#### step_size

```python
@property
def step_size() -> float
```

(float):  [Read-Only] The amount to adjust the value by, when using a controller or keyboard

<a id="unreal.RadialSlider.is_focusable"></a>

#### is_focusable

```python
@property
def is_focusable() -> bool
```

(bool):  [Read-Only] Should the slider be focusable?

<a id="unreal.RadialSlider.use_vertical_drag"></a>

#### use_vertical_drag

```python
@property
def use_vertical_drag() -> bool
```

(bool):  [Read-Write] Whether the value is changed when dragging vertically as opposed to along the radial curve.

<a id="unreal.RadialSlider.use_vertical_drag"></a>

#### use_vertical_drag

```python
@use_vertical_drag.setter
def use_vertical_drag(value: bool) -> None
```

<a id="unreal.RadialSlider.show_slider_handle"></a>

#### show_slider_handle

```python
@property
def show_slider_handle() -> bool
```

(bool):  [Read-Write] Whether to show the slider handle (thumb).

<a id="unreal.RadialSlider.show_slider_handle"></a>

#### show_slider_handle

```python
@show_slider_handle.setter
def show_slider_handle(value: bool) -> None
```

<a id="unreal.RadialSlider.show_slider_hand"></a>

#### show_slider_hand

```python
@property
def show_slider_hand() -> bool
```

(bool):  [Read-Write] Whether to show the slider hand.

<a id="unreal.RadialSlider.show_slider_hand"></a>

#### show_slider_hand

```python
@show_slider_hand.setter
def show_slider_hand(value: bool) -> None
```

<a id="unreal.RadialSlider.on_mouse_capture_begin"></a>

#### on_mouse_capture_begin

```python
@property
def on_mouse_capture_begin() -> OnMouseCaptureBeginEvent
```

(OnMouseCaptureBeginEvent):  [Read-Write] Invoked when the mouse is pressed and a capture begins.

<a id="unreal.RadialSlider.on_mouse_capture_begin"></a>

#### on_mouse_capture_begin

```python
@on_mouse_capture_begin.setter
def on_mouse_capture_begin(value: OnMouseCaptureBeginEvent) -> None
```

<a id="unreal.RadialSlider.on_mouse_capture_end"></a>

#### on_mouse_capture_end

```python
@property
def on_mouse_capture_end() -> OnMouseCaptureEndEvent
```

(OnMouseCaptureEndEvent):  [Read-Write] Invoked when the mouse is released and a capture ends.

<a id="unreal.RadialSlider.on_mouse_capture_end"></a>

#### on_mouse_capture_end

```python
@on_mouse_capture_end.setter
def on_mouse_capture_end(value: OnMouseCaptureEndEvent) -> None
```

<a id="unreal.RadialSlider.on_controller_capture_begin"></a>

#### on_controller_capture_begin

```python
@property
def on_controller_capture_begin() -> OnControllerCaptureBeginEvent
```

(OnControllerCaptureBeginEvent):  [Read-Write] Invoked when the controller capture begins.

<a id="unreal.RadialSlider.on_controller_capture_begin"></a>

#### on_controller_capture_begin

```python
@on_controller_capture_begin.setter
def on_controller_capture_begin(value: OnControllerCaptureBeginEvent) -> None
```

<a id="unreal.RadialSlider.on_controller_capture_end"></a>

#### on_controller_capture_end

```python
@property
def on_controller_capture_end() -> OnControllerCaptureEndEvent
```

(OnControllerCaptureEndEvent):  [Read-Write] Invoked when the controller capture ends.

<a id="unreal.RadialSlider.on_controller_capture_end"></a>

#### on_controller_capture_end

```python
@on_controller_capture_end.setter
def on_controller_capture_end(value: OnControllerCaptureEndEvent) -> None
```

<a id="unreal.RadialSlider.on_value_changed"></a>

#### on_value_changed

```python
@property
def on_value_changed() -> OnFloatValueChangedEvent
```

(OnFloatValueChangedEvent):  [Read-Write] Called when the value is changed by slider or typing.

<a id="unreal.RadialSlider.on_value_changed"></a>

#### on_value_changed

```python
@on_value_changed.setter
def on_value_changed(value: OnFloatValueChangedEvent) -> None
```

<a id="unreal.RadialSlider.set_value_tags"></a>

#### set_value_tags

```python
def set_value_tags(value_tags: Array[float]) -> None
```

x.set_value_tags(value_tags) -> None
Adds value tags to the slider.

Args:
    value_tags (Array[float]):

<a id="unreal.RadialSlider.set_value"></a>

#### set_value

```python
def set_value(value: float) -> None
```

x.set_value(value) -> None
Sets the current value of the slider.

Args:
    value (float):

<a id="unreal.RadialSlider.set_use_vertical_drag"></a>

#### set_use_vertical_drag

```python
def set_use_vertical_drag(use_vertical_drag: bool) -> None
```

x.set_use_vertical_drag(use_vertical_drag) -> None
Set whether the value is changed when dragging vertically as opposed to along the radial curve.

Args:
    use_vertical_drag (bool):

<a id="unreal.RadialSlider.set_step_size"></a>

#### set_step_size

```python
def set_step_size(value: float) -> None
```

x.set_step_size(value) -> None
Sets the amount to adjust the value by, when using a controller or keyboard

Args:
    value (float):

<a id="unreal.RadialSlider.set_slider_range"></a>

#### set_slider_range

```python
def set_slider_range(slider_range: RuntimeFloatCurve) -> None
```

x.set_slider_range(slider_range) -> None
Sets the curve for the slider range

Args:
    slider_range (RuntimeFloatCurve):

<a id="unreal.RadialSlider.set_slider_progress_color"></a>

#### set_slider_progress_color

```python
def set_slider_progress_color(value: LinearColor) -> None
```

x.set_slider_progress_color(value) -> None
Sets the progress color of the slider bar

Args:
    value (LinearColor):

<a id="unreal.RadialSlider.set_slider_handle_start_angle"></a>

#### set_slider_handle_start_angle

```python
def set_slider_handle_start_angle(value: float) -> None
```

x.set_slider_handle_start_angle(value) -> None
Sets the minimum angle of the slider.

Args:
    value (float):

<a id="unreal.RadialSlider.set_slider_handle_end_angle"></a>

#### set_slider_handle_end_angle

```python
def set_slider_handle_end_angle(value: float) -> None
```

x.set_slider_handle_end_angle(value) -> None
Sets the maximum angle of the slider.

Args:
    value (float):

<a id="unreal.RadialSlider.set_slider_handle_color"></a>

#### set_slider_handle_color

```python
def set_slider_handle_color(value: LinearColor) -> None
```

x.set_slider_handle_color(value) -> None
Sets the color of the handle bar

Args:
    value (LinearColor):

<a id="unreal.RadialSlider.set_slider_bar_color"></a>

#### set_slider_bar_color

```python
def set_slider_bar_color(value: LinearColor) -> None
```

x.set_slider_bar_color(value) -> None
Sets the color of the slider bar

Args:
    value (LinearColor):

<a id="unreal.RadialSlider.set_show_slider_handle"></a>

#### set_show_slider_handle

```python
def set_show_slider_handle(show_slider_handle: bool) -> None
```

x.set_show_slider_handle(show_slider_handle) -> None
Whether to show the slider handle (thumb).

Args:
    show_slider_handle (bool):

<a id="unreal.RadialSlider.set_show_slider_hand"></a>

#### set_show_slider_hand

```python
def set_show_slider_hand(show_slider_hand: bool) -> None
```

x.set_show_slider_hand(show_slider_hand) -> None
Whether to show the slider hand.

Args:
    show_slider_hand (bool):

<a id="unreal.RadialSlider.set_locked"></a>

#### set_locked

```python
def set_locked(value: bool) -> None
```

x.set_locked(value) -> None
Sets the handle to be interactive or fixed

Args:
    value (bool):

<a id="unreal.RadialSlider.set_hand_start_end_ratio"></a>

#### set_hand_start_end_ratio

```python
def set_hand_start_end_ratio(value: Vector2D) -> None
```

x.set_hand_start_end_ratio(value) -> None
Sets the start and end of the hand as a ratio to the slider radius (so 0.0 to 1.0 is from the slider center to the handle).

Args:
    value (Vector2D):

<a id="unreal.RadialSlider.set_custom_default_value"></a>

#### set_custom_default_value

```python
def set_custom_default_value(value: float) -> None
```

x.set_custom_default_value(value) -> None
Sets the current custom default value of the slider.

Args:
    value (float):

<a id="unreal.RadialSlider.set_center_background_color"></a>

#### set_center_background_color

```python
def set_center_background_color(value: LinearColor) -> None
```

x.set_center_background_color(value) -> None
Sets the color of the slider bar

Args:
    value (LinearColor):

<a id="unreal.RadialSlider.set_angular_offset"></a>

#### set_angular_offset

```python
def set_angular_offset(value: float) -> None
```

x.set_angular_offset(value) -> None
Sets the Angular Offset for the slider.

Args:
    value (float):

<a id="unreal.RadialSlider.get_value"></a>

#### get_value

```python
def get_value() -> float
```

x.get_value() -> float
Gets the current value of the slider.

Returns:
    float:

<a id="unreal.RadialSlider.get_normalized_slider_handle_position"></a>

#### get_normalized_slider_handle_position

```python
def get_normalized_slider_handle_position() -> float
```

x.get_normalized_slider_handle_position() -> float
Get the current raw slider alpha from 0 to 1

Returns:
    float:

<a id="unreal.RadialSlider.get_custom_default_value"></a>

#### get_custom_default_value

```python
def get_custom_default_value() -> float
```

x.get_custom_default_value() -> float
Gets the current custom default value of the slider.

Returns:
    float:

<a id="unreal.Subsystem"></a>