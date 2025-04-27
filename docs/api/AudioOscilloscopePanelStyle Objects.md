## AudioOscilloscopePanelStyle Objects

```python
class AudioOscilloscopePanelStyle(SlateWidgetStyle)
```

Represents the appearance of an SAudioOscilloscopePanelWidget

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioOscilloscopePanelStyle.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``time_ruler_style`` (FixedSampleSequenceRulerStyle):  [Read-Write] The time rule style.
- ``trigger_threshold_line_style`` (TriggerThresholdLineStyle):  [Read-Write] The triggerthreshold line style.
- ``value_grid_style`` (SampledSequenceValueGridOverlayStyle):  [Read-Write] The value grid style.
- ``wave_viewer_style`` (SampledSequenceViewerStyle):  [Read-Write] The waveform view style.

<a id="unreal.AudioOscilloscopePanelStyle.__init__"></a>

#### __init__

```python
def __init__(
    time_ruler_style: FixedSampleSequenceRulerStyle = [
        15.000000,
        [[255.000000, 0.100000, 0.200000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[1.000000, 1.000000, 1.000000, 0.900000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED],
        [[1.000000, 1.000000, 1.000000, 0.900000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED],
        [
            None, None,
            [
                0, False, False, False, None,
                [0.000000, 0.000000, 0.000000, 1.000000]
            ], "Regular", 10.000000, 0, 0.000000, False, False, 1.000000
        ], 5.000000,
        [[0.000000, 0.000000, 0.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], 1280.000000,
        30.000000
    ],
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
    wave_viewer_style: SampledSequenceViewerStyle = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], 1.000000,
        [[0.000000, 0.000000, 0.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED],
        [[0.000000, 0.000000, 0.000000, 0.500000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED],
        [[0.000000, 0.000000, 0.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], 1.000000, 2.500000,
        [[0.020000, 0.020000, 0.020000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], 1280.000000,
        720.000000
    ],
    trigger_threshold_line_style: TriggerThresholdLineStyle = [[
        1.000000, 1.000000, 1.000000, 1.000000
    ]]
) -> None
```

<a id="unreal.AudioOscilloscopePanelStyle.time_ruler_style"></a>

#### time_ruler_style

```python
@property
def time_ruler_style() -> FixedSampleSequenceRulerStyle
```

(FixedSampleSequenceRulerStyle):  [Read-Write] The time rule style.

<a id="unreal.AudioOscilloscopePanelStyle.time_ruler_style"></a>

#### time_ruler_style

```python
@time_ruler_style.setter
def time_ruler_style(value: FixedSampleSequenceRulerStyle) -> None
```

<a id="unreal.AudioOscilloscopePanelStyle.value_grid_style"></a>

#### value_grid_style

```python
@property
def value_grid_style() -> SampledSequenceValueGridOverlayStyle
```

(SampledSequenceValueGridOverlayStyle):  [Read-Write] The value grid style.

<a id="unreal.AudioOscilloscopePanelStyle.value_grid_style"></a>

#### value_grid_style

```python
@value_grid_style.setter
def value_grid_style(value: SampledSequenceValueGridOverlayStyle) -> None
```

<a id="unreal.AudioOscilloscopePanelStyle.wave_viewer_style"></a>

#### wave_viewer_style

```python
@property
def wave_viewer_style() -> SampledSequenceViewerStyle
```

(SampledSequenceViewerStyle):  [Read-Write] The waveform view style.

<a id="unreal.AudioOscilloscopePanelStyle.wave_viewer_style"></a>

#### wave_viewer_style

```python
@wave_viewer_style.setter
def wave_viewer_style(value: SampledSequenceViewerStyle) -> None
```

<a id="unreal.AudioOscilloscopePanelStyle.trigger_threshold_line_style"></a>

#### trigger_threshold_line_style

```python
@property
def trigger_threshold_line_style() -> TriggerThresholdLineStyle
```

(TriggerThresholdLineStyle):  [Read-Write] The triggerthreshold line style.

<a id="unreal.AudioOscilloscopePanelStyle.trigger_threshold_line_style"></a>

#### trigger_threshold_line_style

```python
@trigger_threshold_line_style.setter
def trigger_threshold_line_style(value: TriggerThresholdLineStyle) -> None
```

<a id="unreal.TriggerThresholdLineStyle"></a>