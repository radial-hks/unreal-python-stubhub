## HyperlinkStyle Objects

```python
class HyperlinkStyle(SlateWidgetStyle)
```

Represents the appearance of an SHyperlink

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``padding`` (Margin):  [Read-Write] Padding
- ``text_style`` (TextBlockStyle):  [Read-Write] Text style
- ``underline_style`` (ButtonStyle):  [Read-Write] Underline style

<a id="unreal.HyperlinkStyle.__init__"></a>

#### __init__

```python
def __init__(
        underline_style: ButtonStyle = [
            [[[1.000000, 1.000000, 1.000000, 1.000000],
              SlateColorStylingMode.USE_COLOR_SPECIFIED],
             SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE,
             SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
             [0.000000, 0.000000, 0.000000, 0.000000], None,
             [[0.000000, 0.000000, 0.000000, 0.000000],
              [[0.000000, 0.000000, 0.000000, 0.000000],
               SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
              SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
            [[[1.000000, 1.000000, 1.000000, 1.000000],
              SlateColorStylingMode.USE_COLOR_SPECIFIED],
             SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE,
             SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
             [0.000000, 0.000000, 0.000000, 0.000000], None,
             [[0.000000, 0.000000, 0.000000, 0.000000],
              [[0.000000, 0.000000, 0.000000, 0.000000],
               SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
              SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
            [[[1.000000, 1.000000, 1.000000, 1.000000],
              SlateColorStylingMode.USE_COLOR_SPECIFIED],
             SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE,
             SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
             [0.000000, 0.000000, 0.000000, 0.000000], None,
             [[0.000000, 0.000000, 0.000000, 0.000000],
              [[0.000000, 0.000000, 0.000000, 0.000000],
               SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
              SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
            [[[1.000000, 1.000000, 1.000000, 1.000000],
              SlateColorStylingMode.USE_COLOR_SPECIFIED],
             SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
             SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
             [0.000000, 0.000000, 0.000000, 0.000000], None,
             [[0.000000, 0.000000, 0.000000, 0.000000],
              [[0.000000, 0.000000, 0.000000, 0.000000],
               SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
              SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
            [[1.000000, 0.000000, 1.000000, 1.000000],
             SlateColorStylingMode.USE_COLOR_FOREGROUND],
            [[1.000000, 0.000000, 1.000000, 1.000000],
             SlateColorStylingMode.USE_COLOR_FOREGROUND],
            [[1.000000, 0.000000, 1.000000, 1.000000],
             SlateColorStylingMode.USE_COLOR_FOREGROUND],
            [[1.000000, 0.000000, 1.000000, 1.000000],
             SlateColorStylingMode.USE_COLOR_FOREGROUND],
            [0.000000, 0.000000, 0.000000, 0.000000],
            [0.000000, 0.000000, 0.000000, 0.000000], [None], [None]
        ],
        text_style: TextBlockStyle = [
            [
                None, None,
                [
                    0, False, False, False, None,
                    [0.000000, 0.000000, 0.000000, 1.000000]
                ], "None", 24.000000, 0, 0.000000, False, False, 1.000000
            ],
            [[1.000000, 0.000000, 1.000000, 1.000000],
             SlateColorStylingMode.USE_COLOR_SPECIFIED], [0.000000, 0.000000],
            [0.000000, 0.000000, 0.000000, 1.000000],
            [[0.000000, 0.000000, 0.000000, 1.000000],
             SlateColorStylingMode.USE_COLOR_SPECIFIED],
            [[[1.000000, 1.000000, 1.000000, 1.000000],
              SlateColorStylingMode.USE_COLOR_SPECIFIED],
             SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE,
             SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
             [0.000000, 0.000000, 0.000000, 0.000000], None,
             [[0.000000, 0.000000, 0.000000, 0.000000],
              [[0.000000, 0.000000, 0.000000, 0.000000],
               SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
              SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
            [[[1.000000, 1.000000, 1.000000, 1.000000],
              SlateColorStylingMode.USE_COLOR_SPECIFIED],
             SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE,
             SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
             [0.000000, 0.000000, 0.000000, 0.000000], None,
             [[0.000000, 0.000000, 0.000000, 0.000000],
              [[0.000000, 0.000000, 0.000000, 0.000000],
               SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
              SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
            [[[1.000000, 1.000000, 1.000000, 1.000000],
              SlateColorStylingMode.USE_COLOR_SPECIFIED],
             SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE,
             SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
             [0.000000, 0.000000, 0.000000, 0.000000], None,
             [[0.000000, 0.000000, 0.000000, 0.000000],
              [[0.000000, 0.000000, 0.000000, 0.000000],
               SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
              SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
            TextTransformPolicy.NONE, TextOverflowPolicy.CLIP
        ],
        padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.HyperlinkStyle.underline_style"></a>

#### underline_style

```python
@property
def underline_style() -> ButtonStyle
```

(ButtonStyle):  [Read-Write] Underline style

<a id="unreal.HyperlinkStyle.underline_style"></a>

#### underline_style

```python
@underline_style.setter
def underline_style(value: ButtonStyle) -> None
```

<a id="unreal.HyperlinkStyle.text_style"></a>

#### text_style

```python
@property
def text_style() -> TextBlockStyle
```

(TextBlockStyle):  [Read-Write] Text style

<a id="unreal.HyperlinkStyle.text_style"></a>

#### text_style

```python
@text_style.setter
def text_style(value: TextBlockStyle) -> None
```

<a id="unreal.HyperlinkStyle.padding"></a>

#### padding

```python
@property
def padding() -> Margin
```

(Margin):  [Read-Write] Padding

<a id="unreal.HyperlinkStyle.padding"></a>

#### padding

```python
@padding.setter
def padding(value: Margin) -> None
```

<a id="unreal.InlineEditableTextBlockStyle"></a>