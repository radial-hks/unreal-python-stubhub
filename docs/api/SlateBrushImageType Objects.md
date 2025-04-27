## SlateBrushImageType Objects

```python
class SlateBrushImageType(EnumBase)
```

Enumerates brush image types.

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateBrush.h

<a id="unreal.SlateBrushImageType.NO_IMAGE"></a>

#### NO_IMAGE

0: No image is loaded.  Color only brushes, transparent brushes etc.

<a id="unreal.SlateBrushImageType.FULL_COLOR"></a>

#### FULL_COLOR

1: The image to be loaded is in full color.

<a id="unreal.SlateBrushImageType.LINEAR"></a>

#### LINEAR

2: The image is a special texture in linear space (usually a rendering resource such as a lookup table).

<a id="unreal.SlateBrushImageType.VECTOR"></a>

#### VECTOR

3: The image is vector graphics and will be rendered and cached in full color using size/scale requested by slate

<a id="unreal.SlateBrushRoundingType"></a>