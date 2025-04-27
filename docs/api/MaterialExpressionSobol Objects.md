## MaterialExpressionSobol Objects

```python
class MaterialExpressionSobol(MaterialExpression)
```

Material Expression Sobol

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionSobol.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``const_index`` (uint32):  [Read-Write] Sobol point number. Only used if Index is not connected.
- ``const_seed`` (Vector2D):  [Read-Write] 2D Seed for sequence randomization. Only used if Seed is not connected.
- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]

<a id="unreal.MaterialExpressionSparseVolumeTextureBase"></a>