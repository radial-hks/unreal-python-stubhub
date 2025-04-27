## ScrollBox Objects

```python
class ScrollBox(PanelWidget)
```

An arbitrary scrollable collection of widgets.  Great for presenting 10-100 widgets in a list.  Doesn't support virtualization.

**C++ Source:**

- **Module**: UMG
- **File**: ScrollBox.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``allow_overscroll`` (bool):  [Read-Write] Disable to stop scrollbars from activating inertial overscrolling
- ``allow_right_click_drag_scrolling`` (bool):  [Read-Write] Option to disable right-click-drag scrolling
- ``always_show_scrollbar`` (bool):  [Read-Write]
- ``always_show_scrollbar_track`` (bool):  [Read-Write]
- ``animate_wheel_scrolling`` (bool):  [Read-Write] True to lerp smoothly when wheel scrolling along the scroll box
- ``back_pad_scrolling`` (bool):  [Read-Write] Whether to back pad this scroll box, allowing user to scroll backward until child contents are no longer visible
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``consume_mouse_wheel`` (ConsumeMouseWheel):  [Read-Write] When mouse wheel events should be consumed.
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``enable_touch_scrolling`` (bool):  [Read-Write] True to allow scrolling using touch input.
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``front_pad_scrolling`` (bool):  [Read-Write] Whether to front pad this scroll box, allowing user to scroll forward until child contents are no longer visible
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``navigation_destination`` (DescendantScrollDestination):  [Read-Write] Sets where to scroll a widget to when using explicit navigation or if ScrollWhenFocusChanges is enabled
- ``navigation_scroll_padding`` (float):  [Read-Write] The amount of padding to ensure exists between the item being navigated to, at the edge of the
  scrollbox.  Use this if you want to ensure there's a preview of the next item the user could scroll to.
- ``on_scroll_bar_visibility_changed`` (OnScrollBarVisibilityChangedEvent):  [Read-Write] Called when the scrollbar visibility has changed
- ``on_user_scrolled`` (OnUserScrolledEvent):  [Read-Write] Called when the scroll has changed
- ``orientation`` (Orientation):  [Read-Write] The orientation of the scrolling and stacking in the box.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``scroll_animation_interpolation_speed`` (float):  [Read-Write]
- ``scroll_bar_visibility`` (SlateVisibility):  [Read-Write] Visibility
- ``scroll_when_focus_changes`` (ScrollWhenFocusChanges):  [Read-Write] Scroll behavior when user focus is given to a child widget
- ``scrollbar_padding`` (Margin):  [Read-Write] The margin around the scrollbar
- ``scrollbar_thickness`` (Vector2D):  [Read-Write] The thickness of the scrollbar thumb
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``wheel_scroll_multiplier`` (float):  [Read-Write] The multiplier to apply when wheel scrolling
- ``widget_bar_style`` (ScrollBarStyle):  [Read-Write] The bar style
- ``widget_style`` (ScrollBoxStyle):  [Read-Write] The style

<a id="unreal.ScrollBox.scroll_animation_interpolation_speed"></a>

#### scroll_animation_interpolation_speed

```python
@property
def scroll_animation_interpolation_speed() -> float
```

(float):  [Read-Write]

<a id="unreal.ScrollBox.scroll_animation_interpolation_speed"></a>

#### scroll_animation_interpolation_speed

```python
@scroll_animation_interpolation_speed.setter
def scroll_animation_interpolation_speed(value: float) -> None
```

<a id="unreal.ScrollBox.enable_touch_scrolling"></a>

#### enable_touch_scrolling

```python
@property
def enable_touch_scrolling() -> bool
```

(bool):  [Read-Write] True to allow scrolling using touch input.

<a id="unreal.ScrollBox.enable_touch_scrolling"></a>

#### enable_touch_scrolling

```python
@enable_touch_scrolling.setter
def enable_touch_scrolling(value: bool) -> None
```

<a id="unreal.ScrollBox.widget_style"></a>

#### widget_style

```python
@property
def widget_style() -> ScrollBoxStyle
```

