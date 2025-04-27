## SlateBrushOutlineSettings Objects

```python
class SlateBrushOutlineSettings(StructBase)
```

Possible options for rounded box brush image

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateBrush.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (SlateColor):  [Read-Write] Tinting applied to the border outline.
- ``corner_radii`` (Vector4):  [Read-Write] Radius in Slate Units applied to the outline at each corner. X = Top Left, Y = Top Right, Z = Bottom Right, W = Bottom Left
- ``rounding_type`` (SlateBrushRoundingType):  [Read-Write] The Rounding Type *
- ``use_brush_transparency`` (bool):  [Read-Write] True if we should use the owning brush's transparency as our own *
- ``width`` (float):  [Read-Write] Line width in Slate Units applied to the border outline.

<a id="unreal.SlateBrushOutlineSettings.__init__"></a>

#### __init__

```python
def __init__(corner_radii: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000],
             color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000],
                                  SlateColorStylingMode.USE_COLOR_SPECIFIED],
             width: float = 0.000000,
             rounding_type: SlateBrushRoundingType = SlateBrushRoundingType.
             FIXED_RADIUS,
             use_brush_transparency: bool = False) -> None
```

<a id="unreal.SlateBrushOutlineSettings.corner_radii"></a>

#### corner_radii

```python
@property
def corner_radii() -> Vector4
```

(Vector4):  [Read-Write] Radius in Slate Units applied to the outline at each corner. X = Top Left, Y = Top Right, Z = Bottom Right, W = Bottom Left

<a id="unreal.SlateBrushOutlineSettings.corner_radii"></a>

#### corner_radii

```python
@corner_radii.setter
def corner_radii(value: Vector4) -> None
```

<a id="unreal.SlateBrushOutlineSettings.color"></a>

#### color

```python
@property
def color() -> SlateColor
```

(SlateColor):  [Read-Write] Tinting applied to the border outline.

<a id="unreal.SlateBrushOutlineSettings.color"></a>

#### color

```python
@color.setter
def color(value: SlateColor) -> None
```

<a id="unreal.SlateBrushOutlineSettings.width"></a>

#### width

```python
@property
def width() -> float
```

(float):  [Read-Write] Line width in Slate Units applied to the border outline.

<a id="unreal.SlateBrushOutlineSettings.width"></a>

#### width

```python
@width.setter
def width(value: float) -> None
```

<a id="unreal.SlateBrushOutlineSettings.rounding_type"></a>

#### rounding_type

```python
@property
def rounding_type() -> SlateBrushRoundingType
```

(SlateBrushRoundingType):  [Read-Write] The Rounding Type *

<a id="unreal.SlateBrushOutlineSettings.rounding_type"></a>

#### rounding_type

```python
@rounding_type.setter
def rounding_type(value: SlateBrushRoundingType) -> None
```

<a id="unreal.SlateBrushOutlineSettings.use_brush_transparency"></a>

#### use_brush_transparency

```python
@property
def use_brush_transparency() -> bool
```

(bool):  [Read-Write] True if we should use the owning brush's transparency as our own *

<a id="unreal.SlateBrushOutlineSettings.use_brush_transparency"></a>

#### use_brush_transparency

```python
@use_brush_transparency.setter
def use_brush_transparency(value: bool) -> None
```

<a id="unreal.SlateColor"></a>