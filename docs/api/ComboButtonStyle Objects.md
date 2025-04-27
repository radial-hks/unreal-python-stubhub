## ComboButtonStyle Objects

```python
class ComboButtonStyle(SlateWidgetStyle)
```

Represents the appearance of an SComboButton

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``button_style`` (ButtonStyle):  [Read-Write] The style to use for our SButton.
- ``content_padding`` (Margin):  [Read-Write] * Button Content Padding
- ``down_arrow_align`` (VerticalAlignment):  [Read-Write] * Dropdown arrow vertical alignment
- ``down_arrow_image`` (SlateBrush):  [Read-Write] Image to use for the down arrow.
- ``down_arrow_padding`` (Margin):  [Read-Write] * Dropdown arrow padding (if a dropdown arrow exists)
- ``menu_border_brush`` (SlateBrush):  [Read-Write] Brush to use to add a "menu border" around the drop-down content.
- ``menu_border_padding`` (Margin):  [Read-Write] Padding to use to add a "menu border" around the drop-down content.
- ``shadow_color_and_opacity`` (LinearColor):  [Read-Write] The color and opacity of the shadow for the down arrow.
  Only active if ShadowOffset is not (0,0).
- ``shadow_offset`` (DeprecateSlateVector2D):  [Read-Write] How much should the shadow be offset for the down arrow?
  An offset of 0 implies no shadow.

<a id="unreal.ComboButtonStyle.__init__"></a>

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
    down_arrow_image: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000],
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
    shadow_offset: DeprecateSlateVector2D = [0.000000, 0.000000],
    shadow_color_and_opacity: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    menu_border_brush: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    menu_border_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
    content_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
    down_arrow_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
    down_arrow_align: VerticalAlignment = VerticalAlignment.V_ALIGN_FILL
) -> None
```

<a id="unreal.ComboButtonStyle.button_style"></a>

#### button_style

```python
@property
def button_style() -> ButtonStyle
```

(ButtonStyle):  [Read-Write] The style to use for our SButton.

<a id="unreal.ComboButtonStyle.button_style"></a>

#### button_style

```python
@button_style.setter
def button_style(value: ButtonStyle) -> None
```

<a id="unreal.ComboButtonStyle.down_arrow_image"></a>

#### down_arrow_image

```python
@property
def down_arrow_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to use for the down arrow.

<a id="unreal.ComboButtonStyle.down_arrow_image"></a>

#### down_arrow_image

```python
@down_arrow_image.setter
def down_arrow_image(value: SlateBrush) -> None
```

<a id="unreal.ComboButtonStyle.shadow_offset"></a>

#### shadow_offset

```python
@property
def shadow_offset() -> DeprecateSlateVector2D
```

(DeprecateSlateVector2D):  [Read-Write] How much should the shadow be offset for the down arrow?
An offset of 0 implies no shadow.

<a id="unreal.ComboButtonStyle.shadow_offset"></a>

#### shadow_offset

```python
@shadow_offset.setter
def shadow_offset(value: DeprecateSlateVector2D) -> None
```

<a id="unreal.ComboButtonStyle.shadow_color_and_opacity"></a>

#### shadow_color_and_opacity

```python
@property
def shadow_color_and_opacity() -> LinearColor
```

(LinearColor):  [Read-Write] The color and opacity of the shadow for the down arrow.
Only active if ShadowOffset is not (0,0).

<a id="unreal.ComboButtonStyle.shadow_color_and_opacity"></a>

#### shadow_color_and_opacity

```python
@shadow_color_and_opacity.setter
def shadow_color_and_opacity(value: LinearColor) -> None
```

<a id="unreal.ComboButtonStyle.menu_border_brush"></a>

#### menu_border_brush

```python
@property
def menu_border_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] Brush to use to add a "menu border" around the drop-down content.

<a id="unreal.ComboButtonStyle.menu_border_brush"></a>

#### menu_border_brush

```python
@menu_border_brush.setter
def menu_border_brush(value: SlateBrush) -> None
```

<a id="unreal.ComboButtonStyle.menu_border_padding"></a>

#### menu_border_padding

```python
@property
def menu_border_padding() -> Margin
```

(Margin):  [Read-Write] Padding to use to add a "menu border" around the drop-down content.

<a id="unreal.ComboButtonStyle.menu_border_padding"></a>

#### menu_border_padding

```python
@menu_border_padding.setter
def menu_border_padding(value: Margin) -> None
```

<a id="unreal.ComboButtonStyle.content_padding"></a>

#### content_padding

```python
@property
def content_padding() -> Margin
```

(Margin):  [Read-Write] * Button Content Padding

<a id="unreal.ComboButtonStyle.content_padding"></a>

#### content_padding

```python
@content_padding.setter
def content_padding(value: Margin) -> None
```

<a id="unreal.ComboButtonStyle.down_arrow_padding"></a>

#### down_arrow_padding

```python
@property
def down_arrow_padding() -> Margin
```

(Margin):  [Read-Write] * Dropdown arrow padding (if a dropdown arrow exists)

<a id="unreal.ComboButtonStyle.down_arrow_padding"></a>

#### down_arrow_padding

```python
@down_arrow_padding.setter
def down_arrow_padding(value: Margin) -> None
```

<a id="unreal.ComboButtonStyle.down_arrow_align"></a>

#### down_arrow_align

```python
@property
def down_arrow_align() -> VerticalAlignment
```

(VerticalAlignment):  [Read-Write] * Dropdown arrow vertical alignment

<a id="unreal.ComboButtonStyle.down_arrow_align"></a>

#### down_arrow_align

```python
@down_arrow_align.setter
def down_arrow_align(value: VerticalAlignment) -> None
```

<a id="unreal.ButtonStyle"></a>