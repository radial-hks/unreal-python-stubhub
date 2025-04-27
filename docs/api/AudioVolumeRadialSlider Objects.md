## AudioVolumeRadialSlider Objects

```python
class AudioVolumeRadialSlider(AudioRadialSlider)
```

An audio slider widget, for use with volume.

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioRadialSlider.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``center_background_color`` (LinearColor):  [Read-Write] The color to draw the widget background.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``hand_start_end_ratio`` (Vector2D):  [Read-Write] Start and end of the hand as a ratio to the slider radius (so 0.0 to 1.0 is from the slider center to the handle).
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_units_text_read_only`` (bool):  [Read-Write] Whether to set the units part of the text label read only.
- ``is_value_text_read_only`` (bool):  [Read-Write] Whether to set the value part of the text label read only.
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_value_changed`` (OnAudioRadialSliderValueChangedEvent):  [Read-Write] Called when the value is changed by slider or typing.
- ``output_range`` (Vector2D):  [Read-Write] Output range
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``show_label_only_on_hover`` (bool):  [Read-Write] If true, show text label only on hover; if false always show label.
- ``show_units_text`` (bool):  [Read-Write] Whether to show the units part of the text label.
- ``slider_bar_color`` (LinearColor):  [Read-Write] The color to draw the slider bar in.
- ``slider_progress_color`` (LinearColor):  [Read-Write] The color to draw the slider progress bar in.
- ``slider_thickness`` (float):  [Read-Write] The slider thickness.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``text_label_background_color`` (LinearColor):  [Read-Write] The color to draw the text label background.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``units_text`` (Text):  [Read-Write] The text label units
- ``value`` (float):  [Read-Write] The normalized linear (0 - 1) slider value position.
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``widget_layout`` (AudioRadialSliderLayout):  [Read-Write] The layout of the widget (position of text label).

<a id="unreal.AudioFrequencyRadialSlider"></a>