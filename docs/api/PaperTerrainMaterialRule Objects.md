## PaperTerrainMaterialRule Objects

```python
class PaperTerrainMaterialRule(StructBase)
```

Rule for a single section of a terrain material

**C++ Source:**

- **Plugin**: Paper2D
- **Module**: Paper2D
- **File**: PaperTerrainMaterial.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``body`` (Array[PaperSprite]):  [Read-Write] A set of sprites to randomly choose to fill up the interior space between the caps in a terrain segment
- ``collision_offset`` (float):  [Read-Write] How much should the collision be lofted from the spline (positive values go out from the spline, negative values go in to the spline)
- ``description`` (Text):  [Read-Write] Readable description for the rule (unused anywhere, just for clarity when editing the material)
- ``draw_order`` (int32):  [Read-Write] Specify a draw order for different materials in a spline. Smaller draw orders are drawn first, negative values are allowed.
- ``enable_collision`` (bool):  [Read-Write] If true, collision is enabled for sections matching this rule
- ``end_cap`` (PaperSprite):  [Read-Write] The sprite to use at the 'right' (closest to spline end) edge of the terrain segment
- ``maximum_angle`` (float):  [Read-Write] Maximum slope angle (in degrees) to apply this rule
- ``minimum_angle`` (float):  [Read-Write] Minimum slope angle (in degrees) to apply this rule
- ``start_cap`` (PaperSprite):  [Read-Write] The sprite to use at the 'left' (closest to spline start) edge of the terrain segment

<a id="unreal.PaperTerrainMaterialRule.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.BlendStackAnimNodeReference"></a>