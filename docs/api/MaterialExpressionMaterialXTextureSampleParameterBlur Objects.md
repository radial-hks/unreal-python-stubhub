## MaterialExpressionMaterialXTextureSampleParameterBlur Objects

```python
class MaterialExpressionMaterialXTextureSampleParameterBlur(
        MaterialExpressionTextureSampleParameter2D)
```

Material Expression Material XTexture Sample Parameter Blur

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeImport
- **File**: MaterialExpressionTextureSampleParameterBlur.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``automatic_view_mip_bias`` (bool):  [Read-Write] Whether the texture should be sampled with per view mip biasing for sharper output with Temporal AA.
- ``channel_names`` (ParameterChannelNames):  [Read-Write]
- ``const_coordinate`` (uint8):  [Read-Write] only used if Coordinates is not hooked up
- ``const_mip_value`` (int32):  [Read-Write] only used if MipValue is not hooked up
- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``filter`` (MaterialXTextureSampleBlurFilter):  [Read-Write] Filter to use when we blur a Texture: Gaussian or Box Linear filter
- ``filter_offset`` (float):  [Read-Write] Offset of the filter when we sample a texture coordinate
- ``filter_size`` (float):  [Read-Write] Size of the filter when we sample a texture coordinate
- ``group`` (Name):  [Read-Write] The name of the parameter Group to display in MaterialInstance Editor. Default is None group
- ``is_default_meshpaint_texture`` (bool):  [Read-Write] Is default selected texture when using mesh paint mode texture painting
- ``kernel_size`` (MAterialXTextureSampleBlurKernel):  [Read-Write] The size of the blur kernel, relative to 0-1 UV space.
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``mip_value_mode`` (TextureMipValueMode):  [Read-Write] Defines how the MipValue property is applied to the texture lookup
- ``parameter_name`` (Name):  [Read-Write]
- ``sampler_source`` (SamplerSourceMode):  [Read-Write] Controls where the sampler for this texture lookup will come from.
  Choose 'from texture asset' to make use of the UTexture addressing settings,
  Otherwise use one of the global samplers, which will not consume a sampler slot.
  This allows materials to use more than 16 unique textures on SM5 platforms.
- ``sampler_type`` (MaterialSamplerType):  [Read-Write]
- ``sort_priority`` (int32):  [Read-Write] Controls where the this parameter is displayed in a material instance parameter list.  The lower the number the higher up in the parameter list.
- ``texture`` (Texture):  [Read-Write]

<a id="unreal.MaterialExpressionTextureSampleParameterBlur"></a>