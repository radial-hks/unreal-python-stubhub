## AudioMeterStyle Objects

```python
class AudioMeterStyle(SlateWidgetStyle)
```

Represents the appearance of an SAudioMeter

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioMeterStyle.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``background_image`` (SlateBrush):  [Read-Write] Image to use to represent the background.
- ``decibels_per_hash`` (int32):  [Read-Write] How wide to draw the decibel scale, if it's enabled
- ``font`` (SlateFontInfo):  [Read-Write] Font family and size to be used when displaying the meter scale.
- ``meter_background_image`` (SlateBrush):  [Read-Write] Image to use to represent the meter background.
- ``meter_padding`` (Vector2D):  [Read-Write] How much padding to add around the meter
- ``meter_peak_image`` (SlateBrush):  [Read-Write] Image to use to represent the meter peak.
- ``meter_size`` (Vector2D):  [Read-Write] How thick to draw the meter
- ``meter_value_background_image`` (SlateBrush):  [Read-Write] Image to use to draw behind the meter value.
- ``meter_value_image`` (SlateBrush):  [Read-Write] Image to use to represent the meter value.
- ``meter_value_padding`` (float):  [Read-Write] How much padding to add around the meter value
- ``peak_value_width`` (float):  [Read-Write] How wide to draw the peak value indicator
- ``scale_hash_height`` (float):  [Read-Write] The height of each hash mark
- ``scale_hash_offset`` (float):  [Read-Write] Offset for the hashes
- ``scale_hash_width`` (float):  [Read-Write] The width of each hash mark
- ``scale_side`` (bool):  [Read-Write] Which side to show the scale. If vertical, true means left side, false means right side. If horizontal, true means above, false means below.
- ``show_scale`` (bool):  [Read-Write] Whether or not to show the decibel scale alongside the meter
- ``value_range_db`` (Vector2D):  [Read-Write] The minimum and maximum value to display in dB (values are clamped in this range)

<a id="unreal.AudioMeterStyle.__init__"></a>

#### __init__

```python
def __init__(
    meter_value_image: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    background_image: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    meter_background_image: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    meter_value_background_image: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    meter_peak_image: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000],
                                     SlateColorStylingMode.USE_COLOR_SPECIFIED
                                     ], SlateBrushDrawType.IMAGE,
                                    SlateBrushTileType.NO_TILE,
                                    SlateBrushMirrorType.NO_MIRROR,
                                    [0.000000, 0.000000],
                                    [0.000000, 0.000000, 0.000000,
                                     0.000000], None,
                                    [[0.000000, 0.000000, 0.000000, 0.000000],
                                     [[0.000000, 0.000000, 0.000000, 0.000000],
                                      SlateColorStylingMode.USE_COLOR_SPECIFIED
                                      ], 0.000000,
                                     SlateBrushRoundingType.HALF_HEIGHT_RADIUS,
                                     False]],
    meter_size: Vector2D = [0.000000, 0.000000],
    meter_padding: Vector2D = [0.000000, 0.000000],
    meter_value_padding: float = 0.000000,
    peak_value_width: float = 0.000000,
    value_range_db: Vector2D = [0.000000, 0.000000],
    show_scale: bool = False,
    scale_side: bool = False,
    scale_hash_offset: float = 0.000000,
    scale_hash_width: float = 0.000000,
    scale_hash_height: float = 0.000000,
    decibels_per_hash: int = 0,
    font: SlateFontInfo = [
        None, None,
        [
            0, False, False, False, None,
            [0.000000, 0.000000, 0.000000, 1.000000]
        ], "None", 24.000000, 0, 0.000000, False, False, 1.000000
    ]
) -> None
```

<a id="unreal.AudioMeterStyle.meter_value_image"></a>

#### meter_value_image

```python
@property
def meter_value_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to use to represent the meter value.

<a id="unreal.AudioMeterStyle.meter_value_image"></a>

#### meter_value_image

```python
@meter_value_image.setter
def meter_value_image(value: SlateBrush) -> None
```

<a id="unreal.AudioMeterStyle.background_image"></a>

#### background_image

```python
@property
def background_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to use to represent the background.

<a id="unreal.AudioMeterStyle.background_image"></a>

#### background_image

```python
@background_image.setter
def background_image(value: SlateBrush) -> None
```

<a id="unreal.AudioMeterStyle.meter_background_image"></a>

#### meter_background_image

```python
@property
def meter_background_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to use to represent the meter background.

<a id="unreal.AudioMeterStyle.meter_background_image"></a>

#### meter_background_image

```python
@meter_background_image.setter
def meter_background_image(value: SlateBrush) -> None
```

<a id="unreal.AudioMeterStyle.meter_value_background_image"></a>

#### meter_value_background_image

```python
@property
def meter_value_background_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to use to draw behind the meter value.

<a id="unreal.AudioMeterStyle.meter_value_background_image"></a>

#### meter_value_background_image

```python
@meter_value_background_image.setter
def meter_value_background_image(value: SlateBrush) -> None
```

<a id="unreal.AudioMeterStyle.meter_peak_image"></a>

