## SizeBox Objects

```python
class SizeBox(ContentWidget)
```

A widget that allows you to specify the size it reports to have and desire.  Not all widgets report a desired size
that you actually desire.  Wrapping them in a SizeBox lets you have the Size Box force them to be a particular size.

* Single Child
* Fixed Size

**C++ Source:**

- **Module**: UMG
- **File**: SizeBox.h

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
- ``height_override`` (float):  [Read-Write] When specified, ignore the content's desired size and report the HeightOverride as the Box's desired height.
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``max_aspect_ratio`` (float):  [Read-Write]
- ``max_desired_height`` (float):  [Read-Write] When specified, will report the MaxDesiredHeight if smaller than the content's desired height.
- ``max_desired_width`` (float):  [Read-Write] When specified, will report the MaxDesiredWidth if smaller than the content's desired width.
- ``min_aspect_ratio`` (float):  [Read-Write]
- ``min_desired_height`` (float):  [Read-Write] When specified, will report the MinDesiredHeight if larger than the content's desired height.
- ``min_desired_width`` (float):  [Read-Write] When specified, will report the MinDesiredWidth if larger than the content's desired width.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``override_height_override`` (bool):  [Read-Write]
- ``override_max_aspect_ratio`` (bool):  [Read-Write]
- ``override_max_desired_height`` (bool):  [Read-Write]
- ``override_max_desired_width`` (bool):  [Read-Write]
- ``override_min_aspect_ratio`` (bool):  [Read-Write]
- ``override_min_desired_height`` (bool):  [Read-Write]
- ``override_min_desired_width`` (bool):  [Read-Write]
- ``override_width_override`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``width_override`` (float):  [Read-Write] When specified, ignore the content's desired size and report the WidthOverride as the Box's desired width.

<a id="unreal.SizeBox.width_override"></a>

#### width_override

```python
@property
def width_override() -> float
```

(float):  [Read-Write] When specified, ignore the content's desired size and report the WidthOverride as the Box's desired width.

<a id="unreal.SizeBox.width_override"></a>

#### width_override

```python
@width_override.setter
def width_override(value: float) -> None
```

<a id="unreal.SizeBox.height_override"></a>

#### height_override

```python
@property
def height_override() -> float
```

(float):  [Read-Write] When specified, ignore the content's desired size and report the HeightOverride as the Box's desired height.

<a id="unreal.SizeBox.height_override"></a>

#### height_override

```python
@height_override.setter
def height_override(value: float) -> None
```

<a id="unreal.SizeBox.min_desired_width"></a>

#### min_desired_width

```python
@property
def min_desired_width() -> float
```

(float):  [Read-Write] When specified, will report the MinDesiredWidth if larger than the content's desired width.

<a id="unreal.SizeBox.min_desired_width"></a>

#### min_desired_width

```python
@min_desired_width.setter
def min_desired_width(value: float) -> None
```

<a id="unreal.SizeBox.min_desired_height"></a>

#### min_desired_height

```python
@property
def min_desired_height() -> float
```

(float):  [Read-Write] When specified, will report the MinDesiredHeight if larger than the content's desired height.

<a id="unreal.SizeBox.min_desired_height"></a>

#### min_desired_height

```python
@min_desired_height.setter
def min_desired_height(value: float) -> None
```

<a id="unreal.SizeBox.max_desired_width"></a>

#### max_desired_width

```python
@property
def max_desired_width() -> float
```

(float):  [Read-Write] When specified, will report the MaxDesiredWidth if smaller than the content's desired width.

<a id="unreal.SizeBox.max_desired_width"></a>

#### max_desired_width

```python
@max_desired_width.setter
def max_desired_width(value: float) -> None
```

<a id="unreal.SizeBox.max_desired_height"></a>

#### max_desired_height

```python
@property
def max_desired_height() -> float
```

(float):  [Read-Write] When specified, will report the MaxDesiredHeight if smaller than the content's desired height.

<a id="unreal.SizeBox.max_desired_height"></a>

#### max_desired_height

```python
@max_desired_height.setter
def max_desired_height(value: float) -> None
```

<a id="unreal.SizeBox.min_aspect_ratio"></a>

#### min_aspect_ratio

```python
@property
def min_aspect_ratio() -> float
```

(float):  [Read-Write]

<a id="unreal.SizeBox.min_aspect_ratio"></a>

#### min_aspect_ratio

```python
@min_aspect_ratio.setter
def min_aspect_ratio(value: float) -> None
```

<a id="unreal.SizeBox.max_aspect_ratio"></a>

#### max_aspect_ratio

```python
@property
def max_aspect_ratio() -> float
```

(float):  [Read-Write]

<a id="unreal.SizeBox.max_aspect_ratio"></a>

#### max_aspect_ratio

```python
@max_aspect_ratio.setter
def max_aspect_ratio(value: float) -> None
```

<a id="unreal.SizeBox.set_width_override"></a>

#### set_width_override

```python
def set_width_override(width_override: float) -> None
```

x.set_width_override(width_override) -> None
When specified, ignore the content's desired size and report the WidthOverride as the Box's desired width.

Args:
    width_override (float):

<a id="unreal.SizeBox.set_min_desired_width"></a>

#### set_min_desired_width

```python
def set_min_desired_width(min_desired_width: float) -> None
```

x.set_min_desired_width(min_desired_width) -> None
When specified, will report the MinDesiredWidth if larger than the content's desired width.

Args:
    min_desired_width (float):

<a id="unreal.SizeBox.set_min_desired_height"></a>

#### set_min_desired_height

```python
def set_min_desired_height(min_desired_height: float) -> None
```

x.set_min_desired_height(min_desired_height) -> None
When specified, will report the MinDesiredHeight if larger than the content's desired height.

Args:
    min_desired_height (float):

<a id="unreal.SizeBox.set_min_aspect_ratio"></a>

#### set_min_aspect_ratio

```python
def set_min_aspect_ratio(min_aspect_ratio: float) -> None
```

x.set_min_aspect_ratio(min_aspect_ratio) -> None
Set Min Aspect Ratio

Args:
    min_aspect_ratio (float):

<a id="unreal.SizeBox.set_max_desired_width"></a>

#### set_max_desired_width

```python
def set_max_desired_width(max_desired_width: float) -> None
```

x.set_max_desired_width(max_desired_width) -> None
When specified, will report the MaxDesiredWidth if smaller than the content's desired width.

Args:
    max_desired_width (float):

<a id="unreal.SizeBox.set_max_desired_height"></a>

#### set_max_desired_height

```python
def set_max_desired_height(max_desired_height: float) -> None
```

x.set_max_desired_height(max_desired_height) -> None
When specified, will report the MaxDesiredHeight if smaller than the content's desired height.

Args:
    max_desired_height (float):

<a id="unreal.SizeBox.set_max_aspect_ratio"></a>

#### set_max_aspect_ratio

```python
def set_max_aspect_ratio(max_aspect_ratio: float) -> None
```

x.set_max_aspect_ratio(max_aspect_ratio) -> None
Set Max Aspect Ratio

Args:
    max_aspect_ratio (float):

<a id="unreal.SizeBox.set_height_override"></a>

#### set_height_override

```python
def set_height_override(height_override: float) -> None
```

x.set_height_override(height_override) -> None
When specified, ignore the content's desired size and report the HeightOverride as the Box's desired height.

Args:
    height_override (float):

<a id="unreal.SizeBox.clear_width_override"></a>

#### clear_width_override

```python
def clear_width_override() -> None
```

x.clear_width_override() -> None
Clear Width Override

<a id="unreal.SizeBox.clear_min_desired_width"></a>

#### clear_min_desired_width

```python
def clear_min_desired_width() -> None
```

x.clear_min_desired_width() -> None
Clear Min Desired Width

<a id="unreal.SizeBox.clear_min_desired_height"></a>

#### clear_min_desired_height

```python
def clear_min_desired_height() -> None
```

x.clear_min_desired_height() -> None
Clear Min Desired Height

<a id="unreal.SizeBox.clear_min_aspect_ratio"></a>

#### clear_min_aspect_ratio

```python
def clear_min_aspect_ratio() -> None
```

x.clear_min_aspect_ratio() -> None
Clear Min Aspect Ratio

<a id="unreal.SizeBox.clear_max_desired_width"></a>

#### clear_max_desired_width

```python
def clear_max_desired_width() -> None
```

x.clear_max_desired_width() -> None
Clear Max Desired Width

<a id="unreal.SizeBox.clear_max_desired_height"></a>

#### clear_max_desired_height

```python
def clear_max_desired_height() -> None
```

x.clear_max_desired_height() -> None
Clear Max Desired Height

<a id="unreal.SizeBox.clear_max_aspect_ratio"></a>

#### clear_max_aspect_ratio

```python
def clear_max_aspect_ratio() -> None
```

x.clear_max_aspect_ratio() -> None
Clear Max Aspect Ratio

<a id="unreal.SizeBox.clear_height_override"></a>

#### clear_height_override

```python
def clear_height_override() -> None
```

x.clear_height_override() -> None
Clear Height Override

<a id="unreal.SizeBoxSlot"></a>