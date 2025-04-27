## BackgroundBlur Objects

```python
class BackgroundBlur(ContentWidget)
```

A background blur is a container widget that can contain one child widget, providing an opportunity
to surround it with adjustable padding and apply a post-process Gaussian blur to all content beneath the widget.

* Single Child
* Blur Effect

**C++ Source:**

- **Module**: UMG
- **File**: BackgroundBlur.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``apply_alpha_to_blur`` (bool):  [Read-Write] True to modulate the strength of the blur based on the widget alpha.
- ``blur_radius`` (int32):  [Read-Write] This is the number of pixels which will be weighted in each direction from any given pixel when computing the blur
  A larger value is more costly but allows for stronger blurs.
- ``blur_strength`` (float):  [Read-Write] How blurry the background is.  Larger numbers mean more blurry but will result in larger runtime cost on the GPU.
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``corner_radius`` (Vector4):  [Read-Write] This is the number of pixels which will be weighted in each direction from any given pixel when computing the blur
  A larger value is more costly but allows for stronger blurs.
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``horizontal_alignment`` (HorizontalAlignment):  [Read-Write] The alignment of the content horizontally.
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``low_quality_fallback_brush`` (SlateBrush):  [Read-Write] An image to draw instead of applying a blur when low quality override mode is enabled.
  You can enable low quality mode for background blurs by setting the cvar Slate.ForceBackgroundBlurLowQualityOverride to 1.
  This is usually done in the project's scalability settings
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``padding`` (Margin):  [Read-Write] The padding area between the slot and the content it contains.
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``vertical_alignment`` (VerticalAlignment):  [Read-Write] The alignment of the content vertically.
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.BackgroundBlur.padding"></a>

#### padding

```python
@property
def padding() -> Margin
```

(Margin):  [Read-Write] The padding area between the slot and the content it contains.

<a id="unreal.BackgroundBlur.padding"></a>

#### padding

```python
@padding.setter
def padding(value: Margin) -> None
```

<a id="unreal.BackgroundBlur.horizontal_alignment"></a>

#### horizontal_alignment

```python
@property
def horizontal_alignment() -> HorizontalAlignment
```

(HorizontalAlignment):  [Read-Write] The alignment of the content horizontally.

<a id="unreal.BackgroundBlur.horizontal_alignment"></a>

#### horizontal_alignment

```python
@horizontal_alignment.setter
def horizontal_alignment(value: HorizontalAlignment) -> None
```

<a id="unreal.BackgroundBlur.vertical_alignment"></a>

#### vertical_alignment

```python
@property
def vertical_alignment() -> VerticalAlignment
```

(VerticalAlignment):  [Read-Write] The alignment of the content vertically.

<a id="unreal.BackgroundBlur.vertical_alignment"></a>

#### vertical_alignment

```python
@vertical_alignment.setter
def vertical_alignment(value: VerticalAlignment) -> None
```

<a id="unreal.BackgroundBlur.apply_alpha_to_blur"></a>

#### apply_alpha_to_blur

```python
@property
def apply_alpha_to_blur() -> bool
```

(bool):  [Read-Write] True to modulate the strength of the blur based on the widget alpha.

<a id="unreal.BackgroundBlur.apply_alpha_to_blur"></a>

#### apply_alpha_to_blur

```python
@apply_alpha_to_blur.setter
def apply_alpha_to_blur(value: bool) -> None
```

<a id="unreal.BackgroundBlur.blur_strength"></a>

#### blur_strength

```python
@property
def blur_strength() -> float
```

(float):  [Read-Write] How blurry the background is.  Larger numbers mean more blurry but will result in larger runtime cost on the GPU.

<a id="unreal.BackgroundBlur.blur_strength"></a>

#### blur_strength

```python
@blur_strength.setter
def blur_strength(value: float) -> None
```

<a id="unreal.BackgroundBlur.blur_radius"></a>

#### blur_radius

```python
@property
def blur_radius() -> int
```

