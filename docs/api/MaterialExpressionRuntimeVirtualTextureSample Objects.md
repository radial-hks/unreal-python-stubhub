## MaterialExpressionRuntimeVirtualTextureSample Objects

```python
class MaterialExpressionRuntimeVirtualTextureSample(MaterialExpression)
```

Material expression for sampling from a runtime virtual texture.

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionRuntimeVirtualTextureSample.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``adaptive`` (bool):  [Read-Write] Enable sparse adaptive page tables. Note that the bound Virtual Texture should have valid adaptive virtual texture settings for sampling to work correctly.
- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``enable_feedback`` (bool):  [Read-Write] Enable virtual texture feedback.
  Disabling this can result in the virtual texture not reaching the correct mip level.
  It should only be used in cases where we don't care about the correct mip level being resident, or some other process is maintaining the correct level.
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``material_type`` (RuntimeVirtualTextureMaterialType):  [Read-Write] How to interpret the virtual texture contents. Note that the bound Virtual Texture should have the same setting for sampling to work correctly.
- ``mip_value_mode`` (RuntimeVirtualTextureMipValueMode):  [Read-Write] Defines how the mip level is calculated for the virtual texture lookup.
- ``single_physical_space`` (bool):  [Read-Write] Enable page table channel packing. Note that the bound Virtual Texture should have the same setting for sampling to work correctly.
- ``texture_address_mode`` (RuntimeVirtualTextureTextureAddressMode):  [Read-Write] Defines the texture addressing mode.
- ``virtual_texture`` (RuntimeVirtualTexture):  [Read-Write] The virtual texture object to sample.
- ``world_position_origin_type`` (PositionOrigin):  [Read-Write] Defines the reference space for the WorldPosition input.

<a id="unreal.MaterialExpressionRuntimeVirtualTextureSampleParameter"></a>