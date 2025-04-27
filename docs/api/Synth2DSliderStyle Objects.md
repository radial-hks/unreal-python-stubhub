## Synth2DSliderStyle Objects

```python
class Synth2DSliderStyle(SlateWidgetStyle)
```

Represents the appearance of an SSynth2DSlider

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: Synth2DSliderStyle.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``background_image`` (SlateBrush):  [Read-Write]
- ``bar_thickness`` (float):  [Read-Write]
- ``disabled_bar_image`` (SlateBrush):  [Read-Write]
- ``disabled_thumb_image`` (SlateBrush):  [Read-Write] Image to use for the 2D handle
- ``normal_bar_image`` (SlateBrush):  [Read-Write]
- ``normal_thumb_image`` (SlateBrush):  [Read-Write] Image to use for the 2D handle

<a id="unreal.Synth2DSliderStyle.__init__"></a>

#### __init__

```python
def __init__(normal_thumb_image: SlateBrush = [
    [[1.000000, 1.000000, 1.000000, 1.000000],
     SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
    SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
    [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
    [[0.000000, 0.000000, 0.000000, 0.000000],
     [[0.000000, 0.000000, 0.000000, 0.000000],
      SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
     SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
],
             disabled_thumb_image: SlateBrush = [
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
             normal_bar_image: SlateBrush = [
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
             disabled_bar_image: SlateBrush = [
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
             background_image: SlateBrush = [
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
             bar_thickness: float = 0.000000) -> None
```

<a id="unreal.Synth2DSliderStyle.normal_thumb_image"></a>

#### normal_thumb_image

```python
@property
def normal_thumb_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to use for the 2D handle

<a id="unreal.Synth2DSliderStyle.normal_thumb_image"></a>

#### normal_thumb_image

```python
@normal_thumb_image.setter
def normal_thumb_image(value: SlateBrush) -> None
```

<a id="unreal.Synth2DSliderStyle.disabled_thumb_image"></a>

#### disabled_thumb_image

```python
@property
def disabled_thumb_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to use for the 2D handle

<a id="unreal.Synth2DSliderStyle.disabled_thumb_image"></a>

#### disabled_thumb_image

```python
@disabled_thumb_image.setter
def disabled_thumb_image(value: SlateBrush) -> None
```

<a id="unreal.Synth2DSliderStyle.normal_bar_image"></a>

#### normal_bar_image

```python
@property
def normal_bar_image() -> SlateBrush
```

(SlateBrush):  [Read-Write]

<a id="unreal.Synth2DSliderStyle.normal_bar_image"></a>

#### normal_bar_image

```python
@normal_bar_image.setter
def normal_bar_image(value: SlateBrush) -> None
```

<a id="unreal.Synth2DSliderStyle.disabled_bar_image"></a>

#### disabled_bar_image

```python
@property
def disabled_bar_image() -> SlateBrush
```

(SlateBrush):  [Read-Write]

<a id="unreal.Synth2DSliderStyle.disabled_bar_image"></a>

#### disabled_bar_image

```python
@disabled_bar_image.setter
def disabled_bar_image(value: SlateBrush) -> None
```

<a id="unreal.Synth2DSliderStyle.background_image"></a>

#### background_image

```python
@property
def background_image() -> SlateBrush
```

(SlateBrush):  [Read-Write]

<a id="unreal.Synth2DSliderStyle.background_image"></a>

#### background_image

```python
@background_image.setter
def background_image(value: SlateBrush) -> None
```

<a id="unreal.Synth2DSliderStyle.bar_thickness"></a>

#### bar_thickness

```python
@property
def bar_thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.Synth2DSliderStyle.bar_thickness"></a>

#### bar_thickness

```python
@bar_thickness.setter
def bar_thickness(value: float) -> None
```

<a id="unreal.SynthKnobStyle"></a>