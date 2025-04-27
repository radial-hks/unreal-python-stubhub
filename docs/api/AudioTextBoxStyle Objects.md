## AudioTextBoxStyle Objects

```python
class AudioTextBoxStyle(SlateWidgetStyle)
```

Represents the appearance of an Audio Text Box

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioWidgetsSlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``background_color`` (SlateColor):  [Read-Write] Color used to draw the label background
- ``background_image`` (SlateBrush):  [Read-Write] Image for the label border

<a id="unreal.AudioTextBoxStyle.__init__"></a>

#### __init__

```python
def __init__(
    background_image: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    background_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000],
                                    SlateColorStylingMode.USE_COLOR_SPECIFIED]
) -> None
```

<a id="unreal.AudioTextBoxStyle.background_image"></a>

#### background_image

```python
@property
def background_image() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image for the label border

<a id="unreal.AudioTextBoxStyle.background_image"></a>

#### background_image

```python
@background_image.setter
def background_image(value: SlateBrush) -> None
```

<a id="unreal.AudioTextBoxStyle.background_color"></a>

#### background_color

```python
@property
def background_color() -> SlateColor
```

(SlateColor):  [Read-Write] Color used to draw the label background

<a id="unreal.AudioTextBoxStyle.background_color"></a>

#### background_color

```python
@background_color.setter
def background_color(value: SlateColor) -> None
```

<a id="unreal.AudioMaterialKnobStyle"></a>