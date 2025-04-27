## AudioRadialSliderStyle Objects

```python
class AudioRadialSliderStyle(SlateWidgetStyle)
```

Represents the appearance of an Audio Radial Slider

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioWidgetsSlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``center_background_color`` (SlateColor):  [Read-Write] Color used to draw the slider center background
- ``default_slider_radius`` (float):  [Read-Write] Default size of the slider itself (not including label)
- ``label_padding`` (float):  [Read-Write] Size of the padding between the label and the slider
- ``slider_bar_color`` (SlateColor):  [Read-Write] Color used to draw the unprogressed slider bar
- ``slider_progress_color`` (SlateColor):  [Read-Write] Color used to draw the progress bar
- ``text_box_style`` (AudioTextBoxStyle):  [Read-Write] The style to use for the audio text box widget.

<a id="unreal.AudioRadialSliderStyle.__init__"></a>

#### __init__

```python
def __init__(text_box_style: AudioTextBoxStyle = [
    [[[0.000000, 0.000000, 0.000000, 0.000000],
      0], SlateBrushDrawType.ROUNDED_BOX, SlateBrushTileType.NO_TILE,
     SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
     [0.000000, 0.000000, 0.000000, 0.000000], None,
     [[4.000000, 4.000000, 4.000000, 4.000000],
      [[0.000000, 0.000000, 0.000000, 0.000000],
       SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
      SlateBrushRoundingType.FIXED_RADIUS, False]],
    [[0.000000, 0.000000, 0.000000, 0.000000], 0]
],
             center_background_color: SlateColor = [[
                 1.000000, 0.000000, 1.000000, 1.000000
             ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
             slider_bar_color: SlateColor = [[
                 1.000000, 0.000000, 1.000000, 1.000000
             ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
             slider_progress_color: SlateColor = [[
                 1.000000, 0.000000, 1.000000, 1.000000
             ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
             label_padding: float = 0.000000,
             default_slider_radius: float = 0.000000) -> None
```

<a id="unreal.AudioRadialSliderStyle.text_box_style"></a>

#### text_box_style

```python
@property
def text_box_style() -> AudioTextBoxStyle
```

(AudioTextBoxStyle):  [Read-Write] The style to use for the audio text box widget.

<a id="unreal.AudioRadialSliderStyle.text_box_style"></a>

#### text_box_style

```python
@text_box_style.setter
def text_box_style(value: AudioTextBoxStyle) -> None
```

<a id="unreal.AudioRadialSliderStyle.center_background_color"></a>

#### center_background_color

```python
@property
def center_background_color() -> SlateColor
```

(SlateColor):  [Read-Write] Color used to draw the slider center background

<a id="unreal.AudioRadialSliderStyle.center_background_color"></a>

#### center_background_color

```python
@center_background_color.setter
def center_background_color(value: SlateColor) -> None
```

<a id="unreal.AudioRadialSliderStyle.slider_bar_color"></a>

#### slider_bar_color

```python
@property
def slider_bar_color() -> SlateColor
```

(SlateColor):  [Read-Write] Color used to draw the unprogressed slider bar

<a id="unreal.AudioRadialSliderStyle.slider_bar_color"></a>

#### slider_bar_color

```python
@slider_bar_color.setter
def slider_bar_color(value: SlateColor) -> None
```

<a id="unreal.AudioRadialSliderStyle.slider_progress_color"></a>

#### slider_progress_color

```python
@property
def slider_progress_color() -> SlateColor
```

(SlateColor):  [Read-Write] Color used to draw the progress bar

<a id="unreal.AudioRadialSliderStyle.slider_progress_color"></a>

#### slider_progress_color

```python
@slider_progress_color.setter
def slider_progress_color(value: SlateColor) -> None
```

<a id="unreal.AudioRadialSliderStyle.label_padding"></a>

#### label_padding

```python
@property
def label_padding() -> float
```

(float):  [Read-Write] Size of the padding between the label and the slider

<a id="unreal.AudioRadialSliderStyle.label_padding"></a>

#### label_padding

```python
@label_padding.setter
def label_padding(value: float) -> None
```

<a id="unreal.AudioRadialSliderStyle.default_slider_radius"></a>

#### default_slider_radius

```python
@property
def default_slider_radius() -> float
```

(float):  [Read-Write] Default size of the slider itself (not including label)

<a id="unreal.AudioRadialSliderStyle.default_slider_radius"></a>

#### default_slider_radius

```python
@default_slider_radius.setter
def default_slider_radius(value: float) -> None
```

<a id="unreal.PlayheadOverlayStyle"></a>