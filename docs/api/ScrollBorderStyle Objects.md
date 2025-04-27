## ScrollBorderStyle Objects

```python
class ScrollBorderStyle(SlateWidgetStyle)
```

Represents the appearance of an FScrollBorderStyle

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bottom_shadow_brush`` (SlateBrush):  [Read-Write] Brush used to draw the bottom shadow of a scrollborder
- ``top_shadow_brush`` (SlateBrush):  [Read-Write] Brush used to draw the top shadow of a scrollborder

<a id="unreal.ScrollBorderStyle.__init__"></a>

#### __init__

```python
def __init__(
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
    ]
) -> None
```

<a id="unreal.ScrollBorderStyle.top_shadow_brush"></a>

#### top_shadow_brush

```python
@property
def top_shadow_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to draw the top shadow of a scrollborder

<a id="unreal.ScrollBorderStyle.top_shadow_brush"></a>

#### top_shadow_brush

```python
@top_shadow_brush.setter
def top_shadow_brush(value: SlateBrush) -> None
```

<a id="unreal.ScrollBorderStyle.bottom_shadow_brush"></a>

#### bottom_shadow_brush

```python
@property
def bottom_shadow_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to draw the bottom shadow of a scrollborder

<a id="unreal.ScrollBorderStyle.bottom_shadow_brush"></a>

#### bottom_shadow_brush

```python
@bottom_shadow_brush.setter
def bottom_shadow_brush(value: SlateBrush) -> None
```

<a id="unreal.WindowStyle"></a>