## MaterialExpressionMaterialXDodge Objects

```python
class MaterialExpressionMaterialXDodge(MaterialExpression)
```

Blend nodes take two 1-4 channel inputs and apply the same operator to all channels.
Blend nodes support an optional float input mix , which can be used
to mix the original B value with the result of the blend operation.
Operation: B/(1-A)
Result: Lerp(B, B/(1-A), Alpha)

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeImport
- **File**: MaterialExpressionDodge.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``const_alpha`` (float):  [Read-Write] only used if Alpha is not hooked up
- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]

<a id="unreal.MaterialExpressionDodge"></a>