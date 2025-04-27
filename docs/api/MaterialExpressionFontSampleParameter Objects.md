## MaterialExpressionFontSampleParameter Objects

```python
class MaterialExpressionFontSampleParameter(MaterialExpressionFontSample)
```

Material Expression Font Sample Parameter

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionFontSampleParameter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``font`` (Font):  [Read-Write] font resource that will be sampled
- ``font_texture_page`` (int32):  [Read-Write] allow access to the various font pages
- ``group`` (Name):  [Read-Write] The name of the parameter Group to display in MaterialInstance Editor. Default is None group
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``parameter_name`` (Name):  [Read-Write] name to be referenced when we want to find and set thsi parameter
- ``sort_priority`` (int32):  [Read-Write] Controls where the this parameter is displayed in a material instance parameter list. The lower the number the higher up in the parameter list.

<a id="unreal.MaterialExpressionFontSignedDistance"></a>