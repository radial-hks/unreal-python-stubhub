## ButtonStyle Objects

```python
class ButtonStyle(SlateWidgetStyle)
```

Represents the appearance of an SButton

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``disabled`` (SlateBrush):  [Read-Write] Button appearance when disabled, by default this is set to an invalid resource when that is the case default disabled drawing is used.
- ``disabled_foreground`` (SlateColor):  [Read-Write] Foreground Color when disabled
- ``hovered`` (SlateBrush):  [Read-Write] Button appearance when hovered
- ``hovered_foreground`` (SlateColor):  [Read-Write] Foreground Color when hovered
- ``hovered_slate_sound`` (SlateSound):  [Read-Write] The sound the button should play when initially hovered over
- ``normal`` (SlateBrush):  [Read-Write] Button appearance when the button is not hovered or pressed
- ``normal_foreground`` (SlateColor):  [Read-Write] Foreground Color when the button is not hovered or pressed
- ``normal_padding`` (Margin):  [Read-Write] Padding that accounts for the border in the button's background image.
  When this is applied, the content of the button should appear flush
  with the button's border. Use this padding when the button is not pressed.
- ``pressed`` (SlateBrush):  [Read-Write] Button appearance when pressed
- ``pressed_foreground`` (SlateColor):  [Read-Write] Foreground Color when pressed
- ``pressed_padding`` (Margin):  [Read-Write] Same as NormalPadding but used when the button is pressed. Allows for moving the content to match
  any "movement" in the button's border image.
- ``pressed_slate_sound`` (SlateSound):  [Read-Write] The sound the button should play when pressed

<a id="unreal.ButtonStyle.__init__"></a>

#### __init__

```python
def __init__(normal: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000],
                                    SlateColorStylingMode.USE_COLOR_SPECIFIED],
                                   SlateBrushDrawType.IMAGE,
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
             hovered: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000],
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
             pressed: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000],
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
             disabled: SlateBrush = [
                 [[1.000000, 1.000000, 1.000000, 1.000000],
                  SlateColorStylingMode.USE_COLOR_SPECIFIED],
                 SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE,
                 SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
                 [0.000000, 0.000000, 0.000000,
                  0.000000], None,
                 [[0.000000, 0.000000, 0.000000, 0.000000],
                  [[0.000000, 0.000000, 0.000000, 0.000000],
                   SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
                  SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
             ],
             normal_foreground: SlateColor = [
                 [1.000000, 0.000000, 1.000000,
                  1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED
             ],
             hovered_foreground: SlateColor = [
                 [1.000000, 0.000000, 1.000000,
                  1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED
             ],
             pressed_foreground: SlateColor = [
                 [1.000000, 0.000000, 1.000000,
                  1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED
             ],
             disabled_foreground: SlateColor = [
                 [1.000000, 0.000000, 1.000000,
                  1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED
             ],
             normal_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
             pressed_padding: Margin = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             pressed_slate_sound: SlateSound = [None],
             hovered_slate_sound: SlateSound = [None]) -> None
```

<a id="unreal.ButtonStyle.normal"></a>

#### normal

```python
@property
def normal() -> SlateBrush
```

(SlateBrush):  [Read-Write] Button appearance when the button is not hovered or pressed

<a id="unreal.ButtonStyle.normal"></a>

#### normal

```python
@normal.setter
def normal(value: SlateBrush) -> None
```

<a id="unreal.ButtonStyle.hovered"></a>

#### hovered

```python
@property
def hovered() -> SlateBrush
```

(SlateBrush):  [Read-Write] Button appearance when hovered

<a id="unreal.ButtonStyle.hovered"></a>

#### hovered

```python
@hovered.setter
def hovered(value: SlateBrush) -> None
```

<a id="unreal.ButtonStyle.pressed"></a>

#### pressed

```python
@property
def pressed() -> SlateBrush
```

(SlateBrush):  [Read-Write] Button appearance when pressed

<a id="unreal.ButtonStyle.pressed"></a>

#### pressed

