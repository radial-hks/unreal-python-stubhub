## Button Objects

```python
class Button(ContentWidget)
```

The button is a click-able primitive widget to enable basic interaction, you
can place any other widget inside a button to make a more complex and
interesting click-able element in your UI.

* Single Child
* Clickable

**C++ Source:**

- **Module**: UMG
- **File**: Button.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``background_color`` (LinearColor):  [Read-Write] The color multiplier for the button background
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``click_method`` (ButtonClickMethod):  [Read-Write] The type of mouse action required by the user to trigger the buttons 'Click'
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``color_and_opacity`` (LinearColor):  [Read-Write] The color multiplier for the button content
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_focusable`` (bool):  [Read-Write] Sometimes a button should only be mouse-clickable and never keyboard focusable.
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_clicked`` (OnButtonClickedEvent):  [Read-Write] Called when the button is clicked
- ``on_hovered`` (OnButtonHoverEvent):  [Read-Write]
- ``on_pressed`` (OnButtonPressedEvent):  [Read-Write] Called when the button is pressed
- ``on_released`` (OnButtonReleasedEvent):  [Read-Write] Called when the button is released
- ``on_unhovered`` (OnButtonHoverEvent):  [Read-Write]
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``press_method`` (ButtonPressMethod):  [Read-Write] The type of keyboard/gamepad button press action required by the user to trigger the buttons 'Click'
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``touch_method`` (ButtonTouchMethod):  [Read-Write] The type of touch action required by the user to trigger the buttons 'Click'
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``widget_style`` (ButtonStyle):  [Read-Write] The button style used at runtime

<a id="unreal.Button.widget_style"></a>

#### widget_style

```python
@property
def widget_style() -> ButtonStyle
```

(ButtonStyle):  [Read-Write] The button style used at runtime

<a id="unreal.Button.widget_style"></a>

#### widget_style

```python
@widget_style.setter
def widget_style(value: ButtonStyle) -> None
```

<a id="unreal.Button.color_and_opacity"></a>

#### color_and_opacity

```python
@property
def color_and_opacity() -> LinearColor
```

(LinearColor):  [Read-Write] The color multiplier for the button content

<a id="unreal.Button.color_and_opacity"></a>

#### color_and_opacity

```python
@color_and_opacity.setter
def color_and_opacity(value: LinearColor) -> None
```

<a id="unreal.Button.background_color"></a>

#### background_color

```python
@property
def background_color() -> LinearColor
```

(LinearColor):  [Read-Write] The color multiplier for the button background

<a id="unreal.Button.background_color"></a>

#### background_color

```python
@background_color.setter
def background_color(value: LinearColor) -> None
```

<a id="unreal.Button.click_method"></a>

#### click_method

```python
@property
def click_method() -> ButtonClickMethod
```

(ButtonClickMethod):  [Read-Write] The type of mouse action required by the user to trigger the buttons 'Click'

<a id="unreal.Button.click_method"></a>

#### click_method

```python
@click_method.setter
def click_method(value: ButtonClickMethod) -> None
```

<a id="unreal.Button.touch_method"></a>

#### touch_method

```python
@property
def touch_method() -> ButtonTouchMethod
```

(ButtonTouchMethod):  [Read-Write] The type of touch action required by the user to trigger the buttons 'Click'

<a id="unreal.Button.touch_method"></a>

#### touch_method

```python
@touch_method.setter
def touch_method(value: ButtonTouchMethod) -> None
```

<a id="unreal.Button.press_method"></a>

#### press_method

```python
@property
def press_method() -> ButtonPressMethod
```

(ButtonPressMethod):  [Read-Write] The type of keyboard/gamepad button press action required by the user to trigger the buttons 'Click'

<a id="unreal.Button.press_method"></a>

#### press_method

```python
@press_method.setter
def press_method(value: ButtonPressMethod) -> None
```

<a id="unreal.Button.is_focusable"></a>

#### is_focusable

```python
@property
def is_focusable() -> bool
```

