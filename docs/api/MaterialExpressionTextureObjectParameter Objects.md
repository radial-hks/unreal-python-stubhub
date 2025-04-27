## MaterialExpressionTextureObjectParameter Objects

```python
class MaterialExpressionTextureObjectParameter(
        MaterialExpressionTextureSampleParameter)
```

Material Expression Texture Object Parameter

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionTextureObjectParameter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``automatic_view_mip_bias`` (bool):  [Read-Write] Whether the texture should be sampled with per view mip biasing for sharper output with Temporal AA.
- ``channel_names`` (ParameterChannelNames):  [Read-Write]
- ``const_coordinate`` (uint8):  [Read-Write] only used if Coordinates is not hooked up
- ``const_mip_value`` (int32):  [Read-Write] only used if MipValue is not hooked up
- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``group`` (Name):  [Read-Write] The name of the parameter Group to display in MaterialInstance Editor. Default is None group
- ``is_default_meshpaint_texture`` (bool):  [Read-Write] Is default selected texture when using mesh paint mode texture painting
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

<a id="unreal.MaterialExpressionTextureProperty"></a>