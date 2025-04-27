## ProgressBar Objects

```python
class ProgressBar(Widget)
```

The progress bar widget is a simple bar that fills up that can be restyled to fit any number of uses.

* No Children

**C++ Source:**

- **Module**: UMG
- **File**: ProgressBar.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``bar_fill_style`` (ProgressBarFillStyle):  [Read-Write] Defines the visual style of the progress bar fill - scale or mask
- ``bar_fill_type`` (ProgressBarFillType):  [Read-Write] Defines the direction in which the progress bar fills
- ``border_padding`` (Vector2D):  [Read-Write]
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``fill_color_and_opacity`` (LinearColor):  [Read-Write] Fill Color and Opacity
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_marquee`` (bool):  [Read-Write]
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``percent`` (float):  [Read-Write] Used to determine the fill position of the progress bar ranging 0..1
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``widget_style`` (ProgressBarStyle):  [Read-Write] The progress bar style

<a id="unreal.ProgressBar.widget_style"></a>

#### widget_style

```python
@property
def widget_style() -> ProgressBarStyle
```

(ProgressBarStyle):  [Read-Write] The progress bar style

<a id="unreal.ProgressBar.widget_style"></a>

#### widget_style

```python
@widget_style.setter
def widget_style(value: ProgressBarStyle) -> None
```

<a id="unreal.ProgressBar.percent"></a>

#### percent

```python
@property
def percent() -> float
```

(float):  [Read-Write] Used to determine the fill position of the progress bar ranging 0..1

<a id="unreal.ProgressBar.percent"></a>

#### percent

```python
@percent.setter
def percent(value: float) -> None
```

<a id="unreal.ProgressBar.bar_fill_type"></a>

#### bar_fill_type

```python
@property
def bar_fill_type() -> ProgressBarFillType
```

(ProgressBarFillType):  [Read-Write] Defines the direction in which the progress bar fills

<a id="unreal.ProgressBar.bar_fill_type"></a>

#### bar_fill_type

```python
@bar_fill_type.setter
def bar_fill_type(value: ProgressBarFillType) -> None
```

<a id="unreal.ProgressBar.bar_fill_style"></a>

#### bar_fill_style

```python
@property
def bar_fill_style() -> ProgressBarFillStyle
```

(ProgressBarFillStyle):  [Read-Write] Defines the visual style of the progress bar fill - scale or mask

<a id="unreal.ProgressBar.bar_fill_style"></a>

#### bar_fill_style

```python
@bar_fill_style.setter
def bar_fill_style(value: ProgressBarFillStyle) -> None
```

<a id="unreal.ProgressBar.is_marquee"></a>

#### is_marquee

```python
@property
def is_marquee() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ProgressBar.is_marquee"></a>

#### is_marquee

```python
@is_marquee.setter
def is_marquee(value: bool) -> None
```

<a id="unreal.ProgressBar.border_padding"></a>

#### border_padding

```python
@property
def border_padding() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.ProgressBar.border_padding"></a>

#### border_padding

```python
@border_padding.setter
def border_padding(value: Vector2D) -> None
```

<a id="unreal.ProgressBar.fill_color_and_opacity"></a>

#### fill_color_and_opacity

```python
@property
def fill_color_and_opacity() -> LinearColor
```

(LinearColor):  [Read-Write] Fill Color and Opacity

<a id="unreal.ProgressBar.fill_color_and_opacity"></a>

#### fill_color_and_opacity

```python
@fill_color_and_opacity.setter
def fill_color_and_opacity(value: LinearColor) -> None
```

<a id="unreal.ProgressBar.set_percent"></a>

#### set_percent

```python
def set_percent(percent: float) -> None
```

x.set_percent(percent) -> None
Sets the current value of the ProgressBar.

Args:
    percent (float):

<a id="unreal.ProgressBar.set_is_marquee"></a>

#### set_is_marquee

```python
def set_is_marquee(inb_is_marquee: bool) -> None
```

x.set_is_marquee(inb_is_marquee) -> None
Sets the progress bar to show as a marquee.

Args:
    inb_is_marquee (bool):

<a id="unreal.ProgressBar.set_fill_color_and_opacity"></a>

#### set_fill_color_and_opacity

```python
def set_fill_color_and_opacity(color: LinearColor) -> None
```

x.set_fill_color_and_opacity(color) -> None
Sets the fill color of the progress bar.

Args:
    color (LinearColor):

<a id="unreal.RetainerBox"></a>