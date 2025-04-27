## AudioSliderStyle Objects

```python
class AudioSliderStyle(SlateWidgetStyle)
```

Represents the appearance of an Audio Slider

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioWidgetsSlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``label_padding`` (float):  [Read-Write] Size of the padding between the label and the slider
- ``slider_background_color`` (SlateColor):  [Read-Write] Color used to draw the slider background
- ``slider_background_size`` (Vector2D):  [Read-Write] Size of the slider background (slider default is vertical)
- ``slider_bar_color`` (SlateColor):  [Read-Write] Color used to draw the slider bar
- ``slider_style`` (SliderStyle):  [Read-Write] The style to use for the underlying SSlider.
- ``slider_thumb_color`` (SlateColor):  [Read-Write] Color used to draw the slider thumb (handle)
- ``text_box_style`` (AudioTextBoxStyle):  [Read-Write] The style to use for the audio text box widget.
- ``widget_background_color`` (SlateColor):  [Read-Write] Color used to draw the widget background
- ``widget_background_image`` (SlateBrush):  [Read-Write] Image for the widget background

<a id="unreal.AudioSliderStyle.__init__"></a>

#### __init__

```python
def __init__(
    slider_style: SliderStyle = [
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
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], 2.000000
    ],
    text_box_style: AudioTextBoxStyle = [
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
    widget_background_image: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    slider_background_color: SlateColor = [[
        1.000000, 0.000000, 1.000000, 1.000000
    ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
    slider_background_size: Vector2D = [0.000000, 0.000000],
    label_padding: float = 0.000000,
    slider_bar_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000],
                                    SlateColorStylingMode.USE_COLOR_SPECIFIED],
    slider_thumb_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000],
                                      SlateColorStylingMode.USE_COLOR_SPECIFIED
                                      ],
    widget_background_color: SlateColor = [[
        1.000000, 0.000000, 1.000000, 1.000000
    ], SlateColorStylingMode.USE_COLOR_SPECIFIED]
) -> None
```

<a id="unreal.AudioSliderStyle.slider_style"></a>

#### slider_style

```python
@property
def slider_style() -> SliderStyle
```

(SliderStyle):  [Read-Write] The style to use for the underlying SSlider.

<a id="unreal.AudioSliderStyle.slider_style"></a>

#### slider_style

```python
@slider_style.setter
def slider_style(value: SliderStyle) -> None
```

<a id="unreal.AudioSliderStyle.text_box_style"></a>

#### text_box_style

```python
@property
def text_box_style() -> AudioTextBoxStyle
```

(AudioTextBoxStyle):  [Read-Write] The style to use for the audio text box widget.

<a id="unreal.AudioSliderStyle.text_box_style"></a>

#### text_box_style

```python
@text_box_style.setter
def text_box_style(value: AudioTextBoxStyle) -> None
```

<a id="unreal.AudioSliderStyle.widget_background_image"></a>

#### widget_background_image

```python
@property
def widget_background_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image for the widget background

<a id="unreal.AudioSliderStyle.widget_background_image"></a>

#### widget_background_image

```python
@widget_background_image.setter
def widget_background_image(value: SlateBrush) -> None
```

<a id="unreal.AudioSliderStyle.slider_background_color"></a>

#### slider_background_color

```python
@property
def slider_background_color() -> SlateColor
```

(SlateColor):  [Read-Write] Color used to draw the slider background

<a id="unreal.AudioSliderStyle.slider_background_color"></a>

#### slider_background_color

```python
@slider_background_color.setter
def slider_background_color(value: SlateColor) -> None
```

<a id="unreal.AudioSliderStyle.slider_background_size"></a>

#### slider_background_size

```python
@property
def slider_background_size() -> Vector2D
```

(Vector2D):  [Read-Write] Size of the slider background (slider default is vertical)

<a id="unreal.AudioSliderStyle.slider_background_size"></a>

#### slider_background_size

```python
@slider_background_size.setter
def slider_background_size(value: Vector2D) -> None
```

<a id="unreal.AudioSliderStyle.label_padding"></a>

#### label_padding

```python
@property
def label_padding() -> float
```

(float):  [Read-Write] Size of the padding between the label and the slider

<a id="unreal.AudioSliderStyle.label_padding"></a>

#### label_padding

```python
@label_padding.setter
def label_padding(value: float) -> None
```

<a id="unreal.AudioSliderStyle.slider_bar_color"></a>

#### slider_bar_color

```python
@property
def slider_bar_color() -> SlateColor
```

(SlateColor):  [Read-Write] Color used to draw the slider bar

<a id="unreal.AudioSliderStyle.slider_bar_color"></a>

#### slider_bar_color

```python
@slider_bar_color.setter
def slider_bar_color(value: SlateColor) -> None
```

<a id="unreal.AudioSliderStyle.slider_thumb_color"></a>

#### slider_thumb_color

```python
@property
def slider_thumb_color() -> SlateColor
```

(SlateColor):  [Read-Write] Color used to draw the slider thumb (handle)

<a id="unreal.AudioSliderStyle.slider_thumb_color"></a>

#### slider_thumb_color

```python
@slider_thumb_color.setter
def slider_thumb_color(value: SlateColor) -> None
```

<a id="unreal.AudioSliderStyle.widget_background_color"></a>

#### widget_background_color

```python
@property
def widget_background_color() -> SlateColor
```

(SlateColor):  [Read-Write] Color used to draw the widget background

<a id="unreal.AudioSliderStyle.widget_background_color"></a>

#### widget_background_color

```python
@widget_background_color.setter
def widget_background_color(value: SlateColor) -> None
```

<a id="unreal.AudioRadialSliderStyle"></a>