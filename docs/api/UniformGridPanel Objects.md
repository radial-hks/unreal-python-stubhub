## UniformGridPanel Objects

```python
class UniformGridPanel(PanelWidget)
```

A panel that evenly divides up available space between all of its children.

**C++ Source:**

- **Module**: UMG
- **File**: UniformGridPanel.h

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
- ``min_desired_slot_height`` (float):  [Read-Write] The minimum desired height of the slots
- ``min_desired_slot_width`` (float):  [Read-Write] The minimum desired width of the slots
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
- ``slot_padding`` (Margin):  [Read-Write] Padding given to each slot
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.UniformGridPanel.slot_padding"></a>

#### slot_padding

```python
@property
def slot_padding() -> Margin
```

(Margin):  [Read-Write] Padding given to each slot

<a id="unreal.UniformGridPanel.slot_padding"></a>

#### slot_padding

```python
@slot_padding.setter
def slot_padding(value: Margin) -> None
```

<a id="unreal.UniformGridPanel.min_desired_slot_width"></a>

#### min_desired_slot_width

```python
@property
def min_desired_slot_width() -> float
```

(float):  [Read-Write] The minimum desired width of the slots

<a id="unreal.UniformGridPanel.min_desired_slot_width"></a>

#### min_desired_slot_width

```python
@min_desired_slot_width.setter
def min_desired_slot_width(value: float) -> None
```

<a id="unreal.UniformGridPanel.min_desired_slot_height"></a>

#### min_desired_slot_height

```python
@property
def min_desired_slot_height() -> float
```

(float):  [Read-Write] The minimum desired height of the slots

<a id="unreal.UniformGridPanel.min_desired_slot_height"></a>

#### min_desired_slot_height

```python
@min_desired_slot_height.setter
def min_desired_slot_height(value: float) -> None
```

<a id="unreal.UniformGridPanel.set_slot_padding"></a>

#### set_slot_padding

```python
def set_slot_padding(slot_padding: Margin) -> None
```

x.set_slot_padding(slot_padding) -> None
Set Slot Padding

Args:
    slot_padding (Margin):

<a id="unreal.UniformGridPanel.set_min_desired_slot_width"></a>

#### set_min_desired_slot_width

```python
def set_min_desired_slot_width(min_desired_slot_width: float) -> None
```

x.set_min_desired_slot_width(min_desired_slot_width) -> None
Set Min Desired Slot Width

Args:
    min_desired_slot_width (float):

<a id="unreal.UniformGridPanel.set_min_desired_slot_height"></a>

#### set_min_desired_slot_height

```python
def set_min_desired_slot_height(min_desired_slot_height: float) -> None
```

x.set_min_desired_slot_height(min_desired_slot_height) -> None
Set Min Desired Slot Height

Args:
    min_desired_slot_height (float):

<a id="unreal.UniformGridPanel.add_child_to_uniform_grid"></a>

#### add_child_to_uniform_grid

```python
def add_child_to_uniform_grid(content: Widget,
                              row: int = 0,
                              column: int = 0) -> UniformGridSlot
```

x.add_child_to_uniform_grid(content, row=0, column=0) -> UniformGridSlot
Add Child to Uniform Grid

Args:
    content (Widget): 
    row (int32): 
    column (int32): 

Returns:
    UniformGridSlot:

<a id="unreal.UniformGridSlot"></a>