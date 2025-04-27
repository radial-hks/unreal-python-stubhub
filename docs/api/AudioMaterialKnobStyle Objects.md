## AudioMaterialKnobStyle Objects

```python
class AudioMaterialKnobStyle(AudioMaterialWidgetStyle)
```

Represents the appearance of an Audio Material Knob

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioMaterialSlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desired_size`` (Vector2f):  [Read-Write] Desired Draw size of the rendered material
- ``knob_accent_color`` (LinearColor):  [Read-Write] The knob's Accent color value.
- ``knob_bar_color`` (LinearColor):  [Read-Write] The knob Bar's Color value.
- ``knob_bar_fill_max_color`` (LinearColor):  [Read-Write] The knob Bar's Fill color value representing the Ending section of the fill.
- ``knob_bar_fill_mid_color`` (LinearColor):  [Read-Write] The knob Bar's Fill color value representing the Middle section of the fill.
- ``knob_bar_fill_min_color`` (LinearColor):  [Read-Write] The knob Bar's Fill color value representing the Starting section of the fill.
- ``knob_bar_fill_tint_color`` (LinearColor):  [Read-Write] The knob Bar Fill color's Tint value.
- ``knob_bar_shadow_color`` (LinearColor):  [Read-Write] The knob Bar's Shadow color value.
- ``knob_edge_fill_color`` (LinearColor):  [Read-Write] The knob's Edge Fill color value.
- ``knob_indicator_dot_color`` (LinearColor):  [Read-Write] The knob's Indicator Dot color value.
- ``knob_main_color`` (LinearColor):  [Read-Write] The knob's Main color value.
- ``knob_shadow_color`` (LinearColor):  [Read-Write] The knob's Shadow color value.
- ``knob_smooth_bevel_color`` (LinearColor):  [Read-Write] The knob's Smooth Bevel color value.
- ``material`` (MaterialInterface):  [Read-Write] Material used to render the Slate
- ``text_box_style`` (AudioTextBoxStyle):  [Read-Write] The style to use for the audio text box widget.

<a id="unreal.AudioMaterialKnobStyle.__init__"></a>

#### __init__

```python
def __init__(
    material: MaterialInterface = None,
    desired_size: Vector2f = [0.000000, 0.000000],
    knob_main_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    knob_accent_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    knob_shadow_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    knob_smooth_bevel_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    knob_indicator_dot_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    knob_edge_fill_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    knob_bar_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    knob_bar_shadow_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    knob_bar_fill_min_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    knob_bar_fill_mid_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    knob_bar_fill_max_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    knob_bar_fill_tint_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
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
    ]
) -> None
```

<a id="unreal.AudioMaterialKnobStyle.knob_main_color"></a>

#### knob_main_color

```python
@property
def knob_main_color() -> LinearColor
```

(LinearColor):  [Read-Write] The knob's Main color value.

<a id="unreal.AudioMaterialKnobStyle.knob_main_color"></a>

#### knob_main_color

```python
@knob_main_color.setter
def knob_main_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialKnobStyle.knob_accent_color"></a>

#### knob_accent_color

```python
@property
def knob_accent_color() -> LinearColor
```

(LinearColor):  [Read-Write] The knob's Accent color value.

<a id="unreal.AudioMaterialKnobStyle.knob_accent_color"></a>

#### knob_accent_color

```python
@knob_accent_color.setter
def knob_accent_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialKnobStyle.knob_shadow_color"></a>

#### knob_shadow_color

```python
@property
def knob_shadow_color() -> LinearColor
```

(LinearColor):  [Read-Write] The knob's Shadow color value.

<a id="unreal.AudioMaterialKnobStyle.knob_shadow_color"></a>

#### knob_shadow_color

```python
@knob_shadow_color.setter
def knob_shadow_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialKnobStyle.knob_smooth_bevel_color"></a>

#### knob_smooth_bevel_color

```python
@property
def knob_smooth_bevel_color() -> LinearColor
```

(LinearColor):  [Read-Write] The knob's Smooth Bevel color value.

<a id="unreal.AudioMaterialKnobStyle.knob_smooth_bevel_color"></a>

#### knob_smooth_bevel_color

```python
@knob_smooth_bevel_color.setter
def knob_smooth_bevel_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialKnobStyle.knob_indicator_dot_color"></a>

