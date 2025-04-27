## MaterialExpressionMaterialXUnpremult Objects

```python
class MaterialExpressionMaterialXUnpremult(MaterialExpression)
```

Divide the RGB channels of the input by the Alpha channel of the input. If the
Alpha value is zero, the original color4 input value is passed through unchanged.
Input must be of type float4

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeImport
- **File**: MaterialExpressionUnpremult.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]

<a id="unreal.MaterialExpressionUnpremult"></a>