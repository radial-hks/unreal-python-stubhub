## SampledSequenceViewerStyle Objects

```python
class SampledSequenceViewerStyle(SlateWidgetStyle)
```

Represents the appearance of a Sampled Sequence Viewer

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioWidgetsSlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``background_brush`` (SlateBrush):  [Read-Write]
- ``desired_height`` (float):  [Read-Write]
- ``desired_width`` (float):  [Read-Write]
- ``major_grid_line_color`` (SlateColor):  [Read-Write]
- ``minor_grid_line_color`` (SlateColor):  [Read-Write]
- ``sample_markers_size`` (float):  [Read-Write]
- ``sequence_background_color`` (SlateColor):  [Read-Write]
- ``sequence_color`` (SlateColor):  [Read-Write]
- ``sequence_line_thickness`` (float):  [Read-Write]
- ``zero_crossing_line_color`` (SlateColor):  [Read-Write]
- ``zero_crossing_line_thickness`` (float):  [Read-Write]

<a id="unreal.SampledSequenceViewerStyle.__init__"></a>

#### __init__

```python
def __init__(sequence_color: SlateColor = [[
    1.000000, 0.000000, 1.000000, 1.000000
], SlateColorStylingMode.USE_COLOR_SPECIFIED],
             sequence_line_thickness: float = 0.000000,
             major_grid_line_color: SlateColor = [[
                 1.000000, 0.000000, 1.000000, 1.000000
             ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
             minor_grid_line_color: SlateColor = [[
                 1.000000, 0.000000, 1.000000, 1.000000
             ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
             zero_crossing_line_color: SlateColor = [[
                 1.000000, 0.000000, 1.000000, 1.000000
             ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
             zero_crossing_line_thickness: float = 0.000000,
             sample_markers_size: float = 0.000000,
             sequence_background_color: SlateColor = [[
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
             desired_width: float = 0.000000,
             desired_height: float = 0.000000) -> None
```

<a id="unreal.SampledSequenceViewerStyle.sequence_color"></a>

#### sequence_color

```python
@property
def sequence_color() -> SlateColor
```

(SlateColor):  [Read-Write]

<a id="unreal.SampledSequenceViewerStyle.sequence_color"></a>

#### sequence_color

```python
@sequence_color.setter
def sequence_color(value: SlateColor) -> None
```

<a id="unreal.SampledSequenceViewerStyle.sequence_line_thickness"></a>

#### sequence_line_thickness

```python
@property
def sequence_line_thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.SampledSequenceViewerStyle.sequence_line_thickness"></a>

#### sequence_line_thickness

```python
@sequence_line_thickness.setter
def sequence_line_thickness(value: float) -> None
```

<a id="unreal.SampledSequenceViewerStyle.major_grid_line_color"></a>

#### major_grid_line_color

```python
@property
def major_grid_line_color() -> SlateColor
```

(SlateColor):  [Read-Write]

<a id="unreal.SampledSequenceViewerStyle.major_grid_line_color"></a>

#### major_grid_line_color

```python
@major_grid_line_color.setter
def major_grid_line_color(value: SlateColor) -> None
```

<a id="unreal.SampledSequenceViewerStyle.minor_grid_line_color"></a>

#### minor_grid_line_color

```python
@property
def minor_grid_line_color() -> SlateColor
```

(SlateColor):  [Read-Write]

<a id="unreal.SampledSequenceViewerStyle.minor_grid_line_color"></a>

#### minor_grid_line_color

```python
@minor_grid_line_color.setter
def minor_grid_line_color(value: SlateColor) -> None
```

<a id="unreal.SampledSequenceViewerStyle.zero_crossing_line_color"></a>

#### zero_crossing_line_color

```python
@property
def zero_crossing_line_color() -> SlateColor
```

(SlateColor):  [Read-Write]

<a id="unreal.SampledSequenceViewerStyle.zero_crossing_line_color"></a>

#### zero_crossing_line_color

```python
@zero_crossing_line_color.setter
def zero_crossing_line_color(value: SlateColor) -> None
```

<a id="unreal.SampledSequenceViewerStyle.zero_crossing_line_thickness"></a>

#### zero_crossing_line_thickness

```python
@property
def zero_crossing_line_thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.SampledSequenceViewerStyle.zero_crossing_line_thickness"></a>

#### zero_crossing_line_thickness

```python
@zero_crossing_line_thickness.setter
def zero_crossing_line_thickness(value: float) -> None
```

<a id="unreal.SampledSequenceViewerStyle.sample_markers_size"></a>

#### sample_markers_size

```python
@property
def sample_markers_size() -> float
```

(float):  [Read-Write]

<a id="unreal.SampledSequenceViewerStyle.sample_markers_size"></a>

#### sample_markers_size

```python
@sample_markers_size.setter
def sample_markers_size(value: float) -> None
```

<a id="unreal.SampledSequenceViewerStyle.sequence_background_color"></a>

#### sequence_background_color

```python
@property
def sequence_background_color() -> SlateColor
```

(SlateColor):  [Read-Write]

<a id="unreal.SampledSequenceViewerStyle.sequence_background_color"></a>

#### sequence_background_color

```python
@sequence_background_color.setter
def sequence_background_color(value: SlateColor) -> None
```

<a id="unreal.SampledSequenceViewerStyle.background_brush"></a>

#### background_brush

```python
@property
def background_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write]

<a id="unreal.SampledSequenceViewerStyle.background_brush"></a>

#### background_brush

```python
@background_brush.setter
def background_brush(value: SlateBrush) -> None
```

<a id="unreal.SampledSequenceViewerStyle.desired_width"></a>

#### desired_width

```python
@property
def desired_width() -> float
```

(float):  [Read-Write]

<a id="unreal.SampledSequenceViewerStyle.desired_width"></a>

#### desired_width

```python
@desired_width.setter
def desired_width(value: float) -> None
```

<a id="unreal.SampledSequenceViewerStyle.desired_height"></a>

#### desired_height

```python
@property
def desired_height() -> float
```

(float):  [Read-Write]

<a id="unreal.SampledSequenceViewerStyle.desired_height"></a>

#### desired_height

```python
@desired_height.setter
def desired_height(value: float) -> None
```

<a id="unreal.SampledSequenceValueGridOverlayStyle"></a>