## MaterialInstanceBasePropertyOverrides Objects

```python
class MaterialInstanceBasePropertyOverrides(StructBase)
```

Properties from the base material that can be overridden in material instances.

**C++ Source:**

- **Module**: Engine
- **File**: MaterialInstanceBasePropertyOverrides.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_mode`` (BlendMode):  [Read-Write] The blend mode
- ``cast_dynamic_shadow_as_masked`` (bool):  [Read-Write] Whether the material should cast shadows as masked even though it has a translucent blend mode.
- ``displacement_fade_range`` (DisplacementFadeRange):  [Read-Write]
- ``displacement_scaling`` (DisplacementScaling):  [Read-Write]
- ``dithered_lod_transition`` (bool):  [Read-Write] Whether the material should support a dithered LOD transition when used with the foliage system.
- ``enable_displacement_fade`` (bool):  [Read-Write] Whether or not displacement fade is enabled.
- ``enable_tessellation`` (bool):  [Read-Write] Whether or not tessellation is enabled. Required for displacement to work.
- ``has_pixel_animation`` (bool):  [Read-Write] Whether the opaque material has any pixel animations happening, that isn't included in the geometric velocities.
  This allows to disable renderer's heuristics that assumes animation is fully described with motion vector, such as TSR's anti-flickering heuristic.
- ``is_thin_surface`` (bool):  [Read-Write] Indicates that the material should be rendered as.
- ``max_world_position_offset_displacement`` (float):  [Read-Write] The maximum World Position Offset distance. Zero means no maximum.
- ``opacity_mask_clip_value`` (float):  [Read-Write] If BlendMode is BLEND_Masked, the surface is not rendered where OpacityMask < OpacityMaskClipValue.
- ``output_translucent_velocity`` (bool):  [Read-Write] Whether the material should output velocity even though it has a translucent blend mode.
- ``override_b_enable_displacement_fade`` (bool):  [Read-Write] Enables override of the eanble displacement fade property.
- ``override_b_enable_tessellation`` (bool):  [Read-Write] Enables override of the enable tessellation property.
- ``override_b_has_pixel_animation`` (bool):  [Read-Write] Enables override of the has pixel animation property.
- ``override_b_is_thin_surface`` (bool):  [Read-Write] Enables override of the IsThinSurface property.
- ``override_blend_mode`` (bool):  [Read-Write] Enables override of the blend mode.
- ``override_cast_dynamic_shadow_as_masked`` (bool):  [Read-Write] Enables override of whether to shadow using masked opacity on translucent materials.
- ``override_displacement_fade_range`` (bool):  [Read-Write] Enables override of the displacement fading range.
- ``override_displacement_scaling`` (bool):  [Read-Write] Enables override of the displacement magnitude and center property.
- ``override_dithered_lod_transition`` (bool):  [Read-Write] Enables override of the dithered LOD transition property.
- ``override_max_world_position_offset_displacement`` (bool):  [Read-Write] Enables override of the max world position offset property.
- ``override_opacity_mask_clip_value`` (bool):  [Read-Write] Enables override of the opacity mask clip value.
- ``override_output_translucent_velocity`` (bool):  [Read-Write] Enables override of the output velocity property.
- ``override_shading_model`` (bool):  [Read-Write] Enables override of the shading model.
- ``override_two_sided`` (bool):  [Read-Write] Enables override of the two sided property.
- ``shading_model`` (MaterialShadingModel):  [Read-Write] The shading model
- ``two_sided`` (bool):  [Read-Write] Indicates that the material should be rendered without backface culling and the normal should be flipped for backfaces.

<a id="unreal.MaterialInstanceBasePropertyOverrides.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.LightmassParameterizedMaterialSettings"></a>