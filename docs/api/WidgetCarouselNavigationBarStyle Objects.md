## WidgetCarouselNavigationBarStyle Objects

```python
class WidgetCarouselNavigationBarStyle(SlateWidgetStyle)
```

Widget Carousel Navigation Bar Style

**C++ Source:**

- **Module**: WidgetCarousel
- **File**: WidgetCarouselStyle.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``center_button_style`` (ButtonStyle):  [Read-Write]
- ``highlight_brush`` (SlateBrush):  [Read-Write]
- ``left_button_style`` (ButtonStyle):  [Read-Write]
- ``right_button_style`` (ButtonStyle):  [Read-Write]

<a id="unreal.WidgetCarouselNavigationBarStyle.__init__"></a>

#### __init__

```python
def __init__(
    highlight_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000],
                                    SlateColorStylingMode.USE_COLOR_SPECIFIED],
                                   SlateBrushDrawType.IMAGE,
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
    left_button_style: ButtonStyle = [
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
    center_button_style: ButtonStyle = [
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
    right_button_style: ButtonStyle = [
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
    ]
) -> None
```

<a id="unreal.WidgetCarouselNavigationBarStyle.highlight_brush"></a>

#### highlight_brush

```python
@property
def highlight_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write]

<a id="unreal.WidgetCarouselNavigationBarStyle.highlight_brush"></a>

#### highlight_brush

```python
@highlight_brush.setter
def highlight_brush(value: SlateBrush) -> None
```

<a id="unreal.WidgetCarouselNavigationBarStyle.left_button_style"></a>

#### left_button_style

```python
@property
def left_button_style() -> ButtonStyle
```

(ButtonStyle):  [Read-Write]

<a id="unreal.WidgetCarouselNavigationBarStyle.left_button_style"></a>

#### left_button_style

```python
@left_button_style.setter
def left_button_style(value: ButtonStyle) -> None
```

<a id="unreal.WidgetCarouselNavigationBarStyle.center_button_style"></a>

#### center_button_style

```python
@property
def center_button_style() -> ButtonStyle
```

(ButtonStyle):  [Read-Write]

<a id="unreal.WidgetCarouselNavigationBarStyle.center_button_style"></a>

#### center_button_style

```python
@center_button_style.setter
def center_button_style(value: ButtonStyle) -> None
```

<a id="unreal.WidgetCarouselNavigationBarStyle.right_button_style"></a>

#### right_button_style

```python
@property
def right_button_style() -> ButtonStyle
```

(ButtonStyle):  [Read-Write]

<a id="unreal.WidgetCarouselNavigationBarStyle.right_button_style"></a>

#### right_button_style

```python
@right_button_style.setter
def right_button_style(value: ButtonStyle) -> None
```

<a id="unreal.VREditorFloatingUICreationContext"></a>