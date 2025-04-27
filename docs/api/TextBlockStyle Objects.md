## TextBlockStyle Objects

```python
class TextBlockStyle(SlateWidgetStyle)
```

Represents the appearance of an STextBlock

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_and_opacity`` (SlateColor):  [Read-Write] The color and opacity of this text
- ``font`` (SlateFontInfo):  [Read-Write] Font family and size to be used when displaying this text.
- ``highlight_color`` (SlateColor):  [Read-Write] The color of highlighted text
- ``highlight_shape`` (SlateBrush):  [Read-Write] The shape of highlighted text
- ``overflow_policy`` (TextOverflowPolicy):  [Read-Write] Determines what happens to text that is clipped and doesn't fit within the clip rect of a text widget
- ``selected_background_color`` (SlateColor):  [Read-Write] The background color of selected text
- ``shadow_color_and_opacity`` (LinearColor):  [Read-Write] The color and opacity of the shadow
- ``shadow_offset`` (DeprecateSlateVector2D):  [Read-Write] How much should the shadow be offset? An offset of 0 implies no shadow.
- ``strike_brush`` (SlateBrush):  [Read-Write] The brush used to draw an strike through the text (if any)
- ``transform_policy`` (TextTransformPolicy):  [Read-Write] The Text Transform Policy (defaults to None)
- ``underline_brush`` (SlateBrush):  [Read-Write] The brush used to draw an underline under the text (if any)

<a id="unreal.TextBlockStyle.__init__"></a>

#### __init__

```python
def __init__(
        font: SlateFontInfo = [
            None, None,
            [
                0, False, False, False, None,
                [0.000000, 0.000000, 0.000000, 1.000000]
            ], "None", 24.000000, 0, 0.000000, False, False, 1.000000
        ],
        color_and_opacity: SlateColor = [[
            1.000000, 0.000000, 1.000000, 1.000000
        ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
        shadow_offset: DeprecateSlateVector2D = [0.000000, 0.000000],
        shadow_color_and_opacity: LinearColor = [
            0.000000, 0.000000, 0.000000, 0.000000
        ],
        highlight_color: SlateColor = [[
            1.000000, 0.000000, 1.000000, 1.000000
        ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
        highlight_shape: SlateBrush = [
            [[1.000000, 1.000000, 1.000000, 1.000000],
             SlateColorStylingMode.USE_COLOR_SPECIFIED],
            SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE,
            SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
            [0.000000, 0.000000, 0.000000, 0.000000], None,
            [[0.000000, 0.000000, 0.000000, 0.000000],
             [[0.000000, 0.000000, 0.000000, 0.000000],
              SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
             SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
        ],
        strike_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000],
                                     SlateColorStylingMode.USE_COLOR_SPECIFIED
                                     ], SlateBrushDrawType.IMAGE,
                                    SlateBrushTileType.NO_TILE,
                                    SlateBrushMirrorType.NO_MIRROR,
                                    [0.000000, 0.000000],
                                    [0.000000, 0.000000, 0.000000,
                                     0.000000], None,
                                    [[0.000000, 0.000000, 0.000000, 0.000000],
                                     [[0.000000, 0.000000, 0.000000, 0.000000],
                                      SlateColorStylingMode.USE_COLOR_SPECIFIED
                                      ], 0.000000,
                                     SlateBrushRoundingType.HALF_HEIGHT_RADIUS,
                                     False]],
        underline_brush: SlateBrush = [
            [[1.000000, 1.000000, 1.000000, 1.000000],
             SlateColorStylingMode.USE_COLOR_SPECIFIED],
            SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE,
            SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
            [0.000000, 0.000000, 0.000000, 0.000000], None,
            [[0.000000, 0.000000, 0.000000, 0.000000],
             [[0.000000, 0.000000, 0.000000, 0.000000],
              SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
             SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
        ],
        transform_policy: TextTransformPolicy = TextTransformPolicy.NONE,
        overflow_policy: TextOverflowPolicy = TextOverflowPolicy.CLIP) -> None
```

<a id="unreal.TextBlockStyle.font"></a>

#### font

