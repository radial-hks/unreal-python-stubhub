## NiagaraSpriteRendererProperties Objects

```python
class NiagaraSpriteRendererProperties(NiagaraRendererProperties)
```

Niagara Sprite Renderer Properties

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraSpriteRendererProperties.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alignment`` (NiagaraSpriteAlignment):  [Read-Write] Imagine the particle texture having an arrow pointing up, these modes define how the particle aligns that texture to other particle attributes.
- ``allow_in_cull_proxies`` (bool):  [Read-Write]
- ``alpha_threshold`` (float):  [Read-Write] Alpha channel values larger than the threshold are considered occupied and will be contained in the bounding geometry.
  Raising this threshold slightly can reduce overdraw in particles using this animation asset.
- ``bounding_mode`` (SubUVBoundingVertexCount):  [Read-Write] More bounding vertices results in reduced overdraw, but adds more triangle overhead.
  The eight vertex mode is best used when the SubUV texture has a lot of space to cut out that is not captured by the four vertex version,
  and when the particles using the texture will be few and large.
- ``camera_offset_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for camera offset when generating sprites?
- ``cast_shadows`` (bool):  [Read-Write] When disabled the renderer will not cast shadows.
  The component controls if shadows are enabled, this flag allows you to disable the renderer casting shadows.
- ``color_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for color when generating sprites?
- ``custom_sorting_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for custom sorting? Defaults to Particles.NormalizedAge.
- ``cutout_texture`` (Texture2D):  [Read-Write] Texture to generate bounding geometry from.
- ``dynamic_material1_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for dynamic material parameters when generating sprites?
- ``dynamic_material2_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for dynamic material parameters when generating sprites?
- ``dynamic_material3_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for dynamic material parameters when generating sprites?
- ``dynamic_material_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for dynamic material parameters when generating sprites?
- ``enable_camera_distance_culling`` (bool):  [Read-Write] Enables frustum culling of individual sprites
- ``facing_mode`` (NiagaraSpriteFacingMode):  [Read-Write] Determines how the particle billboard orients itself relative to the camera.
- ``gpu_translucent_latency`` (NiagaraRendererGpuTranslucentLatency):  [Read-Write] Gpu simulations run at different points in the frame depending on what features are used, i.e. depth buffer, distance fields, etc.
  Opaque materials will run latent when these features are used.
  Translucent materials can choose if they want to use this frames or the previous frames data to match opaque draws.
- ``macro_uv_radius`` (float):  [Read-Write] World space radius that UVs generated with the ParticleMacroUV material node will tile based on.
- ``material`` (MaterialInterface):  [Read-Write] The material used to render the particle. Note that it must have the Use with Niagara Sprites flag checked.
- ``material_parameters`` (NiagaraRendererMaterialParameters):  [Read-Write] If this array has entries, we will create a MaterialInstanceDynamic per Emitter instance from Material and set the Material parameters using the Niagara simulation variables listed.
- ``material_random_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for material randoms when generating sprites?
- ``material_user_param_binding`` (NiagaraUserParameterBinding):  [Read-Write] Use the UMaterialInterface bound to this user variable if it is set to a valid value. If this is bound to a valid value and Material is also set, UserParamBinding wins.
- ``max_camera_distance`` (float):  [Read-Write]
- ``max_facing_camera_blend_distance`` (float):  [Read-Write] When FacingMode is FacingCameraDistanceBlend, the distance at which the sprite is fully facing the camera position
- ``min_camera_distance`` (float):  [Read-Write]
- ``min_facing_camera_blend_distance`` (float):  [Read-Write] When FacingMode is FacingCameraDistanceBlend, the distance at which the sprite is fully facing the camera plane.
- ``motion_vector_setting`` (NiagaraRendererMotionVectorSetting):  [Read-Write] Hint about how to generate motion (velocity) vectors for this renderer.
- ``normalized_age_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for Normalized Age?
- ``opacity_source_mode`` (OpacitySourceMode):  [Read-Write]
- ``pivot_in_uv_space`` (Vector2D):  [Read-Write] Determines the location of the pivot point of this particle. It follows Unreal's UV space, which has the upper left of the image at 0,0 and bottom right at 1,1. The middle is at 0.5, 0.5.
  NOTE: This value is ignored if "Pivot Offset Binding" is bound to a valid attribute