(ScrollBoxStyle):  [Read-Write] The style

<a id="unreal.ScrollBox.widget_style"></a>

#### widget_style

```python
@widget_style.setter
def widget_style(value: ScrollBoxStyle) -> None
```

<a id="unreal.ScrollBox.widget_bar_style"></a>

#### widget_bar_style

```python
@property
def widget_bar_style() -> ScrollBarStyle
```

(ScrollBarStyle):  [Read-Write] The bar style

<a id="unreal.ScrollBox.widget_bar_style"></a>

#### widget_bar_style

```python
@widget_bar_style.setter
def widget_bar_style(value: ScrollBarStyle) -> None
```

<a id="unreal.ScrollBox.orientation"></a>

#### orientation

```python
@property
def orientation() -> Orientation
```

(Orientation):  [Read-Write] The orientation of the scrolling and stacking in the box.

<a id="unreal.ScrollBox.orientation"></a>

#### orientation

```python
@orientation.setter
def orientation(value: Orientation) -> None
```

<a id="unreal.ScrollBox.scroll_bar_visibility"></a>

#### scroll_bar_visibility

```python
@property
def scroll_bar_visibility() -> SlateVisibility
```

(SlateVisibility):  [Read-Write] Visibility

<a id="unreal.ScrollBox.scroll_bar_visibility"></a>

#### scroll_bar_visibility

```python
@scroll_bar_visibility.setter
def scroll_bar_visibility(value: SlateVisibility) -> None
```

<a id="unreal.ScrollBox.consume_mouse_wheel"></a>

#### consume_mouse_wheel

```python
@property
def consume_mouse_wheel() -> ConsumeMouseWheel
```

(ConsumeMouseWheel):  [Read-Write] When mouse wheel events should be consumed.

<a id="unreal.ScrollBox.consume_mouse_wheel"></a>

#### consume_mouse_wheel

```python
@consume_mouse_wheel.setter
def consume_mouse_wheel(value: ConsumeMouseWheel) -> None
```

<a id="unreal.ScrollBox.scrollbar_thickness"></a>

#### scrollbar_thickness

```python
@property
def scrollbar_thickness() -> Vector2D
```

(Vector2D):  [Read-Write] The thickness of the scrollbar thumb

<a id="unreal.ScrollBox.scrollbar_thickness"></a>

#### scrollbar_thickness

```python
@scrollbar_thickness.setter
def scrollbar_thickness(value: Vector2D) -> None
```

<a id="unreal.ScrollBox.scrollbar_padding"></a>

#### scrollbar_padding

```python
@property
def scrollbar_padding() -> Margin
```

(Margin):  [Read-Write] The margin around the scrollbar

<a id="unreal.ScrollBox.scrollbar_padding"></a>

#### scrollbar_padding

```python
@scrollbar_padding.setter
def scrollbar_padding(value: Margin) -> None
```

<a id="unreal.ScrollBox.always_show_scrollbar"></a>

#### always_show_scrollbar

```python
@property
def always_show_scrollbar() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ScrollBox.always_show_scrollbar"></a>

#### always_show_scrollbar

```python
@always_show_scrollbar.setter
def always_show_scrollbar(value: bool) -> None
```

<a id="unreal.ScrollBox.always_show_scrollbar_track"></a>

#### always_show_scrollbar_track

```python
@property
def always_show_scrollbar_track() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ScrollBox.always_show_scrollbar_track"></a>

#### always_show_scrollbar_track

```python
@always_show_scrollbar_track.setter
def always_show_scrollbar_track(value: bool) -> None
```

<a id="unreal.ScrollBox.allow_overscroll"></a>

#### allow_overscroll

```python
@property
def allow_overscroll() -> bool
```

(bool):  [Read-Write] Disable to stop scrollbars from activating inertial overscrolling

<a id="unreal.ScrollBox.allow_overscroll"></a>

#### allow_overscroll

```python
@allow_overscroll.setter
def allow_overscroll(value: bool) -> None
```

<a id="unreal.ScrollBox.back_pad_scrolling"></a>

#### back_pad_scrolling

