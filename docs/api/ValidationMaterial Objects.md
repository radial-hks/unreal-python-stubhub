## ValidationMaterial Objects

```python
class ValidationMaterial(Material)
```

Validation Material

**C++ Source:**

- **Plugin**: DataValidation
- **Module**: DataValidation
- **File**: EditorValidator_Material.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_front_layer_translucency`` (bool):  [Read-Write] Allows a translucent material to be used with Front Layer Translucency by compiling additional shaders. Useful for controlling what should be included in Front Layer Translucency.
- ``allow_negative_emissive_color`` (bool):  [Read-Write] Whether the material should allow outputting negative emissive color values.  Only allowed on unlit materials.
- ``allow_translucent_custom_depth_writes`` (bool):  [Read-Write] Allows a translucent material to be used with custom depth writing by compiling additional shaders.
- ``allow_variable_rate_shading`` (bool):  [Read-Write] Allows the use of variable rate shading when evaluating this material. This will only apply to the base/translucency pass.
- ``always_evaluate_world_position_offset`` (bool):  [Read-Write] Forces World Position Offset to always be evaluated for this material, even if the primitive it's applied to has disabled it
  via "Evaluate World Position Offset" or "World Position Offset Disable Distance".
- ``apply_cloud_fogging`` (bool):  [Read-Write] When true, translucent materials receive cloud contribution as part of the fog evaluation, per vertex or per pixel according to the other selected options. This is a rough approximation but can help in some cases. Defaults to false. Fog is applied on clouds, so Apply Fogging must be true to use this feature.
- ``asset_import_data`` (AssetImportData):  [Read-Write] Importing data and options used for this material
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``automatically_set_usage_in_editor`` (bool):  [Read-Write] Whether to automatically set usage flags based on what the material is applied to in the editor.
  It can be useful to disable this on a base material with many instances, where adding another usage flag accidentally (eg bUsedWithSkeletalMeshes) can add a lot of shader permutations.
- ``blend_mode`` (BlendMode):  [Read-Write] Determines how the material's color is blended with background colors.
- ``blendable_location`` (BlendableLocation):  [Read-Write] Where the node is inserted in the (post processing) graph, only used if domain is PostProcess
- ``blendable_output_alpha`` (bool):  [Read-Write] If this is enabled, the blendable will output alpha
- ``blendable_priority`` (int32):  [Read-Write] If multiple nodes with the same  type are inserted at the same point, this defined order and if they get combined, only used if domain is PostProcess
- ``cast_dynamic_shadow_as_masked`` (bool):  [Read-Write] Whether the material should cast shadows as masked even though it has a translucent blend mode.
- ``cast_ray_traced_shadows`` (bool):  [Read-Write] when true, the material casts ray tracing shadows.
- ``compute_fog_per_pixel`` (bool):  [Read-Write] When true, translucent materials have fog computed for every pixel, which costs more but fixes artifacts due to low tessellation.
- ``contact_shadows`` (bool):  [Read-Write] Contact shadows on translucency
- ``decal_blend_mode`` (DecalBlendMode):  [Read-Write]
  deprecated: No longer used.
- ``disable_depth_test`` (bool):  [Read-Write] Whether to draw on top of opaque pixels even if behind them. This only has meaning for translucency.
- ``disable_pre_exposure_scale`` (bool):  [Read-Write] Disable pre-exposure scale in post process materials (multiply by View.OneOverPreExposure on inputs, View.PreExposure on output).  Useful for
  materials that don't care about the absolute intensity of SceneColor (for example, a blur), simplifying custom HLSL and saving some performance.
  Or useful for non-color UserSceneTextures (for example, mask, matte, modulation, offset, or ID textures), where pre-exposure scale is
  undesirable.  Pre-exposure scale can be manually reapplied via custom HLSL if needed on specific inputs or the output.
