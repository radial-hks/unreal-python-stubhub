## ComboBoxStyle Objects

```python
class ComboBoxStyle(SlateWidgetStyle)
```

Represents the appearance of an SComboBox

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``combo_button_style`` (ComboButtonStyle):  [Read-Write] The style to use for our SComboButton
- ``content_padding`` (Margin):  [Read-Write] * Button Content Padding
- ``menu_row_padding`` (Margin):  [Read-Write] * Menu Row Padding
- ``pressed_slate_sound`` (SlateSound):  [Read-Write] The sound the button should play when pressed
- ``selection_change_slate_sound`` (SlateSound):  [Read-Write] The Sound to play when the selection is changed

<a id="unreal.ComboBoxStyle.__init__"></a>

#### __init__

```python
def __init__(
    combo_button_style: ComboButtonStyle = [
        [[[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         [[1.000000, 0.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_FOREGROUND],
         [[1.000000, 0.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_FOREGROUND],
         [[1.000000, 0.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_FOREGROUND],
         [[1.000000, 0.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_FOREGROUND],
         [0.000000, 0.000000, 0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000, 0.000000], [None], [None]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 1.000000],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [0.000000, 0.000000, 0.000000, 0.000000],
        [5.000000, 5.000000, 5.000000, 5.000000],
        [2.000000, 2.000000, 2.000000,
         2.000000], VerticalAlignment.V_ALIGN_CENTER
    ],
    pressed_slate_sound: SlateSound = [None],
    selection_change_slate_sound: SlateSound = [None],
    content_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
    menu_row_padding: Margin = [0.000000, 0.000000, 0.000000,
                                0.000000]) -> None
```

<a id="unreal.ComboBoxStyle.combo_button_style"></a>

#### combo_button_style

```python
@property
def combo_button_style() -> ComboButtonStyle
```

(ComboButtonStyle):  [Read-Write] The style to use for our SComboButton

<a id="unreal.ComboBoxStyle.combo_button_style"></a>

#### combo_button_style

```python
@combo_button_style.setter
def combo_button_style(value: ComboButtonStyle) -> None
```

<a id="unreal.ComboBoxStyle.pressed_slate_sound"></a>

#### pressed_slate_sound

```python
@property
def pressed_slate_sound() -> SlateSound
```

(SlateSound):  [Read-Write] The sound the button should play when pressed

<a id="unreal.ComboBoxStyle.pressed_slate_sound"></a>

#### pressed_slate_sound

```python
@pressed_slate_sound.setter
def pressed_slate_sound(value: SlateSound) -> None
```

<a id="unreal.ComboBoxStyle.selection_change_slate_sound"></a>

#### selection_change_slate_sound

```python
@property
def selection_change_slate_sound() -> SlateSound
```

(SlateSound):  [Read-Write] The Sound to play when the selection is changed

<a id="unreal.ComboBoxStyle.selection_change_slate_sound"></a>

#### selection_change_slate_sound

```python
@selection_change_slate_sound.setter
def selection_change_slate_sound(value: SlateSound) -> None
```

<a id="unreal.ComboBoxStyle.content_padding"></a>

#### content_padding

```python
@property
def content_padding() -> Margin
```

(Margin):  [Read-Write] * Button Content Padding

<a id="unreal.ComboBoxStyle.content_padding"></a>

#### content_padding

```python
@content_padding.setter
def content_padding(value: Margin) -> None
```

<a id="unreal.ComboBoxStyle.menu_row_padding"></a>

#### menu_row_padding

```python
@property
def menu_row_padding() -> Margin
```

(Margin):  [Read-Write] * Menu Row Padding

<a id="unreal.ComboBoxStyle.menu_row_padding"></a>

#### menu_row_padding

```python
@menu_row_padding.setter
def menu_row_padding(value: Margin) -> None
```

<a id="unreal.SlateSound"></a>