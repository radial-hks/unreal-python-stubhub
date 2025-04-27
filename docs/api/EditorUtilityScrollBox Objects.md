## EditorUtilityScrollBox Objects

```python
class EditorUtilityScrollBox(ScrollBox)
```

Editor Utility Scroll Box

**C++ Source:**

- **Module**: Blutility
- **File**: EditorUtilityWidgetComponents.h

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

<a id="unreal.EditorUtilitySlider"></a>