## Slider Objects

```python
class Slider(Widget)
```

A simple widget that shows a sliding bar with a handle that allows you to control the value in a user define range (between 0..1 by default).

* No Children

**C++ Source:**

- **Module**: UMG
- **File**: Slider.h

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
- ``max_value`` (float):  [Read-Write] The maximum value the slider can be set to.
- ``min_value`` (float):  [Read-Write] The minimum value the slider can be set to.
- ``mouse_uses_step`` (bool):  [Read-Write] Sets new value if mouse position is greater/less than half the step size.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_controller_capture_begin`` (OnControllerCaptureBeginEvent):  [Read-Write] Invoked when the controller capture begins.
- ``on_controller_capture_end`` (OnControllerCaptureEndEvent):  [Read-Write] Invoked when the controller capture ends.
- ``on_mouse_capture_begin`` (OnMouseCaptureBeginEvent):  [Read-Write] Invoked when the mouse is pressed and a capture begins.
- ``on_mouse_capture_end`` (OnMouseCaptureEndEvent):  [Read-Write] Invoked when the mouse is released and a capture ends.
- ``on_value_changed`` (OnFloatValueChangedEvent):  [Read-Write] Called when the value is changed by slider or typing.
- ``orientation`` (Orientation):  [Read-Write] The slider's orientation.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``requires_controller_lock`` (bool):  [Read-Write] Sets whether we have to lock input to change the slider value.
- ``slider_bar_color`` (LinearColor):  [Read-Write] The color to draw the slider bar in.
- ``slider_handle_color`` (LinearColor):  [Read-Write] The color to draw the slider handle in.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``step_size`` (float):  [Read-Write] The amount to adjust the value by, when using a controller or keyboard
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``value`` (float):  [Read-Write] The volume value to display.
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``widget_style`` (SliderStyle):  [Read-Write] The progress bar style

<a id="unreal.Slider.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write] The volume value to display.

<a id="unreal.Slider.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.Slider.min_value"></a>

#### min_value

```python
@property
def min_value() -> float
```

(float):  [Read-Write] The minimum value the slider can be set to.

<a id="unreal.Slider.min_value"></a>

#### min_value

```python
@min_value.setter
def min_value(value: float) -> None
```

<a id="unreal.Slider.max_value"></a>

#### max_value

```python
@property
def max_value() -> float
```

(float):  [Read-Write] The maximum value the slider can be set to.

<a id="unreal.Slider.max_value"></a>

#### max_value

```python
@max_value.setter
def max_value(value: float) -> None
```

<a id="unreal.Slider.widget_style"></a>

#### widget_style

```python
@property
def widget_style() -> SliderStyle
```

(SliderStyle):  [Read-Write] The progress bar style

<a id="unreal.Slider.widget_style"></a>

#### widget_style

```python
@widget_style.setter
def widget_style(value: SliderStyle) -> None
```

<a id="unreal.Slider.orientation"></a>

#### orientation

```python
@property
def orientation() -> Orientation
```

(Orientation):  [Read-Write] The slider's orientation.

<a id="unreal.Slider.orientation"></a>

#### orientation

```python
@orientation.setter
def orientation(value: Orientation) -> None
```

<a id="unreal.Slider.slider_bar_color"></a>

#### slider_bar_color

```python
@property
def slider_bar_color() -> LinearColor
```

(LinearColor):  [Read-Write] The color to draw the slider bar in.

<a id="unreal.Slider.slider_bar_color"></a>

#### slider_bar_color

```python
@slider_bar_color.setter
def slider_bar_color(value: LinearColor) -> None
```

<a id="unreal.Slider.slider_handle_color"></a>

#### slider_handle_color

```python
@property
def slider_handle_color() -> LinearColor
```

(LinearColor):  [Read-Write] The color to draw the slider handle in.

<a id="unreal.Slider.slider_handle_color"></a>

#### slider_handle_color

```python
@slider_handle_color.setter
def slider_handle_color(value: LinearColor) -> None
```

<a id="unreal.Slider.indent_handle"></a>

#### indent_handle

```python
@property
def indent_handle() -> bool
```

(bool):  [Read-Write] Whether the slidable area should be indented to fit the handle.

<a id="unreal.Slider.indent_handle"></a>

#### indent_handle

```python
@indent_handle.setter
def indent_handle(value: bool) -> None
```

<a id="unreal.Slider.locked"></a>

#### locked

```python
@property
def locked() -> bool
```

(bool):  [Read-Write] Whether the handle is interactive or fixed.

<a id="unreal.Slider.locked"></a>

#### locked

```python
@locked.setter
def locked(value: bool) -> None
```

<a id="unreal.Slider.mouse_uses_step"></a>

#### mouse_uses_step

```python
@property
def mouse_uses_step() -> bool
```

(bool):  [Read-Only] Sets new value if mouse position is greater/less than half the step size.

<a id="unreal.Slider.requires_controller_lock"></a>

#### requires_controller_lock

```python
@property
def requires_controller_lock() -> bool
```

(bool):  [Read-Only] Sets whether we have to lock input to change the slider value.

<a id="unreal.Slider.step_size"></a>

#### step_size

```python
@property
def step_size() -> float
```

(float):  [Read-Write] The amount to adjust the value by, when using a controller or keyboard

