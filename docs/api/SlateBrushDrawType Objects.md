## SlateBrushDrawType Objects

```python
class SlateBrushDrawType(EnumBase)
```

Enumerates ways in which an image can be drawn.

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateBrush.h

<a id="unreal.SlateBrushDrawType.NO_DRAW_TYPE"></a>

#### NO_DRAW_TYPE

0: Don't do anything

<a id="unreal.SlateBrushDrawType.BOX"></a>

#### BOX

1: Draw a 3x3 box, where the sides and the middle stretch based on the Margin

<a id="unreal.SlateBrushDrawType.BORDER"></a>

#### BORDER

2: Draw a 3x3 border where the sides tile and the middle is empty

<a id="unreal.SlateBrushDrawType.IMAGE"></a>

#### IMAGE

3: Draw an image; margin is ignored

<a id="unreal.SlateBrushDrawType.ROUNDED_BOX"></a>

#### ROUNDED_BOX

4: Draw a solid rectangle with an outline and corner radius

<a id="unreal.SlateBrushTileType"></a>