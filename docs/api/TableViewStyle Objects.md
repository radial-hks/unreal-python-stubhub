## TableViewStyle Objects

```python
class TableViewStyle(SlateWidgetStyle)
```

Represents the appearance of an STableView

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``background_brush`` (SlateBrush):  [Read-Write] Brush used when a selected row is active

<a id="unreal.TableViewStyle.__init__"></a>

#### __init__

```python
def __init__(
    background_brush: SlateBrush = [
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

<a id="unreal.TableViewStyle.background_brush"></a>

#### background_brush

```python
@property
def background_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush used when a selected row is active

<a id="unreal.TableViewStyle.background_brush"></a>

#### background_brush

```python
@background_brush.setter
def background_brush(value: SlateBrush) -> None
```

<a id="unreal.ScrollBoxStyle"></a>