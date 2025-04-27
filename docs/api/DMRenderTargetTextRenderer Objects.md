## DMRenderTargetTextRenderer Objects

```python
class DMRenderTargetTextRenderer(DMRenderTargetWidgetRendererBase)
```

Renderer that renders an STextBlock widget and exposes all its parameters/properties.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMRenderTargetTextRenderer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_wrap_text`` (bool):  [Read-Write]
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``flow_direction`` (TextFlowDirection):  [Read-Write]
- ``font_info`` (SlateFontInfo):  [Read-Write]
- ``has_highlight`` (bool):  [Read-Write]
- ``has_shadow`` (bool):  [Read-Write]
- ``highlight_color`` (LinearColor):  [Read-Write]
- ``justify`` (TextJustify):  [Read-Write]
- ``line_height`` (float):  [Read-Write] Multiplier on the base font height.
- ``override_render_target_size`` (bool):  [Read-Write] When true, will change the size of the render target to fit the text.
- ``padding_bottom`` (float):  [Read-Write] Extra space adding beyond the edge of the glyphs. Useful for shadows, glows, etc.
- ``padding_left`` (float):  [Read-Write] Extra space adding beyond the edge of the glyphs. Useful for shadows, glows, etc.
- ``padding_right`` (float):  [Read-Write] Extra space adding beyond the edge of the glyphs. Useful for shadows, glows, etc.
- ``padding_top`` (float):  [Read-Write] Extra space adding beyond the edge of the glyphs. Useful for shadows, glows, etc.
- ``shadow_color`` (LinearColor):  [Read-Write]
- ``shadow_offset`` (Vector2D):  [Read-Write]
- ``shaping_method`` (TextShapingMethod):  [Read-Write]
- ``strike_brush`` (InstancedStruct):  [Read-Write]
- ``text`` (Text):  [Read-Write]
- ``text_color`` (LinearColor):  [Read-Write]
- ``transform_policy`` (TextTransformPolicy):  [Read-Write]
- ``wrap_text_at`` (float):  [Read-Write]
- ``wrapping_policy`` (TextWrappingPolicy):  [Read-Write]

<a id="unreal.DMRenderTargetTextRenderer.font_info"></a>

#### font_info

```python
@property
def font_info() -> SlateFontInfo
```

(SlateFontInfo):  [Read-Write]

<a id="unreal.DMRenderTargetTextRenderer.font_info"></a>

#### font_info

```python
@font_info.setter
def font_info(value: SlateFontInfo) -> None
```

<a id="unreal.DMRenderTargetTextRenderer.text"></a>

#### text

```python
@property
def text() -> Text
```

(Text):  [Read-Write]

<a id="unreal.DMRenderTargetTextRenderer.text"></a>

#### text

```python
@text.setter
def text(value: Text) -> None
```

<a id="unreal.DMRenderTargetTextRenderer.text_color"></a>

#### text_color

```python
@property
def text_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.DMRenderTargetTextRenderer.text_color"></a>

#### text_color

```python
@text_color.setter
def text_color(value: LinearColor) -> None
```

<a id="unreal.DMRenderTargetTextRenderer.has_highlight"></a>

#### has_highlight

```python
@property
def has_highlight() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMRenderTargetTextRenderer.has_highlight"></a>

#### has_highlight

```python
@has_highlight.setter
def has_highlight(value: bool) -> None
```

<a id="unreal.DMRenderTargetTextRenderer.highlight_color"></a>

#### highlight_color

```python
@property
def highlight_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.DMRenderTargetTextRenderer.highlight_color"></a>

#### highlight_color

```python
@highlight_color.setter
def highlight_color(value: LinearColor) -> None
```

<a id="unreal.DMRenderTargetTextRenderer.has_shadow"></a>

#### has_shadow

```python
@property
def has_shadow() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMRenderTargetTextRenderer.has_shadow"></a>

#### has_shadow

```python
@has_shadow.setter
def has_shadow(value: bool) -> None
```

<a id="unreal.DMRenderTargetTextRenderer.shadow_color"></a>

#### shadow_color

```python
@property
def shadow_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.DMRenderTargetTextRenderer.shadow_color"></a>

#### shadow_color

```python
@shadow_color.setter
def shadow_color(value: LinearColor) -> None
```

<a id="unreal.DMRenderTargetTextRenderer.shadow_offset"></a>

#### shadow_offset

```python
@property
def shadow_offset() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.DMRenderTargetTextRenderer.shadow_offset"></a>

#### shadow_offset

```python
@shadow_offset.setter
def shadow_offset(value: Vector2D) -> None
```