#### knob_indicator_dot_color

```python
@property
def knob_indicator_dot_color() -> LinearColor
```

(LinearColor):  [Read-Write] The knob's Indicator Dot color value.

<a id="unreal.AudioMaterialKnobStyle.knob_indicator_dot_color"></a>

#### knob_indicator_dot_color

```python
@knob_indicator_dot_color.setter
def knob_indicator_dot_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialKnobStyle.knob_edge_fill_color"></a>

#### knob_edge_fill_color

```python
@property
def knob_edge_fill_color() -> LinearColor
```

(LinearColor):  [Read-Write] The knob's Edge Fill color value.

<a id="unreal.AudioMaterialKnobStyle.knob_edge_fill_color"></a>

#### knob_edge_fill_color

```python
@knob_edge_fill_color.setter
def knob_edge_fill_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialKnobStyle.knob_bar_color"></a>

#### knob_bar_color

```python
@property
def knob_bar_color() -> LinearColor
```

(LinearColor):  [Read-Write] The knob Bar's Color value.

<a id="unreal.AudioMaterialKnobStyle.knob_bar_color"></a>

#### knob_bar_color

```python
@knob_bar_color.setter
def knob_bar_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialKnobStyle.knob_bar_shadow_color"></a>

#### knob_bar_shadow_color

```python
@property
def knob_bar_shadow_color() -> LinearColor
```

(LinearColor):  [Read-Write] The knob Bar's Shadow color value.

<a id="unreal.AudioMaterialKnobStyle.knob_bar_shadow_color"></a>

#### knob_bar_shadow_color

```python
@knob_bar_shadow_color.setter
def knob_bar_shadow_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialKnobStyle.knob_bar_fill_min_color"></a>

#### knob_bar_fill_min_color

```python
@property
def knob_bar_fill_min_color() -> LinearColor
```

(LinearColor):  [Read-Write] The knob Bar's Fill color value representing the Starting section of the fill.

<a id="unreal.AudioMaterialKnobStyle.knob_bar_fill_min_color"></a>

#### knob_bar_fill_min_color

```python
@knob_bar_fill_min_color.setter
def knob_bar_fill_min_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialKnobStyle.knob_bar_fill_mid_color"></a>

#### knob_bar_fill_mid_color

```python
@property
def knob_bar_fill_mid_color() -> LinearColor
```

(LinearColor):  [Read-Write] The knob Bar's Fill color value representing the Middle section of the fill.

<a id="unreal.AudioMaterialKnobStyle.knob_bar_fill_mid_color"></a>

#### knob_bar_fill_mid_color

```python
@knob_bar_fill_mid_color.setter
def knob_bar_fill_mid_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialKnobStyle.knob_bar_fill_max_color"></a>

#### knob_bar_fill_max_color

```python
@property
def knob_bar_fill_max_color() -> LinearColor
```

(LinearColor):  [Read-Write] The knob Bar's Fill color value representing the Ending section of the fill.

<a id="unreal.AudioMaterialKnobStyle.knob_bar_fill_max_color"></a>

#### knob_bar_fill_max_color

```python
@knob_bar_fill_max_color.setter
def knob_bar_fill_max_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialKnobStyle.knob_bar_fill_tint_color"></a>

#### knob_bar_fill_tint_color

```python
@property
def knob_bar_fill_tint_color() -> LinearColor
```

(LinearColor):  [Read-Write] The knob Bar Fill color's Tint value.

<a id="unreal.AudioMaterialKnobStyle.knob_bar_fill_tint_color"></a>

#### knob_bar_fill_tint_color

```python
@knob_bar_fill_tint_color.setter
def knob_bar_fill_tint_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialKnobStyle.text_box_style"></a>

#### text_box_style

```python
@property
def text_box_style() -> AudioTextBoxStyle
```

(AudioTextBoxStyle):  [Read-Write] The style to use for the audio text box widget.

<a id="unreal.AudioMaterialKnobStyle.text_box_style"></a>

#### text_box_style

```python
@text_box_style.setter
def text_box_style(value: AudioTextBoxStyle) -> None
```

<a id="unreal.AudioMaterialEnvelopeStyle"></a>