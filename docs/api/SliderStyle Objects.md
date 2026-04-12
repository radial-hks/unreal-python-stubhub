## SliderStyle Objects

```python
class SliderStyle(SlateWidgetStyle)
```

Represents the appearance of an SSlider

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bar_thickness`` (float):  [Read-Write]
- ``disabled_bar_image`` (SlateBrush):  [Read-Write] Image to use when the slider bar is in its disabled state
- ``disabled_thumb_image`` (SlateBrush):  [Read-Write] Image to use when the slider thumb is in its disabled state
- ``hovered_bar_image`` (SlateBrush):  [Read-Write] Image to use when the slider bar is in its hovered state
- ``hovered_thumb_image`` (SlateBrush):  [Read-Write] Image to use when the slider thumb is in its hovered state
- ``normal_bar_image`` (SlateBrush):  [Read-Write] Image to use when the slider bar is in its normal state
- ``normal_thumb_image`` (SlateBrush):  [Read-Write] Image to use when the slider thumb is in its normal state

<a id="unreal.SliderStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(normal_bar_image: SlateBrush = [
    [[1.000000, 1.000000, 1.000000, 1.000000],
     SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
    SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
    [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
    [[0.000000, 0.000000, 0.000000, 0.000000],
     [[0.000000, 0.000000, 0.000000, 0.000000],
      SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
     SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
],
             hovered_bar_image: SlateBrush = [
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
             normal_thumb_image: SlateBrush = [
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
             hovered_thumb_image: SlateBrush = [
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
             bar_thickness: float = 0.000000) -> None
```

<a id="unreal.SliderStyle.normal_bar_image"></a>

#### normal\_bar\_image

```python
@property
def normal_bar_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to use when the slider bar is in its normal state

<a id="unreal.SliderStyle.normal_bar_image"></a>

#### normal\_bar\_image

```python
@normal_bar_image.setter
def normal_bar_image(value: SlateBrush) -> None
```

<a id="unreal.SliderStyle.hovered_bar_image"></a>

#### hovered\_bar\_image

```python
@property
def hovered_bar_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to use when the slider bar is in its hovered state

<a id="unreal.SliderStyle.hovered_bar_image"></a>

#### hovered\_bar\_image

```python
@hovered_bar_image.setter
def hovered_bar_image(value: SlateBrush) -> None
```

<a id="unreal.SliderStyle.disabled_bar_image"></a>

#### disabled\_bar\_image

```python
@property
def disabled_bar_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to use when the slider bar is in its disabled state

<a id="unreal.SliderStyle.disabled_bar_image"></a>

#### disabled\_bar\_image

```python
@disabled_bar_image.setter
def disabled_bar_image(value: SlateBrush) -> None
```

<a id="unreal.SliderStyle.normal_thumb_image"></a>

#### normal\_thumb\_image

```python
@property
def normal_thumb_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to use when the slider thumb is in its normal state

<a id="unreal.SliderStyle.normal_thumb_image"></a>

#### normal\_thumb\_image

```python
@normal_thumb_image.setter
def normal_thumb_image(value: SlateBrush) -> None
```

<a id="unreal.SliderStyle.hovered_thumb_image"></a>

#### hovered\_thumb\_image

```python
@property
def hovered_thumb_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to use when the slider thumb is in its hovered state

<a id="unreal.SliderStyle.hovered_thumb_image"></a>

#### hovered\_thumb\_image

```python
@hovered_thumb_image.setter
def hovered_thumb_image(value: SlateBrush) -> None
```

<a id="unreal.SliderStyle.disabled_thumb_image"></a>

#### disabled\_thumb\_image

```python
@property
def disabled_thumb_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to use when the slider thumb is in its disabled state

<a id="unreal.SliderStyle.disabled_thumb_image"></a>

#### disabled\_thumb\_image

```python
@disabled_thumb_image.setter
def disabled_thumb_image(value: SlateBrush) -> None
```

<a id="unreal.SliderStyle.bar_thickness"></a>

#### bar\_thickness

```python
@property
def bar_thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.SliderStyle.bar_thickness"></a>

#### bar\_thickness

```python
@bar_thickness.setter
def bar_thickness(value: float) -> None
```

<a id="unreal.SplitterStyle"></a>