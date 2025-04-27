## MaterialExpressionMaterialXOverlay Objects

```python
class MaterialExpressionMaterialXOverlay(MaterialExpression)
```

Blend nodes take two 1-4 channel inputs and apply the same operator to all channels.
Blend nodes support an optional float input mix , which can be used
to mix the original B value with the result of the blend operation.
Operation: 2*A*B          if A < 0.5;
           1-(1-A)(1-B) if A >= 0.5
Result: Lerp(B, Op, Alpha)

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeImport
- **File**: MaterialExpressionOverlay.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``const_alpha`` (float):  [Read-Write] only used if Alpha is not hooked up
- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]

<a id="unreal.MaterialExpressionOverlay"></a>