```python
@property
def back_pad_scrolling() -> bool
```

(bool):  [Read-Only] Whether to back pad this scroll box, allowing user to scroll backward until child contents are no longer visible

<a id="unreal.ScrollBox.front_pad_scrolling"></a>

#### front_pad_scrolling

```python
@property
def front_pad_scrolling() -> bool
```

(bool):  [Read-Only] Whether to front pad this scroll box, allowing user to scroll forward until child contents are no longer visible

<a id="unreal.ScrollBox.animate_wheel_scrolling"></a>

#### animate_wheel_scrolling

```python
@property
def animate_wheel_scrolling() -> bool
```

(bool):  [Read-Write] True to lerp smoothly when wheel scrolling along the scroll box

<a id="unreal.ScrollBox.animate_wheel_scrolling"></a>

#### animate_wheel_scrolling

```python
@animate_wheel_scrolling.setter
def animate_wheel_scrolling(value: bool) -> None
```

<a id="unreal.ScrollBox.navigation_destination"></a>

#### navigation_destination

```python
@property
def navigation_destination() -> DescendantScrollDestination
```

(DescendantScrollDestination):  [Read-Write] Sets where to scroll a widget to when using explicit navigation or if ScrollWhenFocusChanges is enabled

<a id="unreal.ScrollBox.navigation_destination"></a>

#### navigation_destination

```python
@navigation_destination.setter
def navigation_destination(value: DescendantScrollDestination) -> None
```

<a id="unreal.ScrollBox.navigation_scroll_padding"></a>

#### navigation_scroll_padding

```python
@property
def navigation_scroll_padding() -> float
```

(float):  [Read-Only] The amount of padding to ensure exists between the item being navigated to, at the edge of the
scrollbox.  Use this if you want to ensure there's a preview of the next item the user could scroll to.

<a id="unreal.ScrollBox.scroll_when_focus_changes"></a>

#### scroll_when_focus_changes

```python
@property
def scroll_when_focus_changes() -> ScrollWhenFocusChanges
```

(ScrollWhenFocusChanges):  [Read-Write] Scroll behavior when user focus is given to a child widget

<a id="unreal.ScrollBox.scroll_when_focus_changes"></a>

#### scroll_when_focus_changes

```python
@scroll_when_focus_changes.setter
def scroll_when_focus_changes(value: ScrollWhenFocusChanges) -> None
```

<a id="unreal.ScrollBox.allow_right_click_drag_scrolling"></a>

#### allow_right_click_drag_scrolling

```python
@property
def allow_right_click_drag_scrolling() -> bool
```

(bool):  [Read-Write] Option to disable right-click-drag scrolling

<a id="unreal.ScrollBox.allow_right_click_drag_scrolling"></a>

#### allow_right_click_drag_scrolling

```python
@allow_right_click_drag_scrolling.setter
def allow_right_click_drag_scrolling(value: bool) -> None
```

<a id="unreal.ScrollBox.wheel_scroll_multiplier"></a>

#### wheel_scroll_multiplier

```python
@property
def wheel_scroll_multiplier() -> float
```

(float):  [Read-Write] The multiplier to apply when wheel scrolling

<a id="unreal.ScrollBox.wheel_scroll_multiplier"></a>

#### wheel_scroll_multiplier

```python
@wheel_scroll_multiplier.setter
def wheel_scroll_multiplier(value: float) -> None
```

<a id="unreal.ScrollBox.on_user_scrolled"></a>

#### on_user_scrolled

```python
@property
def on_user_scrolled() -> OnUserScrolledEvent
```

(OnUserScrolledEvent):  [Read-Write] Called when the scroll has changed

<a id="unreal.ScrollBox.on_user_scrolled"></a>

#### on_user_scrolled

```python
@on_user_scrolled.setter
def on_user_scrolled(value: OnUserScrolledEvent) -> None
```

<a id="unreal.ScrollBox.on_scroll_bar_visibility_changed"></a>

#### on_scroll_bar_visibility_changed

