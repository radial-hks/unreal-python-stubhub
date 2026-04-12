## EarthDragBorderWidget Objects

```python
class EarthDragBorderWidget(ContentWidget)
```

Earth Drag Border Widget

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesEditorUI
- **File**: EarthDragBorder.h

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
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_drag_enter_event`` (OnDragEnterEvent):  [Read-Write]
- ``on_drag_leave_event`` (OnDragLeaveEvent):  [Read-Write]
- ``on_drag_over_event`` (OnDragOverEvent):  [Read-Write]
- ``on_drop_handle`` (OnDropEvent):  [Read-Write]
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

<a id="unreal.EarthDragBorderWidget.on_drag_enter_event"></a>

#### on\_drag\_enter\_event

```python
@property
def on_drag_enter_event() -> OnDragEnterEvent
```

(OnDragEnterEvent):  [Read-Write]

<a id="unreal.EarthDragBorderWidget.on_drag_enter_event"></a>

#### on\_drag\_enter\_event

```python
@on_drag_enter_event.setter
def on_drag_enter_event(value: OnDragEnterEvent) -> None
```

<a id="unreal.EarthDragBorderWidget.on_drag_leave_event"></a>

#### on\_drag\_leave\_event

```python
@property
def on_drag_leave_event() -> OnDragLeaveEvent
```

(OnDragLeaveEvent):  [Read-Write]

<a id="unreal.EarthDragBorderWidget.on_drag_leave_event"></a>

#### on\_drag\_leave\_event

```python
@on_drag_leave_event.setter
def on_drag_leave_event(value: OnDragLeaveEvent) -> None
```

<a id="unreal.EarthDragBorderWidget.on_drag_over_event"></a>

#### on\_drag\_over\_event

```python
@property
def on_drag_over_event() -> OnDragOverEvent
```

(OnDragOverEvent):  [Read-Write]

<a id="unreal.EarthDragBorderWidget.on_drag_over_event"></a>

#### on\_drag\_over\_event

```python
@on_drag_over_event.setter
def on_drag_over_event(value: OnDragOverEvent) -> None
```

<a id="unreal.EarthDragBorderWidget.on_drop_handle"></a>

#### on\_drop\_handle

```python
@property
def on_drop_handle() -> OnDropEvent
```

(OnDropEvent):  [Read-Write]

<a id="unreal.EarthDragBorderWidget.on_drop_handle"></a>

#### on\_drop\_handle

```python
@on_drop_handle.setter
def on_drop_handle(value: OnDropEvent) -> None
```

<a id="unreal.EarthTabContentWidget"></a>