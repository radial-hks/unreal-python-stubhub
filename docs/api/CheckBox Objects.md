## CheckBox Objects

```python
class CheckBox(ContentWidget)
```

The checkbox widget allows you to display a toggled state of 'unchecked', 'checked' and
'indeterminable.  You can use the checkbox for a classic checkbox, or as a toggle button,
or as radio buttons.

* Single Child
* Toggle

**C++ Source:**

- **Module**: UMG
- **File**: CheckBox.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``checked_state`` (CheckBoxState):  [Read-Write] Whether the check box is currently in a checked state
- ``click_method`` (ButtonClickMethod):  [Read-Write] The type of mouse action required by the user to trigger the buttons 'Click'
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``horizontal_alignment`` (HorizontalAlignment):  [Read-Write] How the content of the toggle button should align within the given space
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_focusable`` (bool):  [Read-Write] Sometimes a button should only be mouse-clickable and never keyboard focusable.
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_check_state_changed`` (OnCheckBoxComponentStateChanged):  [Read-Write] Called when the checked state has changed
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
- ``widget_style`` (CheckBoxStyle):  [Read-Write] The checkbox bar style

<a id="unreal.CheckBox.checked_state"></a>

#### checked_state

```python
@property
def checked_state() -> CheckBoxState
```

(CheckBoxState):  [Read-Write] Whether the check box is currently in a checked state

<a id="unreal.CheckBox.checked_state"></a>

#### checked_state

```python
@checked_state.setter
def checked_state(value: CheckBoxState) -> None
```

<a id="unreal.CheckBox.widget_style"></a>

#### widget_style

```python
@property
def widget_style() -> CheckBoxStyle
```

(CheckBoxStyle):  [Read-Write] The checkbox bar style

<a id="unreal.CheckBox.widget_style"></a>

#### widget_style

```python
@widget_style.setter
def widget_style(value: CheckBoxStyle) -> None
```

<a id="unreal.CheckBox.horizontal_alignment"></a>

#### horizontal_alignment

```python
@property
def horizontal_alignment() -> HorizontalAlignment
```

(HorizontalAlignment):  [Read-Only] How the content of the toggle button should align within the given space

<a id="unreal.CheckBox.click_method"></a>

#### click_method

```python
@property
def click_method() -> ButtonClickMethod
```

(ButtonClickMethod):  [Read-Write] The type of mouse action required by the user to trigger the buttons 'Click'

<a id="unreal.CheckBox.click_method"></a>

#### click_method

```python
@click_method.setter
def click_method(value: ButtonClickMethod) -> None
```

<a id="unreal.CheckBox.touch_method"></a>

#### touch_method

```python
@property
def touch_method() -> ButtonTouchMethod
```

(ButtonTouchMethod):  [Read-Write] The type of touch action required by the user to trigger the buttons 'Click'

<a id="unreal.CheckBox.touch_method"></a>

#### touch_method

```python
@touch_method.setter
def touch_method(value: ButtonTouchMethod) -> None
```

<a id="unreal.CheckBox.press_method"></a>

#### press_method

```python
@property
def press_method() -> ButtonPressMethod
```

(ButtonPressMethod):  [Read-Write] The type of keyboard/gamepad button press action required by the user to trigger the buttons 'Click'

<a id="unreal.CheckBox.press_method"></a>

#### press_method

```python
@press_method.setter
def press_method(value: ButtonPressMethod) -> None
```

<a id="unreal.CheckBox.is_focusable"></a>

#### is_focusable

```python
@property
def is_focusable() -> bool
```

(bool):  [Read-Only] Sometimes a button should only be mouse-clickable and never keyboard focusable.

<a id="unreal.CheckBox.on_check_state_changed"></a>

#### on_check_state_changed

```python
@property
def on_check_state_changed() -> OnCheckBoxComponentStateChanged
```

(OnCheckBoxComponentStateChanged):  [Read-Write] Called when the checked state has changed

<a id="unreal.CheckBox.on_check_state_changed"></a>

#### on_check_state_changed

```python
@on_check_state_changed.setter
def on_check_state_changed(value: OnCheckBoxComponentStateChanged) -> None
```

<a id="unreal.CheckBox.set_touch_method"></a>

#### set_touch_method

```python
def set_touch_method(touch_method: ButtonTouchMethod) -> None
```

x.set_touch_method(touch_method) -> None
Sets the touch method.

Args:
    touch_method (ButtonTouchMethod):

<a id="unreal.CheckBox.set_press_method"></a>

#### set_press_method

```python
def set_press_method(press_method: ButtonPressMethod) -> None
```

x.set_press_method(press_method) -> None
Sets the press method.

Args:
    press_method (ButtonPressMethod):

<a id="unreal.CheckBox.set_is_checked"></a>

#### set_is_checked

```python
def set_is_checked(is_checked: bool) -> None
```

x.set_is_checked(is_checked) -> None
Sets the checked state.

Args:
    is_checked (bool):

<a id="unreal.CheckBox.set_click_method"></a>

#### set_click_method

```python
def set_click_method(click_method: ButtonClickMethod) -> None
```

x.set_click_method(click_method) -> None
Sets the click method.

Args:
    click_method (ButtonClickMethod):

<a id="unreal.CheckBox.set_checked_state"></a>

#### set_checked_state

```python
def set_checked_state(checked_state: CheckBoxState) -> None
```

x.set_checked_state(checked_state) -> None
Sets the checked state.

Args:
    checked_state (CheckBoxState):

<a id="unreal.CheckBox.is_pressed"></a>

#### is_pressed

```python
def is_pressed() -> bool
```

x.is_pressed() -> bool
Returns true if this button is currently pressed

Returns:
    bool:

<a id="unreal.CheckBox.is_checked"></a>

#### is_checked

```python
def is_checked() -> bool
```

x.is_checked() -> bool
Returns true if the checkbox is currently checked

Returns:
    bool:

<a id="unreal.CheckBox.get_checked_state"></a>

#### get_checked_state

```python
def get_checked_state() -> CheckBoxState
```

x.get_checked_state() -> CheckBoxState
Returns the full current checked state.

Returns:
    CheckBoxState:

<a id="unreal.CircularThrobber"></a>