- ``displacement_fade_range`` (DisplacementFadeRange):  [Read-Write]
- ``displacement_scaling`` (DisplacementScaling):  [Read-Write]
- ``dither_opacity_mask`` (bool):  [Read-Write] Dither opacity mask. When combined with Temporal AA this can be used as a form of limited translucency which supports all lighting features.
- ``dithered_lod_transition`` (bool):  [Read-Write] Whether meshes rendered with the material should support dithered LOD transitions.
- ``editor_only_data`` (MaterialInterfaceEditorOnlyData):  [Read-Only]
- ``enable_displacement_fade`` (bool):  [Read-Write] Enables fading out and disabling of dynamic displacement in the distance, as displacement becomes unnoticeable
- ``enable_exec_wire`` (bool):  [Read-Write]
- ``enable_mobile_separate_translucency`` (bool):  [Read-Write] Indicates that the translucent material should not be affected by bloom or DOF. (Note: Depth testing is not available)
- ``enable_new_hlsl_generator`` (bool):  [Read-Write]
- ``enable_responsive_aa`` (bool):  [Read-Write] Indicates that the material should be rendered using responsive anti-aliasing. Improves sharpness of small moving particles such as sparks.
  Only use for small moving features because it will cause aliasing of the background.
- ``enable_stencil_test`` (bool):  [Read-Write] Selectively execute post process material only for pixels that pass the stencil test against the Custom Depth/Stencil buffer.
  Pixels that fail the stencil test are filled with the previous post process material output or scene color.
- ``enable_tessellation`` (bool):  [Read-Write] Whether tessellation is enabled on the material. NOTE: Required for displacement to work.
- ``float_precision_mode`` (MaterialFloatPrecisionMode):  [Read-Write] How to use full (highp) precision in the pixel shader.
  highp is slower than the default (mediump) but can be used to work around precision-related rendering errors.
  Use 'Full-precision for MaterialExpressions only' if you still want to keep the precision of the halfs in .ush/.usf
  This setting has no effect on older mobile devices that do not support high precision.
- ``force_compatible_with_light_function_atlas`` (bool):  [Read-Write] Indicates that this material is safe to use with the light function atlas:
   - texture coordinates are manipulated in a way that works.
   - world position and depth are not used in the graph or do work with the atlas.
  Forces all deferred lights to go the fast batched lighting code path (no screen shadow mask).
- ``forward_blends_sky_light_cubemaps`` (bool):  [Read-Write] * Enables blending of sky light cubemap textures. When disabled, the secondary cubemap is only visible when the blend factor is 1.
- ``forward_render_use_preintegrated_gf_for_simple_ibl`` (bool):  [Read-Write] Forward (including mobile) renderer: use preintegrated GF lut for simple IBL, but will use one more sampler.
- ``fully_rough`` (bool):  [Read-Write] Forces the material to be completely rough. Saves a number of instructions and one sampler.
- ``generate_spherical_particle_normals`` (bool):  [Read-Write] Whether to generate spherical normals for particles that use this material.
- ``has_pixel_animation`` (bool):  [Read-Write] Whether the opaque material has any pixel animations happening, that isn't included in the geometric velocities.
  This allows to disable renderer's heuristics that assumes animation is fully described with motion vector, such as TSR's anti-flickering heuristic.
- ``is_blendable`` (bool):  [Read-Write] Allows blendability to be turned off, only used if domain is PostProcess
- ``is_sky`` (bool):  [Read-Write] Unlit and Opaque materials can be used as sky material on a sky dome mesh. When IsSky is true, these meshes will not receive any contribution from the aerial perspective. Height and Volumetric fog effects will still be applied.
- ``is_thin_surface`` (bool):  [Read-Write] Indicates that the material should be rendered as a thin surface (i.e., without inner volume). Only used by Substrate materials. Enabling ThinSurface will disable subsurface profiles.
- ``lightmass_settings`` (LightmassMaterialInterfaceSettings):  [Read-Write] The Lightmass settings for this object.
- ``material_decal_response`` (MaterialDecalResponse):  [Read-Write] Defines how the material reacts on DBuffer decals (Affects look, performance and texture/sample usage).
  Non DBuffer Decals can be disabled on the primitive (e.g. static mesh)
- ``material_domain`` (MaterialDomain):  [Read-Write] The domain that the material's attributes will be evaluated in.
  Certain pieces of material functionality are only valid in certain domains, for example vertex normal is only valid on a surface.
- ``max_world_position_offset_displacement`` (float):  [Read-Write] Specifies the max world position offset of the material. Use this value to resolve issues with culling and self-occlusion caused by
  World Position Offset, and/or to restrict how much offset is permitted (i.e. values are clamped on each axis).
  NOTE: A value of 0.0 effectively means "no maximum", and will not clamp the offsets, however it will also not extend culling bounds.
