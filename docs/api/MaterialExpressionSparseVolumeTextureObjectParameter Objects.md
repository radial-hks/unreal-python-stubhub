## MaterialExpressionSparseVolumeTextureObjectParameter Objects

```python
class MaterialExpressionSparseVolumeTextureObjectParameter(
        MaterialExpressionSparseVolumeTextureSampleParameter)
```

Material Expression Sparse Volume Texture Object Parameter

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionSparseVolumeTextureObject.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``const_mip_value`` (int32):  [Read-Write] Only used if MipValue is not hooked up
- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``group`` (Name):  [Read-Write] The name of the parameter Group to display in MaterialInstance Editor. Default is None group
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``mip_value_mode`` (TextureMipValueMode):  [Read-Write] Defines how the MipValue property is applied to the texture lookup
- ``parameter_name`` (Name):  [Read-Write] Name to be referenced when we want to find and set this parameter
- ``sampler_source`` (SamplerSourceMode):  [Read-Write] Controls where the sampler for this texture lookup will come from.
  Choose 'from texture asset' to make use of the USparseVolumeTexture addressing settings,
  Otherwise use one of the global samplers, which will not consume a sampler slot.
  This allows materials to use more than 16 unique textures on SM5 platforms.
- ``sort_priority`` (int32):  [Read-Write] Controls where the this parameter is displayed in a material instance parameter list. The lower the number the higher up in the parameter list.
- ``sparse_volume_texture`` (SparseVolumeTexture):  [Read-Write] The Sparse Volume Texture to sample.

<a id="unreal.MaterialExpressionSpeedTree"></a>