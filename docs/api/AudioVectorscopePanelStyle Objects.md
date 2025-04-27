## AudioVectorscopePanelStyle Objects

```python
class AudioVectorscopePanelStyle(SlateWidgetStyle)
```

Represents the appearance of an SAudioVectorscopePanelWidget

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioVectorscopePanelStyle.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``value_grid_style`` (SampledSequenceValueGridOverlayStyle):  [Read-Write] The value grid style.
- ``vector_viewer_style`` (SampledSequenceVectorViewerStyle):  [Read-Write] The vector view style.

<a id="unreal.AudioVectorscopePanelStyle.__init__"></a>

#### __init__

```python
def __init__(
    value_grid_style: SampledSequenceValueGridOverlayStyle = [
        [[0.000000, 0.000000, 0.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], 1.000000,
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED],
        [
            None, None,
            [
                0, False, False, False, None,
                [0.000000, 0.000000, 0.000000, 1.000000]
            ], "Regular", 10.000000, 0, 0.000000, False, False, 1.000000
        ], 1280.000000, 720.000000
    ],
    vector_viewer_style: SampledSequenceVectorViewerStyle = [
        [[0.000000, 0.000000, 0.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [1.000000, 1.000000, 1.000000, 1.000000], 1.000000
    ]
) -> None
```

<a id="unreal.AudioVectorscopePanelStyle.value_grid_style"></a>

#### value_grid_style

```python
@property
def value_grid_style() -> SampledSequenceValueGridOverlayStyle
```

(SampledSequenceValueGridOverlayStyle):  [Read-Write] The value grid style.

<a id="unreal.AudioVectorscopePanelStyle.value_grid_style"></a>

#### value_grid_style

```python
@value_grid_style.setter
def value_grid_style(value: SampledSequenceValueGridOverlayStyle) -> None
```

<a id="unreal.AudioVectorscopePanelStyle.vector_viewer_style"></a>

#### vector_viewer_style

```python
@property
def vector_viewer_style() -> SampledSequenceVectorViewerStyle
```

(SampledSequenceVectorViewerStyle):  [Read-Write] The vector view style.

<a id="unreal.AudioVectorscopePanelStyle.vector_viewer_style"></a>

#### vector_viewer_style

```python
@vector_viewer_style.setter
def vector_viewer_style(value: SampledSequenceVectorViewerStyle) -> None
```

<a id="unreal.SampledSequenceVectorViewerStyle"></a>