- ``mobile_enable_high_quality_brdf`` (bool):  [Read-Write] Use the high quality brdf functions on mobile to get better visual effects but adds GPU cost.
- ``nanite_override_material`` (MaterialOverrideNanite):  [Read-Write] An override material which will be used instead of this one when rendering with Nanite.
- ``neural_profile`` (NeuralProfile):  [Read-Write] Neural network profile. For internal usage, not editable/visible
- ``neural_profile_id`` (int8):  [Read-Write] Set by reference object cannot be modified.
- ``normal_curvature_to_roughness`` (bool):  [Read-Write] Reduce roughness based on screen space normal changes.
- ``num_customized_u_vs`` (int32):  [Read-Write] Number of customized UV inputs to display.  Unconnected customized UV inputs will just pass through the vertex UVs.
- ``opacity_mask_clip_value`` (float):  [Read-Write] If BlendMode is BLEND_Masked, the surface is not rendered where OpacityMask < OpacityMaskClipValue.
  If BlendMode is BLEND_Translucent, BLEND_Additive, or BLEND_Modulate, and "Output Depth and Velocity" is enabled,
  the object velocity is not rendered where Opacity < OpacityMaskClipValue.
- ``output_translucent_velocity`` (bool):  [Read-Write] When true, translucent materials will output motion vectors and write to depth buffer in velocity pass.
- ``parameter_group_data`` (Array[ParameterGroupData]):  [Read-Write]
  deprecated: GetEditorOnlyData().ParameterGroupData
- ``phys_material`` (PhysicalMaterial):  [Read-Write] Physical material to use for this graphics material. Used for sounds, effects etc.
- ``phys_material_mask`` (PhysicalMaterialMask):  [Read-Write] Physical material mask to use for this graphics material. Used for sounds, effects etc.
- ``physical_material_map`` (PhysicalMaterial):  [Read-Write] Physical material mask map to use for this graphics material. Used for sounds, effects etc.
- ``pixel_depth_offset_mode`` (PixelDepthOffsetMode):  [Read-Write] Controls whether refraction takes into account the material surface coverage, or not.
- ``preshader_gap`` (uint16):  [Read-Write] If non-zero, overrides r.Material.PreshaderGapInterval for this material.  Workaround for a platform specific register overflow bug.
- ``preview_mesh`` (SoftObjectPath):  [Read-Write] The mesh used by the material editor to preview the material.
- ``refraction_coverage_mode`` (RefractionCoverageMode):  [Read-Write] Controls whether refraction takes into account the material surface coverage, or not.
- ``refraction_depth_bias`` (float):  [Read-Write] This is the refraction depth bias, larger values offset distortion to prevent closer objects from rendering into the distorted surface at acute viewing angles but increases the disconnect between surface and where the refraction starts.
- ``refraction_method`` (RefractionMode):  [Read-Write] Controls how the Refraction input is interpreted and how the refraction offset into scene color is computed for this material.
- ``resolution_relative_to_input`` (Name):  [Read-Write] Set output resolution relative to the given User Scene Texture input.  Negative User Texture Divisors upsample (clamped at full resolution).
- ``screen_space_reflections`` (bool):  [Read-Write] SSR on translucency
- ``shading_model`` (MaterialShadingModel):  [Read-Write] Determines how inputs are combined to create the material's final color.
- ``shading_rate`` (MaterialShadingRate):  [Read-Write] Select what shading rate to apply, on platforms that support variable rate shading.
  Non-1x1 rates will reduce the rasterization fidelity for the material; they will not super-sample the material.
  This can save GPU performance on materials where reduced fidelity is acceptable.
- ``stencil_compare`` (MaterialStencilCompare):  [Read-Write]
- ``stencil_ref_value`` (uint8):  [Read-Write]
- ``subsurface_profile`` (SubsurfaceProfile):  [Read-Write] SubsurfaceProfile, for Screen Space Subsurface Scattering..
- ``tangent_space_normal`` (bool):  [Read-Write] Whether the material takes a tangent space normal or a world space normal as input.
  (TangentSpace requires extra instructions but is often more convenient).
- ``thumbnail_info`` (ThumbnailInfo):  [Read-Only] Information for thumbnail rendering
- ``translucency_directional_lighting_intensity`` (float):  [Read-Write] Useful for artificially increasing the influence of the normal on the lighting result for translucency.
  A value larger than 1 increases the influence of the normal, a value smaller than 1 makes the lighting more ambient.
