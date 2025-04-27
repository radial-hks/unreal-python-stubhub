## TextBlock Objects

```python
class TextBlock(TextLayoutWidget)
```

A simple static text widget.

* No Children
* Text

**C++ Source:**

- **Module**: UMG
- **File**: TextBlock.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``apply_line_height_to_bottom_line`` (bool):  [Read-Write] Whether to leave extra space below the last line due to line height.
- ``auto_wrap_text`` (bool):  [Read-Write] True if we're wrapping text automatically based on the computed horizontal space for this widget.
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``color_and_opacity`` (SlateColor):  [Read-Write] The color of the text
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``font`` (SlateFontInfo):  [Read-Write] The font to render the text with
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``justification`` (TextJustify):  [Read-Write] How the text should be aligned with the margin.
- ``line_height_percentage`` (float):  [Read-Write] The amount to scale each lines height by.
- ``margin`` (Margin):  [Read-Write] The amount of blank space left around the edges of text area.
- ``min_desired_width`` (float):  [Read-Write] The minimum desired size for the text
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
- ``shadow_color_and_opacity`` (LinearColor):  [Read-Write] The color of the shadow
- ``shadow_offset`` (Vector2D):  [Read-Write] The direction the shadow is cast
- ``shaped_text_options`` (ShapedTextOptions):  [Read-Write] Controls how the text within this widget should be shaped.
- ``simple_text_mode`` (bool):  [Read-Write] If this is enabled, text shaping, wrapping, justification are disabled in favor of much faster text layout and measurement.
  This feature is only suitable for "simple" text (ie, text containing only numbers or basic ASCII) as it disables the complex text rendering support required for certain languages (such as Arabic and Thai).
  It is significantly faster for text that can take advantage of it (particularly if that text changes frequently), but shouldn't be used for localized user-facing text.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``strike_brush`` (SlateBrush):  [Read-Write] The brush to strike through text with
- ``text`` (Text):  [Read-Write] The text to display
- ``text_overflow_policy`` (TextOverflowPolicy):  [Read-Write] Sets what happens to text that is clipped and doesn't fit within the clip rect for this widget
- ``text_transform_policy`` (TextTransformPolicy):  [Read-Write] The text transformation policy to apply to this text block.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``wrap_text_at`` (float):  [Read-Write] Whether text wraps onto a new line when it's length exceeds this width; if this value is zero or negative, no wrapping occurs.
- ``wrap_with_invalidation_panel`` (bool):  [Read-Write] If true, it will automatically wrap this text widget with an invalidation panel
- ``wrapping_policy`` (TextWrappingPolicy):  [Read-Write] The wrapping policy to use.

<a id="unreal.TextBlock.text"></a>

#### text

```python
@property
def text() -> Text
```

(Text):  [Read-Write] The text to display

<a id="unreal.TextBlock.text"></a>

#### text

```python
@text.setter
def text(value: Text) -> None
```

<a id="unreal.TextBlock.color_and_opacity"></a>

#### color_and_opacity

```python
@property
def color_and_opacity() -> SlateColor
```

(SlateColor):  [Read-Write] The color of the text

<a id="unreal.TextBlock.color_and_opacity"></a>

#### color_and_opacity

```python
@color_and_opacity.setter
def color_and_opacity(value: SlateColor) -> None
```

<a id="unreal.TextBlock.min_desired_width"></a>

#### min_desired_width

```python
@property
def min_desired_width() -> float
```

(float):  [Read-Write] The minimum desired size for the text

<a id="unreal.TextBlock.min_desired_width"></a>

#### min_desired_width

```python
@min_desired_width.setter
def min_desired_width(value: float) -> None
```

<a id="unreal.TextBlock.font"></a>

#### font

```python
@property
def font() -> SlateFontInfo
```

(SlateFontInfo):  [Read-Write] The font to render the text with

<a id="unreal.TextBlock.font"></a>

#### font

```python
@font.setter
def font(value: SlateFontInfo) -> None
```

<a id="unreal.TextBlock.strike_brush"></a>

#### strike_brush

