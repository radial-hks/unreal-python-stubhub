## ScrollBoxStyle Objects

```python
class ScrollBoxStyle(SlateWidgetStyle)
```

Represents the appearance of an SScrollBox

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bar_thickness`` (float):  [Read-Write]
- ``bottom_shadow_brush`` (SlateBrush):  [Read-Write] Brush used to draw the bottom shadow of a scrollbox
- ``horizontal_scrolled_content_padding`` (Margin):  [Read-Write] Padding scroll panel that presents the scrolled content
- ``left_shadow_brush`` (SlateBrush):  [Read-Write] Brush used to draw the left shadow of a scrollbox
- ``right_shadow_brush`` (SlateBrush):  [Read-Write] Brush used to draw the right shadow of a scrollbox
- ``top_shadow_brush`` (SlateBrush):  [Read-Write] Brush used to draw the top shadow of a scrollbox
- ``vertical_scrolled_content_padding`` (Margin):  [Read-Write] Padding scroll panel that presents the scrolled content

<a id="unreal.ScrollBoxStyle.__init__"></a>

#### __init__

```python
def __init__(
    bar_thickness: float = 0.000000,
    top_shadow_brush: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    bottom_shadow_brush: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    left_shadow_brush: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    right_shadow_brush: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    horizontal_scrolled_content_padding: Margin = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    vertical_scrolled_content_padding: Margin = [
        0.000000, 0.000000, 0.000000, 0.000000
    ]
) -> None
```

<a id="unreal.ScrollBoxStyle.bar_thickness"></a>

#### bar_thickness

```python
@property
def bar_thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.ScrollBoxStyle.bar_thickness"></a>

#### bar_thickness

```python
@bar_thickness.setter
def bar_thickness(value: float) -> None
```

<a id="unreal.ScrollBoxStyle.top_shadow_brush"></a>

#### top_shadow_brush

```python
@property
def top_shadow_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to draw the top shadow of a scrollbox

<a id="unreal.ScrollBoxStyle.top_shadow_brush"></a>

#### top_shadow_brush

```python
@top_shadow_brush.setter
def top_shadow_brush(value: SlateBrush) -> None
```

<a id="unreal.ScrollBoxStyle.bottom_shadow_brush"></a>

#### bottom_shadow_brush

```python
@property
def bottom_shadow_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to draw the bottom shadow of a scrollbox

<a id="unreal.ScrollBoxStyle.bottom_shadow_brush"></a>

#### bottom_shadow_brush

```python
@bottom_shadow_brush.setter
def bottom_shadow_brush(value: SlateBrush) -> None
```

<a id="unreal.ScrollBoxStyle.left_shadow_brush"></a>

#### left_shadow_brush

```python
@property
def left_shadow_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to draw the left shadow of a scrollbox

<a id="unreal.ScrollBoxStyle.left_shadow_brush"></a>

#### left_shadow_brush

```python
@left_shadow_brush.setter
def left_shadow_brush(value: SlateBrush) -> None
```

<a id="unreal.ScrollBoxStyle.right_shadow_brush"></a>

#### right_shadow_brush

```python
@property
def right_shadow_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to draw the right shadow of a scrollbox

<a id="unreal.ScrollBoxStyle.right_shadow_brush"></a>

#### right_shadow_brush

```python
@right_shadow_brush.setter
def right_shadow_brush(value: SlateBrush) -> None
```

<a id="unreal.ScrollBoxStyle.horizontal_scrolled_content_padding"></a>

#### horizontal_scrolled_content_padding

```python
@property
def horizontal_scrolled_content_padding() -> Margin
```

(Margin):  [Read-Write] Padding scroll panel that presents the scrolled content

<a id="unreal.ScrollBoxStyle.horizontal_scrolled_content_padding"></a>

#### horizontal_scrolled_content_padding

```python
@horizontal_scrolled_content_padding.setter
def horizontal_scrolled_content_padding(value: Margin) -> None
```

<a id="unreal.ScrollBoxStyle.vertical_scrolled_content_padding"></a>

#### vertical_scrolled_content_padding

```python
@property
def vertical_scrolled_content_padding() -> Margin
```

(Margin):  [Read-Write] Padding scroll panel that presents the scrolled content

<a id="unreal.ScrollBoxStyle.vertical_scrolled_content_padding"></a>

#### vertical_scrolled_content_padding

```python
@vertical_scrolled_content_padding.setter
def vertical_scrolled_content_padding(value: Margin) -> None
```

<a id="unreal.ScrollBorderStyle"></a>