(bool):  [Read-Only] Sometimes a button should only be mouse-clickable and never keyboard focusable.

<a id="unreal.Button.on_clicked"></a>

#### on_clicked

```python
@property
def on_clicked() -> OnButtonClickedEvent
```

(OnButtonClickedEvent):  [Read-Write] Called when the button is clicked

<a id="unreal.Button.on_clicked"></a>

#### on_clicked

```python
@on_clicked.setter
def on_clicked(value: OnButtonClickedEvent) -> None
```

<a id="unreal.Button.on_pressed"></a>

#### on_pressed

```python
@property
def on_pressed() -> OnButtonPressedEvent
```

(OnButtonPressedEvent):  [Read-Write] Called when the button is pressed

<a id="unreal.Button.on_pressed"></a>

#### on_pressed

```python
@on_pressed.setter
def on_pressed(value: OnButtonPressedEvent) -> None
```

<a id="unreal.Button.on_released"></a>

#### on_released

```python
@property
def on_released() -> OnButtonReleasedEvent
```

(OnButtonReleasedEvent):  [Read-Write] Called when the button is released

<a id="unreal.Button.on_released"></a>

#### on_released

```python
@on_released.setter
def on_released(value: OnButtonReleasedEvent) -> None
```

<a id="unreal.Button.on_hovered"></a>

#### on_hovered

```python
@property
def on_hovered() -> OnButtonHoverEvent
```

(OnButtonHoverEvent):  [Read-Write]

<a id="unreal.Button.on_hovered"></a>

#### on_hovered

```python
@on_hovered.setter
def on_hovered(value: OnButtonHoverEvent) -> None
```

<a id="unreal.Button.on_unhovered"></a>

#### on_unhovered

```python
@property
def on_unhovered() -> OnButtonHoverEvent
```

(OnButtonHoverEvent):  [Read-Write]

<a id="unreal.Button.on_unhovered"></a>

#### on_unhovered

```python
@on_unhovered.setter
def on_unhovered(value: OnButtonHoverEvent) -> None
```

<a id="unreal.Button.set_touch_method"></a>

#### set_touch_method

```python
def set_touch_method(touch_method: ButtonTouchMethod) -> None
```

x.set_touch_method(touch_method) -> None
Set Touch Method

Args:
    touch_method (ButtonTouchMethod):

<a id="unreal.Button.set_style"></a>

#### set_style

```python
def set_style(style: ButtonStyle) -> None
```

x.set_style(style) -> None
Sets the color multiplier for the button background

Args:
    style (ButtonStyle):

<a id="unreal.Button.set_press_method"></a>

#### set_press_method

```python
def set_press_method(press_method: ButtonPressMethod) -> None
```

x.set_press_method(press_method) -> None
Set Press Method

Args:
    press_method (ButtonPressMethod):

<a id="unreal.Button.set_color_and_opacity"></a>

#### set_color_and_opacity

```python
def set_color_and_opacity(color_and_opacity: LinearColor) -> None
```

x.set_color_and_opacity(color_and_opacity) -> None
Sets the color multiplier for the button content

Args:
    color_and_opacity (LinearColor):

<a id="unreal.Button.set_click_method"></a>

#### set_click_method

```python
def set_click_method(click_method: ButtonClickMethod) -> None
```

x.set_click_method(click_method) -> None
Set Click Method

Args:
    click_method (ButtonClickMethod):

<a id="unreal.Button.set_background_color"></a>

#### set_background_color

```python
def set_background_color(background_color: LinearColor) -> None
```

x.set_background_color(background_color) -> None
Sets the color multiplier for the button background

Args:
    background_color (LinearColor):

<a id="unreal.Button.is_pressed"></a>

#### is_pressed

```python
def is_pressed() -> bool
```

x.is_pressed() -> bool
Returns true if the user is actively pressing the button.  Do not use this for detecting 'Clicks', use the OnClicked event instead.

Returns:
    bool: true if the user is actively pressing the button otherwise false.

<a id="unreal.ButtonSlot"></a>