```python
@property
def strike_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] The brush to strike through text with

<a id="unreal.TextBlock.strike_brush"></a>

#### strike_brush

```python
@strike_brush.setter
def strike_brush(value: SlateBrush) -> None
```

<a id="unreal.TextBlock.shadow_offset"></a>

#### shadow_offset

```python
@property
def shadow_offset() -> Vector2D
```

(Vector2D):  [Read-Write] The direction the shadow is cast

<a id="unreal.TextBlock.shadow_offset"></a>

#### shadow_offset

```python
@shadow_offset.setter
def shadow_offset(value: Vector2D) -> None
```

<a id="unreal.TextBlock.shadow_color_and_opacity"></a>

#### shadow_color_and_opacity

```python
@property
def shadow_color_and_opacity() -> LinearColor
```

(LinearColor):  [Read-Write] The color of the shadow

<a id="unreal.TextBlock.shadow_color_and_opacity"></a>

#### shadow_color_and_opacity

```python
@shadow_color_and_opacity.setter
def shadow_color_and_opacity(value: LinearColor) -> None
```

<a id="unreal.TextBlock.wrap_with_invalidation_panel"></a>

#### wrap_with_invalidation_panel

```python
@property
def wrap_with_invalidation_panel() -> bool
```

(bool):  [Read-Only] If true, it will automatically wrap this text widget with an invalidation panel

<a id="unreal.TextBlock.text_transform_policy"></a>

#### text_transform_policy

```python
@property
def text_transform_policy() -> TextTransformPolicy
```

(TextTransformPolicy):  [Read-Write] The text transformation policy to apply to this text block.

<a id="unreal.TextBlock.text_transform_policy"></a>

#### text_transform_policy

```python
@text_transform_policy.setter
def text_transform_policy(value: TextTransformPolicy) -> None
```

<a id="unreal.TextBlock.text_overflow_policy"></a>

#### text_overflow_policy

```python
@property
def text_overflow_policy() -> TextOverflowPolicy
```

(TextOverflowPolicy):  [Read-Write] Sets what happens to text that is clipped and doesn't fit within the clip rect for this widget

<a id="unreal.TextBlock.text_overflow_policy"></a>

#### text_overflow_policy

```python
@text_overflow_policy.setter
def text_overflow_policy(value: TextOverflowPolicy) -> None
```

<a id="unreal.TextBlock.simple_text_mode"></a>

#### simple_text_mode

```python
@property
def simple_text_mode() -> bool
```

(bool):  [Read-Only] If this is enabled, text shaping, wrapping, justification are disabled in favor of much faster text layout and measurement.
This feature is only suitable for "simple" text (ie, text containing only numbers or basic ASCII) as it disables the complex text rendering support required for certain languages (such as Arabic and Thai).
It is significantly faster for text that can take advantage of it (particularly if that text changes frequently), but shouldn't be used for localized user-facing text.

<a id="unreal.TextBlock.set_text_transform_policy"></a>

#### set_text_transform_policy

```python
def set_text_transform_policy(transform_policy: TextTransformPolicy) -> None
```

x.set_text_transform_policy(transform_policy) -> None
Set the text transformation policy for this text block.

Args:
    transform_policy (TextTransformPolicy): the new text transformation policy.

<a id="unreal.TextBlock.set_text_overflow_policy"></a>

#### set_text_overflow_policy

```python
def set_text_overflow_policy(overflow_policy: TextOverflowPolicy) -> None
```

x.set_text_overflow_policy(overflow_policy) -> None
Set the text overflow policy for this text block.

Args:
    overflow_policy (TextOverflowPolicy): the new text overflow policy.

<a id="unreal.TextBlock.set_text"></a>

#### set_text

```python
def set_text(text: Text) -> None
```

x.set_text(text) -> None
Directly sets the widget text.
Warning: This will wipe any binding created for the Text property!

Args:
    text (Text): The text to assign to the widget

<a id="unreal.TextBlock.set_strike_brush"></a>

#### set_strike_brush

```python
def set_strike_brush(strike_brush: SlateBrush) -> None
```

x.set_strike_brush(strike_brush) -> None
Dynamically set the strike brush for this text block

Args:
    strike_brush (SlateBrush): The new brush to use to strike through text

<a id="unreal.TextBlock.set_shadow_offset"></a>

#### set_shadow_offset

```python
def set_shadow_offset(shadow_offset: Vector2D) -> None
```

x.set_shadow_offset(shadow_offset) -> None
Sets the offset that the text drop shadow should be drawn at

Args:
    shadow_offset (Vector2D): The new offset

<a id="unreal.TextBlock.set_shadow_color_and_opacity"></a>

#### set_shadow_color_and_opacity

```python
def set_shadow_color_and_opacity(
        shadow_color_and_opacity: LinearColor) -> None
