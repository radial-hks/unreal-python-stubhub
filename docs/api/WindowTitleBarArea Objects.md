## WindowTitleBarArea Objects

```python
class WindowTitleBarArea(ContentWidget)
```

A panel for defining a region of the UI that should allow users to drag the window on desktop platforms.

**C++ Source:**

- **Module**: UMG
- **File**: WindowTitleBarArea.h

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
- ``double_click_toggles_fullscreen`` (bool):  [Read-Write] Should double clicking the title bar area toggle fullscreen instead of maximizing the window.
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
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
- ``window_buttons_enabled`` (bool):  [Read-Write] Should the title bar area diaplay window minimize/maximize/close buttons.

<a id="unreal.WindowTitleBarArea.window_buttons_enabled"></a>

#### window_buttons_enabled

```python
@property
def window_buttons_enabled() -> bool
```

(bool):  [Read-Write] Should the title bar area diaplay window minimize/maximize/close buttons.

<a id="unreal.WindowTitleBarArea.window_buttons_enabled"></a>

#### window_buttons_enabled

```python
@window_buttons_enabled.setter
def window_buttons_enabled(value: bool) -> None
```

<a id="unreal.WindowTitleBarArea.double_click_toggles_fullscreen"></a>

#### double_click_toggles_fullscreen

```python
@property
def double_click_toggles_fullscreen() -> bool
```

(bool):  [Read-Write] Should double clicking the title bar area toggle fullscreen instead of maximizing the window.

<a id="unreal.WindowTitleBarArea.double_click_toggles_fullscreen"></a>

#### double_click_toggles_fullscreen

```python
@double_click_toggles_fullscreen.setter
def double_click_toggles_fullscreen(value: bool) -> None
```

<a id="unreal.WindowTitleBarArea.set_vertical_alignment"></a>

#### set_vertical_alignment

```python
def set_vertical_alignment(vertical_alignment: VerticalAlignment) -> None
```

x.set_vertical_alignment(vertical_alignment) -> None
Set Vertical Alignment

Args:
    vertical_alignment (VerticalAlignment):

<a id="unreal.WindowTitleBarArea.set_padding"></a>

#### set_padding

```python
def set_padding(padding: Margin) -> None
```

x.set_padding(padding) -> None
Set Padding

Args:
    padding (Margin):

<a id="unreal.WindowTitleBarArea.set_horizontal_alignment"></a>

#### set_horizontal_alignment

```python
def set_horizontal_alignment(
        horizontal_alignment: HorizontalAlignment) -> None
```

x.set_horizontal_alignment(horizontal_alignment) -> None
Set Horizontal Alignment

Args:
    horizontal_alignment (HorizontalAlignment):

<a id="unreal.WindowTitleBarAreaSlot"></a>