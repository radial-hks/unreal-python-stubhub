## ScrollBarStyle Objects

```python
class ScrollBarStyle(SlateWidgetStyle)
```

Represents the appearance of an SScrollBar

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dragged_thumb_image`` (SlateBrush):  [Read-Write] Image to use when the scrollbar thumb is in its dragged state
- ``horizontal_background_image`` (SlateBrush):  [Read-Write] Background image to use when the scrollbar is oriented horizontally
- ``horizontal_bottom_slot_image`` (SlateBrush):  [Read-Write] The image to use to represent the track below the thumb when the scrollbar is oriented horizontally
- ``horizontal_top_slot_image`` (SlateBrush):  [Read-Write] The image to use to represent the track above the thumb when the scrollbar is oriented horizontally
- ``hovered_thumb_image`` (SlateBrush):  [Read-Write] Image to use when the scrollbar thumb is in its hovered state
- ``normal_thumb_image`` (SlateBrush):  [Read-Write] Image to use when the scrollbar thumb is in its normal state
- ``thickness`` (float):  [Read-Write]
- ``vertical_background_image`` (SlateBrush):  [Read-Write] Background image to use when the scrollbar is oriented vertically
- ``vertical_bottom_slot_image`` (SlateBrush):  [Read-Write] The image to use to represent the track below the thumb when the scrollbar is oriented vertically
- ``vertical_top_slot_image`` (SlateBrush):  [Read-Write] The image to use to represent the track above the thumb when the scrollbar is oriented vertically

<a id="unreal.ScrollBarStyle.__init__"></a>

#### __init__

```python
def __init__(horizontal_background_image: SlateBrush = [
    [[1.000000, 1.000000, 1.000000, 1.000000],
     SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
    SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
    [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
    [[0.000000, 0.000000, 0.000000, 0.000000],
     [[0.000000, 0.000000, 0.000000, 0.000000],
      SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
     SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
],
             vertical_background_image: SlateBrush = [
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
             vertical_top_slot_image: SlateBrush = [
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
             horizontal_top_slot_image: SlateBrush = [
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
             vertical_bottom_slot_image: SlateBrush = [
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
             horizontal_bottom_slot_image: SlateBrush = [
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
             dragged_thumb_image: SlateBrush = [
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
             thickness: float = 0.000000) -> None
```

<a id="unreal.ScrollBarStyle.horizontal_background_image"></a>

#### horizontal_background_image

```python
@property
def horizontal_background_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Background image to use when the scrollbar is oriented horizontally

<a id="unreal.ScrollBarStyle.horizontal_background_image"></a>

#### horizontal_background_image

```python
@horizontal_background_image.setter
def horizontal_background_image(value: SlateBrush) -> None
```

<a id="unreal.ScrollBarStyle.vertical_background_image"></a>

#### vertical_background_image

```python
@property
def vertical_background_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Background image to use when the scrollbar is oriented vertically

<a id="unreal.ScrollBarStyle.vertical_background_image"></a>

#### vertical_background_image

```python
@vertical_background_image.setter
def vertical_background_image(value: SlateBrush) -> None
```

<a id="unreal.ScrollBarStyle.vertical_top_slot_image"></a>

#### vertical_top_slot_image

```python
@property
def vertical_top_slot_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] The image to use to represent the track above the thumb when the scrollbar is oriented vertically

<a id="unreal.ScrollBarStyle.vertical_top_slot_image"></a>

#### vertical_top_slot_image

```python
@vertical_top_slot_image.setter
def vertical_top_slot_image(value: SlateBrush) -> None
```

<a id="unreal.ScrollBarStyle.horizontal_top_slot_image"></a>

#### horizontal_top_slot_image

```python
@property
def horizontal_top_slot_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] The image to use to represent the track above the thumb when the scrollbar is oriented horizontally

<a id="unreal.ScrollBarStyle.horizontal_top_slot_image"></a>

#### horizontal_top_slot_image

```python
@horizontal_top_slot_image.setter
def horizontal_top_slot_image(value: SlateBrush) -> None
```

<a id="unreal.ScrollBarStyle.vertical_bottom_slot_image"></a>

#### vertical_bottom_slot_image

```python
@property
def vertical_bottom_slot_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] The image to use to represent the track below the thumb when the scrollbar is oriented vertically

<a id="unreal.ScrollBarStyle.vertical_bottom_slot_image"></a>

#### vertical_bottom_slot_image

```python
@vertical_bottom_slot_image.setter
def vertical_bottom_slot_image(value: SlateBrush) -> None
```

<a id="unreal.ScrollBarStyle.horizontal_bottom_slot_image"></a>

#### horizontal_bottom_slot_image

```python
@property
def horizontal_bottom_slot_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] The image to use to represent the track below the thumb when the scrollbar is oriented horizontally

<a id="unreal.ScrollBarStyle.horizontal_bottom_slot_image"></a>

#### horizontal_bottom_slot_image

```python
@horizontal_bottom_slot_image.setter
def horizontal_bottom_slot_image(value: SlateBrush) -> None
```

<a id="unreal.ScrollBarStyle.normal_thumb_image"></a>

#### normal_thumb_image

```python
@property
def normal_thumb_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to use when the scrollbar thumb is in its normal state

<a id="unreal.ScrollBarStyle.normal_thumb_image"></a>

#### normal_thumb_image

```python
@normal_thumb_image.setter
def normal_thumb_image(value: SlateBrush) -> None
```

<a id="unreal.ScrollBarStyle.hovered_thumb_image"></a>

#### hovered_thumb_image

```python
@property
def hovered_thumb_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to use when the scrollbar thumb is in its hovered state

<a id="unreal.ScrollBarStyle.hovered_thumb_image"></a>

#### hovered_thumb_image

```python
@hovered_thumb_image.setter
def hovered_thumb_image(value: SlateBrush) -> None
```

<a id="unreal.ScrollBarStyle.dragged_thumb_image"></a>

#### dragged_thumb_image

```python
@property
def dragged_thumb_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to use when the scrollbar thumb is in its dragged state

<a id="unreal.ScrollBarStyle.dragged_thumb_image"></a>

#### dragged_thumb_image

```python
@dragged_thumb_image.setter
def dragged_thumb_image(value: SlateBrush) -> None
```

<a id="unreal.ScrollBarStyle.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.ScrollBarStyle.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.TableRowStyle"></a>