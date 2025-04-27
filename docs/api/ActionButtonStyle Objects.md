## ActionButtonStyle Objects

```python
class ActionButtonStyle(SlateWidgetStyle)
```

Represents the appearance of an SActionButton

**C++ Source:**

- **Module**: ToolWidgets
- **File**: ToolWidgetsSlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``action_button_type`` (Name):  [Read-Write] The type to use for our SActionButton.
- ``button_content_padding`` ('undefined'):  [Read-Write] Spacing between button's border and the content. Default uses ButtonStyle.
- ``button_style`` (ButtonStyle):  [Read-Write] The style to use for our SButton.
- ``combo_button_content_padding`` ('undefined'):  [Read-Write] Spacing between button's border and the content. Default uses ComboButtonStyle.
- ``combo_button_style`` (ComboButtonStyle):  [Read-Write] The style to use for our SComboButton.
- ``has_down_arrow`` (bool):  [Read-Write] Whether to show a down arrow for the combo button
- ``horizontal_content_alignment`` (HorizontalAlignment):  [Read-Write] Horizontal Content alignment within the button.
- ``icon_brush`` ('undefined'):  [Read-Write] Icon Brush to use.
- ``icon_button_style`` ('undefined'):  [Read-Write] The style to use for our SButton when an icon is present. ButtonStyle used if not specified.
- ``icon_color_and_opacity`` ('undefined'):  [Read-Write] Icon Color/Tint, defaults is determined by ActionButtonType.
- ``text_block_style`` (TextBlockStyle):  [Read-Write] The style to use for the button Text.

<a id="unreal.ActionButtonStyle.__init__"></a>

#### __init__

```python
def __init__(
    button_style: ButtonStyle = [
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
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
        [0.000000, 0.000000, 0.000000, 0.000000], [None], [None]
    ],
    button_content_padding: type = (),
    combo_button_style: ComboButtonStyle = [
        [[[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.IMAGE,
          SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
          [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
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
    has_down_arrow: bool = False,
    combo_button_content_padding: type = (),
    horizontal_content_alignment: HorizontalAlignment = HorizontalAlignment.
    H_ALIGN_FILL,
    text_block_style: TextBlockStyle = [
        [
            None, None,
            [
                0, False, False, False, None,
                [0.000000, 0.000000, 0.000000, 1.000000]
            ], "None", 24.000000, 0, 0.000000, False, False, 1.000000
        ],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], [0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000, 1.000000],
        [[0.000000, 0.000000, 0.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        TextTransformPolicy.NONE, TextOverflowPolicy.CLIP
    ],
    icon_brush: type = (),
    icon_color_and_opacity: type = (),
    action_button_type: Name = "None",
    icon_button_style: type = ()) -> None
```

<a id="unreal.ActionButtonStyle.button_style"></a>

#### button_style

```python
@property
def button_style() -> ButtonStyle
```

(ButtonStyle):  [Read-Write] The style to use for our SButton.

<a id="unreal.ActionButtonStyle.button_style"></a>

#### button_style

```python
@button_style.setter
def button_style(value: ButtonStyle) -> None
```

<a id="unreal.ActionButtonStyle.button_content_padding"></a>

#### button_content_padding

```python
@property
def button_content_padding() -> type
```

('undefined'):  [Read-Write] Spacing between button's border and the content. Default uses ButtonStyle.

<a id="unreal.ActionButtonStyle.button_content_padding"></a>

#### button_content_padding

```python
@button_content_padding.setter
def button_content_padding(value: type) -> None
```

<a id="unreal.ActionButtonStyle.combo_button_style"></a>

#### combo_button_style

```python
@property
def combo_button_style() -> ComboButtonStyle
```

(ComboButtonStyle):  [Read-Write] The style to use for our SComboButton.

<a id="unreal.ActionButtonStyle.combo_button_style"></a>

#### combo_button_style

```python
@combo_button_style.setter
def combo_button_style(value: ComboButtonStyle) -> None
```

<a id="unreal.ActionButtonStyle.has_down_arrow"></a>

#### has_down_arrow

```python
@property
def has_down_arrow() -> bool
```

(bool):  [Read-Write] Whether to show a down arrow for the combo button

<a id="unreal.ActionButtonStyle.has_down_arrow"></a>

#### has_down_arrow

```python
@has_down_arrow.setter
def has_down_arrow(value: bool) -> None
```

<a id="unreal.ActionButtonStyle.combo_button_content_padding"></a>

#### combo_button_content_padding

```python
@property
def combo_button_content_padding() -> type
```

('undefined'):  [Read-Write] Spacing between button's border and the content. Default uses ComboButtonStyle.

<a id="unreal.ActionButtonStyle.combo_button_content_padding"></a>

#### combo_button_content_padding

```python
@combo_button_content_padding.setter
def combo_button_content_padding(value: type) -> None
```

<a id="unreal.ActionButtonStyle.horizontal_content_alignment"></a>

#### horizontal_content_alignment

```python
@property
def horizontal_content_alignment() -> HorizontalAlignment
```

(HorizontalAlignment):  [Read-Write] Horizontal Content alignment within the button.

<a id="unreal.ActionButtonStyle.horizontal_content_alignment"></a>

#### horizontal_content_alignment

```python
@horizontal_content_alignment.setter
def horizontal_content_alignment(value: HorizontalAlignment) -> None
```

<a id="unreal.ActionButtonStyle.text_block_style"></a>

#### text_block_style

```python
@property
def text_block_style() -> TextBlockStyle
```

(TextBlockStyle):  [Read-Write] The style to use for the button Text.

<a id="unreal.ActionButtonStyle.text_block_style"></a>

#### text_block_style

```python
@text_block_style.setter
def text_block_style(value: TextBlockStyle) -> None
```

<a id="unreal.ActionButtonStyle.icon_brush"></a>

#### icon_brush

```python
@property
def icon_brush() -> type
```

('undefined'):  [Read-Write] Icon Brush to use.

<a id="unreal.ActionButtonStyle.icon_brush"></a>

#### icon_brush

```python
@icon_brush.setter
def icon_brush(value: type) -> None
```

<a id="unreal.ActionButtonStyle.icon_color_and_opacity"></a>

#### icon_color_and_opacity

```python
@property
def icon_color_and_opacity() -> type
```

('undefined'):  [Read-Write] Icon Color/Tint, defaults is determined by ActionButtonType.

<a id="unreal.ActionButtonStyle.icon_color_and_opacity"></a>

#### icon_color_and_opacity

```python
@icon_color_and_opacity.setter
def icon_color_and_opacity(value: type) -> None
```

<a id="unreal.ActionButtonStyle.action_button_type"></a>

#### action_button_type

```python
@property
def action_button_type() -> Name
```

(Name):  [Read-Write] The type to use for our SActionButton.

<a id="unreal.ActionButtonStyle.action_button_type"></a>

#### action_button_type

```python
@action_button_type.setter
def action_button_type(value: Name) -> None
```

<a id="unreal.ActionButtonStyle.icon_button_style"></a>

#### icon_button_style

```python
@property
def icon_button_style() -> type
```

('undefined'):  [Read-Write] The style to use for our SButton when an icon is present. ButtonStyle used if not specified.

<a id="unreal.ActionButtonStyle.icon_button_style"></a>

#### icon_button_style

```python
@icon_button_style.setter
def icon_button_style(value: type) -> None
```

<a id="unreal.PropertyPathTestBaseStruct"></a>