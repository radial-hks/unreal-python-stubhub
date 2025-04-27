## DetailsView Objects

```python
class DetailsView(PropertyViewBase)
```

The details view allows you to display the value of an object properties.

**C++ Source:**

- **Module**: ScriptableEditorWidgets
- **File**: DetailsView.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``allow_favorite_system`` (bool):  [Read-Write] If false, the current properties editor will never display the favorite system
- ``allow_filtering`` (bool):  [Read-Write] True if we allow filtering through search and the filter dropdown menu.
- ``auto_load_asset`` (bool):  [Read-Write] Load the object (if it's an asset) when the widget is created.
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``categories_to_show`` (Array[Name]):  [Read-Write] Which categories to show in the details panel. If both this and the Properties To Show lists are empty, all properties will show.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``column_width`` (float):  [Read-Write] The default column width
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``force_hidden_property_visibility`` (bool):  [Read-Write] If true, all properties will be visible, not just those with CPF_Edit
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_property_changed`` (OnPropertyValueChanged):  [Read-Write] Sets a delegate called when the property value changes
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``properties_to_show`` (Array[Name]):  [Read-Write] Which properties to show in the details panel. If both this and the Categories To Show lists are empty, all properties will show.
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``show_animated_properties_option`` (bool):  [Read-Write] True if you want to show the 'Show Only Animated Properties'. Only valid in conjunction with bAllowFiltering
- ``show_keyable_properties_option`` (bool):  [Read-Write] True if you want to show the 'Show Only Keyable Properties'. Only valid in conjunction with bAllowFiltering
- ``show_modified_properties_option`` (bool):  [Read-Write] True if you want to show the 'Show Only Modified Properties'. Only valid in conjunction with bAllowFiltering
- ``show_scroll_bar`` (bool):  [Read-Write] If false, the details panel's scrollbar will always be hidden. Useful when embedding details panels in widgets that either grow to accommodate them, or with scrollbars of their own.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``view_identifier`` (Name):  [Read-Write] Identifier for this details view; NAME_None if this view is anonymous
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.SinglePropertyView"></a>