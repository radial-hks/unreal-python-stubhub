## MaterialExpressionNoise Objects

```python
class MaterialExpressionNoise(MaterialExpression)
```

Material Expression Noise

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionNoise.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``level_scale`` (float):  [Read-Write] usually 2 but higher values allow efficient use of few levels
- ``levels`` (int32):  [Read-Write] 1 = fast but little detail, .. larger numbers cost more performance
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``noise_function`` (NoiseFunction):  [Read-Write] Noise function, affects performance and look
- ``output_max`` (float):  [Read-Write]
- ``output_min`` (float):  [Read-Write]
- ``quality`` (int32):  [Read-Write] Lower numbers are faster and lower quality, higher numbers are slower and higher quality
- ``repeat_size`` (uint32):  [Read-Write] How many units in each tile (if Tiling is on)
- ``scale`` (float):  [Read-Write] can also be done with a multiply on the Position
- ``tiling`` (bool):  [Read-Write] Whether to use tiling noise pattern, useful for baking to seam-free repeating textures
- ``turbulence`` (bool):  [Read-Write] How multiple frequencies are getting combined
- ``world_position_origin_type`` (PositionOrigin):  [Read-Write] Defines the reference space for the Position input.

<a id="unreal.MaterialExpressionNormalize"></a>