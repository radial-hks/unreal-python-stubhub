## Border Objects

```python
class Border(ContentWidget)
```

A border is a container widget that can contain one child widget, providing an opportunity
to surround it with a background image and adjustable padding.

* Single Child
* Image

**C++ Source:**

- **Module**: UMG
- **File**: Border.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``background`` (SlateBrush):  [Read-Write] Brush to drag as the background
- ``brush_color`` (LinearColor):  [Read-Write] Color and opacity of the actual border image
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``content_color_and_opacity`` (LinearColor):  [Read-Write] Color and opacity multiplier of content in the border
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``desired_size_scale`` (Vector2D):  [Read-Write] Scales the computed desired size of this border and its contents. Useful
  for making things that slide open without having to hard-code their size.
  Note: if the parent widget is set up to ignore this widget's desired size,
  then changing this value will have no effect.
- ``flip_for_right_to_left_flow_direction`` (bool):  [Read-Write] Flips the background image if the localization's flow direction is RightToLeft
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``horizontal_alignment`` (HorizontalAlignment):  [Read-Write] The alignment of the content horizontally.
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_mouse_button_down_event`` (OnPointerEvent):  [Read-Write]
- ``on_mouse_button_up_event`` (OnPointerEvent):  [Read-Write]
- ``on_mouse_double_click_event`` (OnPointerEvent):  [Read-Write]
- ``on_mouse_move_event`` (OnPointerEvent):  [Read-Write]
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``padding`` (Margin):  [Read-Write] The padding area between the slot and the content it contains.
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``show_effect_when_disabled`` (bool):  [Read-Write] Whether or not to show the disabled effect when this border is disabled
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``vertical_alignment`` (VerticalAlignment):  [Read-Write] The alignment of the content vertically.
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.Border.horizontal_alignment"></a>

#### horizontal_alignment

```python
@property
def horizontal_alignment() -> HorizontalAlignment
```

(HorizontalAlignment):  [Read-Write] The alignment of the content horizontally.

<a id="unreal.Border.horizontal_alignment"></a>

#### horizontal_alignment

```python
@horizontal_alignment.setter
def horizontal_alignment(value: HorizontalAlignment) -> None
```

<a id="unreal.Border.vertical_alignment"></a>

#### vertical_alignment

```python
@property
def vertical_alignment() -> VerticalAlignment
```

(VerticalAlignment):  [Read-Write] The alignment of the content vertically.

<a id="unreal.Border.vertical_alignment"></a>

#### vertical_alignment

```python
@vertical_alignment.setter
def vertical_alignment(value: VerticalAlignment) -> None
```

<a id="unreal.Border.show_effect_when_disabled"></a>

#### show_effect_when_disabled

```python
@property
def show_effect_when_disabled() -> bool
```

(bool):  [Read-Write] Whether or not to show the disabled effect when this border is disabled

<a id="unreal.Border.show_effect_when_disabled"></a>

#### show_effect_when_disabled

```python
@show_effect_when_disabled.setter
def show_effect_when_disabled(value: bool) -> None
```

<a id="unreal.Border.content_color_and_opacity"></a>

#### content_color_and_opacity

```python
@property
def content_color_and_opacity() -> LinearColor
```

(LinearColor):  [Read-Write] Color and opacity multiplier of content in the border

<a id="unreal.Border.content_color_and_opacity"></a>

#### content_color_and_opacity

```python
@content_color_and_opacity.setter
def content_color_and_opacity(value: LinearColor) -> None
```

<a id="unreal.Border.padding"></a>

#### padding

```python
@property
def padding() -> Margin
```

(Margin):  [Read-Write] The padding area between the slot and the content it contains.

<a id="unreal.Border.padding"></a>

#### padding

```python
@padding.setter
def padding(value: Margin) -> None
```

<a id="unreal.Border.background"></a>

#### background

```python
@property
def background() -> SlateBrush
```

(SlateBrush):  [Read-Only] Brush to drag as the background

<a id="unreal.Border.brush_color"></a>

#### brush_color

```python
@property
def brush_color() -> LinearColor
```

(LinearColor):  [Read-Write] Color and opacity of the actual border image

<a id="unreal.Border.brush_color"></a>

#### brush_color

