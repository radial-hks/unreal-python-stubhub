## ProgressBarStyle Objects

```python
class ProgressBarStyle(SlateWidgetStyle)
```

Represents the appearance of an SProgressBar

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``background_image`` (SlateBrush):  [Read-Write] Background image to use for the progress bar
- ``enable_fill_animation`` (bool):  [Read-Write] Enables a simple animation on the fill image to give the appearance that progress has not stalled. Disable this if you have a custom material which animates itself.
  This requires a pattern in your material or texture to give the appearance of movement.  A solid color will show no movement.
- ``fill_image`` (SlateBrush):  [Read-Write] Foreground image to use for the progress bar
- ``marquee_image`` (SlateBrush):  [Read-Write] Image to use for marquee mode

<a id="unreal.ProgressBarStyle.__init__"></a>

#### __init__

```python
def __init__(background_image: SlateBrush = [
    [[1.000000, 1.000000, 1.000000, 1.000000],
     SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
    SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
    [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
    [[0.000000, 0.000000, 0.000000, 0.000000],
     [[0.000000, 0.000000, 0.000000, 0.000000],
      SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
     SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
],
             fill_image: SlateBrush = [
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
             marquee_image: SlateBrush = [
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
             enable_fill_animation: bool = False) -> None
```

<a id="unreal.ProgressBarStyle.background_image"></a>

#### background_image

```python
@property
def background_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Background image to use for the progress bar

<a id="unreal.ProgressBarStyle.background_image"></a>

#### background_image

```python
@background_image.setter
def background_image(value: SlateBrush) -> None
```

<a id="unreal.ProgressBarStyle.fill_image"></a>

#### fill_image

```python
@property
def fill_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Foreground image to use for the progress bar

<a id="unreal.ProgressBarStyle.fill_image"></a>

#### fill_image

```python
@fill_image.setter
def fill_image(value: SlateBrush) -> None
```

<a id="unreal.ProgressBarStyle.marquee_image"></a>

#### marquee_image

```python
@property
def marquee_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to use for marquee mode

<a id="unreal.ProgressBarStyle.marquee_image"></a>

#### marquee_image

```python
@marquee_image.setter
def marquee_image(value: SlateBrush) -> None
```

<a id="unreal.ProgressBarStyle.enable_fill_animation"></a>

#### enable_fill_animation

```python
@property
def enable_fill_animation() -> bool
```

(bool):  [Read-Write] Enables a simple animation on the fill image to give the appearance that progress has not stalled. Disable this if you have a custom material which animates itself.
This requires a pattern in your material or texture to give the appearance of movement.  A solid color will show no movement.

<a id="unreal.ProgressBarStyle.enable_fill_animation"></a>

#### enable_fill_animation

```python
@enable_fill_animation.setter
def enable_fill_animation(value: bool) -> None
```

<a id="unreal.SliderStyle"></a>