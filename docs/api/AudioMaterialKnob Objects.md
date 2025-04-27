## AudioMaterialKnob Objects

```python
class AudioMaterialKnob(Widget)
```

A simple widget that shows a turning Knob that allows you to control the value between 0..1.
Knob is rendered by using material instead of texture.

* No Children

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioMaterialKnob.h

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
- ``fine_tune_speed`` (float):  [Read-Write] The tune speed when fine-tuning the knob
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``locked`` (bool):  [Read-Write] Whether the knob is interactive or fixed.
- ``mouse_uses_step`` (bool):  [Read-Write] Sets new value if mouse position is greater/less than half the step size.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_knob_value_changed`` (OnKnobValueChangedEvent):  [Read-Write] Called when the value is changed by knob.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``step_size`` (float):  [Read-Write] The amount to adjust the value by, when using steps
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``tune_speed`` (float):  [Read-Write] The tune speed of the knob
- ``value`` (float):  [Read-Write] Default Value of the Knob
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``widget_style`` (AudioMaterialKnobStyle):  [Read-Write] The button's style

<a id="unreal.AudioMaterialKnob.widget_style"></a>

#### widget_style

```python
@property
def widget_style() -> AudioMaterialKnobStyle
```

(AudioMaterialKnobStyle):  [Read-Write] The button's style

<a id="unreal.AudioMaterialKnob.widget_style"></a>

#### widget_style

```python
@widget_style.setter
def widget_style(value: AudioMaterialKnobStyle) -> None
```

<a id="unreal.AudioMaterialKnob.on_knob_value_changed"></a>

#### on_knob_value_changed

```python
@property
def on_knob_value_changed() -> OnKnobValueChangedEvent
```

(OnKnobValueChangedEvent):  [Read-Write] Called when the value is changed by knob.

<a id="unreal.AudioMaterialKnob.on_knob_value_changed"></a>

#### on_knob_value_changed

```python
@on_knob_value_changed.setter
def on_knob_value_changed(value: OnKnobValueChangedEvent) -> None
```

<a id="unreal.AudioMaterialKnob.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write] Default Value of the Knob

<a id="unreal.AudioMaterialKnob.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.AudioMaterialKnob.tune_speed"></a>

#### tune_speed

```python
@property
def tune_speed() -> float
```

(float):  [Read-Write] The tune speed of the knob

<a id="unreal.AudioMaterialKnob.tune_speed"></a>

#### tune_speed

```python
@tune_speed.setter
def tune_speed(value: float) -> None
```

<a id="unreal.AudioMaterialKnob.fine_tune_speed"></a>

#### fine_tune_speed

```python
@property
def fine_tune_speed() -> float
```

(float):  [Read-Write] The tune speed when fine-tuning the knob

<a id="unreal.AudioMaterialKnob.fine_tune_speed"></a>

#### fine_tune_speed

```python
@fine_tune_speed.setter
def fine_tune_speed(value: float) -> None
```

<a id="unreal.AudioMaterialKnob.locked"></a>

#### locked

```python
@property
def locked() -> bool
```

(bool):  [Read-Write] Whether the knob is interactive or fixed.

<a id="unreal.AudioMaterialKnob.locked"></a>

#### locked

```python
@locked.setter
def locked(value: bool) -> None
```

<a id="unreal.AudioMaterialKnob.mouse_uses_step"></a>

#### mouse_uses_step

```python
@property
def mouse_uses_step() -> bool
```

(bool):  [Read-Write] Sets new value if mouse position is greater/less than half the step size.

<a id="unreal.AudioMaterialKnob.mouse_uses_step"></a>

#### mouse_uses_step

```python
@mouse_uses_step.setter
def mouse_uses_step(value: bool) -> None
```

<a id="unreal.AudioMaterialKnob.step_size"></a>

#### step_size

```python
@property
def step_size() -> float
```

(float):  [Read-Write] The amount to adjust the value by, when using steps

<a id="unreal.AudioMaterialKnob.step_size"></a>

#### step_size

```python
@step_size.setter
def step_size(value: float) -> None
```

<a id="unreal.AudioMaterialKnob.set_value"></a>

#### set_value

```python
def set_value(value: float) -> None
```

x.set_value(value) -> None
Set the current value of the knob. InValue is Clamped between 0.f - 1.f

Args:
    value (float):

<a id="unreal.AudioMaterialKnob.set_tune_speed"></a>

#### set_tune_speed

```python
def set_tune_speed(value: float) -> None
```

x.set_tune_speed(value) -> None
Set the knobs tune speed. InValue is Clamped between 0.f - 1.f

Args:
    value (float):

<a id="unreal.AudioMaterialKnob.set_step_size"></a>

#### set_step_size

```python
def set_step_size(value: float) -> None
```

x.set_step_size(value) -> None
Set the amount to adjust the value when using steps

Args:
    value (float):

<a id="unreal.AudioMaterialKnob.set_mouse_uses_step"></a>

#### set_mouse_uses_step

```python
def set_mouse_uses_step(uses_step: bool) -> None
```

x.set_mouse_uses_step(uses_step) -> None
Set the knob to use steps when turning On Mouse move

Args:
    uses_step (bool):

<a id="unreal.AudioMaterialKnob.set_locked"></a>

#### set_locked

```python
def set_locked(locked: bool) -> None
```

x.set_locked(locked) -> None
Set the knob to be interactive or fixed

Args:
    locked (bool):

<a id="unreal.AudioMaterialKnob.set_fine_tune_speed"></a>

#### set_fine_tune_speed

```python
def set_fine_tune_speed(value: float) -> None
```

x.set_fine_tune_speed(value) -> None
Set the knobs fine-tune speed. InValue is Clamped between 0.f - 1.f

Args:
    value (float):

<a id="unreal.AudioMaterialKnob.get_value"></a>

#### get_value

```python
def get_value() -> float
```

x.get_value() -> float
Get the current value of the knob.

Returns:
    float:

<a id="unreal.AudioMaterialKnob.get_tune_speed"></a>

#### get_tune_speed

```python
def get_tune_speed() -> float
```

x.get_tune_speed() -> float
Get the Knobs tune speed

Returns:
    float:

<a id="unreal.AudioMaterialKnob.get_step_size"></a>

#### get_step_size

```python
def get_step_size() -> float
```

x.get_step_size() -> float
Get Step Size

Returns:
    float:

<a id="unreal.AudioMaterialKnob.get_mouse_uses_step"></a>

#### get_mouse_uses_step

```python
def get_mouse_uses_step() -> bool
```

x.get_mouse_uses_step() -> bool
Get whether the knob uses steps when tuning On Mouse move

Returns:
    bool:

<a id="unreal.AudioMaterialKnob.get_is_locked"></a>

#### get_is_locked

```python
def get_is_locked() -> bool
```

x.get_is_locked() -> bool
Get whether the knob is interactive or fixed.

Returns:
    bool:

<a id="unreal.AudioMaterialKnob.get_fine_tune_speed"></a>

#### get_fine_tune_speed

```python
def get_fine_tune_speed() -> float
```

x.get_fine_tune_speed() -> float
Get the Knobs fine-tune speed

Returns:
    float:

<a id="unreal.AudioMaterialMeter"></a>