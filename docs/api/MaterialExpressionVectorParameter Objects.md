## MaterialExpressionVectorParameter Objects

```python
class MaterialExpressionVectorParameter(MaterialExpressionParameter)
```

Material Expression Vector Parameter

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionVectorParameter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel_names`` (ParameterChannelNames):  [Read-Write]
- ``default_value`` (LinearColor):  [Read-Write]
- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``group`` (Name):  [Read-Write] The name of the parameter Group to display in MaterialInstance Editor. Default is None group
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``parameter_name`` (Name):  [Read-Write] The name of the parameter
- ``primitive_data_index`` (uint8):  [Read-Write]
- ``sort_priority`` (int32):  [Read-Write] Controls where the this parameter is displayed in a material instance parameter list.  The lower the number the higher up in the parameter list.
- ``use_custom_primitive_data`` (bool):  [Read-Write]

<a id="unreal.MaterialExpressionChannelMaskParameter"></a>