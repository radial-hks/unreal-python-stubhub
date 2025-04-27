## SplitterStyle Objects

```python
class SplitterStyle(SlateWidgetStyle)
```

Represents the appearance of an SSplitter

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``handle_highlight_brush`` (SlateBrush):  [Read-Write] Brush used to draw the handle in its highlight state
- ``handle_normal_brush`` (SlateBrush):  [Read-Write] Brush used to draw the handle in its normal state

<a id="unreal.SplitterStyle.__init__"></a>

#### __init__

```python
def __init__(
    handle_normal_brush: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    handle_highlight_brush: SlateBrush = [
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

<a id="unreal.SplitterStyle.handle_normal_brush"></a>

#### handle_normal_brush

```python
@property
def handle_normal_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to draw the handle in its normal state

<a id="unreal.SplitterStyle.handle_normal_brush"></a>

#### handle_normal_brush

```python
@handle_normal_brush.setter
def handle_normal_brush(value: SlateBrush) -> None
```

<a id="unreal.SplitterStyle.handle_highlight_brush"></a>

#### handle_highlight_brush

```python
@property
def handle_highlight_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used to draw the handle in its highlight state

<a id="unreal.SplitterStyle.handle_highlight_brush"></a>

#### handle_highlight_brush

```python
@handle_highlight_brush.setter
def handle_highlight_brush(value: SlateBrush) -> None
```

<a id="unreal.TableViewStyle"></a>