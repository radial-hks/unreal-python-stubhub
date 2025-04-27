## EditorUtilitySpinBox Objects

```python
class EditorUtilitySpinBox(SpinBox)
```

Editor Utility Spin Box

**C++ Source:**

- **Module**: Blutility
- **File**: EditorUtilityWidgetComponents.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``always_uses_delta_snap`` (bool):  [Read-Write] Whether this spin box should use the delta snapping logic for typed values - default false
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clear_keyboard_focus_on_commit`` (bool):  [Read-Write] Whether to remove the keyboard focus from the spin box when the value is committed
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``delta`` (float):  [Read-Write] The amount by which to change the spin box value as the slider moves.
- ``enable_slider`` (bool):  [Read-Write] Whether this spin box should have slider feature enabled
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``font`` (SlateFontInfo):  [Read-Write] Font color and opacity (overrides style)
- ``foreground_color`` (SlateColor):  [Read-Write]
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``justification`` (TextJustify):  [Read-Write] The justification the value text should appear as.
- ``keyboard_type`` (VirtualKeyboardType):  [Read-Write] If we're on a platform that requires a virtual keyboard, what kind of keyboard should this widget use?
- ``max_fractional_digits`` (int32):  [Read-Write] The maximum required fractional digits - default 6
- ``max_slider_value`` (float):  [Read-Write] The maximum allowable value that can be specified using the slider
- ``max_value`` (float):  [Read-Write] The maximum allowable value that can be manually entered into the spin box
- ``min_desired_width`` (float):  [Read-Write] The minimum width of the spin box
- ``min_fractional_digits`` (int32):  [Read-Write] The minimum required fractional digits - default 1
- ``min_slider_value`` (float):  [Read-Write] The minimum allowable value that can be specified using the slider
- ``min_value`` (float):  [Read-Write] The minimum allowable value that can be manually entered into the spin box
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_begin_slider_movement`` (OnSpinBoxBeginSliderMovement):  [Read-Write] Called right before the slider begins to move
- ``on_end_slider_movement`` (OnSpinBoxValueChangedEvent):  [Read-Write] Called right after the slider handle is released by the user
- ``on_value_changed`` (OnSpinBoxValueChangedEvent):  [Read-Write] Called when the value is changed interactively by the user
- ``on_value_committed`` (OnSpinBoxValueCommittedEvent):  [Read-Write] Called when the value is committed. Occurs when the user presses Enter or the text box loses focus.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``override_max_slider_value`` (bool):  [Read-Write] Whether the optional MaxSliderValue attribute of the widget is set
- ``override_max_value`` (bool):  [Read-Write] Whether the optional MaxValue attribute of the widget is set
- ``override_min_slider_value`` (bool):  [Read-Write] Whether the optional MinSliderValue attribute of the widget is set
- ``override_min_value`` (bool):  [Read-Write] Whether the optional MinValue attribute of the widget is set
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``select_all_text_on_commit`` (bool):  [Read-Write] Whether to select the text in the spin box when the value is committed
- ``slider_exponent`` (float):  [Read-Write] The exponent by which to increase the delta as the mouse moves. 1 is constant (never increases the delta).
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``value`` (float):  [Read-Write] Value stored in this spin box
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``widget_style`` (SpinBoxStyle):  [Read-Write] The Style

<a id="unreal.EditorUtilityThrobber"></a>