<a id="unreal.Slider.step_size"></a>

#### step_size

```python
@step_size.setter
def step_size(value: float) -> None
```

<a id="unreal.Slider.is_focusable"></a>

#### is_focusable

```python
@property
def is_focusable() -> bool
```

(bool):  [Read-Only] Should the slider be focusable?

<a id="unreal.Slider.on_mouse_capture_begin"></a>

#### on_mouse_capture_begin

```python
@property
def on_mouse_capture_begin() -> OnMouseCaptureBeginEvent
```

(OnMouseCaptureBeginEvent):  [Read-Write] Invoked when the mouse is pressed and a capture begins.

<a id="unreal.Slider.on_mouse_capture_begin"></a>

#### on_mouse_capture_begin

```python
@on_mouse_capture_begin.setter
def on_mouse_capture_begin(value: OnMouseCaptureBeginEvent) -> None
```

<a id="unreal.Slider.on_mouse_capture_end"></a>

#### on_mouse_capture_end

```python
@property
def on_mouse_capture_end() -> OnMouseCaptureEndEvent
```

(OnMouseCaptureEndEvent):  [Read-Write] Invoked when the mouse is released and a capture ends.

<a id="unreal.Slider.on_mouse_capture_end"></a>

#### on_mouse_capture_end

```python
@on_mouse_capture_end.setter
def on_mouse_capture_end(value: OnMouseCaptureEndEvent) -> None
```

<a id="unreal.Slider.on_controller_capture_begin"></a>

#### on_controller_capture_begin

```python
@property
def on_controller_capture_begin() -> OnControllerCaptureBeginEvent
```

(OnControllerCaptureBeginEvent):  [Read-Write] Invoked when the controller capture begins.

<a id="unreal.Slider.on_controller_capture_begin"></a>

#### on_controller_capture_begin

```python
@on_controller_capture_begin.setter
def on_controller_capture_begin(value: OnControllerCaptureBeginEvent) -> None
```

<a id="unreal.Slider.on_controller_capture_end"></a>

#### on_controller_capture_end

```python
@property
def on_controller_capture_end() -> OnControllerCaptureEndEvent
```

(OnControllerCaptureEndEvent):  [Read-Write] Invoked when the controller capture ends.

<a id="unreal.Slider.on_controller_capture_end"></a>

#### on_controller_capture_end

```python
@on_controller_capture_end.setter
def on_controller_capture_end(value: OnControllerCaptureEndEvent) -> None
```

<a id="unreal.Slider.on_value_changed"></a>

#### on_value_changed

```python
@property
def on_value_changed() -> OnFloatValueChangedEvent
```

(OnFloatValueChangedEvent):  [Read-Write] Called when the value is changed by slider or typing.

<a id="unreal.Slider.on_value_changed"></a>

#### on_value_changed

```python
@on_value_changed.setter
def on_value_changed(value: OnFloatValueChangedEvent) -> None
```

<a id="unreal.Slider.set_value"></a>

#### set_value

```python
def set_value(value: float) -> None
```

x.set_value(value) -> None
Sets the current value of the slider.

Args:
    value (float):

<a id="unreal.Slider.set_step_size"></a>

#### set_step_size

```python
def set_step_size(value: float) -> None
```

x.set_step_size(value) -> None
Sets the amount to adjust the value by, when using a controller or keyboard.

Args:
    value (float):

<a id="unreal.Slider.set_slider_handle_color"></a>

#### set_slider_handle_color

```python
def set_slider_handle_color(value: LinearColor) -> None
```

x.set_slider_handle_color(value) -> None
Sets the color of the handle bar

Args:
    value (LinearColor):

<a id="unreal.Slider.set_slider_bar_color"></a>

#### set_slider_bar_color

```python
def set_slider_bar_color(value: LinearColor) -> None
```

x.set_slider_bar_color(value) -> None
Sets the color of the slider bar.

Args:
    value (LinearColor):

<a id="unreal.Slider.set_min_value"></a>

#### set_min_value

```python
def set_min_value(value: float) -> None
```

x.set_min_value(value) -> None
Sets the minimum value of the slider.

Args:
    value (float):

<a id="unreal.Slider.set_max_value"></a>

#### set_max_value

```python
def set_max_value(value: float) -> None
```

x.set_max_value(value) -> None
Sets the maximum value of the slider.

Args:
    value (float):

<a id="unreal.Slider.set_locked"></a>

#### set_locked

```python
def set_locked(value: bool) -> None
```

x.set_locked(value) -> None
Sets the handle to be interactive or fixed.

Args:
    value (bool):

<a id="unreal.Slider.set_indent_handle"></a>

#### set_indent_handle

```python
def set_indent_handle(value: bool) -> None
```

x.set_indent_handle(value) -> None
Sets if the slidable area should be indented to fit the handle.

Args:
    value (bool):

<a id="unreal.Slider.get_value"></a>

#### get_value

```python
def get_value() -> float
```

x.get_value() -> float
Gets the current value of the slider.

Returns:
    float:

<a id="unreal.Slider.get_normalized_value"></a>

#### get_normalized_value

```python
def get_normalized_value() -> float
```

x.get_normalized_value() -> float
Get the current value scaled from 0 to 1

Returns:
    float:

<a id="unreal.Spacer"></a>