(int32):  [Read-Write] This is the number of pixels which will be weighted in each direction from any given pixel when computing the blur
A larger value is more costly but allows for stronger blurs.

<a id="unreal.BackgroundBlur.blur_radius"></a>

#### blur_radius

```python
@blur_radius.setter
def blur_radius(value: int) -> None
```

<a id="unreal.BackgroundBlur.corner_radius"></a>

#### corner_radius

```python
@property
def corner_radius() -> Vector4
```

(Vector4):  [Read-Write] This is the number of pixels which will be weighted in each direction from any given pixel when computing the blur
A larger value is more costly but allows for stronger blurs.

<a id="unreal.BackgroundBlur.corner_radius"></a>

#### corner_radius

```python
@corner_radius.setter
def corner_radius(value: Vector4) -> None
```

<a id="unreal.BackgroundBlur.low_quality_fallback_brush"></a>

#### low_quality_fallback_brush

```python
@property
def low_quality_fallback_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] An image to draw instead of applying a blur when low quality override mode is enabled.
You can enable low quality mode for background blurs by setting the cvar Slate.ForceBackgroundBlurLowQualityOverride to 1.
This is usually done in the project's scalability settings

<a id="unreal.BackgroundBlur.low_quality_fallback_brush"></a>

#### low_quality_fallback_brush

```python
@low_quality_fallback_brush.setter
def low_quality_fallback_brush(value: SlateBrush) -> None
```

<a id="unreal.BackgroundBlur.set_vertical_alignment"></a>

#### set_vertical_alignment

```python
def set_vertical_alignment(vertical_alignment: VerticalAlignment) -> None
```

x.set_vertical_alignment(vertical_alignment) -> None
Set Vertical Alignment

Args:
    vertical_alignment (VerticalAlignment):

<a id="unreal.BackgroundBlur.set_padding"></a>

#### set_padding

```python
def set_padding(padding: Margin) -> None
```

x.set_padding(padding) -> None
Set Padding

Args:
    padding (Margin):

<a id="unreal.BackgroundBlur.set_low_quality_fallback_brush"></a>

#### set_low_quality_fallback_brush

```python
def set_low_quality_fallback_brush(brush: SlateBrush) -> None
```

x.set_low_quality_fallback_brush(brush) -> None
Set Low Quality Fallback Brush

Args:
    brush (SlateBrush):

<a id="unreal.BackgroundBlur.set_horizontal_alignment"></a>

#### set_horizontal_alignment

```python
def set_horizontal_alignment(
        horizontal_alignment: HorizontalAlignment) -> None
```

x.set_horizontal_alignment(horizontal_alignment) -> None
Set Horizontal Alignment

Args:
    horizontal_alignment (HorizontalAlignment):

<a id="unreal.BackgroundBlur.set_corner_radius"></a>

#### set_corner_radius

```python
def set_corner_radius(corner_radius: Vector4) -> None
```

x.set_corner_radius(corner_radius) -> None
Set Corner Radius

Args:
    corner_radius (Vector4):

<a id="unreal.BackgroundBlur.set_blur_strength"></a>

#### set_blur_strength

```python
def set_blur_strength(strength: float) -> None
```

x.set_blur_strength(strength) -> None
Set Blur Strength

Args:
    strength (float):

<a id="unreal.BackgroundBlur.set_blur_radius"></a>

#### set_blur_radius

```python
def set_blur_radius(blur_radius: int) -> None
```

x.set_blur_radius(blur_radius) -> None
Set Blur Radius

Args:
    blur_radius (int32):

<a id="unreal.BackgroundBlur.set_apply_alpha_to_blur"></a>

#### set_apply_alpha_to_blur

```python
def set_apply_alpha_to_blur(apply_alpha_to_blur: bool) -> None
```

x.set_apply_alpha_to_blur(apply_alpha_to_blur) -> None
Set Apply Alpha to Blur

Args:
    apply_alpha_to_blur (bool):

<a id="unreal.BackgroundBlurWidget"></a>