- ``translucency_lighting_mode`` (TranslucencyLightingMode):  [Read-Write] Sets the lighting mode that will be used on this material if it is translucent.
- ``translucency_pass`` (MaterialTranslucencyPass):  [Read-Write] Specifies the separate pass in which to render translucency.
  This can be used to avoid artifacts caused by certain post processing effects.
- ``translucent_backscattering_exponent`` (float):  [Read-Write] Controls how diffuse the material's backscattering is when using the MSM_Subsurface shading model.
  Larger exponents give a less diffuse look (smaller, brighter backscattering highlight).
  This is only used when the object is casting a volumetric translucent shadow from a directional light.
- ``translucent_multiple_scattering_extinction`` (LinearColor):  [Read-Write] Colored extinction factor used to approximate multiple scattering in dense volumes.
  This is only used when the object is casting a volumetric translucent shadow.
- ``translucent_self_shadow_density_scale`` (float):  [Read-Write] Scale used to make translucent self-shadowing more or less opaque than the material's shadow on other objects.
  This is only used when the object is casting a volumetric translucent shadow.
- ``translucent_self_shadow_second_density_scale`` (float):  [Read-Write] Used to make a second self shadow gradient, to add interesting shading in the shadow of the first.
- ``translucent_self_shadow_second_opacity`` (float):  [Read-Write] Controls the strength of the second self shadow gradient.
- ``translucent_shadow_density_scale`` (float):  [Read-Write] Scale used to make translucent shadows more or less opaque than the material's actual opacity.
- ``translucent_shadow_start_offset`` (float):  [Read-Write] Local space distance to bias the translucent shadow.  Positive values move the shadow away from the light.
- ``two_sided`` (bool):  [Read-Write] Indicates that the material should be rendered without backface culling and the normal should be flipped for backfaces.
- ``use_alpha_to_coverage`` (bool):  [Read-Write] Use alpha to coverage for masked material on mobile, make sure MSAA is enabled as well.
- ``use_emissive_for_dynamic_area_lighting`` (bool):  [Read-Write] If enabled, the material's emissive colour is injected into the LightPropagationVolume
- ``use_hq_forward_reflections`` (bool):  [Read-Write] * Forward renderer: enables multiple parallax-corrected reflection captures that blend together.
- ``use_lightmap_directionality`` (bool):  [Read-Write] Use lightmap directionality and per pixel normals. If disabled, lighting from lightmaps will be flat but cheaper.
- ``use_material_attributes`` (bool):  [Read-Write] when true, the material attributes pin is used instead of the regular pins.
- ``use_planar_forward_reflections`` (bool):  [Read-Write] Enables planar reflection when using the forward renderer or mobile. Enabling this setting reduces the number of samplers available to the material as one more sampler will be used for the planar reflection.
- ``use_translucency_vertex_fog`` (bool):  [Read-Write] When true, translucent materials are fogged. Defaults to true.
- ``used_shading_models`` (str):  [Read-Only] These are the shading models present in this material. Note that all these shading models might not be used in all feature levels and quality levels.
- ``used_with_beam_trails`` (bool):  [Read-Write] Indicates that the material and its instances can be used with beam trails
  This will result in the shaders required to support beam trails being compiled which will increase shader compile time and memory usage.
- ``used_with_clothing`` (bool):  [Read-Write] Indicates that the material and its instances can be used with clothing
  This will result in the shaders required to support clothing being compiled which will increase shader compile time and memory usage.
- ``used_with_editor_compositing`` (bool):  [Read-Write] Indicates that the material and its instances can be used with editor compositing
  This will result in the shaders required to support editor compositing being compiled which will increase shader compile time and memory usage.
- ``used_with_geometry_cache`` (bool):  [Read-Write]
- ``used_with_geometry_collections`` (bool):  [Read-Write] Indicates that the material and its instances can be use with geometry collections
  This will result in the shaders required to support geometry collections being compiled which will increase shader compile time and memory usage.
- ``used_with_hair_strands`` (bool):  [Read-Write] Indicates that the material and its instances can be use with hair strands
  This will result in the shaders required to support hair strands geometries being compiled which will increase shader compile time and memory usage.
