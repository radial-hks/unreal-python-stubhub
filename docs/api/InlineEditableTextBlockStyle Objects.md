## InlineEditableTextBlockStyle Objects

```python
class InlineEditableTextBlockStyle(SlateWidgetStyle)
```

Represents the appearance of an SInlineEditableTextBlock

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``editable_text_box_style`` (EditableTextBoxStyle):  [Read-Write] The style of the editable text box, which dictates the font, color, and shadow options.
- ``text_style`` (TextBlockStyle):  [Read-Write] The style of the text block, which dictates the font, color, and shadow options. Style overrides all other properties!

<a id="unreal.InlineEditableTextBlockStyle.__init__"></a>

#### __init__

```python
def __init__(
    editable_text_box_style: EditableTextBoxStyle = [
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [4.000000, 2.000000, 4.000000, 2.000000],
        [[
            None, None,
            [
                0, False, False, False, None,
                [0.000000, 0.000000, 0.000000, 1.000000]
            ], "Regular", 9.000000, 0, 0.000000, False, False, 1.000000
        ],
         [[1.000000, 0.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_FOREGROUND], [0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000, 1.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000], 0],
         [[[0.000000, 0.000000, 0.000000, 0.000000],
           0], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE,
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
         TextTransformPolicy.NONE, TextOverflowPolicy.CLIP],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [0.000000, 0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000, 0.000000],
        [[[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
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
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
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
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
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
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
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
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], 16.000000]
    ],
    text_style: TextBlockStyle = [
        [
            None, None,
            [
                0, False, False, False, None,
                [0.000000, 0.000000, 0.000000, 1.000000]
            ], "None", 24.000000, 0, 0.000000, False, False, 1.000000
        ],
        [[1.000000, 0.000000, 1.000000,
          1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED],
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 1.000000],
        [[0.000000, 0.000000, 0.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        TextTransformPolicy.NONE, TextOverflowPolicy.CLIP
    ]
) -> None
```

<a id="unreal.InlineEditableTextBlockStyle.editable_text_box_style"></a>

#### editable_text_box_style

```python
@property
def editable_text_box_style() -> EditableTextBoxStyle
```

(EditableTextBoxStyle):  [Read-Write] The style of the editable text box, which dictates the font, color, and shadow options.

<a id="unreal.InlineEditableTextBlockStyle.editable_text_box_style"></a>

#### editable_text_box_style

```python
@editable_text_box_style.setter
def editable_text_box_style(value: EditableTextBoxStyle) -> None
```

<a id="unreal.InlineEditableTextBlockStyle.text_style"></a>

#### text_style

```python
@property
def text_style() -> TextBlockStyle
```

(TextBlockStyle):  [Read-Write] The style of the text block, which dictates the font, color, and shadow options. Style overrides all other properties!

<a id="unreal.InlineEditableTextBlockStyle.text_style"></a>

#### text_style

```python
@text_style.setter
def text_style(value: TextBlockStyle) -> None
```

<a id="unreal.ProgressBarStyle"></a>