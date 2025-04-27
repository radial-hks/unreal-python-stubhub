## SegmentedControlStyle Objects

```python
class SegmentedControlStyle(SlateWidgetStyle)
```

Represents the appearance of an SSegmentedControl

**C++ Source:**

- **Module**: SlateCore
- **File**: SegmentedControlStyle.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``background_brush`` (SlateBrush):  [Read-Write] Background of the segmented control
- ``control_style`` (CheckBoxStyle):  [Read-Write] The style to use for our Center Control
- ``first_control_style`` (CheckBoxStyle):  [Read-Write] The style to use for our Left Control
- ``last_control_style`` (CheckBoxStyle):  [Read-Write] The style to use for our Left Control
- ``uniform_padding`` (Margin):  [Read-Write] Padding between each control

<a id="unreal.SegmentedControlStyle.__init__"></a>

#### __init__

```python
def __init__(
    control_style: CheckBoxStyle = [
        SlateCheckBoxType.CHECK_BOX,
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
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [2.000000, 0.000000, 0.000000, 0.000000],
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
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], [None], [None], [None]
    ],
    first_control_style: CheckBoxStyle = [
        SlateCheckBoxType.CHECK_BOX,
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
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [2.000000, 0.000000, 0.000000, 0.000000],
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
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], [None], [None], [None]
    ],
    last_control_style: CheckBoxStyle = [
        SlateCheckBoxType.CHECK_BOX,
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
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [2.000000, 0.000000, 0.000000, 0.000000],
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
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], [None], [None], [None]
    ],
    background_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000],
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
    uniform_padding: Margin = [0.000000, 0.000000, 0.000000,
                               0.000000]) -> None
```

<a id="unreal.SegmentedControlStyle.control_style"></a>

#### control_style

```python
@property
def control_style() -> CheckBoxStyle
```

(CheckBoxStyle):  [Read-Write] The style to use for our Center Control

<a id="unreal.SegmentedControlStyle.control_style"></a>

#### control_style

```python
@control_style.setter
def control_style(value: CheckBoxStyle) -> None
```

<a id="unreal.SegmentedControlStyle.first_control_style"></a>

#### first_control_style

```python
@property
def first_control_style() -> CheckBoxStyle
```

(CheckBoxStyle):  [Read-Write] The style to use for our Left Control

<a id="unreal.SegmentedControlStyle.first_control_style"></a>

#### first_control_style

```python
@first_control_style.setter
def first_control_style(value: CheckBoxStyle) -> None
```

<a id="unreal.SegmentedControlStyle.last_control_style"></a>

#### last_control_style

```python
@property
def last_control_style() -> CheckBoxStyle
```

(CheckBoxStyle):  [Read-Write] The style to use for our Left Control

<a id="unreal.SegmentedControlStyle.last_control_style"></a>

#### last_control_style

```python
@last_control_style.setter
def last_control_style(value: CheckBoxStyle) -> None
```

<a id="unreal.SegmentedControlStyle.background_brush"></a>

#### background_brush

```python
@property
def background_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Background of the segmented control

<a id="unreal.SegmentedControlStyle.background_brush"></a>

#### background_brush

```python
@background_brush.setter
def background_brush(value: SlateBrush) -> None
```

<a id="unreal.SegmentedControlStyle.uniform_padding"></a>

#### uniform_padding

```python
@property
def uniform_padding() -> Margin
```

(Margin):  [Read-Write] Padding between each control

<a id="unreal.SegmentedControlStyle.uniform_padding"></a>

#### uniform_padding

```python
@uniform_padding.setter
def uniform_padding(value: Margin) -> None
```

<a id="unreal.CheckBoxStyle"></a>