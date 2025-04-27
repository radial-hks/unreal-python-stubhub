## CheckBoxStyle Objects

```python
class CheckBoxStyle(SlateWidgetStyle)
```

Represents the appearance of an SCheckBox

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``background_hovered_image`` (SlateBrush):  [Read-Write] Background appearance when hovered
- ``background_image`` (SlateBrush):  [Read-Write] Background appearance
- ``background_pressed_image`` (SlateBrush):  [Read-Write] Background appearance when pressed
- ``border_background_color`` (SlateColor):  [Read-Write] BorderBackgroundColor refers to the actual color and opacity of the supplied border image on toggle buttons
- ``check_box_type`` (SlateCheckBoxType):  [Read-Write] The visual type of the checkbox
- ``checked_foreground`` (SlateColor):  [Read-Write] Foreground Color when checked
- ``checked_hovered_foreground`` (SlateColor):  [Read-Write] Foreground Color when checked and pressed
- ``checked_hovered_image`` (SlateBrush):  [Read-Write] CheckBox appearance when checked and hovered
- ``checked_image`` (SlateBrush):  [Read-Write] CheckBox appearance when the CheckBox is checked
- ``checked_pressed_foreground`` (SlateColor):  [Read-Write] Foreground Color when checked and pressed
- ``checked_pressed_image`` (SlateBrush):  [Read-Write] CheckBox appearance when checked and pressed
- ``checked_slate_sound`` (SlateSound):  [Read-Write] The sound the check box should play when checked
- ``foreground_color`` (SlateColor):  [Read-Write] The normal unchecked foreground color
- ``hovered_foreground`` (SlateColor):  [Read-Write] Foreground Color when hovered
- ``hovered_slate_sound`` (SlateSound):  [Read-Write] The sound the check box should play when initially hovered over
- ``padding`` (Margin):  [Read-Write] Padding
- ``pressed_foreground`` (SlateColor):  [Read-Write] Foreground Color when pressed
- ``unchecked_hovered_image`` (SlateBrush):  [Read-Write] CheckBox appearance when the CheckBox is unchecked and hovered
- ``unchecked_image`` (SlateBrush):  [Read-Write] CheckBox appearance when the CheckBox is unchecked (normal)
- ``unchecked_pressed_image`` (SlateBrush):  [Read-Write] CheckBox appearance when the CheckBox is unchecked and hovered
- ``unchecked_slate_sound`` (SlateSound):  [Read-Write] The sound the check box should play when unchecked
- ``undetermined_foreground`` (SlateColor):  [Read-Write] Foreground Color when the check state is indeterminate
- ``undetermined_hovered_image`` (SlateBrush):  [Read-Write] CheckBox appearance when CheckBox is undetermined and hovered
- ``undetermined_image`` (SlateBrush):  [Read-Write] CheckBox appearance when the CheckBox is undetermined
- ``undetermined_pressed_image`` (SlateBrush):  [Read-Write] CheckBox appearance when CheckBox is undetermined and pressed

<a id="unreal.CheckBoxStyle.__init__"></a>

#### __init__

```python
def __init__(check_box_type: SlateCheckBoxType = SlateCheckBoxType.CHECK_BOX,
             unchecked_image: SlateBrush = [
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
             unchecked_hovered_image: SlateBrush = [
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
             unchecked_pressed_image: SlateBrush = [
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
             checked_image: SlateBrush = [
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
             checked_hovered_image: SlateBrush = [
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
             checked_pressed_image: SlateBrush = [
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
             undetermined_image: SlateBrush = [
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
             undetermined_hovered_image: SlateBrush = [
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
             undetermined_pressed_image: SlateBrush = [
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
             padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
             background_image: SlateBrush = [
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
             background_hovered_image: SlateBrush = [
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
             background_pressed_image: SlateBrush = [
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
             foreground_color: SlateColor = [[
                 1.000000, 0.000000, 1.000000, 1.000000
             ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
             hovered_foreground: SlateColor = [[
                 1.000000, 0.000000, 1.000000, 1.000000
             ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
             pressed_foreground: SlateColor = [[
                 1.000000, 0.000000, 1.000000, 1.000000
             ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
             checked_foreground: SlateColor = [[
                 1.000000, 0.000000, 1.000000, 1.000000
             ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
             checked_hovered_foreground: SlateColor = [[
                 1.000000, 0.000000, 1.000000, 1.000000
             ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
             checked_pressed_foreground: SlateColor = [[
                 1.000000, 0.000000, 1.000000, 1.000000
             ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
             undetermined_foreground: SlateColor = [[
                 1.000000, 0.000000, 1.000000, 1.000000
             ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
             border_background_color: SlateColor = [[
                 1.000000, 0.000000, 1.000000, 1.000000
             ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
             checked_slate_sound: SlateSound = [None],
             unchecked_slate_sound: SlateSound = [None],
             hovered_slate_sound: SlateSound = [None]) -> None
```

<a id="unreal.CheckBoxStyle.check_box_type"></a>

#### check_box_type

```python
@property
def check_box_type() -> SlateCheckBoxType
```

