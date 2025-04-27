## ExpandableArea Objects

```python
class ExpandableArea(Widget)
```

Expandable Area

**C++ Source:**

- **Module**: UMG
- **File**: ExpandableArea.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``area_padding`` (Margin):  [Read-Write]
- ``border_brush`` (SlateBrush):  [Read-Write]
- ``border_color`` (SlateColor):  [Read-Write]
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``header_padding`` (Margin):  [Read-Write]
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_expanded`` (bool):  [Read-Write]
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``max_height`` (float):  [Read-Write] The maximum height of the area
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_expansion_changed`` (OnExpandableAreaExpansionChanged):  [Read-Write] A bindable delegate for the IsChecked.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``style`` (ExpandableAreaStyle):  [Read-Write]
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.ExpandableArea.border_brush"></a>

#### border_brush

```python
@property
def border_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write]

<a id="unreal.ExpandableArea.border_brush"></a>

#### border_brush

```python
@border_brush.setter
def border_brush(value: SlateBrush) -> None
```

<a id="unreal.ExpandableArea.border_color"></a>

#### border_color

```python
@property
def border_color() -> SlateColor
```

(SlateColor):  [Read-Write]

<a id="unreal.ExpandableArea.border_color"></a>

#### border_color

```python
@border_color.setter
def border_color(value: SlateColor) -> None
```

<a id="unreal.ExpandableArea.is_expanded"></a>

#### is_expanded

```python
@property
def is_expanded() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ExpandableArea.is_expanded"></a>

#### is_expanded

```python
@is_expanded.setter
def is_expanded(value: bool) -> None
```

<a id="unreal.ExpandableArea.max_height"></a>

#### max_height

```python
@property
def max_height() -> float
```

(float):  [Read-Write] The maximum height of the area

<a id="unreal.ExpandableArea.max_height"></a>

#### max_height

```python
@max_height.setter
def max_height(value: float) -> None
```

<a id="unreal.ExpandableArea.header_padding"></a>

#### header_padding

```python
@property
def header_padding() -> Margin
```

(Margin):  [Read-Write]

<a id="unreal.ExpandableArea.header_padding"></a>

#### header_padding

```python
@header_padding.setter
def header_padding(value: Margin) -> None
```

<a id="unreal.ExpandableArea.area_padding"></a>

#### area_padding

```python
@property
def area_padding() -> Margin
```

(Margin):  [Read-Write]

<a id="unreal.ExpandableArea.area_padding"></a>

#### area_padding

```python
@area_padding.setter
def area_padding(value: Margin) -> None
```

<a id="unreal.ExpandableArea.on_expansion_changed"></a>

#### on_expansion_changed

```python
@property
def on_expansion_changed() -> OnExpandableAreaExpansionChanged
```

(OnExpandableAreaExpansionChanged):  [Read-Write] A bindable delegate for the IsChecked.

<a id="unreal.ExpandableArea.on_expansion_changed"></a>

#### on_expansion_changed

```python
@on_expansion_changed.setter
def on_expansion_changed(value: OnExpandableAreaExpansionChanged) -> None
```

<a id="unreal.ExpandableArea.set_is_expanded_animated"></a>

#### set_is_expanded_animated

```python
def set_is_expanded_animated(is_expanded: bool) -> None
```

x.set_is_expanded_animated(is_expanded) -> None
Set Is Expanded Animated

Args:
    is_expanded (bool):

<a id="unreal.ExpandableArea.set_is_expanded"></a>

#### set_is_expanded

```python
def set_is_expanded(is_expanded: bool) -> None
```

x.set_is_expanded(is_expanded) -> None
Set Is Expanded

Args:
    is_expanded (bool):

<a id="unreal.ExpandableArea.get_is_expanded"></a>

#### get_is_expanded

```python
def get_is_expanded() -> bool
```

x.get_is_expanded() -> bool
Get Is Expanded

Returns:
    bool:

<a id="unreal.GridPanel"></a>