## AudioSpectrumPlotStyle Objects

```python
class AudioSpectrumPlotStyle(SlateWidgetStyle)
```

Represents the appearance of an SAudioSpectrumPlot

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioSpectrumPlotStyle.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``axis_label_color`` (SlateColor):  [Read-Write]
- ``axis_label_font`` (SlateFontInfo):  [Read-Write]
- ``background_color`` (SlateColor):  [Read-Write]
- ``crosshair_color`` (SlateColor):  [Read-Write]
- ``crosshair_label_font`` (SlateFontInfo):  [Read-Write]
- ``grid_color`` (SlateColor):  [Read-Write]
- ``spectrum_color`` (SlateColor):  [Read-Write]

<a id="unreal.AudioSpectrumPlotStyle.__init__"></a>

#### __init__

```python
def __init__(
    background_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000],
                                    SlateColorStylingMode.USE_COLOR_SPECIFIED],
    grid_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000],
                              SlateColorStylingMode.USE_COLOR_SPECIFIED],
    axis_label_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000],
                                    SlateColorStylingMode.USE_COLOR_SPECIFIED],
    axis_label_font: SlateFontInfo = [
        None, None,
        [
            0, False, False, False, None,
            [0.000000, 0.000000, 0.000000, 1.000000]
        ], "None", 24.000000, 0, 0.000000, False, False, 1.000000
    ],
    spectrum_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000],
                                  SlateColorStylingMode.USE_COLOR_SPECIFIED],
    crosshair_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000],
                                   SlateColorStylingMode.USE_COLOR_SPECIFIED],
    crosshair_label_font: SlateFontInfo = [
        None, None,
        [
            0, False, False, False, None,
            [0.000000, 0.000000, 0.000000, 1.000000]
        ], "None", 24.000000, 0, 0.000000, False, False, 1.000000
    ]
) -> None
```

<a id="unreal.AudioSpectrumPlotStyle.background_color"></a>

#### background_color

```python
@property
def background_color() -> SlateColor
```

(SlateColor):  [Read-Write]

<a id="unreal.AudioSpectrumPlotStyle.background_color"></a>

#### background_color

```python
@background_color.setter
def background_color(value: SlateColor) -> None
```

<a id="unreal.AudioSpectrumPlotStyle.grid_color"></a>

#### grid_color

```python
@property
def grid_color() -> SlateColor
```

(SlateColor):  [Read-Write]

<a id="unreal.AudioSpectrumPlotStyle.grid_color"></a>

#### grid_color

```python
@grid_color.setter
def grid_color(value: SlateColor) -> None
```

<a id="unreal.AudioSpectrumPlotStyle.axis_label_color"></a>

#### axis_label_color

```python
@property
def axis_label_color() -> SlateColor
```

(SlateColor):  [Read-Write]

<a id="unreal.AudioSpectrumPlotStyle.axis_label_color"></a>

#### axis_label_color

```python
@axis_label_color.setter
def axis_label_color(value: SlateColor) -> None
```

<a id="unreal.AudioSpectrumPlotStyle.axis_label_font"></a>

#### axis_label_font

```python
@property
def axis_label_font() -> SlateFontInfo
```

(SlateFontInfo):  [Read-Write]

<a id="unreal.AudioSpectrumPlotStyle.axis_label_font"></a>

#### axis_label_font

```python
@axis_label_font.setter
def axis_label_font(value: SlateFontInfo) -> None
```

<a id="unreal.AudioSpectrumPlotStyle.spectrum_color"></a>

#### spectrum_color

```python
@property
def spectrum_color() -> SlateColor
```

(SlateColor):  [Read-Write]

<a id="unreal.AudioSpectrumPlotStyle.spectrum_color"></a>

#### spectrum_color

```python
@spectrum_color.setter
def spectrum_color(value: SlateColor) -> None
```

<a id="unreal.AudioSpectrumPlotStyle.crosshair_color"></a>

#### crosshair_color

```python
@property
def crosshair_color() -> SlateColor
```

(SlateColor):  [Read-Write]

<a id="unreal.AudioSpectrumPlotStyle.crosshair_color"></a>

#### crosshair_color

```python
@crosshair_color.setter
def crosshair_color(value: SlateColor) -> None
```

<a id="unreal.AudioSpectrumPlotStyle.crosshair_label_font"></a>

#### crosshair_label_font

```python
@property
def crosshair_label_font() -> SlateFontInfo
```

(SlateFontInfo):  [Read-Write]

<a id="unreal.AudioSpectrumPlotStyle.crosshair_label_font"></a>

#### crosshair_label_font

```python
@crosshair_label_font.setter
def crosshair_label_font(value: SlateFontInfo) -> None
```

<a id="unreal.AudioSliderStyle"></a>