```python
@pressed.setter
def pressed(value: SlateBrush) -> None
```

<a id="unreal.ButtonStyle.disabled"></a>

#### disabled

```python
@property
def disabled() -> SlateBrush
```

(SlateBrush):  [Read-Write] Button appearance when disabled, by default this is set to an invalid resource when that is the case default disabled drawing is used.

<a id="unreal.ButtonStyle.disabled"></a>

#### disabled

```python
@disabled.setter
def disabled(value: SlateBrush) -> None
```

<a id="unreal.ButtonStyle.normal_foreground"></a>

#### normal_foreground

```python
@property
def normal_foreground() -> SlateColor
```

(SlateColor):  [Read-Write] Foreground Color when the button is not hovered or pressed

<a id="unreal.ButtonStyle.normal_foreground"></a>

#### normal_foreground

```python
@normal_foreground.setter
def normal_foreground(value: SlateColor) -> None
```

<a id="unreal.ButtonStyle.hovered_foreground"></a>

#### hovered_foreground

```python
@property
def hovered_foreground() -> SlateColor
```

(SlateColor):  [Read-Write] Foreground Color when hovered

<a id="unreal.ButtonStyle.hovered_foreground"></a>

#### hovered_foreground

```python
@hovered_foreground.setter
def hovered_foreground(value: SlateColor) -> None
```

<a id="unreal.ButtonStyle.pressed_foreground"></a>

#### pressed_foreground

```python
@property
def pressed_foreground() -> SlateColor
```

(SlateColor):  [Read-Write] Foreground Color when pressed

<a id="unreal.ButtonStyle.pressed_foreground"></a>

#### pressed_foreground

```python
@pressed_foreground.setter
def pressed_foreground(value: SlateColor) -> None
```

<a id="unreal.ButtonStyle.disabled_foreground"></a>

#### disabled_foreground

```python
@property
def disabled_foreground() -> SlateColor
```

(SlateColor):  [Read-Write] Foreground Color when disabled

<a id="unreal.ButtonStyle.disabled_foreground"></a>

#### disabled_foreground

```python
@disabled_foreground.setter
def disabled_foreground(value: SlateColor) -> None
```

<a id="unreal.ButtonStyle.normal_padding"></a>

#### normal_padding

```python
@property
def normal_padding() -> Margin
```

(Margin):  [Read-Write] Padding that accounts for the border in the button's background image.
When this is applied, the content of the button should appear flush
with the button's border. Use this padding when the button is not pressed.

<a id="unreal.ButtonStyle.normal_padding"></a>

#### normal_padding

```python
@normal_padding.setter
def normal_padding(value: Margin) -> None
```

<a id="unreal.ButtonStyle.pressed_padding"></a>

#### pressed_padding

```python
@property
def pressed_padding() -> Margin
```

(Margin):  [Read-Write] Same as NormalPadding but used when the button is pressed. Allows for moving the content to match
any "movement" in the button's border image.

<a id="unreal.ButtonStyle.pressed_padding"></a>

#### pressed_padding

```python
@pressed_padding.setter
def pressed_padding(value: Margin) -> None
```

<a id="unreal.ButtonStyle.pressed_slate_sound"></a>

#### pressed_slate_sound

```python
@property
def pressed_slate_sound() -> SlateSound
```

(SlateSound):  [Read-Write] The sound the button should play when pressed

<a id="unreal.ButtonStyle.pressed_slate_sound"></a>

#### pressed_slate_sound

```python
@pressed_slate_sound.setter
def pressed_slate_sound(value: SlateSound) -> None
```

<a id="unreal.ButtonStyle.hovered_slate_sound"></a>

#### hovered_slate_sound

```python
@property
def hovered_slate_sound() -> SlateSound
```

(SlateSound):  [Read-Write] The sound the button should play when initially hovered over

<a id="unreal.ButtonStyle.hovered_slate_sound"></a>

#### hovered_slate_sound

```python
@hovered_slate_sound.setter
def hovered_slate_sound(value: SlateSound) -> None
```

<a id="unreal.SlateFontInfo"></a>