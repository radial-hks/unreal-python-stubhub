## SampledSequenceVectorViewerStyle Objects

```python
class SampledSequenceVectorViewerStyle(SlateWidgetStyle)
```

Represents the appearance of a trigger threshold line

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: SampledSequenceVectorViewerStyle.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``background_brush`` (SlateBrush):  [Read-Write]
- ``background_color`` (SlateColor):  [Read-Write] The background color.
- ``line_color`` (LinearColor):  [Read-Write] The vector view line color.
- ``line_thickness`` (float):  [Read-Write] The vector view line thickness.

<a id="unreal.SampledSequenceVectorViewerStyle.__init__"></a>

#### __init__

```python
def __init__(background_color: SlateColor = [[
    1.000000, 0.000000, 1.000000, 1.000000
], SlateColorStylingMode.USE_COLOR_SPECIFIED],
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
             line_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             line_thickness: float = 0.000000) -> None
```

<a id="unreal.SampledSequenceVectorViewerStyle.background_color"></a>

#### background_color

```python
@property
def background_color() -> SlateColor
```

(SlateColor):  [Read-Write] The background color.

<a id="unreal.SampledSequenceVectorViewerStyle.background_color"></a>

#### background_color

```python
@background_color.setter
def background_color(value: SlateColor) -> None
```

<a id="unreal.SampledSequenceVectorViewerStyle.background_brush"></a>

#### background_brush

```python
@property
def background_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write]

<a id="unreal.SampledSequenceVectorViewerStyle.background_brush"></a>

#### background_brush

```python
@background_brush.setter
def background_brush(value: SlateBrush) -> None
```

<a id="unreal.SampledSequenceVectorViewerStyle.line_color"></a>

#### line_color

```python
@property
def line_color() -> LinearColor
```

(LinearColor):  [Read-Write] The vector view line color.

<a id="unreal.SampledSequenceVectorViewerStyle.line_color"></a>

#### line_color

```python
@line_color.setter
def line_color(value: LinearColor) -> None
```

<a id="unreal.SampledSequenceVectorViewerStyle.line_thickness"></a>

#### line_thickness

```python
@property
def line_thickness() -> float
```

(float):  [Read-Write] The vector view line thickness.

<a id="unreal.SampledSequenceVectorViewerStyle.line_thickness"></a>

#### line_thickness

```python
@line_thickness.setter
def line_thickness(value: float) -> None
```

<a id="unreal.AudioMaterialEnvelopeSettings"></a>