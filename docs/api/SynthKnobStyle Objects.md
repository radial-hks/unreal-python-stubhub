## SynthKnobStyle Objects

```python
class SynthKnobStyle(SlateWidgetStyle)
```

Represents the appearance of an SSynthKnob

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SynthKnobStyle.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``knob_size`` (SynthKnobSize):  [Read-Write] The size of the knobs to use.
- ``large_knob`` (SlateBrush):  [Read-Write] Image to use for the large knob
- ``large_knob_overlay`` (SlateBrush):  [Read-Write] Image to use for the dot handle
- ``max_value_angle`` (float):  [Read-Write] Image to use for the medium knob dot handle
- ``medium_knob`` (SlateBrush):  [Read-Write] Image to use for the medium large knob
- ``medium_knob_overlay`` (SlateBrush):  [Read-Write] Image to use for the medium knob dot handle
- ``min_value_angle`` (float):  [Read-Write] Image to use for the medium knob dot handle

<a id="unreal.SynthKnobStyle.__init__"></a>

#### __init__

```python
def __init__(large_knob: SlateBrush = [
    [[1.000000, 1.000000, 1.000000, 1.000000],
     SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
    SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
    [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
    [[0.000000, 0.000000, 0.000000, 0.000000],
     [[0.000000, 0.000000, 0.000000, 0.000000],
      SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
     SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
],
             large_knob_overlay: SlateBrush = [
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
             medium_knob: SlateBrush = [
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
             medium_knob_overlay: SlateBrush = [
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
             min_value_angle: float = 0.000000,
             max_value_angle: float = 0.000000,
             knob_size: SynthKnobSize = SynthKnobSize.MEDIUM) -> None
```

<a id="unreal.SynthKnobStyle.large_knob"></a>

#### large_knob

```python
@property
def large_knob() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to use for the large knob

<a id="unreal.SynthKnobStyle.large_knob"></a>

#### large_knob

```python
@large_knob.setter
def large_knob(value: SlateBrush) -> None
```

<a id="unreal.SynthKnobStyle.large_knob_overlay"></a>

#### large_knob_overlay

```python
@property
def large_knob_overlay() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to use for the dot handle

<a id="unreal.SynthKnobStyle.large_knob_overlay"></a>

#### large_knob_overlay

```python
@large_knob_overlay.setter
def large_knob_overlay(value: SlateBrush) -> None
```

<a id="unreal.SynthKnobStyle.medium_knob"></a>

#### medium_knob

```python
@property
def medium_knob() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to use for the medium large knob

<a id="unreal.SynthKnobStyle.medium_knob"></a>

#### medium_knob

```python
@medium_knob.setter
def medium_knob(value: SlateBrush) -> None
```

<a id="unreal.SynthKnobStyle.medium_knob_overlay"></a>

#### medium_knob_overlay

```python
@property
def medium_knob_overlay() -> SlateBrush
```

(SlateBrush):  [Read-Write] Image to use for the medium knob dot handle

<a id="unreal.SynthKnobStyle.medium_knob_overlay"></a>

#### medium_knob_overlay

```python
@medium_knob_overlay.setter
def medium_knob_overlay(value: SlateBrush) -> None
```

<a id="unreal.SynthKnobStyle.min_value_angle"></a>

#### min_value_angle

```python
@property
def min_value_angle() -> float
```

(float):  [Read-Write] Image to use for the medium knob dot handle

<a id="unreal.SynthKnobStyle.min_value_angle"></a>

#### min_value_angle

```python
@min_value_angle.setter
def min_value_angle(value: float) -> None
```

<a id="unreal.SynthKnobStyle.max_value_angle"></a>

#### max_value_angle

```python
@property
def max_value_angle() -> float
```

(float):  [Read-Write] Image to use for the medium knob dot handle

<a id="unreal.SynthKnobStyle.max_value_angle"></a>

#### max_value_angle

```python
@max_value_angle.setter
def max_value_angle(value: float) -> None
```

<a id="unreal.SynthKnobStyle.knob_size"></a>

#### knob_size

```python
@property
def knob_size() -> SynthKnobSize
```

(SynthKnobSize):  [Read-Write] The size of the knobs to use.

<a id="unreal.SynthKnobStyle.knob_size"></a>

#### knob_size

```python
@knob_size.setter
def knob_size(value: SynthKnobSize) -> None
```

<a id="unreal.SynthSlateStyle"></a>