## EarthTabButtonWidget Objects

```python
class EarthTabButtonWidget(UserWidget)
```

Earth Tab Button Widget

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesEditorUI
- **File**: EarthTabButton.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``auto_execute_command`` (bool):  [Read-Write]
- ``button`` (Button):  [Read-Write]
- ``button_display_name`` (Text):  [Read-Write]
- ``button_name`` (Name):  [Read-Write]
- ``button_texture`` (Texture):  [Read-Write]
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``color_and_opacity`` (LinearColor):  [Read-Write] The color and opacity of this widget.  Tints all child widgets.
- ``command_class`` (type(Class)):  [Read-Write]
- ``command_key`` (str):  [Read-Write]
- ``command_param_key`` (str):  [Read-Write]
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``desired_focus_widget`` (WidgetChild):  [Read-Write]
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``foreground_color`` (SlateColor):  [Read-Write] The foreground color of the widget, this is inherited by sub widgets.  Any color property
  that is marked as inherit will use this color.
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_focusable`` (bool):  [Read-Write] Setting this flag to true, allows this widget to accept focus when clicked, or when navigated to.
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_checked`` (OnEarthTabButtonChecked):  [Read-Write]
- ``on_unchecked`` (OnEarthTabButtonUnchecked):  [Read-Write]
- ``on_visibility_changed`` (OnVisibilityChangedEvent):  [Read-Write] Called when the visibility has changed
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``padding`` (Margin):  [Read-Write] The padding area around the content.
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``preview_background`` (Texture2D):  [Read-Write] A preview background that you can use when designing the UI to get a sense of scale on the screen.  Use
  a texture with a screenshot of your game in it, for example if you were designing a HUD.
- ``priority`` (int32):  [Read-Write]
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``stop_action`` (bool):  [Read-Write]
- ``tick_frequency`` (WidgetTickFrequency):  [Read-Write] This widget is allowed to tick. If this is unchecked tick will never be called, animations will not play correctly, and latent actions will not execute.
  Uncheck this for performance reasons only
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``widget_class`` (type(Class)):  [Read-Write]
- ``widget_data`` (DataTable):  [Read-Write]

<a id="unreal.EarthTabButtonWidget.button"></a>

#### button

```python
@property
def button() -> Button
```

(Button):  [Read-Write]

<a id="unreal.EarthTabButtonWidget.button"></a>

#### button

```python
@button.setter
def button(value: Button) -> None
```

<a id="unreal.EarthTabButtonWidget.button_name"></a>

#### button\_name