```python
@property
def font() -> SlateFontInfo
```

(SlateFontInfo):  [Read-Write] Font family and size to be used when displaying this text.

<a id="unreal.TextBlockStyle.font"></a>

#### font

```python
@font.setter
def font(value: SlateFontInfo) -> None
```

<a id="unreal.TextBlockStyle.color_and_opacity"></a>

#### color_and_opacity

```python
@property
def color_and_opacity() -> SlateColor
```

(SlateColor):  [Read-Write] The color and opacity of this text

<a id="unreal.TextBlockStyle.color_and_opacity"></a>

#### color_and_opacity

```python
@color_and_opacity.setter
def color_and_opacity(value: SlateColor) -> None
```

<a id="unreal.TextBlockStyle.shadow_offset"></a>

#### shadow_offset

```python
@property
def shadow_offset() -> DeprecateSlateVector2D
```

(DeprecateSlateVector2D):  [Read-Write] How much should the shadow be offset? An offset of 0 implies no shadow.

<a id="unreal.TextBlockStyle.shadow_offset"></a>

#### shadow_offset

```python
@shadow_offset.setter
def shadow_offset(value: DeprecateSlateVector2D) -> None
```

<a id="unreal.TextBlockStyle.shadow_color_and_opacity"></a>

#### shadow_color_and_opacity

```python
@property
def shadow_color_and_opacity() -> LinearColor
```

(LinearColor):  [Read-Write] The color and opacity of the shadow

<a id="unreal.TextBlockStyle.shadow_color_and_opacity"></a>

#### shadow_color_and_opacity

```python
@shadow_color_and_opacity.setter
def shadow_color_and_opacity(value: LinearColor) -> None
```

<a id="unreal.TextBlockStyle.highlight_color"></a>

#### highlight_color

```python
@property
def highlight_color() -> SlateColor
```

(SlateColor):  [Read-Write] The color of highlighted text

<a id="unreal.TextBlockStyle.highlight_color"></a>

#### highlight_color

```python
@highlight_color.setter
def highlight_color(value: SlateColor) -> None
```

<a id="unreal.TextBlockStyle.highlight_shape"></a>

#### highlight_shape

```python
@property
def highlight_shape() -> SlateBrush
```

(SlateBrush):  [Read-Write] The shape of highlighted text

<a id="unreal.TextBlockStyle.highlight_shape"></a>

#### highlight_shape

```python
@highlight_shape.setter
def highlight_shape(value: SlateBrush) -> None
```

<a id="unreal.TextBlockStyle.strike_brush"></a>

#### strike_brush

```python
@property
def strike_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] The brush used to draw an strike through the text (if any)

<a id="unreal.TextBlockStyle.strike_brush"></a>

#### strike_brush

```python
@strike_brush.setter
def strike_brush(value: SlateBrush) -> None
```

<a id="unreal.TextBlockStyle.underline_brush"></a>

#### underline_brush

```python
@property
def underline_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] The brush used to draw an underline under the text (if any)

<a id="unreal.TextBlockStyle.underline_brush"></a>

#### underline_brush

```python
@underline_brush.setter
def underline_brush(value: SlateBrush) -> None
```

<a id="unreal.TextBlockStyle.transform_policy"></a>

#### transform_policy

```python
@property
def transform_policy() -> TextTransformPolicy
```

(TextTransformPolicy):  [Read-Write] The Text Transform Policy (defaults to None)

<a id="unreal.TextBlockStyle.transform_policy"></a>

#### transform_policy

```python
@transform_policy.setter
def transform_policy(value: TextTransformPolicy) -> None
```

<a id="unreal.TextBlockStyle.overflow_policy"></a>

#### overflow_policy

```python
@property
def overflow_policy() -> TextOverflowPolicy
```

(TextOverflowPolicy):  [Read-Write] Determines what happens to text that is clipped and doesn't fit within the clip rect of a text widget

<a id="unreal.TextBlockStyle.overflow_policy"></a>

#### overflow_policy

```python
@overflow_policy.setter
def overflow_policy(value: TextOverflowPolicy) -> None
```

<a id="unreal.InputChord"></a>