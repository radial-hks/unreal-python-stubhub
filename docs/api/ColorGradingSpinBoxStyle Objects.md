## ColorGradingSpinBoxStyle Objects

```python
class ColorGradingSpinBoxStyle(SlateWidgetStyle)
```

Represents the appearance of a color grading spin box

**C++ Source:**

- **Module**: AdvancedWidgets
- **File**: ColorGradingSpinBoxStyle.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active_border_brush`` (SlateBrush):  [Read-Write] Brush used to draw the border of the spinbox when it's in active use by the user
- ``border_brush`` (SlateBrush):  [Read-Write] Brush used to draw the border of the spinbox
- ``hovered_border_brush`` (SlateBrush):  [Read-Write] Brush used to draw the border of the spinbox when it's hovered over
- ``selector_brush`` (SlateBrush):  [Read-Write] Brush used to draw the selector indicating the current value
- ``selector_width`` (float):  [Read-Write] Width of the selector

<a id="unreal.ColorGradingSpinBoxStyle.__init__"></a>

#### __init__

```python
def __init__(border_brush: SlateBrush = [
    [[1.000000, 1.000000, 1.000000, 1.000000],
     SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
    SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
    [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
    [[0.000000, 0.000000, 0.000000, 0.000000],
     [[0.000000, 0.000000, 0.000000, 0.000000],
      SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
     SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
],
             active_border_brush: SlateBrush = [
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
             hovered_border_brush: SlateBrush = [
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
             selector_brush: SlateBrush = [
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
             selector_width: float = 0.000000) -> None
```

<a id="unreal.ColorGradingSpinBoxStyle.border_brush"></a>

#### border_brush

```python
@property
def border_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to draw the border of the spinbox

<a id="unreal.ColorGradingSpinBoxStyle.border_brush"></a>

#### border_brush

```python
@border_brush.setter
def border_brush(value: SlateBrush) -> None
```

<a id="unreal.ColorGradingSpinBoxStyle.active_border_brush"></a>

#### active_border_brush

```python
@property
def active_border_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to draw the border of the spinbox when it's in active use by the user

<a id="unreal.ColorGradingSpinBoxStyle.active_border_brush"></a>

#### active_border_brush

```python
@active_border_brush.setter
def active_border_brush(value: SlateBrush) -> None
```

<a id="unreal.ColorGradingSpinBoxStyle.hovered_border_brush"></a>

#### hovered_border_brush

```python
@property
def hovered_border_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to draw the border of the spinbox when it's hovered over

<a id="unreal.ColorGradingSpinBoxStyle.hovered_border_brush"></a>

#### hovered_border_brush

```python
@hovered_border_brush.setter
def hovered_border_brush(value: SlateBrush) -> None
```

<a id="unreal.ColorGradingSpinBoxStyle.selector_brush"></a>

#### selector_brush

```python
@property
def selector_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to draw the selector indicating the current value

<a id="unreal.ColorGradingSpinBoxStyle.selector_brush"></a>

#### selector_brush

```python
@selector_brush.setter
def selector_brush(value: SlateBrush) -> None
```

<a id="unreal.ColorGradingSpinBoxStyle.selector_width"></a>

#### selector_width

```python
@property
def selector_width() -> float
```

(float):  [Read-Write] Width of the selector

<a id="unreal.ColorGradingSpinBoxStyle.selector_width"></a>

#### selector_width

```python
@selector_width.setter
def selector_width(value: float) -> None
```

<a id="unreal.SubobjectData"></a>