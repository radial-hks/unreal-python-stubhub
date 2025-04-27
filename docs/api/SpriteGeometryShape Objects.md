## SpriteGeometryShape Objects

```python
class SpriteGeometryShape(StructBase)
```

A single piece of geometry (e.g., a polygon which may be convex or concave, a box, or a circle)

**C++ Source:**

- **Plugin**: Paper2D
- **Module**: Paper2D
- **File**: SpriteEditorOnlyTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``box_position`` (Vector2D):  [Read-Only] Center of the box or circle, acts as the pivot point for polygons (but may not be at the center of them)
- ``box_size`` (Vector2D):  [Read-Only] Size of the box or major/minor dimensions of the circle
  Note: Only valid when GeometryType is Box or Circle
- ``negative_winding`` (bool):  [Read-Only] For Polygon geometry, this tells us if the winding should be negative (CW) regardless of the order in Vertices
- ``rotation`` (float):  [Read-Only] Rotation of the shape (in degrees)
- ``shape_type`` (SpriteShapeType):  [Read-Only] The type of this piece of geometry
- ``vertices`` (Array[Vector2D]):  [Read-Write] Vertices for the polygon (valid for Box and Polygon, but empty for Circle)

<a id="unreal.SpriteGeometryShape.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.SpritePolygon"></a>