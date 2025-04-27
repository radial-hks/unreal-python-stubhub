## MaterialExpressionFirstPersonOutput Objects

```python
class MaterialExpressionFirstPersonOutput(MaterialExpressionCustomOutput)
```

Material output expression for writing first person rendering properties.

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionFirstPersonOutput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``const_first_person_interpolation_alpha`` (float):  [Read-Write] Only used if FirstPersonInterpolationAlpha is not hooked up. Interpolates between world space and first person space. Valid range is [0, 1], from world space to first person space.
- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]

<a id="unreal.MaterialExpressionFloatToUInt"></a>