```python
@property
def on_scroll_bar_visibility_changed() -> OnScrollBarVisibilityChangedEvent
```

(OnScrollBarVisibilityChangedEvent):  [Read-Write] Called when the scrollbar visibility has changed

<a id="unreal.ScrollBox.on_scroll_bar_visibility_changed"></a>

#### on_scroll_bar_visibility_changed

```python
@on_scroll_bar_visibility_changed.setter
def on_scroll_bar_visibility_changed(
        value: OnScrollBarVisibilityChangedEvent) -> None
```

<a id="unreal.ScrollBox.set_wheel_scroll_multiplier"></a>

#### set_wheel_scroll_multiplier

```python
def set_wheel_scroll_multiplier(new_wheel_scroll_multiplier: float) -> None
```

x.set_wheel_scroll_multiplier(new_wheel_scroll_multiplier) -> None
Set Wheel Scroll Multiplier

Args:
    new_wheel_scroll_multiplier (float):

<a id="unreal.ScrollBox.set_scroll_when_focus_changes"></a>

#### set_scroll_when_focus_changes

```python
def set_scroll_when_focus_changes(
        new_scroll_when_focus_changes: ScrollWhenFocusChanges) -> None
```

x.set_scroll_when_focus_changes(new_scroll_when_focus_changes) -> None
Set Scroll when Focus Changes

Args:
    new_scroll_when_focus_changes (ScrollWhenFocusChanges):

<a id="unreal.ScrollBox.set_scroll_offset"></a>

#### set_scroll_offset

```python
def set_scroll_offset(new_scroll_offset: float) -> None
```

x.set_scroll_offset(new_scroll_offset) -> None
Updates the scroll offset of the scrollbox.

Args:
    new_scroll_offset (float): is in Slate Units.

<a id="unreal.ScrollBox.set_scroll_bar_visibility"></a>

#### set_scroll_bar_visibility

```python
def set_scroll_bar_visibility(
        new_scroll_bar_visibility: SlateVisibility) -> None
```

x.set_scroll_bar_visibility(new_scroll_bar_visibility) -> None
Set Scroll Bar Visibility

Args:
    new_scroll_bar_visibility (SlateVisibility):

<a id="unreal.ScrollBox.set_scrollbar_thickness"></a>

#### set_scrollbar_thickness

```python
def set_scrollbar_thickness(new_scrollbar_thickness: Vector2D) -> None
```

x.set_scrollbar_thickness(new_scrollbar_thickness) -> None
Set Scrollbar Thickness

Args:
    new_scrollbar_thickness (Vector2D):

<a id="unreal.ScrollBox.set_scrollbar_padding"></a>

#### set_scrollbar_padding

```python
def set_scrollbar_padding(new_scrollbar_padding: Margin) -> None
```

x.set_scrollbar_padding(new_scrollbar_padding) -> None
Set Scrollbar Padding

Args:
    new_scrollbar_padding (Margin):

<a id="unreal.ScrollBox.set_scroll_animation_interpolation_speed"></a>

#### set_scroll_animation_interpolation_speed

```python
def set_scroll_animation_interpolation_speed(
        new_scroll_animation_interpolation_speed: float) -> None
```

x.set_scroll_animation_interpolation_speed(new_scroll_animation_interpolation_speed) -> None
Set Scroll Animation Interpolation Speed

Args:
    new_scroll_animation_interpolation_speed (float):

<a id="unreal.ScrollBox.set_orientation"></a>

#### set_orientation

```python
def set_orientation(new_orientation: Orientation) -> None
```

x.set_orientation(new_orientation) -> None
Set Orientation

Args:
    new_orientation (Orientation):

<a id="unreal.ScrollBox.set_navigation_destination"></a>

#### set_navigation_destination

```python
def set_navigation_destination(
        new_navigation_destination: DescendantScrollDestination) -> None
```

x.set_navigation_destination(new_navigation_destination) -> None
Set Navigation Destination

Args:
    new_navigation_destination (DescendantScrollDestination):

<a id="unreal.ScrollBox.set_consume_mouse_wheel"></a>

#### set_consume_mouse_wheel

