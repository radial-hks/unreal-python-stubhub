## MaterialExpressionVectorNoise Objects

```python
class MaterialExpressionVectorNoise(MaterialExpression)
```

Material Expression Vector Noise

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionVectorNoise.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``noise_function`` (VectorNoiseFunction):  [Read-Write] Noise function, affects performance and look
- ``quality`` (int32):  [Read-Write] For noise functions where applicable, lower numbers are faster and lower quality, higher numbers are slower and higher quality
- ``tile_size`` (uint32):  [Read-Write] How many units in each tile (if Tiling is on)
  For Perlin noise functions, Tile Size must be a multiple of three
- ``tiling`` (bool):  [Read-Write] Whether tile the noise pattern, useful for baking to seam-free repeating textures
- ``world_position_origin_type`` (PositionOrigin):  [Read-Write] Defines the reference space for the Position input.

<a id="unreal.MaterialExpressionVertexColor"></a>