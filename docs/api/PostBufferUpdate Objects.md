## PostBufferUpdate Objects

```python
class PostBufferUpdate(Widget)
```

Widget that when drawn, will trigger the slate post buffer to update. Does not draw anything itself.
This allows for you to perform layered UI / sampling effects with the GetSlatePost material functions,
by placing this widget after UI you would like to be processed / sampled is drawn.

* No Children

**C++ Source:**

- **Module**: UMG
- **File**: PostBufferUpdate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``buffers_to_update`` (Array[SlatePostRT]):  [Read-Write] Buffers that we should update, all of these buffers will be affected by 'bPerformDefaultPostBufferUpdate' if disabled
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
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
- ``perform_default_post_buffer_update`` (bool):  [Read-Write] True if we should do the default post buffer update of the scene before any UI.
  If any PostBufferUpdate widget has this set as false, be default scene copy / processing will not occur.
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``update_buffer_infos`` (Array[SlatePostBufferUpdateInfo]):  [Read-Write] Buffer to update when this widget is drawn, along with info needed to update that buffer if desired intra-frame
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.PostBufferUpdate.perform_default_post_buffer_update"></a>

#### perform_default_post_buffer_update

```python
@property
def perform_default_post_buffer_update() -> bool
```

(bool):  [Read-Write] True if we should do the default post buffer update of the scene before any UI.
If any PostBufferUpdate widget has this set as false, be default scene copy / processing will not occur.

<a id="unreal.PostBufferUpdate.perform_default_post_buffer_update"></a>

#### perform_default_post_buffer_update

```python
@perform_default_post_buffer_update.setter
def perform_default_post_buffer_update(value: bool) -> None
```

<a id="unreal.ProgressBar"></a>