```

x.set_shadow_color_and_opacity(shadow_color_and_opacity) -> None
Sets the color and opacity of the text drop shadow
Note: if opacity is zero no shadow will be drawn

Args:
    shadow_color_and_opacity (LinearColor): The new drop shadow color and opacity

<a id="unreal.TextBlock.set_opacity"></a>

#### set_opacity

```python
def set_opacity(opacity: float) -> None
```

x.set_opacity(opacity) -> None
Sets the opacity of the text in this text block

Args:
    opacity (float): The new text opacity

<a id="unreal.TextBlock.set_min_desired_width"></a>

#### set_min_desired_width

```python
def set_min_desired_width(min_desired_width: float) -> None
```

x.set_min_desired_width(min_desired_width) -> None
Set the minimum desired width for this text block

Args:
    min_desired_width (float): new minimum desired width

<a id="unreal.TextBlock.set_font_outline_material"></a>

#### set_font_outline_material

```python
def set_font_outline_material(material: MaterialInterface) -> None
```

x.set_font_outline_material(material) -> None
Set Font Outline Material

Args:
    material (MaterialInterface):

<a id="unreal.TextBlock.set_font_material"></a>

#### set_font_material

```python
def set_font_material(material: MaterialInterface) -> None
```

x.set_font_material(material) -> None
Set Font Material

Args:
    material (MaterialInterface):

<a id="unreal.TextBlock.set_font"></a>

#### set_font

```python
def set_font(font_info: SlateFontInfo) -> None
```

x.set_font(font_info) -> None
Dynamically set the font info for this text block

Args:
    font_info (SlateFontInfo): The new font info

<a id="unreal.TextBlock.set_color_and_opacity"></a>

#### set_color_and_opacity

```python
def set_color_and_opacity(color_and_opacity: SlateColor) -> None
```

x.set_color_and_opacity(color_and_opacity) -> None
Sets the color and opacity of the text in this text block

Args:
    color_and_opacity (SlateColor): The new text color and opacity

<a id="unreal.TextBlock.set_auto_wrap_text"></a>

#### set_auto_wrap_text

```python
def set_auto_wrap_text(auto_text_wrap: bool) -> None
```

x.set_auto_wrap_text(auto_text_wrap) -> None
Set the auto wrap for this text block.

Args:
    auto_text_wrap (bool): to turn wrap on or off.

<a id="unreal.TextBlock.get_text"></a>

#### get_text

```python
def get_text() -> Text
```

x.get_text() -> Text
Gets the widget text

Returns:
    Text: The widget text

<a id="unreal.TextBlock.get_dynamic_outline_material"></a>

#### get_dynamic_outline_material

```python
def get_dynamic_outline_material() -> MaterialInstanceDynamic
```

x.get_dynamic_outline_material() -> MaterialInstanceDynamic
Get Dynamic Outline Material

Returns:
    MaterialInstanceDynamic:

<a id="unreal.TextBlock.get_dynamic_font_material"></a>

#### get_dynamic_font_material

```python
def get_dynamic_font_material() -> MaterialInstanceDynamic
```

x.get_dynamic_font_material() -> MaterialInstanceDynamic
Get Dynamic Font Material

Returns:
    MaterialInstanceDynamic:

<a id="unreal.Throbber"></a>