## AudioMaterialMeterStyle Objects

```python
class AudioMaterialMeterStyle(AudioMaterialWidgetStyle)
```

Represents the appearance of an Audio Material Meter

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioMaterialSlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``decibels_per_hash`` (int32):  [Read-Write] How wide to draw the decibel scale, if it's enabled
- ``desired_size`` (Vector2f):  [Read-Write] Desired Draw size of the rendered material
- ``font`` (SlateFontInfo):  [Read-Write] Font family and size to be used when displaying the meter scale.
- ``material`` (MaterialInterface):  [Read-Write] Material used to render the Slate
- ``meter_fill_background_color`` (LinearColor):  [Read-Write] The meter's Background Fill color value.
- ``meter_fill_max_color`` (LinearColor):  [Read-Write] The meter's Fill color value representing the Ending section of the fill.
- ``meter_fill_mid_color`` (LinearColor):  [Read-Write] The meter's Fill color value representing the Middle section of the fill.
- ``meter_fill_min_color`` (LinearColor):  [Read-Write] The meter's Fill color value representing the Starting section of the fill.
- ``meter_padding`` (Vector2D):  [Read-Write] How much padding to add around the meter
- ``scale_hash_height`` (float):  [Read-Write] The height of each hash mark
- ``scale_hash_offset`` (float):  [Read-Write] Offset for the hashes
- ``scale_hash_width`` (float):  [Read-Write] The width of each hash mark
- ``scale_side`` (bool):  [Read-Write] Which side to show the scale. If vertical, true means left side, false means right side. If horizontal, true means above, false means below.
- ``show_scale`` (bool):  [Read-Write] Whether or not to show the decibel scale alongside the meter
- ``value_range_db`` (Vector2D):  [Read-Write] The minimum and maximum value to display in dB (values are clamped in this range)

<a id="unreal.AudioMaterialMeterStyle.__init__"></a>

#### __init__

```python
def __init__(
    material: MaterialInterface = None,
    desired_size: Vector2f = [0.000000, 0.000000],
    meter_fill_min_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    meter_fill_mid_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    meter_fill_max_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    meter_fill_background_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    meter_padding: Vector2D = [0.000000, 0.000000],
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

<a id="unreal.AudioMaterialMeterStyle.meter_fill_min_color"></a>

#### meter_fill_min_color

```python
@property
def meter_fill_min_color() -> LinearColor
```

(LinearColor):  [Read-Write] The meter's Fill color value representing the Starting section of the fill.

<a id="unreal.AudioMaterialMeterStyle.meter_fill_min_color"></a>

#### meter_fill_min_color

```python
@meter_fill_min_color.setter
def meter_fill_min_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialMeterStyle.meter_fill_mid_color"></a>

#### meter_fill_mid_color

```python
@property
def meter_fill_mid_color() -> LinearColor
```

(LinearColor):  [Read-Write] The meter's Fill color value representing the Middle section of the fill.

<a id="unreal.AudioMaterialMeterStyle.meter_fill_mid_color"></a>

#### meter_fill_mid_color

```python
@meter_fill_mid_color.setter
def meter_fill_mid_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialMeterStyle.meter_fill_max_color"></a>

#### meter_fill_max_color

```python
@property
def meter_fill_max_color() -> LinearColor
```

(LinearColor):  [Read-Write] The meter's Fill color value representing the Ending section of the fill.

<a id="unreal.AudioMaterialMeterStyle.meter_fill_max_color"></a>

#### meter_fill_max_color

```python
@meter_fill_max_color.setter
def meter_fill_max_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialMeterStyle.meter_fill_background_color"></a>

#### meter_fill_background_color

```python
@property
def meter_fill_background_color() -> LinearColor
```

(LinearColor):  [Read-Write] The meter's Background Fill color value.

<a id="unreal.AudioMaterialMeterStyle.meter_fill_background_color"></a>