- ``used_with_heterogeneous_volumes`` (bool):  [Read-Write] Indicates that the material and its instances with heterogeneous volumes. Without that flag, it can only be used on volumetric fog.
  This will result in the shaders required to support Heterogeneous Volumes rendering being compiled which will increase shader compile time and memory usage.
- ``used_with_instanced_static_meshes`` (bool):  [Read-Write] Indicates that the material and its instances can be used with instanced static meshes
  This will result in the shaders required to support instanced static meshes being compiled which will increase shader compile time and memory usage.
- ``used_with_lidar_point_cloud`` (bool):  [Read-Write] Indicates that the material and its instances can be use with LiDAR Point Clouds
  This will result in the shaders required to support LiDAR Point Cloud geometries being compiled which will increase shader compile time and memory usage.
- ``used_with_mesh_particles`` (bool):  [Read-Write] Indicates that the material and its instances can be used with mesh particles
  This will result in the shaders required to support mesh particles being compiled which will increase shader compile time and memory usage.
- ``used_with_morph_targets`` (bool):  [Read-Write] Indicates that the material and its instances can be used with morph targets
  This will result in the shaders required to support morph targets being compiled which will increase shader compile time and memory usage.
- ``used_with_nanite`` (bool):  [Read-Write] Indicates that the material and its instances can be used with Nanite meshes.
  This will result in the shaders required to support Nanite geometries being compiled which will increase shader compile time and memory usage.
- ``used_with_neural_networks`` (bool):  [Read-Write] Indicates that the material and its instances can be used with neural network engine.
  This will result in the shaders required to support neural network engine being compiled which will increase shader compile time and memory usage.
  In addition, an additional pass will run before the postprocess pass for neural network engine, which will increase the rendering cost due to
  buffer copy and inference.
- ``used_with_niagara_mesh_particles`` (bool):  [Read-Write]
- ``used_with_niagara_ribbons`` (bool):  [Read-Write]
- ``used_with_niagara_sprites`` (bool):  [Read-Write] Indicates that the material and its instances can be used with Niagara sprites (meshes and ribbons, respectively)
  This will result in the shaders required to support Niagara sprites being compiled which will increase shader compile time and memory usage.
- ``used_with_particle_sprites`` (bool):  [Read-Write] Indicates that the material and its instances can be used with particle sprites
  This will result in the shaders required to support particle sprites being compiled which will increase shader compile time and memory usage.
- ``used_with_skeletal_mesh`` (bool):  [Read-Write] Indicates that the material and its instances can be used with skeletal meshes.
  This will result in the shaders required to support skeletal meshes being compiled which will increase shader compile time and memory usage.
- ``used_with_spline_meshes`` (bool):  [Read-Write] Indicates that the material and its instances can be used with spline meshes
  This will result in the shaders required to support spline meshes being compiled which will increase shader compile time and memory usage.
- ``used_with_static_lighting`` (bool):  [Read-Write] Indicates that the material and its instances can be used with static lighting
  This will result in the shaders required to support static lighting being compiled which will increase shader compile time and memory usage.
- ``used_with_virtual_heightfield_mesh`` (bool):  [Read-Write] Indicates that the material and its instances can be used with Virtual Heightfield Mesh.
  This will result in the shaders required to support Virtual Heightfield Mesh geometries being compiled which will increase shader compile time and memory usage.
- ``used_with_volumetric_cloud`` (bool):  [Read-Write] Indicates that the material and its instances with volumetric cloud. Without that flag, it can only be used on volumetric fog.
  This will result in the shaders required to support Volumetric Cloud rendering being compiled which will increase shader compile time and memory usage.
- ``used_with_water`` (bool):  [Read-Write] Indicates that the material and its instances can be use with water
  This will result in the shaders required to support water meshes being compiled which will increase shader compile time and memory usage.
- ``user_scene_texture`` (Name):  [Read-Write] Specify a user generated scene texture as output, overriding the default output implied by "Blendable Location", only used if domain is PostProcess
- ``user_texture_divisor`` (IntPoint):  [Read-Write] A divisor for the resolution of the User Scene Texture above, allowing an intermediate with reduced resolution
- ``wireframe`` (bool):  [Read-Write] Enables a wireframe view of the mesh the material is applied to.
- ``write_only_alpha`` (bool):  [Read-Write] Whether the transluency pass should write its alpha, and only the alpha, into the framebuffer

<a id="unreal.DirtyFilesChangelistValidator"></a>