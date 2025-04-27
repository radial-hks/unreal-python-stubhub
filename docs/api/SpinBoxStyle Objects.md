## SpinBoxStyle Objects

```python
class SpinBoxStyle(SlateWidgetStyle)
```

Represents the appearance of an SSpinBox

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active_background_brush`` (SlateBrush):  [Read-Write]
- ``active_fill_brush`` (SlateBrush):  [Read-Write] Brush used to fill the spinbox when it's active
- ``arrows_image`` (SlateBrush):  [Read-Write] Image used to draw the spinbox arrows
- ``background_brush`` (SlateBrush):  [Read-Write] Brush used to draw the background of the spinbox
- ``hovered_background_brush`` (SlateBrush):  [Read-Write] Brush used to draw the background of the spinbox when it's hovered over
- ``hovered_fill_brush`` (SlateBrush):  [Read-Write] Brush used to fill the spinbox when it's hovered and not active
- ``inactive_fill_brush`` (SlateBrush):  [Read-Write] Brush used to fill the spinbox when it's inactive
- ``inset_padding`` (Margin):  [Read-Write] Padding between the background brush and the fill brush
- ``text_padding`` (Margin):  [Read-Write] Padding to add around the spinbox and its text

<a id="unreal.SpinBoxStyle.__init__"></a>

#### __init__

```python
def __init__(
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
        active_background_brush: SlateBrush = [
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
        hovered_background_brush: SlateBrush = [
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
        active_fill_brush: SlateBrush = [
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
        hovered_fill_brush: SlateBrush = [
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
        inactive_fill_brush: SlateBrush = [
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
        arrows_image: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000],
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
        text_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
        inset_padding: Margin = [0.000000, 0.000000, 0.000000,
                                 0.000000]) -> None
```

<a id="unreal.SpinBoxStyle.background_brush"></a>

#### background_brush

```python
@property
def background_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to draw the background of the spinbox

<a id="unreal.SpinBoxStyle.background_brush"></a>

#### background_brush

```python
@background_brush.setter
def background_brush(value: SlateBrush) -> None
```

<a id="unreal.SpinBoxStyle.active_background_brush"></a>

#### active_background_brush

```python
@property
def active_background_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write]

<a id="unreal.SpinBoxStyle.active_background_brush"></a>

#### active_background_brush

```python
@active_background_brush.setter
def active_background_brush(value: SlateBrush) -> None
```

<a id="unreal.SpinBoxStyle.hovered_background_brush"></a>

#### hovered_background_brush

```python
@property
def hovered_background_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to draw the background of the spinbox when it's hovered over

<a id="unreal.SpinBoxStyle.hovered_background_brush"></a>

#### hovered_background_brush

```python
@hovered_background_brush.setter
def hovered_background_brush(value: SlateBrush) -> None
```

<a id="unreal.SpinBoxStyle.active_fill_brush"></a>

#### active_fill_brush

```python
@property
def active_fill_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to fill the spinbox when it's active

<a id="unreal.SpinBoxStyle.active_fill_brush"></a>

#### active_fill_brush

```python
@active_fill_brush.setter
def active_fill_brush(value: SlateBrush) -> None
```

<a id="unreal.SpinBoxStyle.hovered_fill_brush"></a>

#### hovered_fill_brush

```python
@property
def hovered_fill_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to fill the spinbox when it's hovered and not active

<a id="unreal.SpinBoxStyle.hovered_fill_brush"></a>

#### hovered_fill_brush

```python
@hovered_fill_brush.setter
def hovered_fill_brush(value: SlateBrush) -> None
```

<a id="unreal.SpinBoxStyle.inactive_fill_brush"></a>

#### inactive_fill_brush

```python
@property
def inactive_fill_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to fill the spinbox when it's inactive

<a id="unreal.SpinBoxStyle.inactive_fill_brush"></a>

#### inactive_fill_brush

```python
@inactive_fill_brush.setter
def inactive_fill_brush(value: SlateBrush) -> None
```

<a id="unreal.SpinBoxStyle.arrows_image"></a>

#### arrows_image

```python
@property
def arrows_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image used to draw the spinbox arrows

<a id="unreal.SpinBoxStyle.arrows_image"></a>

#### arrows_image

```python
@arrows_image.setter
def arrows_image(value: SlateBrush) -> None
```

<a id="unreal.SpinBoxStyle.text_padding"></a>

#### text_padding

```python
@property
def text_padding() -> Margin
```

(Margin):  [Read-Write] Padding to add around the spinbox and its text

<a id="unreal.SpinBoxStyle.text_padding"></a>

#### text_padding

```python
@text_padding.setter
def text_padding(value: Margin) -> None
```

<a id="unreal.SpinBoxStyle.inset_padding"></a>

#### inset_padding

```python
@property
def inset_padding() -> Margin
```

(Margin):  [Read-Write] Padding between the background brush and the fill brush

<a id="unreal.SpinBoxStyle.inset_padding"></a>

#### inset_padding

```python
@inset_padding.setter
def inset_padding(value: Margin) -> None
```

<a id="unreal.PaintContext"></a>