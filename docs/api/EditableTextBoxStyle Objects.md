## EditableTextBoxStyle Objects

```python
class EditableTextBoxStyle(SlateWidgetStyle)
```

Represents the appearance of an SEditableTextBox

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``background_color`` (SlateColor):  [Read-Write] The background color applied to the active background image
- ``background_image_focused`` (SlateBrush):  [Read-Write] Border background image when the box is focused
- ``background_image_hovered`` (SlateBrush):  [Read-Write] Border background image when the box is hovered
- ``background_image_normal`` (SlateBrush):  [Read-Write] Border background image when the box is not hovered or focused
- ``background_image_read_only`` (SlateBrush):  [Read-Write] Border background image when the box is read-only
- ``focused_foreground_color`` (SlateColor):  [Read-Write] The foreground color of text when the edit box has keyboard focus.
- ``foreground_color`` (SlateColor):  [Read-Write] The foreground color of text.
- ``h_scroll_bar_padding`` (Margin):  [Read-Write] Padding around the horizontal scrollbar
- ``padding`` (Margin):  [Read-Write] Padding
- ``read_only_foreground_color`` (SlateColor):  [Read-Write] The read-only foreground color of text in read-only mode.
- ``scroll_bar_style`` (ScrollBarStyle):  [Read-Write] Style used for the scrollbars
- ``text_style`` (TextBlockStyle):  [Read-Write] The style of the text block, which dictates the font, color, and shadow options. Style overrides all other properties!
- ``v_scroll_bar_padding`` (Margin):  [Read-Write] Padding around the vertical scrollbar

<a id="unreal.EditableTextBoxStyle.__init__"></a>

#### __init__

```python
def __init__(
    background_image_normal: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    background_image_hovered: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    background_image_focused: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    background_image_read_only: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
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
    ],
    foreground_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000],
                                    SlateColorStylingMode.USE_COLOR_SPECIFIED],
    background_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000],
                                    SlateColorStylingMode.USE_COLOR_SPECIFIED],
    read_only_foreground_color: SlateColor = [[
        1.000000, 0.000000, 1.000000, 1.000000
    ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
    focused_foreground_color: SlateColor = [[
        1.000000, 0.000000, 1.000000, 1.000000
    ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
    h_scroll_bar_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
    v_scroll_bar_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
    scroll_bar_style: ScrollBarStyle = [
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
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED],
         SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
         SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], 16.000000
    ]
) -> None
```

<a id="unreal.EditableTextBoxStyle.background_image_normal"></a>

#### background_image_normal

```python
@property
def background_image_normal() -> SlateBrush
```

(SlateBrush):  [Read-Write] Border background image when the box is not hovered or focused

<a id="unreal.EditableTextBoxStyle.background_image_normal"></a>

#### background_image_normal

```python
@background_image_normal.setter
def background_image_normal(value: SlateBrush) -> None
```

<a id="unreal.EditableTextBoxStyle.background_image_hovered"></a>

#### background_image_hovered

```python
@property
def background_image_hovered() -> SlateBrush
```

(SlateBrush):  [Read-Write] Border background image when the box is hovered

<a id="unreal.EditableTextBoxStyle.background_image_hovered"></a>

#### background_image_hovered

```python
@background_image_hovered.setter
def background_image_hovered(value: SlateBrush) -> None
```

<a id="unreal.EditableTextBoxStyle.background_image_focused"></a>

#### background_image_focused

```python
@property
def background_image_focused() -> SlateBrush
```

(SlateBrush):  [Read-Write] Border background image when the box is focused

<a id="unreal.EditableTextBoxStyle.background_image_focused"></a>

#### background_image_focused

```python
@background_image_focused.setter
def background_image_focused(value: SlateBrush) -> None
```

<a id="unreal.EditableTextBoxStyle.background_image_read_only"></a>

#### background_image_read_only

```python
@property
def background_image_read_only() -> SlateBrush
```

(SlateBrush):  [Read-Write] Border background image when the box is read-only

<a id="unreal.EditableTextBoxStyle.background_image_read_only"></a>

#### background_image_read_only

