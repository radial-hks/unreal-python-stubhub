## WidgetSwitcher Objects

```python
class WidgetSwitcher(PanelWidget)
```

A widget switcher is like a tab control, but without tabs. At most one widget is visible at time.

**C++ Source:**

- **Module**: UMG
- **File**: WidgetSwitcher.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``active_widget_index`` (int32):  [Read-Write] The slot index to display
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
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.WidgetSwitcher.active_widget_index"></a>

#### active_widget_index

```python
@property
def active_widget_index() -> int
```

(int32):  [Read-Write] The slot index to display

<a id="unreal.WidgetSwitcher.active_widget_index"></a>

#### active_widget_index

```python
@active_widget_index.setter
def active_widget_index(value: int) -> None
```

<a id="unreal.WidgetSwitcher.set_active_widget_index"></a>

#### set_active_widget_index

```python
def set_active_widget_index(index: int) -> None
```

x.set_active_widget_index(index) -> None
Activates the widget at the specified index.

Args:
    index (int32):

<a id="unreal.WidgetSwitcher.set_active_widget"></a>

#### set_active_widget

```python
def set_active_widget(widget: Widget) -> None
```

x.set_active_widget(widget) -> None
Activates the widget and makes it the active index.

Args:
    widget (Widget):

<a id="unreal.WidgetSwitcher.get_widget_at_index"></a>

#### get_widget_at_index

```python
def get_widget_at_index(index: int) -> Widget
```

x.get_widget_at_index(index) -> Widget
Get a widget at the provided index

Args:
    index (int32): 

Returns:
    Widget:

<a id="unreal.WidgetSwitcher.get_num_widgets"></a>

#### get_num_widgets

```python
def get_num_widgets() -> int
```

x.get_num_widgets() -> int32
Gets the number of widgets that this switcher manages.

Returns:
    int32:

<a id="unreal.WidgetSwitcher.get_active_widget_index"></a>

#### get_active_widget_index

```python
def get_active_widget_index() -> int
```

x.get_active_widget_index() -> int32
Gets the slot index of the currently active widget

Returns:
    int32:

<a id="unreal.WidgetSwitcher.get_active_widget"></a>

#### get_active_widget

```python
def get_active_widget() -> Widget
```

x.get_active_widget() -> Widget
Get the reference of the currently active widget

Returns:
    Widget:

<a id="unreal.WidgetSwitcherSlot"></a>