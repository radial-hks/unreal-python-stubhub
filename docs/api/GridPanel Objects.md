## GridPanel Objects

```python
class GridPanel(PanelWidget)
```

A table-like panel that retains the width of every column throughout the table.

* Many Children

**C++ Source:**

- **Module**: UMG
- **File**: GridPanel.h

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
- ``column_fill`` (Array[float]):  [Read-Write] The column fill rules
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
- ``row_fill`` (Array[float]):  [Read-Write] The row fill rules
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.GridPanel.column_fill"></a>

#### column_fill

```python
@property
def column_fill() -> Array[float]
```

(Array[float]):  [Read-Only] The column fill rules

<a id="unreal.GridPanel.row_fill"></a>

#### row_fill

```python
@property
def row_fill() -> Array[float]
```

(Array[float]):  [Read-Only] The row fill rules

<a id="unreal.GridPanel.set_row_fill"></a>

#### set_row_fill

```python
def set_row_fill(row_index: int, coefficient: float) -> None
```

x.set_row_fill(row_index, coefficient) -> None
Set Row Fill

Args:
    row_index (int32): 
    coefficient (float):

<a id="unreal.GridPanel.set_column_fill"></a>

#### set_column_fill

```python
def set_column_fill(column_index: int, coefficient: float) -> None
```

x.set_column_fill(column_index, coefficient) -> None
Set Column Fill

Args:
    column_index (int32): 
    coefficient (float):

<a id="unreal.GridPanel.add_child_to_grid"></a>

#### add_child_to_grid

```python
def add_child_to_grid(content: Widget,
                      row: int = 0,
                      column: int = 0) -> GridSlot
```

x.add_child_to_grid(content, row=0, column=0) -> GridSlot
Add Child to Grid

Args:
    content (Widget): 
    row (int32): 
    column (int32): 

Returns:
    GridSlot:

<a id="unreal.GridSlot"></a>