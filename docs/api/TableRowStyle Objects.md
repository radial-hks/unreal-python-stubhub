## TableRowStyle Objects

```python
class TableRowStyle(SlateWidgetStyle)
```

Represents the appearance of an STableRow

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active_brush`` (SlateBrush):  [Read-Write] Brush used when a selected row is active
- ``active_highlighted_brush`` (SlateBrush):  [Read-Write] Brush used when a highlighted row is active
- ``active_hovered_brush`` (SlateBrush):  [Read-Write] Brush used when a selected row is active and hovered
- ``drop_indicator_above`` (SlateBrush):  [Read-Write] Brush used to provide feedback that a user can drop above the hovered row.
- ``drop_indicator_below`` (SlateBrush):  [Read-Write] Brush used to provide feedback that a user can drop below the hovered row.
- ``drop_indicator_onto`` (SlateBrush):  [Read-Write] Brush used to provide feedback that a user can drop onto the hovered row.
- ``even_row_background_brush`` (SlateBrush):  [Read-Write] Brush used when an even row is in its normal state
- ``even_row_background_hovered_brush`` (SlateBrush):  [Read-Write] Brush used when an even row is hovered
- ``inactive_brush`` (SlateBrush):  [Read-Write] Brush used when a selected row is inactive
- ``inactive_highlighted_brush`` (SlateBrush):  [Read-Write] Brush used when a highlighted row is inactive and hovered
- ``inactive_hovered_brush`` (SlateBrush):  [Read-Write] Brush used when a selected row is inactive and hovered
- ``odd_row_background_brush`` (SlateBrush):  [Read-Write] Brush to used when an odd row is in its normal state
- ``odd_row_background_hovered_brush`` (SlateBrush):  [Read-Write] Brush used when an odd row is hovered
- ``parent_row_background_brush`` (SlateBrush):  [Read-Write] Brush used for the top parent row
- ``parent_row_background_hovered_brush`` (SlateBrush):  [Read-Write] Brush used for the top parent row and row is hovered
- ``selected_text_color`` (SlateColor):  [Read-Write] Text color used for the selected row
- ``selector_focused_brush`` (SlateBrush):  [Read-Write] Brush used as a selector when a row is focused
- ``text_color`` (SlateColor):  [Read-Write] Text color used for all rows
- ``use_parent_row_brush`` (bool):  [Read-Write] If using parent row brushes

