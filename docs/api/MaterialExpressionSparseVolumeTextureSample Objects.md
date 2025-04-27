## MaterialExpressionSparseVolumeTextureSample Objects

```python
class MaterialExpressionSparseVolumeTextureSample(
        MaterialExpressionSparseVolumeTextureBase)
```

Material expression for sampling from a runtime virtual texture.

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionSparseVolumeTextureSample.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``const_mip_value`` (int32):  [Read-Write] Only used if MipValue is not hooked up
- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``mip_value_mode`` (TextureMipValueMode):  [Read-Write] Defines how the MipValue property is applied to the texture lookup
- ``sampler_source`` (SamplerSourceMode):  [Read-Write] Controls where the sampler for this texture lookup will come from.
  Choose 'from texture asset' to make use of the USparseVolumeTexture addressing settings,
  Otherwise use one of the global samplers, which will not consume a sampler slot.
  This allows materials to use more than 16 unique textures on SM5 platforms.
- ``sparse_volume_texture`` (SparseVolumeTexture):  [Read-Write] The Sparse Volume Texture to sample.

<a id="unreal.MaterialExpressionSparseVolumeTextureSampleParameter"></a>