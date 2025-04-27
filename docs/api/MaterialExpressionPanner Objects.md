## MaterialExpressionPanner Objects

```python
class MaterialExpressionPanner(MaterialExpression)
```

Material Expression Panner

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionPanner.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``const_coordinate`` (uint32):  [Read-Write] only used if Coordinate is not hooked up
- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``fractional_part`` (bool):  [Read-Write] Output only the fractional part of the pan calculation for greater precision.
  Output is greater than or equal to 0 and less than 1.
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``speed_x`` (float):  [Read-Write]
- ``speed_y`` (float):  [Read-Write]

<a id="unreal.MaterialExpressionParticleColor"></a>