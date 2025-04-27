## SynthKnob Objects

```python
class SynthKnob(Widget)
```

A simple widget that shows a sliding bar with a handle that allows you to control the value between 0..1.

* No Children

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SynthKnob.h

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
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_focusable`` (bool):  [Read-Write] Should the slider be focusable?
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``locked`` (bool):  [Read-Write] Whether the handle is interactive or fixed.
- ``mouse_fine_tune_speed`` (float):  [Read-Write] The speed of the mouse knob control when fine-tuning the knob
- ``mouse_speed`` (float):  [Read-Write] The speed of the mouse knob control
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
- ``parameter_name`` (Text):  [Read-Write] The name of the pararameter. Will show when knob turns.
- ``parameter_units`` (Text):  [Read-Write] The parameter units (e.g. hz). Will append to synth tooltip info.
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``show_tooltip_info`` (bool):  [Read-Write] Enable tool tip window to show parameter information while knob turns
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``step_size`` (float):  [Read-Write] The amount to adjust the value by, when using a controller or keyboard
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``value`` (float):  [Read-Write] The volume value to display.
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``widget_style`` (SynthKnobStyle):  [Read-Write] The synth knob style

<a id="unreal.SynthKnob.step_size"></a>

#### step_size

```python
@property
def step_size() -> float
```

(float):  [Read-Only] The amount to adjust the value by, when using a controller or keyboard

<a id="unreal.SynthKnob.mouse_speed"></a>

#### mouse_speed

```python
@property
def mouse_speed() -> float
```

(float):  [Read-Only] The speed of the mouse knob control

<a id="unreal.SynthKnob.mouse_fine_tune_speed"></a>

#### mouse_fine_tune_speed

```python
@property
def mouse_fine_tune_speed() -> float
```

(float):  [Read-Only] The speed of the mouse knob control when fine-tuning the knob

<a id="unreal.SynthKnob.show_tooltip_info"></a>

#### show_tooltip_info

```python
@property
def show_tooltip_info() -> bool
```

(bool):  [Read-Only] Enable tool tip window to show parameter information while knob turns

<a id="unreal.SynthKnob.parameter_name"></a>

#### parameter_name

```python
@property
def parameter_name() -> Text
```

(Text):  [Read-Only] The name of the pararameter. Will show when knob turns.

<a id="unreal.SynthKnob.parameter_units"></a>

#### parameter_units

```python
@property
def parameter_units() -> Text
```

(Text):  [Read-Only] The parameter units (e.g. hz). Will append to synth tooltip info.

<a id="unreal.SynthKnob.widget_style"></a>

#### widget_style

```python
@property
def widget_style() -> SynthKnobStyle
```

(SynthKnobStyle):  [Read-Write] The synth knob style

<a id="unreal.SynthKnob.widget_style"></a>

#### widget_style

```python
@widget_style.setter
def widget_style(value: SynthKnobStyle) -> None
```

<a id="unreal.SynthKnob.locked"></a>

#### locked

```python
@property
def locked() -> bool
```

(bool):  [Read-Only] Whether the handle is interactive or fixed.

<a id="unreal.SynthKnob.is_focusable"></a>

#### is_focusable

```python
@property
def is_focusable() -> bool
```

(bool):  [Read-Only] Should the slider be focusable?

<a id="unreal.SynthKnob.on_mouse_capture_begin"></a>

#### on_mouse_capture_begin

```python
@property
def on_mouse_capture_begin() -> OnMouseCaptureBeginEvent
```

(OnMouseCaptureBeginEvent):  [Read-Write] Invoked when the mouse is pressed and a capture begins.

<a id="unreal.SynthKnob.on_mouse_capture_begin"></a>

#### on_mouse_capture_begin

```python
@on_mouse_capture_begin.setter
def on_mouse_capture_begin(value: OnMouseCaptureBeginEvent) -> None
```

<a id="unreal.SynthKnob.on_mouse_capture_end"></a>

#### on_mouse_capture_end

```python
@property
def on_mouse_capture_end() -> OnMouseCaptureEndEvent
```

(OnMouseCaptureEndEvent):  [Read-Write] Invoked when the mouse is released and a capture ends.

<a id="unreal.SynthKnob.on_mouse_capture_end"></a>

#### on_mouse_capture_end

```python
@on_mouse_capture_end.setter
def on_mouse_capture_end(value: OnMouseCaptureEndEvent) -> None
```

<a id="unreal.SynthKnob.on_controller_capture_begin"></a>

#### on_controller_capture_begin

```python
@property
def on_controller_capture_begin() -> OnControllerCaptureBeginEvent
```

(OnControllerCaptureBeginEvent):  [Read-Write] Invoked when the controller capture begins.

<a id="unreal.SynthKnob.on_controller_capture_begin"></a>

#### on_controller_capture_begin

```python
@on_controller_capture_begin.setter
def on_controller_capture_begin(value: OnControllerCaptureBeginEvent) -> None
```

<a id="unreal.SynthKnob.on_controller_capture_end"></a>

#### on_controller_capture_end

```python
@property
def on_controller_capture_end() -> OnControllerCaptureEndEvent
```

(OnControllerCaptureEndEvent):  [Read-Write] Invoked when the controller capture ends.

<a id="unreal.SynthKnob.on_controller_capture_end"></a>

#### on_controller_capture_end

```python
@on_controller_capture_end.setter
def on_controller_capture_end(value: OnControllerCaptureEndEvent) -> None
```

<a id="unreal.SynthKnob.on_value_changed"></a>

#### on_value_changed

```python
@property
def on_value_changed() -> OnFloatValueChangedEvent
```

(OnFloatValueChangedEvent):  [Read-Write] Called when the value is changed by slider or typing.

<a id="unreal.SynthKnob.on_value_changed"></a>

#### on_value_changed

```python
@on_value_changed.setter
def on_value_changed(value: OnFloatValueChangedEvent) -> None
```

<a id="unreal.SynthKnob.set_value"></a>

#### set_value

```python
def set_value(value: float) -> None
```

x.set_value(value) -> None
Sets the current value of the slider.

Args:
    value (float):

<a id="unreal.SynthKnob.set_step_size"></a>

#### set_step_size

```python
def set_step_size(value: float) -> None
```

x.set_step_size(value) -> None
Sets the amount to adjust the value by, when using a controller or keyboard

Args:
    value (float):

<a id="unreal.SynthKnob.set_locked"></a>

#### set_locked

```python
def set_locked(value: bool) -> None
```

x.set_locked(value) -> None
Sets the handle to be interactive or fixed

Args:
    value (bool):

<a id="unreal.SynthKnob.get_value"></a>

#### get_value

```python
def get_value() -> float
```

x.get_value() -> float
Gets the current value of the slider.

Returns:
    float:

<a id="unreal.CharacterTrajectoryComponent"></a>