#### meter_peak_image

```python
@property
def meter_peak_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to use to represent the meter peak.

<a id="unreal.AudioMeterStyle.meter_peak_image"></a>

#### meter_peak_image

```python
@meter_peak_image.setter
def meter_peak_image(value: SlateBrush) -> None
```

<a id="unreal.AudioMeterStyle.meter_size"></a>

#### meter_size

```python
@property
def meter_size() -> Vector2D
```

(Vector2D):  [Read-Write] How thick to draw the meter

<a id="unreal.AudioMeterStyle.meter_size"></a>

#### meter_size

```python
@meter_size.setter
def meter_size(value: Vector2D) -> None
```

<a id="unreal.AudioMeterStyle.meter_padding"></a>

#### meter_padding

```python
@property
def meter_padding() -> Vector2D
```

(Vector2D):  [Read-Write] How much padding to add around the meter

<a id="unreal.AudioMeterStyle.meter_padding"></a>

#### meter_padding

```python
@meter_padding.setter
def meter_padding(value: Vector2D) -> None
```

<a id="unreal.AudioMeterStyle.meter_value_padding"></a>

#### meter_value_padding

```python
@property
def meter_value_padding() -> float
```

(float):  [Read-Write] How much padding to add around the meter value

<a id="unreal.AudioMeterStyle.meter_value_padding"></a>

#### meter_value_padding

```python
@meter_value_padding.setter
def meter_value_padding(value: float) -> None
```

<a id="unreal.AudioMeterStyle.peak_value_width"></a>

#### peak_value_width

```python
@property
def peak_value_width() -> float
```

(float):  [Read-Write] How wide to draw the peak value indicator

<a id="unreal.AudioMeterStyle.peak_value_width"></a>

#### peak_value_width

```python
@peak_value_width.setter
def peak_value_width(value: float) -> None
```

<a id="unreal.AudioMeterStyle.value_range_db"></a>

#### value_range_db

```python
@property
def value_range_db() -> Vector2D
```

(Vector2D):  [Read-Write] The minimum and maximum value to display in dB (values are clamped in this range)

<a id="unreal.AudioMeterStyle.value_range_db"></a>

#### value_range_db

```python
@value_range_db.setter
def value_range_db(value: Vector2D) -> None
```

<a id="unreal.AudioMeterStyle.show_scale"></a>

#### show_scale

```python
@property
def show_scale() -> bool
```

(bool):  [Read-Write] Whether or not to show the decibel scale alongside the meter

<a id="unreal.AudioMeterStyle.show_scale"></a>

#### show_scale

```python
@show_scale.setter
def show_scale(value: bool) -> None
```

<a id="unreal.AudioMeterStyle.scale_side"></a>

#### scale_side

```python
@property
def scale_side() -> bool
```

(bool):  [Read-Write] Which side to show the scale. If vertical, true means left side, false means right side. If horizontal, true means above, false means below.

<a id="unreal.AudioMeterStyle.scale_side"></a>

#### scale_side

```python
@scale_side.setter
def scale_side(value: bool) -> None
```

<a id="unreal.AudioMeterStyle.scale_hash_offset"></a>

#### scale_hash_offset

```python
@property
def scale_hash_offset() -> float
```

(float):  [Read-Write] Offset for the hashes

<a id="unreal.AudioMeterStyle.scale_hash_offset"></a>

#### scale_hash_offset

```python
@scale_hash_offset.setter
def scale_hash_offset(value: float) -> None
```

<a id="unreal.AudioMeterStyle.scale_hash_width"></a>

#### scale_hash_width

```python
@property
def scale_hash_width() -> float
```

(float):  [Read-Write] The width of each hash mark

<a id="unreal.AudioMeterStyle.scale_hash_width"></a>

#### scale_hash_width

```python
@scale_hash_width.setter
def scale_hash_width(value: float) -> None
```

<a id="unreal.AudioMeterStyle.scale_hash_height"></a>

#### scale_hash_height

```python
@property
def scale_hash_height() -> float
```

(float):  [Read-Write] The height of each hash mark

<a id="unreal.AudioMeterStyle.scale_hash_height"></a>

#### scale_hash_height

```python
@scale_hash_height.setter
def scale_hash_height(value: float) -> None
```

<a id="unreal.AudioMeterStyle.decibels_per_hash"></a>

#### decibels_per_hash

```python
@property
def decibels_per_hash() -> int
```

(int32):  [Read-Write] How wide to draw the decibel scale, if it's enabled

<a id="unreal.AudioMeterStyle.decibels_per_hash"></a>

#### decibels_per_hash

```python
@decibels_per_hash.setter
def decibels_per_hash(value: int) -> None
```

<a id="unreal.AudioMeterStyle.font"></a>

#### font

```python
@property
def font() -> SlateFontInfo
```

(SlateFontInfo):  [Read-Write] Font family and size to be used when displaying the meter scale.

<a id="unreal.AudioMeterStyle.font"></a>

#### font

```python
@font.setter
def font(value: SlateFontInfo) -> None
```

<a id="unreal.AudioOscilloscopePanelStyle"></a>