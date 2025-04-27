## EditableTextStyle Objects

```python
class EditableTextStyle(SlateWidgetStyle)
```

Represents the appearance of an SEditableText

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``background_image_composing`` (SlateBrush):  [Read-Write] Background image for the selected text
- ``background_image_selected`` (SlateBrush):  [Read-Write] Background image for the selected text
- ``caret_image`` (SlateBrush):  [Read-Write] Image brush used for the caret
- ``color_and_opacity`` (SlateColor):  [Read-Write] The color and opacity of this text
- ``font`` (SlateFontInfo):  [Read-Write] Font family and size to be used when displaying this text.

<a id="unreal.EditableTextStyle.__init__"></a>

#### __init__

```python
def __init__(
    font: SlateFontInfo = [
        None, None,
        [
            0, False, False, False, None,
            [0.000000, 0.000000, 0.000000, 1.000000]
        ], "None", 24.000000, 0, 0.000000, False, False, 1.000000
    ],
    color_and_opacity: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000],
                                     SlateColorStylingMode.USE_COLOR_SPECIFIED
                                     ],
    background_image_selected: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    background_image_composing: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    caret_image: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000],
                                SlateColorStylingMode.USE_COLOR_SPECIFIED],
                               SlateBrushDrawType.IMAGE,
                               SlateBrushTileType.NO_TILE,
                               SlateBrushMirrorType.NO_MIRROR,
                               [0.000000, 0.000000],
                               [0.000000, 0.000000, 0.000000, 0.000000], None,
                               [[0.000000, 0.000000, 0.000000, 0.000000],
                                [[0.000000, 0.000000, 0.000000, 0.000000],
                                 SlateColorStylingMode.USE_COLOR_SPECIFIED],
                                0.000000,
                                SlateBrushRoundingType.HALF_HEIGHT_RADIUS,
                                False]]
) -> None
```

<a id="unreal.EditableTextStyle.font"></a>

#### font

```python
@property
def font() -> SlateFontInfo
```

(SlateFontInfo):  [Read-Write] Font family and size to be used when displaying this text.

<a id="unreal.EditableTextStyle.font"></a>

#### font

```python
@font.setter
def font(value: SlateFontInfo) -> None
```

<a id="unreal.EditableTextStyle.color_and_opacity"></a>

#### color_and_opacity

```python
@property
def color_and_opacity() -> SlateColor
```

(SlateColor):  [Read-Write] The color and opacity of this text

<a id="unreal.EditableTextStyle.color_and_opacity"></a>

#### color_and_opacity

```python
@color_and_opacity.setter
def color_and_opacity(value: SlateColor) -> None
```

<a id="unreal.EditableTextStyle.background_image_selected"></a>

#### background_image_selected

```python
@property
def background_image_selected() -> SlateBrush
```

(SlateBrush):  [Read-Write] Background image for the selected text

<a id="unreal.EditableTextStyle.background_image_selected"></a>

#### background_image_selected

```python
@background_image_selected.setter
def background_image_selected(value: SlateBrush) -> None
```

<a id="unreal.EditableTextStyle.background_image_composing"></a>

#### background_image_composing

```python
@property
def background_image_composing() -> SlateBrush
```

(SlateBrush):  [Read-Write] Background image for the selected text

<a id="unreal.EditableTextStyle.background_image_composing"></a>

#### background_image_composing

```python
@background_image_composing.setter
def background_image_composing(value: SlateBrush) -> None
```

<a id="unreal.EditableTextStyle.caret_image"></a>

#### caret_image

```python
@property
def caret_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image brush used for the caret

<a id="unreal.EditableTextStyle.caret_image"></a>

#### caret_image

```python
@caret_image.setter
def caret_image(value: SlateBrush) -> None
```

<a id="unreal.EditableTextBoxStyle"></a>