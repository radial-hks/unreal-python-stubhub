## SampledSequenceValueGridOverlayStyle Objects

```python
class SampledSequenceValueGridOverlayStyle(SlateWidgetStyle)
```

Represents the appearance of a Sampled Sequence Value Grid Overlay

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioWidgetsSlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desired_height`` (float):  [Read-Write]
- ``desired_width`` (float):  [Read-Write]
- ``grid_color`` (SlateColor):  [Read-Write]
- ``grid_thickness`` (float):  [Read-Write]
- ``label_text_color`` (SlateColor):  [Read-Write]
- ``label_text_font`` (SlateFontInfo):  [Read-Write]

<a id="unreal.SampledSequenceValueGridOverlayStyle.__init__"></a>

#### __init__

```python
def __init__(grid_color: SlateColor = [[
    1.000000, 0.000000, 1.000000, 1.000000
], SlateColorStylingMode.USE_COLOR_SPECIFIED],
             grid_thickness: float = 0.000000,
             label_text_color: SlateColor = [[
                 1.000000, 0.000000, 1.000000, 1.000000
             ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
             label_text_font: SlateFontInfo = [
                 None, None,
                 [
                     0, False, False, False, None,
                     [0.000000, 0.000000, 0.000000, 1.000000]
                 ], "None", 24.000000, 0, 0.000000, False, False, 1.000000
             ],
             desired_width: float = 0.000000,
             desired_height: float = 0.000000) -> None
```

<a id="unreal.SampledSequenceValueGridOverlayStyle.grid_color"></a>

#### grid_color

```python
@property
def grid_color() -> SlateColor
```

(SlateColor):  [Read-Write]

<a id="unreal.SampledSequenceValueGridOverlayStyle.grid_color"></a>

#### grid_color

```python
@grid_color.setter
def grid_color(value: SlateColor) -> None
```

<a id="unreal.SampledSequenceValueGridOverlayStyle.grid_thickness"></a>

#### grid_thickness

```python
@property
def grid_thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.SampledSequenceValueGridOverlayStyle.grid_thickness"></a>

#### grid_thickness

```python
@grid_thickness.setter
def grid_thickness(value: float) -> None
```

<a id="unreal.SampledSequenceValueGridOverlayStyle.label_text_color"></a>

#### label_text_color

```python
@property
def label_text_color() -> SlateColor
```

(SlateColor):  [Read-Write]

<a id="unreal.SampledSequenceValueGridOverlayStyle.label_text_color"></a>

#### label_text_color

```python
@label_text_color.setter
def label_text_color(value: SlateColor) -> None
```

<a id="unreal.SampledSequenceValueGridOverlayStyle.label_text_font"></a>

#### label_text_font

```python
@property
def label_text_font() -> SlateFontInfo
```

(SlateFontInfo):  [Read-Write]

<a id="unreal.SampledSequenceValueGridOverlayStyle.label_text_font"></a>

#### label_text_font

```python
@label_text_font.setter
def label_text_font(value: SlateFontInfo) -> None
```

<a id="unreal.SampledSequenceValueGridOverlayStyle.desired_width"></a>

#### desired_width

```python
@property
def desired_width() -> float
```

(float):  [Read-Write]

<a id="unreal.SampledSequenceValueGridOverlayStyle.desired_width"></a>

#### desired_width

```python
@desired_width.setter
def desired_width(value: float) -> None
```

<a id="unreal.SampledSequenceValueGridOverlayStyle.desired_height"></a>

#### desired_height

```python
@property
def desired_height() -> float
```

(float):  [Read-Write]

<a id="unreal.SampledSequenceValueGridOverlayStyle.desired_height"></a>

#### desired_height

```python
@desired_height.setter
def desired_height(value: float) -> None
```

<a id="unreal.FixedSampleSequenceRulerStyle"></a>