## AudioMaterialButtonStyle Objects

```python
class AudioMaterialButtonStyle(AudioMaterialWidgetStyle)
```

Represents the appearance of an Audio Material Button

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioMaterialSlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``button_accent_color`` (LinearColor):  [Read-Write] The button's Accent color value.
- ``button_main_color`` (LinearColor):  [Read-Write] The button's Main color value.
- ``button_main_color_tint_1`` (LinearColor):  [Read-Write] The button color's Tint value covering one half of the gradient.
- ``button_main_color_tint_2`` (LinearColor):  [Read-Write] The button color's Tint value covering the other half of the gradient.
- ``button_pressed_outline_color`` (LinearColor):  [Read-Write] The button's Outline color value when Pressed.
- ``button_shadow_color`` (LinearColor):  [Read-Write] The button's Shadow color value.
- ``button_unpressed_outline_color`` (LinearColor):  [Read-Write] The button's Outline color value when Unpressed.
- ``desired_size`` (Vector2f):  [Read-Write] Desired Draw size of the rendered material
- ``material`` (MaterialInterface):  [Read-Write] Material used to render the Slate

<a id="unreal.AudioMaterialButtonStyle.__init__"></a>

#### __init__

```python
def __init__(
    material: MaterialInterface = None,
    desired_size: Vector2f = [0.000000, 0.000000],
    button_main_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    button_main_color_tint_1: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    button_main_color_tint_2: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    button_accent_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    button_shadow_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    button_unpressed_outline_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    button_pressed_outline_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ]
) -> None
```

<a id="unreal.AudioMaterialButtonStyle.button_main_color"></a>

#### button_main_color

```python
@property
def button_main_color() -> LinearColor
```

(LinearColor):  [Read-Write] The button's Main color value.

<a id="unreal.AudioMaterialButtonStyle.button_main_color"></a>

#### button_main_color

```python
@button_main_color.setter
def button_main_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialButtonStyle.button_main_color_tint_1"></a>

#### button_main_color_tint_1

```python
@property
def button_main_color_tint_1() -> LinearColor
```

(LinearColor):  [Read-Write] The button color's Tint value covering one half of the gradient.

<a id="unreal.AudioMaterialButtonStyle.button_main_color_tint_1"></a>

#### button_main_color_tint_1

```python
@button_main_color_tint_1.setter
def button_main_color_tint_1(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialButtonStyle.button_main_color_tint_2"></a>

#### button_main_color_tint_2

```python
@property
def button_main_color_tint_2() -> LinearColor
```

(LinearColor):  [Read-Write] The button color's Tint value covering the other half of the gradient.

<a id="unreal.AudioMaterialButtonStyle.button_main_color_tint_2"></a>

#### button_main_color_tint_2

```python
@button_main_color_tint_2.setter
def button_main_color_tint_2(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialButtonStyle.button_accent_color"></a>

#### button_accent_color

```python
@property
def button_accent_color() -> LinearColor
```

(LinearColor):  [Read-Write] The button's Accent color value.

<a id="unreal.AudioMaterialButtonStyle.button_accent_color"></a>

#### button_accent_color

```python
@button_accent_color.setter
def button_accent_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialButtonStyle.button_shadow_color"></a>

#### button_shadow_color

```python
@property
def button_shadow_color() -> LinearColor
```

(LinearColor):  [Read-Write] The button's Shadow color value.

<a id="unreal.AudioMaterialButtonStyle.button_shadow_color"></a>

#### button_shadow_color

```python
@button_shadow_color.setter
def button_shadow_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialButtonStyle.button_unpressed_outline_color"></a>

#### button_unpressed_outline_color

```python
@property
def button_unpressed_outline_color() -> LinearColor
```

(LinearColor):  [Read-Write] The button's Outline color value when Unpressed.

<a id="unreal.AudioMaterialButtonStyle.button_unpressed_outline_color"></a>

#### button_unpressed_outline_color

```python
@button_unpressed_outline_color.setter
def button_unpressed_outline_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialButtonStyle.button_pressed_outline_color"></a>

#### button_pressed_outline_color

```python
@property
def button_pressed_outline_color() -> LinearColor
```

(LinearColor):  [Read-Write] The button's Outline color value when Pressed.

<a id="unreal.AudioMaterialButtonStyle.button_pressed_outline_color"></a>

#### button_pressed_outline_color

```python
@button_pressed_outline_color.setter
def button_pressed_outline_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialSliderStyle"></a>