(SlateCheckBoxType):  [Read-Write] The visual type of the checkbox

<a id="unreal.CheckBoxStyle.check_box_type"></a>

#### check_box_type

```python
@check_box_type.setter
def check_box_type(value: SlateCheckBoxType) -> None
```

<a id="unreal.CheckBoxStyle.unchecked_image"></a>

#### unchecked_image

```python
@property
def unchecked_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] CheckBox appearance when the CheckBox is unchecked (normal)

<a id="unreal.CheckBoxStyle.unchecked_image"></a>

#### unchecked_image

```python
@unchecked_image.setter
def unchecked_image(value: SlateBrush) -> None
```

<a id="unreal.CheckBoxStyle.unchecked_hovered_image"></a>

#### unchecked_hovered_image

```python
@property
def unchecked_hovered_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] CheckBox appearance when the CheckBox is unchecked and hovered

<a id="unreal.CheckBoxStyle.unchecked_hovered_image"></a>

#### unchecked_hovered_image

```python
@unchecked_hovered_image.setter
def unchecked_hovered_image(value: SlateBrush) -> None
```

<a id="unreal.CheckBoxStyle.unchecked_pressed_image"></a>

#### unchecked_pressed_image

```python
@property
def unchecked_pressed_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] CheckBox appearance when the CheckBox is unchecked and hovered

<a id="unreal.CheckBoxStyle.unchecked_pressed_image"></a>

#### unchecked_pressed_image

```python
@unchecked_pressed_image.setter
def unchecked_pressed_image(value: SlateBrush) -> None
```

<a id="unreal.CheckBoxStyle.checked_image"></a>

#### checked_image

```python
@property
def checked_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] CheckBox appearance when the CheckBox is checked

<a id="unreal.CheckBoxStyle.checked_image"></a>

#### checked_image

```python
@checked_image.setter
def checked_image(value: SlateBrush) -> None
```

<a id="unreal.CheckBoxStyle.checked_hovered_image"></a>

#### checked_hovered_image

```python
@property
def checked_hovered_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] CheckBox appearance when checked and hovered

<a id="unreal.CheckBoxStyle.checked_hovered_image"></a>

#### checked_hovered_image

```python
@checked_hovered_image.setter
def checked_hovered_image(value: SlateBrush) -> None
```

<a id="unreal.CheckBoxStyle.checked_pressed_image"></a>

#### checked_pressed_image

```python
@property
def checked_pressed_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] CheckBox appearance when checked and pressed

<a id="unreal.CheckBoxStyle.checked_pressed_image"></a>

#### checked_pressed_image

```python
@checked_pressed_image.setter
def checked_pressed_image(value: SlateBrush) -> None
```

<a id="unreal.CheckBoxStyle.undetermined_image"></a>

#### undetermined_image

```python
@property
def undetermined_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] CheckBox appearance when the CheckBox is undetermined

<a id="unreal.CheckBoxStyle.undetermined_image"></a>

#### undetermined_image

```python
@undetermined_image.setter
def undetermined_image(value: SlateBrush) -> None
```

<a id="unreal.CheckBoxStyle.undetermined_hovered_image"></a>

#### undetermined_hovered_image

```python
@property
def undetermined_hovered_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] CheckBox appearance when CheckBox is undetermined and hovered

<a id="unreal.CheckBoxStyle.undetermined_hovered_image"></a>

#### undetermined_hovered_image

```python
@undetermined_hovered_image.setter
def undetermined_hovered_image(value: SlateBrush) -> None
```

<a id="unreal.CheckBoxStyle.undetermined_pressed_image"></a>

#### undetermined_pressed_image

```python
@property
def undetermined_pressed_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] CheckBox appearance when CheckBox is undetermined and pressed

<a id="unreal.CheckBoxStyle.undetermined_pressed_image"></a>

#### undetermined_pressed_image

```python
@undetermined_pressed_image.setter
def undetermined_pressed_image(value: SlateBrush) -> None
```

<a id="unreal.CheckBoxStyle.padding"></a>

#### padding

```python
@property
def padding() -> Margin
```

(Margin):  [Read-Write] Padding

<a id="unreal.CheckBoxStyle.padding"></a>

#### padding

```python
@padding.setter
def padding(value: Margin) -> None
```

<a id="unreal.CheckBoxStyle.background_image"></a>

#### background_image

```python
@property
def background_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Background appearance

<a id="unreal.CheckBoxStyle.background_image"></a>

#### background_image

```python
@background_image.setter
def background_image(value: SlateBrush) -> None
```

<a id="unreal.CheckBoxStyle.background_hovered_image"></a>

#### background_hovered_image

```python
@property
def background_hovered_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Background appearance when hovered

<a id="unreal.CheckBoxStyle.background_hovered_image"></a>

#### background_hovered_image

```python
@background_hovered_image.setter
def background_hovered_image(value: SlateBrush) -> None
```

<a id="unreal.CheckBoxStyle.background_pressed_image"></a>

#### background_pressed_image

```python
@property
def background_pressed_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Background appearance when pressed

<a id="unreal.CheckBoxStyle.background_pressed_image"></a>

