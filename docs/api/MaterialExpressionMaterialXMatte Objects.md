## MaterialExpressionMaterialXMatte Objects

```python
class MaterialExpressionMaterialXMatte(MaterialExpression)
```

Merge nodes take two 4-channel (color4) inputs and use the built-in alpha channel(s) to control the
compositing of the A and B inputs. "A" and "B" refer to the non-alpha channels of the A and B inputs respectively,
and "a" and "b" refer to the alpha channels of the A and B inputs.
Merge nodes are only defined for float4 inputs
Merge nodes support an optional float input Alpha , which can be used to mix the
original B value with the result of the blend operation.

Operation: A*a + B*(1-a)
Result: Lerp(B, A*a + B*(1-a), Alpha)

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeImport
- **File**: MaterialExpressionMatte.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``const_alpha`` (float):  [Read-Write] only used if Alpha is not hooked up
- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]

<a id="unreal.MaterialExpressionMatte"></a>