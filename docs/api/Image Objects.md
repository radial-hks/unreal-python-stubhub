## Image Objects

```python
class Image(Widget)
```

The image widget allows you to display a Slate Brush, or texture or material in the UI.

* No Children

**C++ Source:**

- **Module**: UMG
- **File**: Image.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``brush`` (SlateBrush):  [Read-Write] Image to draw
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``color_and_opacity`` (LinearColor):  [Read-Write] Color and opacity
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``flip_for_right_to_left_flow_direction`` (bool):  [Read-Write] Flips the image if the localization's flow direction is RightToLeft
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_mouse_button_down_event`` (OnPointerEvent):  [Read-Write]
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

<a id="unreal.Image.brush"></a>

#### brush

```python
@property
def brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to draw

<a id="unreal.Image.brush"></a>

#### brush

```python
@brush.setter
def brush(value: SlateBrush) -> None
```

<a id="unreal.Image.color_and_opacity"></a>

#### color_and_opacity

```python
@property
def color_and_opacity() -> LinearColor
```

(LinearColor):  [Read-Write] Color and opacity

<a id="unreal.Image.color_and_opacity"></a>

#### color_and_opacity

```python
@color_and_opacity.setter
def color_and_opacity(value: LinearColor) -> None
```

<a id="unreal.Image.flip_for_right_to_left_flow_direction"></a>

#### flip_for_right_to_left_flow_direction

```python
@property
def flip_for_right_to_left_flow_direction() -> bool
```

(bool):  [Read-Write] Flips the image if the localization's flow direction is RightToLeft

<a id="unreal.Image.flip_for_right_to_left_flow_direction"></a>

#### flip_for_right_to_left_flow_direction

```python
@flip_for_right_to_left_flow_direction.setter
def flip_for_right_to_left_flow_direction(value: bool) -> None
```

<a id="unreal.Image.set_opacity"></a>

#### set_opacity

```python
def set_opacity(opacity: float) -> None
```

x.set_opacity(opacity) -> None
Set Opacity

Args:
    opacity (float):

<a id="unreal.Image.set_desired_size_override"></a>

#### set_desired_size_override

```python
def set_desired_size_override(desired_size: Vector2D) -> None
```

x.set_desired_size_override(desired_size) -> None
Set Desired Size Override

Args:
    desired_size (Vector2D):

<a id="unreal.Image.set_brush_size"></a>

#### set_brush_size

```python
def set_brush_size(desired_size: Vector2D) -> None
```

deprecated: 'set_brush_size' was renamed to 'set_desired_size_override'.

<a id="unreal.Image.set_color_and_opacity"></a>

#### set_color_and_opacity

```python
def set_color_and_opacity(color_and_opacity: LinearColor) -> None
```

x.set_color_and_opacity(color_and_opacity) -> None
Set Color and Opacity

Args:
    color_and_opacity (LinearColor):

<a id="unreal.Image.set_brush_tint_color"></a>

#### set_brush_tint_color

```python
def set_brush_tint_color(tint_color: SlateColor) -> None
```

x.set_brush_tint_color(tint_color) -> None
Set Brush Tint Color

Args:
    tint_color (SlateColor):

<a id="unreal.Image.set_brush_resource_object"></a>

#### set_brush_resource_object

```python
def set_brush_resource_object(resource_object: Object) -> None
```

x.set_brush_resource_object(resource_object) -> None
Set Brush Resource Object

Args:
    resource_object (Object):

<a id="unreal.Image.set_brush_from_texture_dynamic"></a>

#### set_brush_from_texture_dynamic

```python
def set_brush_from_texture_dynamic(texture: Texture2DDynamic,
                                   match_size: bool = False) -> None
```

x.set_brush_from_texture_dynamic(texture, match_size=False) -> None
Sets the Brush to the specified Dynamic Texture.

Args:
    texture (Texture2DDynamic): Dynamic Texture to use to set on Brush.
    match_size (bool): If true, image will change its size to texture size. If false, texture will be stretched to image size.

<a id="unreal.Image.set_brush_from_texture"></a>

#### set_brush_from_texture

```python
def set_brush_from_texture(texture: Texture2D,
                           match_size: bool = False) -> None
```

x.set_brush_from_texture(texture, match_size=False) -> None
Sets the Brush to the specified Texture.

Args:
    texture (Texture2D): Texture to use to set on Brush.
    match_size (bool): If true, image will change its size to texture size. If false, texture will be stretched to image size.

<a id="unreal.Image.set_brush_from_soft_texture"></a>

#### set_brush_from_soft_texture

```python
def set_brush_from_soft_texture(soft_texture: Texture2D,
                                match_size: bool = False) -> None
```

x.set_brush_from_soft_texture(soft_texture, match_size=False) -> None
Sets the Brush to the specified Soft Texture.

Args:
    soft_texture (Texture2D): Soft Texture to use to set on Brush.
    match_size (bool): If true, image will change its size to texture size. If false, texture will be stretched to image size.

<a id="unreal.Image.set_brush_from_soft_material"></a>

#### set_brush_from_soft_material

```python
def set_brush_from_soft_material(soft_material: MaterialInterface) -> None
```

x.set_brush_from_soft_material(soft_material) -> None
Set Brush from Soft Material

Args:
    soft_material (MaterialInterface):

<a id="unreal.Image.set_brush_from_material"></a>

#### set_brush_from_material

```python
def set_brush_from_material(material: MaterialInterface) -> None
```

x.set_brush_from_material(material) -> None
Set Brush from Material

Args:
    material (MaterialInterface):

<a id="unreal.Image.set_brush_from_atlas_interface"></a>

#### set_brush_from_atlas_interface

```python
def set_brush_from_atlas_interface(atlas_region: SlateTextureAtlasInterface,
                                   match_size: bool = False) -> None
```

x.set_brush_from_atlas_interface(atlas_region, match_size=False) -> None
Sets the Brush to the specified Atlas Region.

Args:
    atlas_region (SlateTextureAtlasInterface): Region of the Atlas to use to set on Brush.
    match_size (bool): If true, image will change its size to atlas region size. If false, atlas region will be stretched to image size.

<a id="unreal.Image.set_brush_from_asset"></a>

#### set_brush_from_asset

```python
def set_brush_from_asset(asset: SlateBrushAsset) -> None
```

x.set_brush_from_asset(asset) -> None
Set Brush from Asset

Args:
    asset (SlateBrushAsset):

<a id="unreal.Image.set_brush"></a>

#### set_brush

```python
def set_brush(brush: SlateBrush) -> None
```

x.set_brush(brush) -> None
Set Brush

Args:
    brush (SlateBrush):

<a id="unreal.Image.get_dynamic_material"></a>

#### get_dynamic_material

```python
def get_dynamic_material() -> MaterialInstanceDynamic
```

x.get_dynamic_material() -> MaterialInstanceDynamic
Get Dynamic Material

Returns:
    MaterialInstanceDynamic:

<a id="unreal.InputKeySelector"></a>