#### background_pressed_image

```python
@background_pressed_image.setter
def background_pressed_image(value: SlateBrush) -> None
```

<a id="unreal.CheckBoxStyle.foreground_color"></a>

#### foreground_color

```python
@property
def foreground_color() -> SlateColor
```

(SlateColor):  [Read-Write] The normal unchecked foreground color

<a id="unreal.CheckBoxStyle.foreground_color"></a>

#### foreground_color

```python
@foreground_color.setter
def foreground_color(value: SlateColor) -> None
```

<a id="unreal.CheckBoxStyle.hovered_foreground"></a>

#### hovered_foreground

```python
@property
def hovered_foreground() -> SlateColor
```

(SlateColor):  [Read-Write] Foreground Color when hovered

<a id="unreal.CheckBoxStyle.hovered_foreground"></a>

#### hovered_foreground

```python
@hovered_foreground.setter
def hovered_foreground(value: SlateColor) -> None
```

<a id="unreal.CheckBoxStyle.pressed_foreground"></a>

#### pressed_foreground

```python
@property
def pressed_foreground() -> SlateColor
```

(SlateColor):  [Read-Write] Foreground Color when pressed

<a id="unreal.CheckBoxStyle.pressed_foreground"></a>

#### pressed_foreground

```python
@pressed_foreground.setter
def pressed_foreground(value: SlateColor) -> None
```

<a id="unreal.CheckBoxStyle.checked_foreground"></a>

#### checked_foreground

```python
@property
def checked_foreground() -> SlateColor
```

(SlateColor):  [Read-Write] Foreground Color when checked

<a id="unreal.CheckBoxStyle.checked_foreground"></a>

#### checked_foreground

```python
@checked_foreground.setter
def checked_foreground(value: SlateColor) -> None
```

<a id="unreal.CheckBoxStyle.checked_hovered_foreground"></a>

#### checked_hovered_foreground

```python
@property
def checked_hovered_foreground() -> SlateColor
```

(SlateColor):  [Read-Write] Foreground Color when checked and pressed

<a id="unreal.CheckBoxStyle.checked_hovered_foreground"></a>

#### checked_hovered_foreground

```python
@checked_hovered_foreground.setter
def checked_hovered_foreground(value: SlateColor) -> None
```

<a id="unreal.CheckBoxStyle.checked_pressed_foreground"></a>

#### checked_pressed_foreground

```python
@property
def checked_pressed_foreground() -> SlateColor
```

(SlateColor):  [Read-Write] Foreground Color when checked and pressed

<a id="unreal.CheckBoxStyle.checked_pressed_foreground"></a>

#### checked_pressed_foreground

```python
@checked_pressed_foreground.setter
def checked_pressed_foreground(value: SlateColor) -> None
```

<a id="unreal.CheckBoxStyle.undetermined_foreground"></a>

#### undetermined_foreground

```python
@property
def undetermined_foreground() -> SlateColor
```

(SlateColor):  [Read-Write] Foreground Color when the check state is indeterminate

<a id="unreal.CheckBoxStyle.undetermined_foreground"></a>

#### undetermined_foreground

```python
@undetermined_foreground.setter
def undetermined_foreground(value: SlateColor) -> None
```

<a id="unreal.CheckBoxStyle.border_background_color"></a>

#### border_background_color

```python
@property
def border_background_color() -> SlateColor
```

(SlateColor):  [Read-Write] BorderBackgroundColor refers to the actual color and opacity of the supplied border image on toggle buttons

<a id="unreal.CheckBoxStyle.border_background_color"></a>

#### border_background_color

```python
@border_background_color.setter
def border_background_color(value: SlateColor) -> None
```

<a id="unreal.CheckBoxStyle.checked_slate_sound"></a>

#### checked_slate_sound

```python
@property
def checked_slate_sound() -> SlateSound
```

(SlateSound):  [Read-Write] The sound the check box should play when checked

<a id="unreal.CheckBoxStyle.checked_slate_sound"></a>

#### checked_slate_sound

```python
@checked_slate_sound.setter
def checked_slate_sound(value: SlateSound) -> None
```

<a id="unreal.CheckBoxStyle.unchecked_slate_sound"></a>

#### unchecked_slate_sound

```python
@property
def unchecked_slate_sound() -> SlateSound
```

(SlateSound):  [Read-Write] The sound the check box should play when unchecked

<a id="unreal.CheckBoxStyle.unchecked_slate_sound"></a>

#### unchecked_slate_sound

```python
@unchecked_slate_sound.setter
def unchecked_slate_sound(value: SlateSound) -> None
```

<a id="unreal.CheckBoxStyle.hovered_slate_sound"></a>

#### hovered_slate_sound

```python
@property
def hovered_slate_sound() -> SlateSound
```

(SlateSound):  [Read-Write] The sound the check box should play when initially hovered over

<a id="unreal.CheckBoxStyle.hovered_slate_sound"></a>

#### hovered_slate_sound

```python
@hovered_slate_sound.setter
def hovered_slate_sound(value: SlateSound) -> None
```

<a id="unreal.HyperlinkStyle"></a>