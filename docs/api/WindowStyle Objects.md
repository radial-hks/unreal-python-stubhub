## WindowStyle Objects

```python
class WindowStyle(SlateWidgetStyle)
```

Represents the appearance of an SWindow

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active_title_brush`` (SlateBrush):  [Read-Write] Brush used to draw the window title area when the window is active
- ``background_brush`` (SlateBrush):  [Read-Write] Brush used to draw the window background
- ``background_color`` (SlateColor):  [Read-Write] Color used to draw the window background
- ``border_brush`` (SlateBrush):  [Read-Write] Brush used to draw the window border
- ``border_color`` (SlateColor):  [Read-Write] Color used to draw the window border
- ``border_padding`` (Margin):  [Read-Write] Window corner rounding.  If this value is <= 0 no rounding will occur.   Used for regular, non-maximized windows only (not tool-tips or decorators.)
- ``child_background_brush`` (SlateBrush):  [Read-Write] Brush used to draw the background of child windows
- ``close_button_style`` (ButtonStyle):  [Read-Write] Style used to draw the window close button
- ``flash_title_brush`` (SlateBrush):  [Read-Write] Brush used to draw the window title area when the window is flashing
- ``inactive_title_brush`` (SlateBrush):  [Read-Write] Brush used to draw the window title area when the window is inactive
- ``maximize_button_style`` (ButtonStyle):  [Read-Write] Style used to draw the window maximize button
- ``minimize_button_style`` (ButtonStyle):  [Read-Write] Style used to draw the window minimize button
- ``outline_brush`` (SlateBrush):  [Read-Write] Brush used to draw the window outline
- ``outline_color`` (SlateColor):  [Read-Write] Color used to draw the window outline
- ``restore_button_style`` (ButtonStyle):  [Read-Write] Style used to draw the window restore button
- ``title_text_style`` (TextBlockStyle):  [Read-Write] Style used to draw the window title text
- ``window_corner_radius`` (int32):  [Read-Write] Window corner rounding.  If this value is <= 0 no rounding will occur.   Used for regular, non-maximized windows only (not tool-tips or decorators.)

<a id="unreal.WindowStyle.__init__"></a>

#### __init__

```python
def __init__(
        minimize_button_style: ButtonStyle = [
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
        maximize_button_style: ButtonStyle = [
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
        restore_button_style: ButtonStyle = [
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
        close_button_style: ButtonStyle = [
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
        title_text_style: TextBlockStyle = [
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
        active_title_brush: SlateBrush = [
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
        inactive_title_brush: SlateBrush = [
            [[1.000000, 1.000000, 1.000000, 1.000000],
             SlateColorStylingMode.USE_COLOR_SPECIFIED],
            SlateBrushDrawType.IMAGE,
            SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
            [0.000000, 0.000000], [0.000000, 0.000000, 0.000000,
                                   0.000000], None,
            [[0.000000, 0.000000, 0.000000, 0.000000],
             [[0.000000, 0.000000, 0.000000, 0.000000],
              SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
             SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
        ],
        flash_title_brush: SlateBrush = [
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
        background_color: SlateColor = [[
            1.000000, 0.000000, 1.000000, 1.000000
        ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
        outline_brush: SlateBrush = [
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
        outline_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000],
                                     SlateColorStylingMode.USE_COLOR_SPECIFIED
                                     ],
        border_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000],
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
        border_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000],
                                    SlateColorStylingMode.USE_COLOR_SPECIFIED],
        background_brush: SlateBrush = [
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
        child_background_brush: SlateBrush = [
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
        window_corner_radius: int = 0,
        border_padding: Margin = [0.000000, 0.000000, 0.000000,
                                  0.000000]) -> None
```

<a id="unreal.WindowStyle.minimize_button_style"></a>

#### minimize_button_style

```python
@property
def minimize_button_style() -> ButtonStyle
```

(ButtonStyle):  [Read-Write] Style used to draw the window minimize button

<a id="unreal.WindowStyle.minimize_button_style"></a>

#### minimize_button_style

```python
@minimize_button_style.setter
def minimize_button_style(value: ButtonStyle) -> None
```

<a id="unreal.WindowStyle.maximize_button_style"></a>

#### maximize_button_style

```python
@property
def maximize_button_style() -> ButtonStyle
```

(ButtonStyle):  [Read-Write] Style used to draw the window maximize button

<a id="unreal.WindowStyle.maximize_button_style"></a>

#### maximize_button_style

```python
@maximize_button_style.setter
def maximize_button_style(value: ButtonStyle) -> None
```

<a id="unreal.WindowStyle.restore_button_style"></a>

#### restore_button_style

```python
@property
def restore_button_style() -> ButtonStyle
```

(ButtonStyle):  [Read-Write] Style used to draw the window restore button

<a id="unreal.WindowStyle.restore_button_style"></a>

#### restore_button_style

```python
@restore_button_style.setter
def restore_button_style(value: ButtonStyle) -> None
```

<a id="unreal.WindowStyle.close_button_style"></a>