- ``pivot_offset_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for pivot offset? (NOTE: Values are expected to be in UV space).
- ``pixel_coverage_blend`` (float):  [Read-Write] When pixel coverage is enabled this allows you to control the blend of the pixel coverage color adjustment.
  i.e. 1.0 = full, 0.5 = 50/50 blend, 0.0 = none
- ``pixel_coverage_mode`` (NiagaraRendererPixelCoverageMode):  [Read-Write] This setting controls what happens when a sprite becomes less than a pixel in size.
  Disabling will apply nothing and can result in flickering issues, especially with Temporal Super Resolution.
  Automatic will enable the appropriate settings when the material blend mode is some form of translucency, project setting must also be enabled.
  When coverage is less than a pixel, we also calculate a percentage of coverage, and then darken or reduce opacity
  to visually compensate. The different enabled settings allow you to control how the coverage amount is applied to
  your particle color.  If particle color is not connected to your material the compensation will not be applied.
- ``platforms`` (NiagaraPlatformSet):  [Read-Write] Platforms on which this renderer is enabled.
- ``position_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for position when generating sprites?
- ``remove_hmd_roll_in_vr`` (bool):  [Read-Write] If true, removes the HMD view roll (e.g. in VR)
- ``renderer_enabled_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Binding to control if the renderer is enabled or disabled.
  When disabled the renderer does not generate or render any particle data.
  When disabled via a static bool the renderer will be removed in cooked content.
- ``renderer_visibility`` (uint32):  [Read-Write] If a render visibility tag is present, particles whose tag matches this value will be visible in this renderer.
- ``renderer_visibility_tag_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for RendererVisibilityTag?
- ``sort_mode`` (NiagaraSortMode):  [Read-Write] Determines how we sort the particles prior to rendering.
- ``sort_only_when_translucent`` (bool):  [Read-Write] If true, the particles are only sorted when using a translucent material.
- ``sort_order_hint`` (int32):  [Read-Write] By default, emitters are drawn in the order that they are added to the system. This value will allow you to control the order in a more fine-grained manner.
        Materials of the same type (i.e. Transparent) will draw in order from lowest to highest within the system. The default value is 0.
- ``sort_precision`` (NiagaraRendererSortPrecision):  [Read-Write] Sort precision to use when sorting is active.
- ``source_mode`` (NiagaraRendererSourceDataMode):  [Read-Write] Whether or not to draw a single element for the Emitter or to draw the particles.
- ``sprite_alignment_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for sprite alignment when generating sprites?
- ``sprite_facing_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for sprite facing when generating sprites?
- ``sprite_rotation_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for sprite rotation (in degrees) when generating sprites?
- ``sprite_size_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for sprite size when generating sprites?
- ``sub_image_blend`` (bool):  [Read-Write] If true, blends the sub-image UV lookup with its next adjacent member using the fractional part of the SubImageIndex float value as the linear interpolation factor.
- ``sub_image_index_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for sprite sub-image indexing when generating sprites?
- ``sub_image_size`` (Vector2D):  [Read-Write] When using SubImage lookups for particles, this variable contains the number of columns in X and the number of rows in Y.
- ``use_material_cutout_texture`` (bool):  [Read-Write] Use the cutout texture from the material opacity mask, or if none exist, from the material opacity.
- ``uv_scale_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for UV scale when generating sprites?
- ``velocity_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for velocity when generating sprites?

<a id="unreal.NiagaraSpriteRendererProperties.use_material_cutout_texture"></a>

#### use_material_cutout_texture

```python
@property
def use_material_cutout_texture() -> bool
```

(bool):  [Read-Only] Use the cutout texture from the material opacity mask, or if none exist, from the material opacity.

<a id="unreal.BakedShallowWaterSimulationComponent"></a>