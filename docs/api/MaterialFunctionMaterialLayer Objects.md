## MaterialFunctionMaterialLayer Objects

```python
class MaterialFunctionMaterialLayer(MaterialFunction)
```

Specialized Material Function that acts as a layer

**C++ Source:**

- **Module**: Engine
- **File**: MaterialFunctionMaterialLayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``description`` (str):  [Read-Write] Description of the function which will be displayed as a tooltip wherever the function is used.
- ``enable_exec_wire`` (bool):  [Read-Write]
- ``enable_new_hlsl_generator`` (bool):  [Read-Write]
- ``expose_to_library`` (bool):  [Read-Write] Whether to list this function in the material function library, which is a window in the material editor that lists categorized functions.
- ``library_categories_text`` (Array[Text]):  [Read-Write] Categories that this function belongs to in the material function library.
  Ideally categories should be chosen carefully so that there are not too many.
- ``prefix_parameter_names`` (bool):  [Read-Write] If true, parameters in this function will have a prefix added to their group name.
- ``preview_blend_mode`` (BlendMode):  [Read-Write] Determines the blend mode when previewing a material function.
- ``thumbnail_info`` (ThumbnailInfo):  [Read-Only] Information for thumbnail rendering
- ``user_exposed_caption`` (str):  [Read-Write] Name of the function to be displayed on the node within the material editor instead of the asset name.

<a id="unreal.MaterialFunctionMaterialLayerInstance"></a>