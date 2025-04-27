## EditorUtilityMultiLineEditableText Objects

```python
class EditorUtilityMultiLineEditableText(MultiLineEditableText)
```

Editor Utility Multi Line Editable Text

**C++ Source:**

- **Module**: Blutility
- **File**: EditorUtilityWidgetComponents.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``allow_context_menu`` (bool):  [Read-Write] Whether the context menu can be opened
- ``apply_line_height_to_bottom_line`` (bool):  [Read-Write] Whether to leave extra space below the last line due to line height.
- ``auto_wrap_text`` (bool):  [Read-Write] True if we're wrapping text automatically based on the computed horizontal space for this widget.
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clear_keyboard_focus_on_commit`` (bool):  [Read-Write] Whether to clear keyboard focus when pressing enter to commit changes
- ``clear_text_selection_on_focus_loss`` (bool):  [Read-Write] Whether to clear text selection when focus is lost
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``hint_text`` (Text):  [Read-Write] Hint text that appears when there is no text in the text box
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_read_only`` (bool):  [Read-Write] Sets the Text as Readonly to prevent it from being modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``justification`` (TextJustify):  [Read-Write] How the text should be aligned with the margin.
- ``line_height_percentage`` (float):  [Read-Write] The amount to scale each lines height by.
- ``margin`` (Margin):  [Read-Write] The amount of blank space left around the edges of text area.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_text_changed`` (OnMultiLineEditableTextChangedEvent):  [Read-Write] Called whenever the text is changed programmatically or interactively by the user
- ``on_text_committed`` (OnMultiLineEditableTextCommittedEvent):  [Read-Write] Called whenever the text is committed.  This happens when the user presses enter or the text box loses focus.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``revert_text_on_escape`` (bool):  [Read-Write] Whether to allow the user to back out of changes when they press the escape key
- ``select_all_text_when_focused`` (bool):  [Read-Write] Whether to select all text when the user clicks to give focus on the widget
- ``shaped_text_options`` (ShapedTextOptions):  [Read-Write] Controls how the text within this widget should be shaped.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``text`` (Text):  [Read-Write] The text content for this editable text box widget
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``virtual_keyboard_dismiss_action`` (VirtualKeyboardDismissAction):  [Read-Write] What action should be taken when the virtual keyboard is dismissed?
- ``virtual_keyboard_options`` (VirtualKeyboardOptions):  [Read-Write] Additional options for the virtual keyboard
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``widget_style`` (TextBlockStyle):  [Read-Write] The style
- ``wrap_text_at`` (float):  [Read-Write] Whether text wraps onto a new line when it's length exceeds this width; if this value is zero or negative, no wrapping occurs.
- ``wrapping_policy`` (TextWrappingPolicy):  [Read-Write] The wrapping policy to use.

<a id="unreal.EditorUtilityMultiLineEditableTextBox"></a>