## MaterialExpressionSpeedTree Objects

```python
class MaterialExpressionSpeedTree(MaterialExpression)
```

Material Expression Speed Tree

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionSpeedTree.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accurate_wind_velocities`` (bool):  [Read-Write] Support accurate velocities from wind. This will incur extra cost per vertex.
- ``billboard_threshold`` (float):  [Read-Write] The threshold for triangles to be removed from the bilboard mesh when not facing the camera (0 = none pass, 1 = all pass).
- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``geometry_type`` (SpeedTreeGeometryType):  [Read-Write] The type of SpeedTree geometry on which this material will be used
- ``lod_type`` (SpeedTreeLODType):  [Read-Write] The type of LOD to use
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``wind_type`` (SpeedTreeWindType):  [Read-Write] The type of wind effect used on this tree. This can only go as high as it was in the SpeedTree Modeler, but you can set it to a lower option for lower quality wind and faster rendering.

<a id="unreal.MaterialExpressionSphereMask"></a>