## PanelWidget Objects

```python
class PanelWidget(Widget)
```

The base class for all UMG panel widgets.  Panel widgets layout a collection of child widgets.

**C++ Source:**

- **Module**: UMG
- **File**: PanelWidget.h

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

<a id="unreal.PanelWidget.remove_child_at"></a>

#### remove_child_at

```python
def remove_child_at(index: int) -> bool
```

x.remove_child_at(index) -> bool
Removes a child by it's index.

Args:
    index (int32): 

Returns:
    bool:

<a id="unreal.PanelWidget.remove_child"></a>

#### remove_child

```python
def remove_child(content: Widget) -> bool
```

x.remove_child(content) -> bool
Removes a specific widget from the container.

Args:
    content (Widget): 

Returns:
    bool: true if the widget was found and removed.

<a id="unreal.PanelWidget.has_child"></a>

#### has_child

```python
def has_child(content: Widget) -> bool
```

x.has_child(content) -> bool
Returns true if panel contains this widget

Args:
    content (Widget): 

Returns:
    bool:

<a id="unreal.PanelWidget.has_any_children"></a>

#### has_any_children

```python
def has_any_children() -> bool
```

x.has_any_children() -> bool
Returns true if there are any child widgets in the panel

Returns:
    bool:

<a id="unreal.PanelWidget.get_children_count"></a>

#### get_children_count

```python
def get_children_count() -> int
```

x.get_children_count() -> int32
Gets number of child widgets in the container.

Returns:
    int32:

<a id="unreal.PanelWidget.get_child_index"></a>

#### get_child_index

```python
def get_child_index(content: Widget) -> int
```

x.get_child_index(content) -> int32
Gets the index of a specific child widget

Args:
    content (Widget): 

Returns:
    int32:

<a id="unreal.PanelWidget.get_child_at"></a>

#### get_child_at

```python
def get_child_at(index: int) -> Widget
```

x.get_child_at(index) -> Widget
Gets the widget at an index.

Args:
    index (int32): The index of the widget.

Returns:
    Widget: The widget at the given index, or nothing if there is no widget there.

<a id="unreal.PanelWidget.get_all_children"></a>

#### get_all_children

```python
def get_all_children() -> Array[Widget]
```

x.get_all_children() -> Array[Widget]
Gets all widgets in the container

Returns:
    Array[Widget]:

<a id="unreal.PanelWidget.clear_children"></a>

#### clear_children

```python
def clear_children() -> None
```

x.clear_children() -> None
Remove all child widgets from the panel widget.

<a id="unreal.PanelWidget.add_child"></a>

#### add_child

```python
def add_child(content: Widget) -> PanelSlot
```

x.add_child(content) -> PanelSlot
Adds a new child widget to the container.  Returns the base slot type,
requires casting to turn it into the type specific to the container.

Args:
    content (Widget): 

Returns:
    PanelSlot:

<a id="unreal.ContentWidget"></a>