<a id="unreal.DMRenderTargetTextRenderer.auto_wrap_text"></a>

#### auto_wrap_text

```python
@property
def auto_wrap_text() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMRenderTargetTextRenderer.auto_wrap_text"></a>

#### auto_wrap_text

```python
@auto_wrap_text.setter
def auto_wrap_text(value: bool) -> None
```

<a id="unreal.DMRenderTargetTextRenderer.wrap_text_at"></a>

#### wrap_text_at

```python
@property
def wrap_text_at() -> float
```

(float):  [Read-Write]

<a id="unreal.DMRenderTargetTextRenderer.wrap_text_at"></a>

#### wrap_text_at

```python
@wrap_text_at.setter
def wrap_text_at(value: float) -> None
```

<a id="unreal.DMRenderTargetTextRenderer.wrapping_policy"></a>

#### wrapping_policy

```python
@property
def wrapping_policy() -> TextWrappingPolicy
```

(TextWrappingPolicy):  [Read-Write]

<a id="unreal.DMRenderTargetTextRenderer.wrapping_policy"></a>

#### wrapping_policy

```python
@wrapping_policy.setter
def wrapping_policy(value: TextWrappingPolicy) -> None
```

<a id="unreal.DMRenderTargetTextRenderer.justify"></a>

#### justify

```python
@property
def justify() -> TextJustify
```

(TextJustify):  [Read-Write]

<a id="unreal.DMRenderTargetTextRenderer.justify"></a>

#### justify

```python
@justify.setter
def justify(value: TextJustify) -> None
```

<a id="unreal.DMRenderTargetTextRenderer.transform_policy"></a>

#### transform_policy

```python
@property
def transform_policy() -> TextTransformPolicy
```

(TextTransformPolicy):  [Read-Write]

<a id="unreal.DMRenderTargetTextRenderer.transform_policy"></a>

#### transform_policy

```python
@transform_policy.setter
def transform_policy(value: TextTransformPolicy) -> None
```

<a id="unreal.DMRenderTargetTextRenderer.flow_direction"></a>

#### flow_direction

```python
@property
def flow_direction() -> TextFlowDirection
```

(TextFlowDirection):  [Read-Write]

<a id="unreal.DMRenderTargetTextRenderer.flow_direction"></a>

#### flow_direction

```python
@flow_direction.setter
def flow_direction(value: TextFlowDirection) -> None
```

<a id="unreal.DMRenderTargetTextRenderer.shaping_method"></a>

#### shaping_method

```python
@property
def shaping_method() -> TextShapingMethod
```

(TextShapingMethod):  [Read-Write]

<a id="unreal.DMRenderTargetTextRenderer.shaping_method"></a>

#### shaping_method

```python
@shaping_method.setter
def shaping_method(value: TextShapingMethod) -> None
```

<a id="unreal.DMRenderTargetTextRenderer.strike_brush"></a>

#### strike_brush

```python
@property
def strike_brush() -> InstancedStruct
```

(InstancedStruct):  [Read-Write]

<a id="unreal.DMRenderTargetTextRenderer.strike_brush"></a>

#### strike_brush

```python
@strike_brush.setter
def strike_brush(value: InstancedStruct) -> None
```

<a id="unreal.DMRenderTargetTextRenderer.line_height"></a>

#### line_height

```python
@property
def line_height() -> float
```

(float):  [Read-Write] Multiplier on the base font height.

<a id="unreal.DMRenderTargetTextRenderer.line_height"></a>

#### line_height

```python
@line_height.setter
def line_height(value: float) -> None
```

<a id="unreal.DMRenderTargetTextRenderer.padding_left"></a>

#### padding_left

```python
@property
def padding_left() -> float
```

(float):  [Read-Write] Extra space adding beyond the edge of the glyphs. Useful for shadows, glows, etc.

<a id="unreal.DMRenderTargetTextRenderer.padding_left"></a>

#### padding_left

```python
@padding_left.setter
def padding_left(value: float) -> None
```

<a id="unreal.DMRenderTargetTextRenderer.padding_right"></a>

#### padding_right

```python
@property
def padding_right() -> float
```

(float):  [Read-Write] Extra space adding beyond the edge of the glyphs. Useful for shadows, glows, etc.

<a id="unreal.DMRenderTargetTextRenderer.padding_right"></a>

#### padding_right

```python
@padding_right.setter
def padding_right(value: float) -> None
```

<a id="unreal.DMRenderTargetTextRenderer.padding_top"></a>

#### padding_top

```python
@property
def padding_top() -> float
```

(float):  [Read-Write] Extra space adding beyond the edge of the glyphs. Useful for shadows, glows, etc.

<a id="unreal.DMRenderTargetTextRenderer.padding_top"></a>

#### padding_top

```python
@padding_top.setter
def padding_top(value: float) -> None
```

<a id="unreal.DMRenderTargetTextRenderer.padding_bottom"></a>

#### padding_bottom

```python
@property
def padding_bottom() -> float
```

(float):  [Read-Write] Extra space adding beyond the edge of the glyphs. Useful for shadows, glows, etc.

<a id="unreal.DMRenderTargetTextRenderer.padding_bottom"></a>

#### padding_bottom

```python
@padding_bottom.setter
def padding_bottom(value: float) -> None
```

<a id="unreal.DMRenderTargetTextRenderer.override_render_target_size"></a>

#### override_render_target_size

```python
@property
def override_render_target_size() -> bool
```

(bool):  [Read-Write] When true, will change the size of the render target to fit the text.

<a id="unreal.DMRenderTargetTextRenderer.override_render_target_size"></a>

#### override_render_target_size

```python
@override_render_target_size.setter
def override_render_target_size(value: bool) -> None
```

<a id="unreal.DMRenderTargetTextRenderer.set_wrap_text_at"></a>

#### set_wrap_text_at

```python
def set_wrap_text_at(wrap_at: float) -> None
```

x.set_wrap_text_at(wrap_at) -> None
Set Wrap Text At

Args:
    wrap_at (float):

<a id="unreal.DMRenderTargetTextRenderer.set_wrapping_policy"></a>

#### set_wrapping_policy

```python
def set_wrapping_policy(wrapping_policy: TextWrappingPolicy) -> None
```

x.set_wrapping_policy(wrapping_policy) -> None
Set Wrapping Policy

Args:
    wrapping_policy (TextWrappingPolicy):

<a id="unreal.DMRenderTargetTextRenderer.set_transform_policy"></a>

#### set_transform_policy

```python
def set_transform_policy(transform_policy: TextTransformPolicy) -> None
```

x.set_transform_policy(transform_policy) -> None
Set Transform Policy

Args:
    transform_policy (TextTransformPolicy):

<a id="unreal.DMRenderTargetTextRenderer.set_text_color"></a>

#### set_text_color

```python
def set_text_color(color: LinearColor) -> None
```

x.set_text_color(color) -> None
Set Text Color

Args:
    color (LinearColor):

<a id="unreal.DMRenderTargetTextRenderer.set_text"></a>

#### set_text

```python
def set_text(text: Text) -> None
```

x.set_text(text) -> None
Set Text

Args:
    text (Text):

<a id="unreal.DMRenderTargetTextRenderer.set_strike_brush"></a>

#### set_strike_brush

```python
def set_strike_brush(strike_brush: InstancedStruct) -> None
```

x.set_strike_brush(strike_brush) -> None
Set Strike Brush

Args:
    strike_brush (InstancedStruct):

<a id="unreal.DMRenderTargetTextRenderer.set_shaping_method"></a>

#### set_shaping_method

```python
def set_shaping_method(shaping_method: TextShapingMethod) -> None
```

x.set_shaping_method(shaping_method) -> None
Set Shaping Method

Args:
    shaping_method (TextShapingMethod):

<a id="unreal.DMRenderTargetTextRenderer.set_shadow_offset"></a>

#### set_shadow_offset

```python
def set_shadow_offset(shadow_offset: Vector2D) -> None
```

x.set_shadow_offset(shadow_offset) -> None
Set Shadow Offset

Args:
    shadow_offset (Vector2D):

<a id="unreal.DMRenderTargetTextRenderer.set_shadow_color"></a>

#### set_shadow_color

```python
def set_shadow_color(shadow_color: LinearColor) -> None
```

x.set_shadow_color(shadow_color) -> None
Set Shadow Color

Args:
    shadow_color (LinearColor):

<a id="unreal.DMRenderTargetTextRenderer.set_padding_top"></a>

#### set_padding_top

```python
def set_padding_top(padding: float) -> None
```

x.set_padding_top(padding) -> None
Set Padding Top

Args:
    padding (float):

<a id="unreal.DMRenderTargetTextRenderer.set_padding_right"></a>

#### set_padding_right

```python
def set_padding_right(padding: float) -> None
```

x.set_padding_right(padding) -> None
Set Padding Right

Args:
    padding (float):

<a id="unreal.DMRenderTargetTextRenderer.set_padding_left"></a>

#### set_padding_left

```python
def set_padding_left(padding: float) -> None
```

x.set_padding_left(padding) -> None
Set Padding Left

Args:
    padding (float):

<a id="unreal.DMRenderTargetTextRenderer.set_padding_bottom"></a>

#### set_padding_bottom

```python
def set_padding_bottom(padding: float) -> None
```

x.set_padding_bottom(padding) -> None
Set Padding Bottom

Args:
    padding (float):

<a id="unreal.DMRenderTargetTextRenderer.set_override_render_target_size"></a>

#### set_override_render_target_size

```python
def set_override_render_target_size(override: bool) -> None
```

x.set_override_render_target_size(override) -> None
Set Override Render Target Size

Args:
    override (bool):

<a id="unreal.DMRenderTargetTextRenderer.set_line_height"></a>

#### set_line_height

```python
def set_line_height(line_height: float) -> None
```

x.set_line_height(line_height) -> None
Set Line Height

Args:
    line_height (float):

<a id="unreal.DMRenderTargetTextRenderer.set_justify"></a>

#### set_justify

```python
def set_justify(justify: TextJustify) -> None
```

x.set_justify(justify) -> None
Set Justify

Args:
    justify (TextJustify):

<a id="unreal.DMRenderTargetTextRenderer.set_highlight_color"></a>

#### set_highlight_color

```python
def set_highlight_color(highlight_color: LinearColor) -> None
```

x.set_highlight_color(highlight_color) -> None
Set Highlight Color

Args:
    highlight_color (LinearColor):

<a id="unreal.DMRenderTargetTextRenderer.set_has_shadow"></a>

#### set_has_shadow

```python
def set_has_shadow(has_shadow: bool) -> None
```

x.set_has_shadow(has_shadow) -> None
Set Has Shadow

Args:
    has_shadow (bool):

<a id="unreal.DMRenderTargetTextRenderer.set_has_highlight"></a>

#### set_has_highlight

```python
def set_has_highlight(has_highlight: bool) -> None
```

x.set_has_highlight(has_highlight) -> None
Set Has Highlight

Args:
    has_highlight (bool):

<a id="unreal.DMRenderTargetTextRenderer.set_font_info"></a>

#### set_font_info

```python
def set_font_info(font_info: SlateFontInfo) -> None
```

x.set_font_info(font_info) -> None
Set Font Info

Args:
    font_info (SlateFontInfo):

<a id="unreal.DMRenderTargetTextRenderer.set_flow_direction"></a>

#### set_flow_direction

```python
def set_flow_direction(flow_direction: TextFlowDirection) -> None
```

x.set_flow_direction(flow_direction) -> None
Set Flow Direction

Args:
    flow_direction (TextFlowDirection):

<a id="unreal.DMRenderTargetTextRenderer.set_background_color"></a>

#### set_background_color

```python
def set_background_color(background_color: LinearColor) -> None
```

x.set_background_color(background_color) -> None
Set Background Color

Args:
    background_color (LinearColor):

<a id="unreal.DMRenderTargetTextRenderer.set_auto_wrap_text"></a>

#### set_auto_wrap_text

```python
def set_auto_wrap_text(auto_wrap: bool) -> None
```

x.set_auto_wrap_text(auto_wrap) -> None
Set Auto Wrap Text

Args:
    auto_wrap (bool):

<a id="unreal.DMRenderTargetTextRenderer.is_overriding_render_target_size"></a>

#### is_overriding_render_target_size

```python
def is_overriding_render_target_size() -> bool
```

x.is_overriding_render_target_size() -> bool
Is Overriding Render Target Size

Returns:
    bool:

<a id="unreal.DMRenderTargetTextRenderer.get_wrap_text_at"></a>

#### get_wrap_text_at

```python
def get_wrap_text_at() -> float
```

x.get_wrap_text_at() -> float
Get Wrap Text At

Returns:
    float:

<a id="unreal.DMRenderTargetTextRenderer.get_wrapping_policy"></a>

#### get_wrapping_policy

```python
def get_wrapping_policy() -> TextWrappingPolicy
```

x.get_wrapping_policy() -> TextWrappingPolicy
Get Wrapping Policy

Returns:
    TextWrappingPolicy:

<a id="unreal.DMRenderTargetTextRenderer.get_transform_policy"></a>

#### get_transform_policy

```python
def get_transform_policy() -> TextTransformPolicy
```

x.get_transform_policy() -> TextTransformPolicy
Get Transform Policy

Returns:
    TextTransformPolicy:

<a id="unreal.DMRenderTargetTextRenderer.get_text_color"></a>

#### get_text_color

```python
def get_text_color() -> LinearColor
```

x.get_text_color() -> LinearColor
Get Text Color

Returns:
    LinearColor:

<a id="unreal.DMRenderTargetTextRenderer.get_text"></a>

#### get_text

```python
def get_text() -> Text
```

x.get_text() -> Text
Get Text

Returns:
    Text:

<a id="unreal.DMRenderTargetTextRenderer.get_strike_brush"></a>

#### get_strike_brush

```python
def get_strike_brush() -> InstancedStruct
```

x.get_strike_brush() -> InstancedStruct
Get Strike Brush

Returns:
    InstancedStruct:

<a id="unreal.DMRenderTargetTextRenderer.get_shaping_method"></a>

#### get_shaping_method

```python
def get_shaping_method() -> TextShapingMethod
```

x.get_shaping_method() -> TextShapingMethod
Get Shaping Method

Returns:
    TextShapingMethod:

<a id="unreal.DMRenderTargetTextRenderer.get_shadow_offset"></a>

#### get_shadow_offset

```python
def get_shadow_offset() -> Vector2D
```

x.get_shadow_offset() -> Vector2D
Get Shadow Offset

Returns:
    Vector2D:

<a id="unreal.DMRenderTargetTextRenderer.get_shadow_color"></a>

#### get_shadow_color

```python
def get_shadow_color() -> LinearColor
```

x.get_shadow_color() -> LinearColor
Get Shadow Color

Returns:
    LinearColor:

<a id="unreal.DMRenderTargetTextRenderer.get_padding_top"></a>

#### get_padding_top

```python
def get_padding_top() -> float
```

x.get_padding_top() -> float
Get Padding Top

Returns:
    float:

<a id="unreal.DMRenderTargetTextRenderer.get_padding_right"></a>

#### get_padding_right

```python
def get_padding_right() -> float
```

x.get_padding_right() -> float
Get Padding Right

Returns:
    float:

<a id="unreal.DMRenderTargetTextRenderer.get_padding_left"></a>

#### get_padding_left

```python
def get_padding_left() -> float
```

x.get_padding_left() -> float
Get Padding Left

Returns:
    float:

<a id="unreal.DMRenderTargetTextRenderer.get_padding_bottom"></a>

#### get_padding_bottom

```python
def get_padding_bottom() -> float
```

x.get_padding_bottom() -> float
Get Padding Bottom

Returns:
    float:

<a id="unreal.DMRenderTargetTextRenderer.get_line_height"></a>

#### get_line_height

```python
def get_line_height() -> float
```

x.get_line_height() -> float
Get Line Height

Returns:
    float:

<a id="unreal.DMRenderTargetTextRenderer.get_justify"></a>

#### get_justify

```python
def get_justify() -> TextJustify
```

x.get_justify() -> TextJustify
Get Justify

Returns:
    TextJustify:

<a id="unreal.DMRenderTargetTextRenderer.get_highlight_color"></a>

#### get_highlight_color

```python
def get_highlight_color() -> LinearColor
```

x.get_highlight_color() -> LinearColor
Get Highlight Color

Returns:
    LinearColor:

<a id="unreal.DMRenderTargetTextRenderer.get_has_shadow"></a>

#### get_has_shadow

```python
def get_has_shadow() -> bool
```

x.get_has_shadow() -> bool
Get Has Shadow

Returns:
    bool:

<a id="unreal.DMRenderTargetTextRenderer.get_has_highlight"></a>

#### get_has_highlight

```python
def get_has_highlight() -> bool
```

x.get_has_highlight() -> bool
Get Has Highlight

Returns:
    bool:

<a id="unreal.DMRenderTargetTextRenderer.get_font_info"></a>

#### get_font_info

```python
def get_font_info() -> SlateFontInfo
```

x.get_font_info() -> SlateFontInfo
Get Font Info

Returns:
    SlateFontInfo:

<a id="unreal.DMRenderTargetTextRenderer.get_flow_direction"></a>

#### get_flow_direction

```python
def get_flow_direction() -> TextFlowDirection
```

x.get_flow_direction() -> TextFlowDirection
Get Flow Direction

Returns:
    TextFlowDirection:

<a id="unreal.DMRenderTargetTextRenderer.get_background_color"></a>

#### get_background_color

```python
def get_background_color() -> LinearColor
```

x.get_background_color() -> LinearColor
Get Background Color

Returns:
    LinearColor:

<a id="unreal.DMRenderTargetTextRenderer.get_auto_wrap_text"></a>

#### get_auto_wrap_text

```python
def get_auto_wrap_text() -> bool
```

x.get_auto_wrap_text() -> bool
Get Auto Wrap Text

Returns:
    bool:

<a id="unreal.DMRenderTargetUMGWidgetRenderer"></a>