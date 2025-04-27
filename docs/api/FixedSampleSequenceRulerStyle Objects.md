## FixedSampleSequenceRulerStyle Objects

```python
class FixedSampleSequenceRulerStyle(SlateWidgetStyle)
```

Represents the appearance of a Sampled Sequence Time Ruler

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioWidgetsSlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``background_brush`` (SlateBrush):  [Read-Write]
- ``background_color`` (SlateColor):  [Read-Write]
- ``desired_height`` (float):  [Read-Write]
- ``desired_width`` (float):  [Read-Write]
- ``handle_brush`` (SlateBrush):  [Read-Write]
- ``handle_color`` (SlateColor):  [Read-Write]
- ``handle_width`` (float):  [Read-Write]
- ``ticks_color`` (SlateColor):  [Read-Write]
- ``ticks_text_color`` (SlateColor):  [Read-Write]
- ``ticks_text_font`` (SlateFontInfo):  [Read-Write]
- ``ticks_text_offset`` (float):  [Read-Write]

<a id="unreal.FixedSampleSequenceRulerStyle.__init__"></a>

#### __init__

```python
def __init__(handle_width: float = 0.000000,
             handle_color: SlateColor = [[
                 1.000000, 0.000000, 1.000000, 1.000000
             ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
             handle_brush: SlateBrush = [
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
             ticks_color: SlateColor = [[
                 1.000000, 0.000000, 1.000000, 1.000000
             ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
             ticks_text_color: SlateColor = [
                 [1.000000, 0.000000, 1.000000,
                  1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED
             ],
             ticks_text_font: SlateFontInfo = [
                 None, None,
                 [
                     0, False, False, False, None,
                     [0.000000, 0.000000, 0.000000, 1.000000]
                 ], "None", 24.000000, 0, 0.000000, False, False, 1.000000
             ],
             ticks_text_offset: float = 0.000000,
             background_color: SlateColor = [
                 [1.000000, 0.000000, 1.000000,
                  1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED
             ],
             background_brush: SlateBrush = [
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
             desired_width: float = 0.000000,
             desired_height: float = 0.000000) -> None
```

<a id="unreal.FixedSampleSequenceRulerStyle.handle_width"></a>

#### handle_width

```python
@property
def handle_width() -> float
```

(float):  [Read-Write]

<a id="unreal.FixedSampleSequenceRulerStyle.handle_width"></a>

#### handle_width

```python
@handle_width.setter
def handle_width(value: float) -> None
```

<a id="unreal.FixedSampleSequenceRulerStyle.handle_color"></a>

#### handle_color

```python
@property
def handle_color() -> SlateColor
```

(SlateColor):  [Read-Write]

<a id="unreal.FixedSampleSequenceRulerStyle.handle_color"></a>

#### handle_color

```python
@handle_color.setter
def handle_color(value: SlateColor) -> None
```

<a id="unreal.FixedSampleSequenceRulerStyle.handle_brush"></a>

#### handle_brush

```python
@property
def handle_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write]

<a id="unreal.FixedSampleSequenceRulerStyle.handle_brush"></a>

#### handle_brush

```python
@handle_brush.setter
def handle_brush(value: SlateBrush) -> None
```

<a id="unreal.FixedSampleSequenceRulerStyle.ticks_color"></a>

#### ticks_color

```python
@property
def ticks_color() -> SlateColor
```

(SlateColor):  [Read-Write]

<a id="unreal.FixedSampleSequenceRulerStyle.ticks_color"></a>

#### ticks_color

```python
@ticks_color.setter
def ticks_color(value: SlateColor) -> None
```

<a id="unreal.FixedSampleSequenceRulerStyle.ticks_text_color"></a>

#### ticks_text_color

```python
@property
def ticks_text_color() -> SlateColor
```

(SlateColor):  [Read-Write]

<a id="unreal.FixedSampleSequenceRulerStyle.ticks_text_color"></a>

#### ticks_text_color

```python
@ticks_text_color.setter
def ticks_text_color(value: SlateColor) -> None
```

<a id="unreal.FixedSampleSequenceRulerStyle.ticks_text_font"></a>

#### ticks_text_font

```python
@property
def ticks_text_font() -> SlateFontInfo
```

(SlateFontInfo):  [Read-Write]

<a id="unreal.FixedSampleSequenceRulerStyle.ticks_text_font"></a>

#### ticks_text_font

```python
@ticks_text_font.setter
def ticks_text_font(value: SlateFontInfo) -> None
```

<a id="unreal.FixedSampleSequenceRulerStyle.ticks_text_offset"></a>

#### ticks_text_offset

```python
@property
def ticks_text_offset() -> float
```

(float):  [Read-Write]

<a id="unreal.FixedSampleSequenceRulerStyle.ticks_text_offset"></a>

#### ticks_text_offset

```python
@ticks_text_offset.setter
def ticks_text_offset(value: float) -> None
```

<a id="unreal.FixedSampleSequenceRulerStyle.background_color"></a>

#### background_color

```python
@property
def background_color() -> SlateColor
```

(SlateColor):  [Read-Write]

<a id="unreal.FixedSampleSequenceRulerStyle.background_color"></a>

#### background_color

```python
@background_color.setter
def background_color(value: SlateColor) -> None
```

<a id="unreal.FixedSampleSequenceRulerStyle.background_brush"></a>

#### background_brush

```python
@property
def background_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write]

<a id="unreal.FixedSampleSequenceRulerStyle.background_brush"></a>

#### background_brush

```python
@background_brush.setter
def background_brush(value: SlateBrush) -> None
```

<a id="unreal.FixedSampleSequenceRulerStyle.desired_width"></a>

#### desired_width

```python
@property
def desired_width() -> float
```

(float):  [Read-Write]

<a id="unreal.FixedSampleSequenceRulerStyle.desired_width"></a>

#### desired_width

```python
@desired_width.setter
def desired_width(value: float) -> None
```

<a id="unreal.FixedSampleSequenceRulerStyle.desired_height"></a>

#### desired_height

```python
@property
def desired_height() -> float
```

(float):  [Read-Write]

<a id="unreal.FixedSampleSequenceRulerStyle.desired_height"></a>

#### desired_height

```python
@desired_height.setter
def desired_height(value: float) -> None
```

<a id="unreal.AudioVectorscopePanelStyle"></a>