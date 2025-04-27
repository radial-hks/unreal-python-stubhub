## MaterialExpressionSceneDepth Objects

```python
class MaterialExpressionSceneDepth(MaterialExpression)
```

Material Expression Scene Depth

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionSceneDepth.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``const_input`` (Vector2D):  [Read-Write] only used if Input is not hooked up
- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``input_mode`` (MaterialSceneAttributeInputMode):  [Read-Write] Coordinates - UV coordinates to apply to the scene depth lookup.
  OffsetFraction - An offset to apply to the scene depth lookup in a 2d fraction of the screen.
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]

<a id="unreal.MaterialExpressionSceneDepthWithoutWater"></a>