## ScrollBar Objects

```python
class ScrollBar(Widget)
```

Scroll Bar

**C++ Source:**

- **Module**: UMG
- **File**: ScrollBar.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``always_show_scrollbar`` (bool):  [Read-Write]
- ``always_show_scrollbar_track`` (bool):  [Read-Write]
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
- ``orientation`` (Orientation):  [Read-Write]
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``padding`` (Margin):  [Read-Write] The margin around the scrollbar
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``thickness`` (Vector2D):  [Read-Write] The thickness of the scrollbar thumb
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``widget_style`` (ScrollBarStyle):  [Read-Write] Style of the scrollbar

<a id="unreal.ScrollBar.widget_style"></a>

#### widget_style

```python
@property
def widget_style() -> ScrollBarStyle
```

(ScrollBarStyle):  [Read-Write] Style of the scrollbar

<a id="unreal.ScrollBar.widget_style"></a>

#### widget_style

```python
@widget_style.setter
def widget_style(value: ScrollBarStyle) -> None
```

<a id="unreal.ScrollBar.always_show_scrollbar"></a>

#### always_show_scrollbar

```python
@property
def always_show_scrollbar() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ScrollBar.always_show_scrollbar"></a>

#### always_show_scrollbar

```python
@always_show_scrollbar.setter
def always_show_scrollbar(value: bool) -> None
```

<a id="unreal.ScrollBar.always_show_scrollbar_track"></a>

#### always_show_scrollbar_track

```python
@property
def always_show_scrollbar_track() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ScrollBar.always_show_scrollbar_track"></a>

#### always_show_scrollbar_track

```python
@always_show_scrollbar_track.setter
def always_show_scrollbar_track(value: bool) -> None
```

<a id="unreal.ScrollBar.orientation"></a>

#### orientation

```python
@property
def orientation() -> Orientation
```

(Orientation):  [Read-Only]

<a id="unreal.ScrollBar.thickness"></a>

#### thickness

```python
@property
def thickness() -> Vector2D
```

(Vector2D):  [Read-Write] The thickness of the scrollbar thumb

<a id="unreal.ScrollBar.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: Vector2D) -> None
```

<a id="unreal.ScrollBar.padding"></a>

#### padding

```python
@property
def padding() -> Margin
```

(Margin):  [Read-Write] The margin around the scrollbar

<a id="unreal.ScrollBar.padding"></a>

#### padding

```python
@padding.setter
def padding(value: Margin) -> None
```

<a id="unreal.ScrollBar.set_state"></a>

#### set_state

```python
def set_state(offset_fraction: float, thumb_size_fraction: float) -> None
```

x.set_state(offset_fraction, thumb_size_fraction) -> None
Set the offset and size of the track's thumb.
Note that the maximum offset is 1.0-ThumbSizeFraction.
If the user can view 1/3 of the items in a single page, the maximum offset will be ~0.667f

Args:
    offset_fraction (float): Offset of the thumbnail from the top as a fraction of the total available scroll space.
    thumb_size_fraction (float): Size of thumbnail as a fraction of the total available scroll space.

<a id="unreal.ScrollBox"></a>