## EditorUtilityComboBoxString Objects

```python
class EditorUtilityComboBoxString(ComboBoxString)
```

Editor Utility Combo Box String

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
- ``content_padding`` (Margin):  [Read-Write]
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``default_options`` (Array[str]):  [Read-Write] The default list of items to be displayed on the combobox.
- ``enable_gamepad_navigation_mode`` (bool):  [Read-Write] When false, directional keys will change the selection. When true, ComboBox
  must be activated and will only capture arrow input while activated.
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``font`` (SlateFontInfo):  [Read-Write] The default font to use in the combobox, only applies if you're not implementing OnGenerateWidgetEvent
  to factory each new entry.
- ``foreground_color`` (SlateColor):  [Read-Write] The foreground color to pass through the hierarchy.
- ``has_down_arrow`` (bool):  [Read-Write] When false, the down arrow is not generated and it is up to the API consumer
  to make their own visual hint that this is a drop down.
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_focusable`` (bool):  [Read-Write]
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``item_style`` (TableRowStyle):  [Read-Write] The item row style.
- ``max_list_height`` (float):  [Read-Write] The max height of the combobox list that opens
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_generate_widget_event`` (GenerateWidgetForString):  [Read-Write] Called when the widget is needed for the item.
- ``on_opening`` (OnOpeningEvent):  [Read-Write] Called when the combobox is opening
- ``on_selection_changed`` (OnSelectionChangedEvent):  [Read-Write] Called when a new item is selected in the combobox.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``scroll_bar_style`` (ScrollBarStyle):  [Read-Write] The scroll bar style.
- ``selected_option`` (str):  [Read-Write] The item in the combobox to select by default
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``widget_style`` (ComboBoxStyle):  [Read-Write] The style.

<a id="unreal.EditorUtilityEditableText"></a>