```python
@background_image_read_only.setter
def background_image_read_only(value: SlateBrush) -> None
```

<a id="unreal.EditableTextBoxStyle.padding"></a>

#### padding

```python
@property
def padding() -> Margin
```

(Margin):  [Read-Write] Padding

<a id="unreal.EditableTextBoxStyle.padding"></a>

#### padding

```python
@padding.setter
def padding(value: Margin) -> None
```

<a id="unreal.EditableTextBoxStyle.text_style"></a>

#### text_style

```python
@property
def text_style() -> TextBlockStyle
```

(TextBlockStyle):  [Read-Write] The style of the text block, which dictates the font, color, and shadow options. Style overrides all other properties!

<a id="unreal.EditableTextBoxStyle.text_style"></a>

#### text_style

```python
@text_style.setter
def text_style(value: TextBlockStyle) -> None
```

<a id="unreal.EditableTextBoxStyle.foreground_color"></a>

#### foreground_color

```python
@property
def foreground_color() -> SlateColor
```

(SlateColor):  [Read-Write] The foreground color of text.

<a id="unreal.EditableTextBoxStyle.foreground_color"></a>

#### foreground_color

```python
@foreground_color.setter
def foreground_color(value: SlateColor) -> None
```

<a id="unreal.EditableTextBoxStyle.background_color"></a>

#### background_color

```python
@property
def background_color() -> SlateColor
```

(SlateColor):  [Read-Write] The background color applied to the active background image

<a id="unreal.EditableTextBoxStyle.background_color"></a>

#### background_color

```python
@background_color.setter
def background_color(value: SlateColor) -> None
```

<a id="unreal.EditableTextBoxStyle.read_only_foreground_color"></a>

#### read_only_foreground_color

```python
@property
def read_only_foreground_color() -> SlateColor
```

(SlateColor):  [Read-Write] The read-only foreground color of text in read-only mode.

<a id="unreal.EditableTextBoxStyle.read_only_foreground_color"></a>

#### read_only_foreground_color

```python
@read_only_foreground_color.setter
def read_only_foreground_color(value: SlateColor) -> None
```

<a id="unreal.EditableTextBoxStyle.focused_foreground_color"></a>

#### focused_foreground_color

```python
@property
def focused_foreground_color() -> SlateColor
```

(SlateColor):  [Read-Write] The foreground color of text when the edit box has keyboard focus.

<a id="unreal.EditableTextBoxStyle.focused_foreground_color"></a>

#### focused_foreground_color

```python
@focused_foreground_color.setter
def focused_foreground_color(value: SlateColor) -> None
```

<a id="unreal.EditableTextBoxStyle.h_scroll_bar_padding"></a>

#### h_scroll_bar_padding

```python
@property
def h_scroll_bar_padding() -> Margin
```

(Margin):  [Read-Write] Padding around the horizontal scrollbar

<a id="unreal.EditableTextBoxStyle.h_scroll_bar_padding"></a>

#### h_scroll_bar_padding

```python
@h_scroll_bar_padding.setter
def h_scroll_bar_padding(value: Margin) -> None
```

<a id="unreal.EditableTextBoxStyle.v_scroll_bar_padding"></a>

#### v_scroll_bar_padding

```python
@property
def v_scroll_bar_padding() -> Margin
```

(Margin):  [Read-Write] Padding around the vertical scrollbar

<a id="unreal.EditableTextBoxStyle.v_scroll_bar_padding"></a>

#### v_scroll_bar_padding

```python
@v_scroll_bar_padding.setter
def v_scroll_bar_padding(value: Margin) -> None
```

<a id="unreal.EditableTextBoxStyle.scroll_bar_style"></a>

#### scroll_bar_style

```python
@property
def scroll_bar_style() -> ScrollBarStyle
```

(ScrollBarStyle):  [Read-Write] Style used for the scrollbars

<a id="unreal.EditableTextBoxStyle.scroll_bar_style"></a>

#### scroll_bar_style

```python
@scroll_bar_style.setter
def scroll_bar_style(value: ScrollBarStyle) -> None
```

<a id="unreal.TextBlockStyle"></a>