```python
def set_consume_mouse_wheel(
        new_consume_mouse_wheel: ConsumeMouseWheel) -> None
```

x.set_consume_mouse_wheel(new_consume_mouse_wheel) -> None
Set Consume Mouse Wheel

Args:
    new_consume_mouse_wheel (ConsumeMouseWheel):

<a id="unreal.ScrollBox.set_animate_wheel_scrolling"></a>

#### set_animate_wheel_scrolling

```python
def set_animate_wheel_scrolling(should_animate_wheel_scrolling: bool) -> None
```

x.set_animate_wheel_scrolling(should_animate_wheel_scrolling) -> None
Set Animate Wheel Scrolling

Args:
    should_animate_wheel_scrolling (bool):

<a id="unreal.ScrollBox.set_always_show_scrollbar"></a>

#### set_always_show_scrollbar

```python
def set_always_show_scrollbar(new_always_show_scrollbar: bool) -> None
```

x.set_always_show_scrollbar(new_always_show_scrollbar) -> None
Set Always Show Scrollbar

Args:
    new_always_show_scrollbar (bool):

<a id="unreal.ScrollBox.set_allow_overscroll"></a>

#### set_allow_overscroll

```python
def set_allow_overscroll(new_allow_overscroll: bool) -> None
```

x.set_allow_overscroll(new_allow_overscroll) -> None
Set Allow Overscroll

Args:
    new_allow_overscroll (bool):

<a id="unreal.ScrollBox.scroll_widget_into_view"></a>

#### scroll_widget_into_view

```python
def scroll_widget_into_view(
        widget_to_find: Widget,
        animate_scroll: bool = True,
        scroll_destination:
    DescendantScrollDestination = DescendantScrollDestination.INTO_VIEW,
        padding: float = 0.000000) -> None
```

x.scroll_widget_into_view(widget_to_find, animate_scroll=True, scroll_destination=DescendantScrollDestination.INTO_VIEW, padding=0.000000) -> None
Scrolls the ScrollBox to the widget during the next layout pass.

Args:
    widget_to_find (Widget): 
    animate_scroll (bool): 
    scroll_destination (DescendantScrollDestination): 
    padding (float):

<a id="unreal.ScrollBox.scroll_to_start"></a>

#### scroll_to_start

```python
def scroll_to_start() -> None
```

x.scroll_to_start() -> None
Scrolls the ScrollBox to the top instantly

<a id="unreal.ScrollBox.scroll_to_end"></a>

#### scroll_to_end

```python
def scroll_to_end() -> None
```

x.scroll_to_end() -> None
Scrolls the ScrollBox to the bottom instantly during the next layout pass.

<a id="unreal.ScrollBox.get_view_offset_fraction"></a>

#### get_view_offset_fraction

```python
def get_view_offset_fraction() -> float
```

x.get_view_offset_fraction() -> float
Get View Offset Fraction

Returns:
    float:

<a id="unreal.ScrollBox.get_view_fraction"></a>

#### get_view_fraction

```python
def get_view_fraction() -> float
```

x.get_view_fraction() -> float
Gets the fraction currently visible in the scrollbox

Returns:
    float:

<a id="unreal.ScrollBox.get_scroll_offset_of_end"></a>

#### get_scroll_offset_of_end

```python
def get_scroll_offset_of_end() -> float
```

x.get_scroll_offset_of_end() -> float
Gets the scroll offset of the bottom of the ScrollBox in Slate Units.

Returns:
    float:

<a id="unreal.ScrollBox.get_scroll_offset"></a>

#### get_scroll_offset

```python
def get_scroll_offset() -> float
```

x.get_scroll_offset() -> float
Gets the scroll offset of the scrollbox in Slate Units.

Returns:
    float:

<a id="unreal.ScrollBox.end_inertial_scrolling"></a>

#### end_inertial_scrolling

```python
def end_inertial_scrolling() -> None
```

x.end_inertial_scrolling() -> None
Instantly stops any inertial scrolling that is currently in progress

<a id="unreal.ScrollBoxSlot"></a>