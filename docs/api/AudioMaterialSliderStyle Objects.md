## AudioMaterialSliderStyle Objects

```python
class AudioMaterialSliderStyle(AudioMaterialWidgetStyle)
```

Represents the appearance of an Audio Material Slider

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioMaterialSlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desired_size`` (Vector2f):  [Read-Write] Desired Draw size of the rendered material
- ``material`` (MaterialInterface):  [Read-Write] Material used to render the Slate
- ``slider_background_accent_color`` (LinearColor):  [Read-Write] The slider Bar's Background Accent color value. Can be thought as the slider's Inner Shadow color value.
- ``slider_background_color`` (LinearColor):  [Read-Write] The slider Bar's Background color value.
- ``slider_handle_main_color`` (LinearColor):  [Read-Write] The slider Handle's Main color value.
- ``slider_handle_outline_color`` (LinearColor):  [Read-Write] The slider Handle's Outline color value.
- ``slider_value_main_color`` (LinearColor):  [Read-Write] The slider's Color value representing the slider's Output Value amount.
- ``text_box_style`` (AudioTextBoxStyle):  [Read-Write] The style to use for the audio text box widget.

<a id="unreal.AudioMaterialSliderStyle.__init__"></a>

#### __init__

```python
def __init__(
    material: MaterialInterface = None,
    desired_size: Vector2f = [0.000000, 0.000000],
    slider_background_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    slider_background_accent_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    slider_value_main_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    slider_handle_main_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    slider_handle_outline_color: LinearColor = [
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

<a id="unreal.AudioMaterialSliderStyle.slider_background_color"></a>

#### slider_background_color

```python
@property
def slider_background_color() -> LinearColor
```

(LinearColor):  [Read-Write] The slider Bar's Background color value.

<a id="unreal.AudioMaterialSliderStyle.slider_background_color"></a>

#### slider_background_color

```python
@slider_background_color.setter
def slider_background_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialSliderStyle.slider_background_accent_color"></a>

#### slider_background_accent_color

```python
@property
def slider_background_accent_color() -> LinearColor
```

(LinearColor):  [Read-Write] The slider Bar's Background Accent color value. Can be thought as the slider's Inner Shadow color value.

<a id="unreal.AudioMaterialSliderStyle.slider_background_accent_color"></a>

#### slider_background_accent_color

```python
@slider_background_accent_color.setter
def slider_background_accent_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialSliderStyle.slider_value_main_color"></a>

#### slider_value_main_color

```python
@property
def slider_value_main_color() -> LinearColor
```

(LinearColor):  [Read-Write] The slider's Color value representing the slider's Output Value amount.

<a id="unreal.AudioMaterialSliderStyle.slider_value_main_color"></a>

#### slider_value_main_color

```python
@slider_value_main_color.setter
def slider_value_main_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialSliderStyle.slider_handle_main_color"></a>

#### slider_handle_main_color

```python
@property
def slider_handle_main_color() -> LinearColor
```

(LinearColor):  [Read-Write] The slider Handle's Main color value.

<a id="unreal.AudioMaterialSliderStyle.slider_handle_main_color"></a>

#### slider_handle_main_color

```python
@slider_handle_main_color.setter
def slider_handle_main_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialSliderStyle.slider_handle_outline_color"></a>

#### slider_handle_outline_color

```python
@property
def slider_handle_outline_color() -> LinearColor
```

(LinearColor):  [Read-Write] The slider Handle's Outline color value.

<a id="unreal.AudioMaterialSliderStyle.slider_handle_outline_color"></a>

#### slider_handle_outline_color

```python
@slider_handle_outline_color.setter
def slider_handle_outline_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialSliderStyle.text_box_style"></a>

#### text_box_style

```python
@property
def text_box_style() -> AudioTextBoxStyle
```

(AudioTextBoxStyle):  [Read-Write] The style to use for the audio text box widget.

<a id="unreal.AudioMaterialSliderStyle.text_box_style"></a>

#### text_box_style

```python
@text_box_style.setter
def text_box_style(value: AudioTextBoxStyle) -> None
```

<a id="unreal.AudioTextBoxStyle"></a>