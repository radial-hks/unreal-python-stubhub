## SpriteGeometryCollection Objects

```python
class SpriteGeometryCollection(StructBase)
```

Sprite Geometry Collection

**C++ Source:**

- **Plugin**: Paper2D
- **Module**: Paper2D
- **File**: SpriteEditorOnlyTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha_threshold`` (float):  [Read-Write] Alpha threshold for a transparent pixel (range 0..1, anything equal or below this value will be considered unimportant)
- ``avoid_vertex_merging`` (bool):  [Read-Write] Experimental: Hint to the triangulation routine that extra vertices should be preserved
- ``detail_amount`` (float):  [Read-Write] Amount to detail to consider when shrink-wrapping (range 0..1, 0 = low detail, 1 = high detail)
- ``geometry_type`` (SpritePolygonMode):  [Read-Write] The geometry type (automatic / manual)
- ``pixels_per_subdivision_x`` (int32):  [Read-Write] Size of a single subdivision (in pixels) in X (for Diced mode)
- ``pixels_per_subdivision_y`` (int32):  [Read-Write] Size of a single subdivision (in pixels) in Y (for Diced mode)
- ``shapes`` (Array[SpriteGeometryShape]):  [Read-Write] List of shapes
- ``simplify_epsilon`` (float):  [Read-Write] This is the threshold below which multiple vertices will be merged together when doing shrink-wrapping.  Higher values result in fewer vertices.

<a id="unreal.SpriteGeometryCollection.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.SpritePolygonCollection"></a>