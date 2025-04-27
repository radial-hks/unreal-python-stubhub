## MaterialExpressionDynamicParameter Objects

```python
class MaterialExpressionDynamicParameter(MaterialExpression)
```

Material Expression Dynamic Parameter

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionDynamicParameter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_value`` (LinearColor):  [Read-Write]
- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``param_names`` (Array[str]):  [Read-Write] The names of the parameters.
  These will show up in Cascade when editing a particle system
  that uses the material it is in...
- ``parameter_index`` (uint32):  [Read-Write] The index of the dynamic parameter for use in tools that allow > 1

<a id="unreal.MaterialExpressionExecBegin"></a>