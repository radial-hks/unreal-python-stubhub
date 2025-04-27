## MaterialExpressionMaterialFunctionCall Objects

```python
class MaterialExpressionMaterialFunctionCall(MaterialExpression)
```

Material Expression Material Function Call

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionMaterialFunctionCall.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``material_function`` (MaterialFunctionInterface):  [Read-Write] The function to call.

<a id="unreal.MaterialExpressionMaterialFunctionCall.set_material_function"></a>

#### set_material_function

```python
def set_material_function(
        new_material_function: MaterialFunctionInterface) -> bool
```

x.set_material_function(new_material_function) -> bool
Set Material Function

Args:
    new_material_function (MaterialFunctionInterface): 

Returns:
    bool:

<a id="unreal.MaterialExpressionMaterialLayerOutput"></a>