<a id="unreal.TableRowStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    selector_focused_brush: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    active_hovered_brush: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    active_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000],
                                 SlateColorStylingMode.USE_COLOR_SPECIFIED],
                                SlateBrushDrawType.IMAGE,
                                SlateBrushTileType.NO_TILE,
                                SlateBrushMirrorType.NO_MIRROR,
                                [0.000000, 0.000000],
                                [0.000000, 0.000000, 0.000000, 0.000000], None,
                                [[0.000000, 0.000000, 0.000000, 0.000000],
                                 [[0.000000, 0.000000, 0.000000, 0.000000],
                                  SlateColorStylingMode.USE_COLOR_SPECIFIED],
                                 0.000000,
                                 SlateBrushRoundingType.HALF_HEIGHT_RADIUS,
                                 False]],
    inactive_hovered_brush: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    inactive_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000],
                                   SlateColorStylingMode.USE_COLOR_SPECIFIED],
                                  SlateBrushDrawType.IMAGE,
                                  SlateBrushTileType.NO_TILE,
                                  SlateBrushMirrorType.NO_MIRROR,
                                  [0.000000, 0.000000],
                                  [0.000000, 0.000000, 0.000000,
                                   0.000000], None,
                                  [[0.000000, 0.000000, 0.000000, 0.000000],
                                   [[0.000000, 0.000000, 0.000000, 0.000000],
                                    SlateColorStylingMode.USE_COLOR_SPECIFIED],
                                   0.000000,
                                   SlateBrushRoundingType.HALF_HEIGHT_RADIUS,
                                   False]],
    use_parent_row_brush: bool = False,
    parent_row_background_brush: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    parent_row_background_hovered_brush: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    even_row_background_hovered_brush: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    even_row_background_brush: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    odd_row_background_hovered_brush: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    odd_row_background_brush: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    text_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000],
                              SlateColorStylingMode.USE_COLOR_SPECIFIED],
    selected_text_color: SlateColor = [[
        1.000000, 0.000000, 1.000000, 1.000000
    ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
    drop_indicator_above: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    drop_indicator_onto: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    drop_indicator_below: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    active_highlighted_brush: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    inactive_highlighted_brush: SlateBrush = [
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

<a id="unreal.TableRowStyle.selector_focused_brush"></a>

#### selector\_focused\_brush

```python
@property
def selector_focused_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used as a selector when a row is focused

<a id="unreal.TableRowStyle.selector_focused_brush"></a>

#### selector\_focused\_brush

```python
@selector_focused_brush.setter
def selector_focused_brush(value: SlateBrush) -> None
```

<a id="unreal.TableRowStyle.active_hovered_brush"></a>

#### active\_hovered\_brush

```python
@property
def active_hovered_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used when a selected row is active and hovered

<a id="unreal.TableRowStyle.active_hovered_brush"></a>

#### active\_hovered\_brush

```python
@active_hovered_brush.setter
def active_hovered_brush(value: SlateBrush) -> None
```

<a id="unreal.TableRowStyle.active_brush"></a>

#### active\_brush

```python
@property
def active_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used when a selected row is active

<a id="unreal.TableRowStyle.active_brush"></a>

#### active\_brush

```python
@active_brush.setter
def active_brush(value: SlateBrush) -> None
```

<a id="unreal.TableRowStyle.inactive_hovered_brush"></a>

#### inactive\_hovered\_brush

```python
@property
def inactive_hovered_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used when a selected row is inactive and hovered

<a id="unreal.TableRowStyle.inactive_hovered_brush"></a>

#### inactive\_hovered\_brush

```python
@inactive_hovered_brush.setter
def inactive_hovered_brush(value: SlateBrush) -> None
```

<a id="unreal.TableRowStyle.inactive_brush"></a>

#### inactive\_brush

```python
@property
def inactive_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used when a selected row is inactive

<a id="unreal.TableRowStyle.inactive_brush"></a>

#### inactive\_brush

```python
@inactive_brush.setter
def inactive_brush(value: SlateBrush) -> None
```

<a id="unreal.TableRowStyle.use_parent_row_brush"></a>

#### use\_parent\_row\_brush

```python
@property
def use_parent_row_brush() -> bool
```

(bool):  [Read-Write] If using parent row brushes

<a id="unreal.TableRowStyle.use_parent_row_brush"></a>

#### use\_parent\_row\_brush

```python
@use_parent_row_brush.setter
def use_parent_row_brush(value: bool) -> None
```

<a id="unreal.TableRowStyle.parent_row_background_brush"></a>

#### parent\_row\_background\_brush

```python
@property
def parent_row_background_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used for the top parent row

<a id="unreal.TableRowStyle.parent_row_background_brush"></a>

#### parent\_row\_background\_brush

```python
@parent_row_background_brush.setter
def parent_row_background_brush(value: SlateBrush) -> None
```

<a id="unreal.TableRowStyle.parent_row_background_hovered_brush"></a>

#### parent\_row\_background\_hovered\_brush

```python
@property
def parent_row_background_hovered_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used for the top parent row and row is hovered

<a id="unreal.TableRowStyle.parent_row_background_hovered_brush"></a>

#### parent\_row\_background\_hovered\_brush

```python
@parent_row_background_hovered_brush.setter
def parent_row_background_hovered_brush(value: SlateBrush) -> None
```

<a id="unreal.TableRowStyle.even_row_background_hovered_brush"></a>

#### even\_row\_background\_hovered\_brush

```python
@property
def even_row_background_hovered_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used when an even row is hovered

<a id="unreal.TableRowStyle.even_row_background_hovered_brush"></a>

#### even\_row\_background\_hovered\_brush

```python
@even_row_background_hovered_brush.setter
def even_row_background_hovered_brush(value: SlateBrush) -> None
```

<a id="unreal.TableRowStyle.even_row_background_brush"></a>

#### even\_row\_background\_brush

```python
@property
def even_row_background_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used when an even row is in its normal state

<a id="unreal.TableRowStyle.even_row_background_brush"></a>

#### even\_row\_background\_brush

```python
@even_row_background_brush.setter
def even_row_background_brush(value: SlateBrush) -> None
```

<a id="unreal.TableRowStyle.odd_row_background_hovered_brush"></a>

#### odd\_row\_background\_hovered\_brush

```python
@property
def odd_row_background_hovered_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used when an odd row is hovered

<a id="unreal.TableRowStyle.odd_row_background_hovered_brush"></a>

#### odd\_row\_background\_hovered\_brush

```python
@odd_row_background_hovered_brush.setter
def odd_row_background_hovered_brush(value: SlateBrush) -> None
```

<a id="unreal.TableRowStyle.odd_row_background_brush"></a>

#### odd\_row\_background\_brush

```python
@property
def odd_row_background_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush to used when an odd row is in its normal state

<a id="unreal.TableRowStyle.odd_row_background_brush"></a>

#### odd\_row\_background\_brush

```python
@odd_row_background_brush.setter
def odd_row_background_brush(value: SlateBrush) -> None
```

<a id="unreal.TableRowStyle.text_color"></a>

#### text\_color

```python
@property
def text_color() -> SlateColor
```

(SlateColor):  [Read-Write] Text color used for all rows

<a id="unreal.TableRowStyle.text_color"></a>

#### text\_color

```python
@text_color.setter
def text_color(value: SlateColor) -> None
```

<a id="unreal.TableRowStyle.selected_text_color"></a>

#### selected\_text\_color

```python
@property
def selected_text_color() -> SlateColor
```

(SlateColor):  [Read-Write] Text color used for the selected row

<a id="unreal.TableRowStyle.selected_text_color"></a>

#### selected\_text\_color

```python
@selected_text_color.setter
def selected_text_color(value: SlateColor) -> None
```

<a id="unreal.TableRowStyle.drop_indicator_above"></a>

#### drop\_indicator\_above

```python
@property
def drop_indicator_above() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to provide feedback that a user can drop above the hovered row.

<a id="unreal.TableRowStyle.drop_indicator_above"></a>

#### drop\_indicator\_above

```python
@drop_indicator_above.setter
def drop_indicator_above(value: SlateBrush) -> None
```

<a id="unreal.TableRowStyle.drop_indicator_onto"></a>

#### drop\_indicator\_onto

```python
@property
def drop_indicator_onto() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to provide feedback that a user can drop onto the hovered row.

<a id="unreal.TableRowStyle.drop_indicator_onto"></a>

#### drop\_indicator\_onto

```python
@drop_indicator_onto.setter
def drop_indicator_onto(value: SlateBrush) -> None
```

<a id="unreal.TableRowStyle.drop_indicator_below"></a>

#### drop\_indicator\_below

```python
@property
def drop_indicator_below() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to provide feedback that a user can drop below the hovered row.

<a id="unreal.TableRowStyle.drop_indicator_below"></a>

#### drop\_indicator\_below

```python
@drop_indicator_below.setter
def drop_indicator_below(value: SlateBrush) -> None
```

<a id="unreal.TableRowStyle.active_highlighted_brush"></a>

#### active\_highlighted\_brush

```python
@property
def active_highlighted_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used when a highlighted row is active

<a id="unreal.TableRowStyle.active_highlighted_brush"></a>

#### active\_highlighted\_brush

```python
@active_highlighted_brush.setter
def active_highlighted_brush(value: SlateBrush) -> None
```

<a id="unreal.TableRowStyle.inactive_highlighted_brush"></a>

#### inactive\_highlighted\_brush

```python
@property
def inactive_highlighted_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used when a highlighted row is inactive and hovered

<a id="unreal.TableRowStyle.inactive_highlighted_brush"></a>

#### inactive\_highlighted\_brush

```python
@inactive_highlighted_brush.setter
def inactive_highlighted_brush(value: SlateBrush) -> None
```

<a id="unreal.ComboBoxStyle"></a>