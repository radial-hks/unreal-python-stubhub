## EditorUtilitySlider Objects

```python
class EditorUtilitySlider(Slider)
```

Editor Utility Slider

**C++ Source:**

- **Module**: Blutility
- **File**: EditorUtilityWidgetComponents.h

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

<a id="unreal.EditorUtilitySpinBox"></a>