```python
@property
def button_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.EarthTabButtonWidget.button_name"></a>

#### button\_name

```python
@button_name.setter
def button_name(value: Name) -> None
```

<a id="unreal.EarthTabButtonWidget.button_display_name"></a>

#### button\_display\_name

```python
@property
def button_display_name() -> Text
```

(Text):  [Read-Write]

<a id="unreal.EarthTabButtonWidget.button_display_name"></a>

#### button\_display\_name

```python
@button_display_name.setter
def button_display_name(value: Text) -> None
```

<a id="unreal.EarthTabButtonWidget.button_texture"></a>

#### button\_texture

```python
@property
def button_texture() -> Texture
```

(Texture):  [Read-Write]

<a id="unreal.EarthTabButtonWidget.button_texture"></a>

#### button\_texture

```python
@button_texture.setter
def button_texture(value: Texture) -> None
```

<a id="unreal.EarthTabButtonWidget.widget_class"></a>

#### widget\_class

```python
@property
def widget_class() -> Class
```

(type(Class)):  [Read-Write]

<a id="unreal.EarthTabButtonWidget.widget_class"></a>

#### widget\_class

```python
@widget_class.setter
def widget_class(value: Class) -> None
```

<a id="unreal.EarthTabButtonWidget.widget_data"></a>

#### widget\_data

```python
@property
def widget_data() -> DataTable
```

(DataTable):  [Read-Write]

<a id="unreal.EarthTabButtonWidget.widget_data"></a>

#### widget\_data

```python
@widget_data.setter
def widget_data(value: DataTable) -> None
```

<a id="unreal.EarthTabButtonWidget.command_class"></a>

#### command\_class

```python
@property
def command_class() -> Class
```

(type(Class)):  [Read-Write]

<a id="unreal.EarthTabButtonWidget.command_class"></a>

#### command\_class

```python
@command_class.setter
def command_class(value: Class) -> None
```

<a id="unreal.EarthTabButtonWidget.command_key"></a>

#### command\_key

```python
@property
def command_key() -> str
```

(str):  [Read-Write]

<a id="unreal.EarthTabButtonWidget.command_key"></a>

#### command\_key

```python
@command_key.setter
def command_key(value: str) -> None
```

<a id="unreal.EarthTabButtonWidget.command_param_key"></a>

#### command\_param\_key

```python
@property
def command_param_key() -> str
```

(str):  [Read-Write]

<a id="unreal.EarthTabButtonWidget.command_param_key"></a>

#### command\_param\_key

```python
@command_param_key.setter
def command_param_key(value: str) -> None
```

<a id="unreal.EarthTabButtonWidget.on_checked"></a>

#### on\_checked

```python
@property
def on_checked() -> OnEarthTabButtonChecked
```

(OnEarthTabButtonChecked):  [Read-Write]

<a id="unreal.EarthTabButtonWidget.on_checked"></a>

#### on\_checked

```python
@on_checked.setter
def on_checked(value: OnEarthTabButtonChecked) -> None
```

<a id="unreal.EarthTabButtonWidget.on_unchecked"></a>

#### on\_unchecked

```python
@property
def on_unchecked() -> OnEarthTabButtonUnchecked
```

(OnEarthTabButtonUnchecked):  [Read-Write]

<a id="unreal.EarthTabButtonWidget.on_unchecked"></a>

#### on\_unchecked

```python
@on_unchecked.setter
def on_unchecked(value: OnEarthTabButtonUnchecked) -> None
```

<a id="unreal.EarthTabButtonWidget.auto_execute_command"></a>

#### auto\_execute\_command

```python
@property
def auto_execute_command() -> bool
```

(bool):  [Read-Write]

<a id="unreal.EarthTabButtonWidget.auto_execute_command"></a>

#### auto\_execute\_command

```python
@auto_execute_command.setter
def auto_execute_command(value: bool) -> None
```

<a id="unreal.EarthTabButtonWidget.set_enabled"></a>

#### set\_enabled

```python
def set_enabled(enabled: bool) -> None
```

x.set_enabled(enabled) -> None
Set Enabled

Args:
    enabled (bool):

<a id="unreal.EarthTabButtonWidget.set_checked"></a>

#### set\_checked

```python
def set_checked(checked: bool) -> None
```

x.set_checked(checked) -> None
Set Checked

Args:
    checked (bool):

<a id="unreal.EarthTabButtonWidget.set_button_texture"></a>

#### set\_button\_texture

```python
def set_button_texture(button_texture: Texture) -> None
```

x.set_button_texture(button_texture) -> None
Set Button Texture

Args:
    button_texture (Texture):

<a id="unreal.EarthTabButtonWidget.set_button_style"></a>

#### set\_button\_style

```python
def set_button_style() -> None
```

x.set_button_style() -> None
Set Button Style

<a id="unreal.EarthTabButtonWidget.set_button_display_name"></a>

#### set\_button\_display\_name

```python
def set_button_display_name(button_display_name: Text) -> None
```

x.set_button_display_name(button_display_name) -> None
Set Button Display Name

Args:
    button_display_name (Text):

<a id="unreal.EarthTabButtonWidget.on_clicked"></a>

#### on\_clicked

```python
def on_clicked() -> None
```

x.on_clicked() -> None
On Clicked

<a id="unreal.EarthTabButtonWidget.get_enabled"></a>

#### get\_enabled

```python
def get_enabled() -> bool
```

x.get_enabled() -> bool
Get Enabled

Returns:
    bool:

<a id="unreal.EarthTabButtonWidget.get_checked"></a>

#### get\_checked

```python
def get_checked() -> bool
```

x.get_checked() -> bool
Get Checked

Returns:
    bool:

<a id="unreal.EarthTabButtonWidget.freeze_command"></a>

#### freeze\_command

```python
def freeze_command(frozen: bool) -> None
```

x.freeze_command(frozen) -> None
Freeze Command

Args:
    frozen (bool):

<a id="unreal.EarthTabButtonWidget.finish_command_manually"></a>

#### finish\_command\_manually

```python
def finish_command_manually() -> None
```

x.finish_command_manually() -> None
Finish Command Manually

<a id="unreal.EarthTabButtonWidget.execute_command_once"></a>

#### execute\_command\_once

```python
def execute_command_once() -> None
```

x.execute_command_once() -> None
Execute Command Once

<a id="unreal.EarthTabButtonWidget.execute_command_manually"></a>

#### execute\_command\_manually

```python
def execute_command_manually() -> None
```

x.execute_command_manually() -> None
Execute Command Manually

<a id="unreal.EarthTabButton"></a>