#### close_button_style

```python
@property
def close_button_style() -> ButtonStyle
```

(ButtonStyle):  [Read-Write] Style used to draw the window close button

<a id="unreal.WindowStyle.close_button_style"></a>

#### close_button_style

```python
@close_button_style.setter
def close_button_style(value: ButtonStyle) -> None
```

<a id="unreal.WindowStyle.title_text_style"></a>

#### title_text_style

```python
@property
def title_text_style() -> TextBlockStyle
```

(TextBlockStyle):  [Read-Write] Style used to draw the window title text

<a id="unreal.WindowStyle.title_text_style"></a>

#### title_text_style

```python
@title_text_style.setter
def title_text_style(value: TextBlockStyle) -> None
```

<a id="unreal.WindowStyle.active_title_brush"></a>

#### active_title_brush

```python
@property
def active_title_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to draw the window title area when the window is active

<a id="unreal.WindowStyle.active_title_brush"></a>

#### active_title_brush

```python
@active_title_brush.setter
def active_title_brush(value: SlateBrush) -> None
```

<a id="unreal.WindowStyle.inactive_title_brush"></a>

#### inactive_title_brush

```python
@property
def inactive_title_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to draw the window title area when the window is inactive

<a id="unreal.WindowStyle.inactive_title_brush"></a>

#### inactive_title_brush

```python
@inactive_title_brush.setter
def inactive_title_brush(value: SlateBrush) -> None
```

<a id="unreal.WindowStyle.flash_title_brush"></a>

#### flash_title_brush

```python
@property
def flash_title_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to draw the window title area when the window is flashing

<a id="unreal.WindowStyle.flash_title_brush"></a>

#### flash_title_brush

```python
@flash_title_brush.setter
def flash_title_brush(value: SlateBrush) -> None
```

<a id="unreal.WindowStyle.background_color"></a>

#### background_color

```python
@property
def background_color() -> SlateColor
```

(SlateColor):  [Read-Write] Color used to draw the window background

<a id="unreal.WindowStyle.background_color"></a>

#### background_color

```python
@background_color.setter
def background_color(value: SlateColor) -> None
```

<a id="unreal.WindowStyle.outline_brush"></a>

#### outline_brush

```python
@property
def outline_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to draw the window outline

<a id="unreal.WindowStyle.outline_brush"></a>

#### outline_brush

```python
@outline_brush.setter
def outline_brush(value: SlateBrush) -> None
```

<a id="unreal.WindowStyle.outline_color"></a>

#### outline_color

```python
@property
def outline_color() -> SlateColor
```

(SlateColor):  [Read-Write] Color used to draw the window outline

<a id="unreal.WindowStyle.outline_color"></a>

#### outline_color

```python
@outline_color.setter
def outline_color(value: SlateColor) -> None
```

<a id="unreal.WindowStyle.border_brush"></a>

#### border_brush

```python
@property
def border_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to draw the window border

<a id="unreal.WindowStyle.border_brush"></a>

#### border_brush

```python
@border_brush.setter
def border_brush(value: SlateBrush) -> None
```

<a id="unreal.WindowStyle.border_color"></a>

#### border_color

```python
@property
def border_color() -> SlateColor
```

(SlateColor):  [Read-Write] Color used to draw the window border

<a id="unreal.WindowStyle.border_color"></a>

#### border_color

```python
@border_color.setter
def border_color(value: SlateColor) -> None
```

<a id="unreal.WindowStyle.background_brush"></a>

#### background_brush

```python
@property
def background_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to draw the window background

<a id="unreal.WindowStyle.background_brush"></a>

#### background_brush

```python
@background_brush.setter
def background_brush(value: SlateBrush) -> None
```

<a id="unreal.WindowStyle.child_background_brush"></a>

#### child_background_brush

```python
@property
def child_background_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to draw the background of child windows

<a id="unreal.WindowStyle.child_background_brush"></a>

#### child_background_brush

```python
@child_background_brush.setter
def child_background_brush(value: SlateBrush) -> None
```

<a id="unreal.WindowStyle.window_corner_radius"></a>

#### window_corner_radius

```python
@property
def window_corner_radius() -> int
```

(int32):  [Read-Write] Window corner rounding.  If this value is <= 0 no rounding will occur.   Used for regular, non-maximized windows only (not tool-tips or decorators.)

<a id="unreal.WindowStyle.window_corner_radius"></a>

#### window_corner_radius

```python
@window_corner_radius.setter
def window_corner_radius(value: int) -> None
```

<a id="unreal.WindowStyle.border_padding"></a>

#### border_padding

```python
@property
def border_padding() -> Margin
```

(Margin):  [Read-Write] Window corner rounding.  If this value is <= 0 no rounding will occur.   Used for regular, non-maximized windows only (not tool-tips or decorators.)

<a id="unreal.WindowStyle.border_padding"></a>

#### border_padding

```python
@border_padding.setter
def border_padding(value: Margin) -> None
```

<a id="unreal.ToolBarStyle"></a>