#### meter_fill_background_color

```python
@meter_fill_background_color.setter
def meter_fill_background_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialMeterStyle.meter_padding"></a>

#### meter_padding

```python
@property
def meter_padding() -> Vector2D
```

(Vector2D):  [Read-Write] How much padding to add around the meter

<a id="unreal.AudioMaterialMeterStyle.meter_padding"></a>

#### meter_padding

```python
@meter_padding.setter
def meter_padding(value: Vector2D) -> None
```

<a id="unreal.AudioMaterialMeterStyle.value_range_db"></a>

#### value_range_db

```python
@property
def value_range_db() -> Vector2D
```

(Vector2D):  [Read-Write] The minimum and maximum value to display in dB (values are clamped in this range)

<a id="unreal.AudioMaterialMeterStyle.value_range_db"></a>

#### value_range_db

```python
@value_range_db.setter
def value_range_db(value: Vector2D) -> None
```

<a id="unreal.AudioMaterialMeterStyle.show_scale"></a>

#### show_scale

```python
@property
def show_scale() -> bool
```

(bool):  [Read-Write] Whether or not to show the decibel scale alongside the meter

<a id="unreal.AudioMaterialMeterStyle.show_scale"></a>

#### show_scale

```python
@show_scale.setter
def show_scale(value: bool) -> None
```

<a id="unreal.AudioMaterialMeterStyle.scale_side"></a>

#### scale_side

```python
@property
def scale_side() -> bool
```

(bool):  [Read-Write] Which side to show the scale. If vertical, true means left side, false means right side. If horizontal, true means above, false means below.

<a id="unreal.AudioMaterialMeterStyle.scale_side"></a>

#### scale_side

```python
@scale_side.setter
def scale_side(value: bool) -> None
```

<a id="unreal.AudioMaterialMeterStyle.scale_hash_offset"></a>

#### scale_hash_offset

```python
@property
def scale_hash_offset() -> float
```

(float):  [Read-Write] Offset for the hashes

<a id="unreal.AudioMaterialMeterStyle.scale_hash_offset"></a>

#### scale_hash_offset

```python
@scale_hash_offset.setter
def scale_hash_offset(value: float) -> None
```

<a id="unreal.AudioMaterialMeterStyle.scale_hash_width"></a>

#### scale_hash_width

```python
@property
def scale_hash_width() -> float
```

(float):  [Read-Write] The width of each hash mark

<a id="unreal.AudioMaterialMeterStyle.scale_hash_width"></a>

#### scale_hash_width

```python
@scale_hash_width.setter
def scale_hash_width(value: float) -> None
```

<a id="unreal.AudioMaterialMeterStyle.scale_hash_height"></a>

#### scale_hash_height

```python
@property
def scale_hash_height() -> float
```

(float):  [Read-Write] The height of each hash mark

<a id="unreal.AudioMaterialMeterStyle.scale_hash_height"></a>

#### scale_hash_height

```python
@scale_hash_height.setter
def scale_hash_height(value: float) -> None
```

<a id="unreal.AudioMaterialMeterStyle.decibels_per_hash"></a>

#### decibels_per_hash

```python
@property
def decibels_per_hash() -> int
```

(int32):  [Read-Write] How wide to draw the decibel scale, if it's enabled

<a id="unreal.AudioMaterialMeterStyle.decibels_per_hash"></a>

#### decibels_per_hash

```python
@decibels_per_hash.setter
def decibels_per_hash(value: int) -> None
```

<a id="unreal.AudioMaterialMeterStyle.font"></a>

#### font

```python
@property
def font() -> SlateFontInfo
```

(SlateFontInfo):  [Read-Write] Font family and size to be used when displaying the meter scale.

<a id="unreal.AudioMaterialMeterStyle.font"></a>

#### font

```python
@font.setter
def font(value: SlateFontInfo) -> None
```

<a id="unreal.AudioMeterStyle"></a>