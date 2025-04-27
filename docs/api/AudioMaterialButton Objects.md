## AudioMaterialButton Objects

```python
class AudioMaterialButton(Widget)
```

A simple widget that shows a button
Button is rendered by using material instead of texture.

* No Children

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioMaterialButton.h

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
- ``is_pressed`` (bool):  [Read-Write] Default Value of the button
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_button_pressed_changed_event`` (OnButtonPressedChangedEvent):  [Read-Write] Called when the value is changed by button.
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
- ``widget_style`` (AudioMaterialButtonStyle):  [Read-Write] The button's style

<a id="unreal.AudioMaterialButton.widget_style"></a>

#### widget_style

```python
@property
def widget_style() -> AudioMaterialButtonStyle
```

(AudioMaterialButtonStyle):  [Read-Write] The button's style

<a id="unreal.AudioMaterialButton.widget_style"></a>

#### widget_style

```python
@widget_style.setter
def widget_style(value: AudioMaterialButtonStyle) -> None
```

<a id="unreal.AudioMaterialButton.on_button_pressed_changed_event"></a>

#### on_button_pressed_changed_event

```python
@property
def on_button_pressed_changed_event() -> OnButtonPressedChangedEvent
```

(OnButtonPressedChangedEvent):  [Read-Write] Called when the value is changed by button.

<a id="unreal.AudioMaterialButton.on_button_pressed_changed_event"></a>

#### on_button_pressed_changed_event

```python
@on_button_pressed_changed_event.setter
def on_button_pressed_changed_event(
        value: OnButtonPressedChangedEvent) -> None
```

<a id="unreal.AudioMaterialButton.is_pressed"></a>

#### is_pressed

```python
@property
def is_pressed() -> bool
```

(bool):  [Read-Write] Default Value of the button

<a id="unreal.AudioMaterialButton.is_pressed"></a>

#### is_pressed

```python
@is_pressed.setter
def is_pressed(value: bool) -> None
```

<a id="unreal.AudioMaterialButton.set_is_pressed"></a>

#### set_is_pressed

```python
def set_is_pressed(pressed: bool) -> None
```

x.set_is_pressed(pressed) -> None
Sets the current value of the slider. InValue is Clamped between 0.f - 1.f

Args:
    pressed (bool):

<a id="unreal.AudioMaterialButton.get_is_pressed"></a>

#### get_is_pressed

```python
def get_is_pressed() -> bool
```

x.get_is_pressed() -> bool
Gets the current value of the slider.

Returns:
    bool:

<a id="unreal.AudioMaterialEnvelope"></a>