```python
@brush_color.setter
def brush_color(value: LinearColor) -> None
```

<a id="unreal.Border.desired_size_scale"></a>

#### desired_size_scale

```python
@property
def desired_size_scale() -> Vector2D
```

(Vector2D):  [Read-Write] Scales the computed desired size of this border and its contents. Useful
for making things that slide open without having to hard-code their size.
Note: if the parent widget is set up to ignore this widget's desired size,
then changing this value will have no effect.

<a id="unreal.Border.desired_size_scale"></a>

#### desired_size_scale

```python
@desired_size_scale.setter
def desired_size_scale(value: Vector2D) -> None
```

<a id="unreal.Border.set_vertical_alignment"></a>

#### set_vertical_alignment

```python
def set_vertical_alignment(vertical_alignment: VerticalAlignment) -> None
```

x.set_vertical_alignment(vertical_alignment) -> None
Set Vertical Alignment

Args:
    vertical_alignment (VerticalAlignment):

<a id="unreal.Border.set_show_effect_when_disabled"></a>

#### set_show_effect_when_disabled

```python
def set_show_effect_when_disabled(show_effect_when_disabled: bool) -> None
```

x.set_show_effect_when_disabled(show_effect_when_disabled) -> None
Set Show Effect when Disabled

Args:
    show_effect_when_disabled (bool):

<a id="unreal.Border.set_padding"></a>

#### set_padding

```python
def set_padding(padding: Margin) -> None
```

x.set_padding(padding) -> None
Set Padding

Args:
    padding (Margin):

<a id="unreal.Border.set_horizontal_alignment"></a>

#### set_horizontal_alignment

```python
def set_horizontal_alignment(
        horizontal_alignment: HorizontalAlignment) -> None
```

x.set_horizontal_alignment(horizontal_alignment) -> None
Set Horizontal Alignment

Args:
    horizontal_alignment (HorizontalAlignment):

<a id="unreal.Border.set_desired_size_scale"></a>

#### set_desired_size_scale

```python
def set_desired_size_scale(scale: Vector2D) -> None
```

x.set_desired_size_scale(scale) -> None
Sets the DesiredSizeScale of this border.

Args:
    scale (Vector2D): The X and Y multipliers for the desired size

<a id="unreal.Border.set_content_color_and_opacity"></a>

#### set_content_color_and_opacity

```python
def set_content_color_and_opacity(
        content_color_and_opacity: LinearColor) -> None
```

x.set_content_color_and_opacity(content_color_and_opacity) -> None
Set Content Color and Opacity

Args:
    content_color_and_opacity (LinearColor):

<a id="unreal.Border.set_brush_from_texture"></a>

#### set_brush_from_texture

```python
def set_brush_from_texture(texture: Texture2D) -> None
```

x.set_brush_from_texture(texture) -> None
Set Brush from Texture

Args:
    texture (Texture2D):

<a id="unreal.Border.set_brush_from_material"></a>

#### set_brush_from_material

```python
def set_brush_from_material(material: MaterialInterface) -> None
```

x.set_brush_from_material(material) -> None
Set Brush from Material

Args:
    material (MaterialInterface):

<a id="unreal.Border.set_brush_from_asset"></a>

#### set_brush_from_asset

```python
def set_brush_from_asset(asset: SlateBrushAsset) -> None
```

x.set_brush_from_asset(asset) -> None
Set Brush from Asset

Args:
    asset (SlateBrushAsset):

<a id="unreal.Border.set_brush_color"></a>

#### set_brush_color

```python
def set_brush_color(brush_color: LinearColor) -> None
```

x.set_brush_color(brush_color) -> None
Set Brush Color

Args:
    brush_color (LinearColor):

<a id="unreal.Border.set_brush"></a>

#### set_brush

```python
def set_brush(brush: SlateBrush) -> None
```

x.set_brush(brush) -> None
Set Brush

Args:
    brush (SlateBrush):

<a id="unreal.Border.get_dynamic_material"></a>

#### get_dynamic_material

```python
def get_dynamic_material() -> MaterialInstanceDynamic
```

x.get_dynamic_material() -> MaterialInstanceDynamic
Get Dynamic Material

Returns:
    MaterialInstanceDynamic:

<a id="unreal.BorderSlot"></a>