## SpotLightComponent Objects

```python
class SpotLightComponent(PointLightComponent)
```

A spot light component emits a directional cone shaped light (Eg a Torch).

**C++ Source:**

- **Module**: Engine
- **File**: SpotLightComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``affect_global_illumination`` (bool):  [Read-Write] Whether the light affects global illumination, when ray-traced global illumination is enabled.
- ``affect_reflection`` (bool):  [Read-Write] Whether the light affects objects in reflections, when ray-traced reflection is enabled.
- ``affect_translucent_lighting`` (bool):  [Read-Write] Whether the light affects translucency or not.  Disabling this can save GPU time when there are many small lights.
- ``affects_world`` (bool):  [Read-Write] Whether the light can affect the world, or whether it is disabled.
  A disabled light will not contribute to the scene in any way.  This setting cannot be changed at runtime and unbuilds lighting when changed.
  Setting this to false has the same effect as deleting the light, so it is useful for non-destructive experiments.
- ``allow_mega_lights`` (bool):  [Read-Write] Whether to allow this light to use MegaLights, if it is enabled in the project settings or Post Process Volume.
  When disabled, the renderer will no longer use stochastic sampling to solve this light's lighting, and will fall back to other shadowing methods, adding significant GPU cost.
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``attenuation_radius`` (float):  [Read-Write] Bounds the light's visible influence.
  This clamping of the light's influence is not physically correct but very important for performance, larger lights cost more.
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``bloom_max_brightness`` (float):  [Read-Write] After exposure is applied, scene color brightness larger than BloomMaxBrightness will be rescaled down to BloomMaxBrightness.
- ``bloom_scale`` (float):  [Read-Write] Scales the additive color.
- ``bloom_threshold`` (float):  [Read-Write] Scene color must be larger than this to create bloom in the light shafts.
- ``bloom_tint`` (Color):  [Read-Write] Multiplies against scene color to create the bloom color.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``cast_deep_shadow`` (bool):  [Read-Write] Whether the light should cast high quality hair-strands self-shadowing. When this option is enabled, an extra GPU cost for this light.
- ``cast_dynamic_shadows`` (bool):  [Read-Write] Whether the light should cast shadows from dynamic objects.  Also requires Cast Shadows to be set to True.
- ``cast_raytraced_shadow`` (CastRayTracedShadow):  [Read-Write]
- ``cast_shadows`` (bool):  [Read-Write] Whether the light should cast any shadows.
- ``cast_shadows_from_cinematic_objects_only`` (bool):  [Read-Write] Whether the light should only cast shadows from components marked as bCastCinematicShadows.
  This is useful for setting up cinematic Movable spotlights aimed at characters and avoiding the shadow depth rendering costs of the background.
  Note: this only works with dynamic shadow maps, not with static shadowing or Ray Traced Distance Field shadows.
- ``cast_static_shadows`` (bool):  [Read-Write] Whether the light should cast shadows from static objects.  Also requires Cast Shadows to be set to True.
- ``cast_translucent_shadows`` (bool):  [Read-Write] Whether the light is allowed to cast dynamic shadows from translucency.
- ``cast_volumetric_shadow`` (bool):  [Read-Write] Whether the light shadows volumetric fog.  Disabling this can save GPU time.
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``contact_shadow_casting_intensity`` (float):  [Read-Write] Intensity of the shadows cast by primitives with "cast contact shadow" enabled. 0 = no shadow, 1 (default) = fully shadowed.
- ``contact_shadow_length`` (float):  [Read-Write] Length of screen space ray trace for sharp contact shadows. Zero is disabled.
- ``contact_shadow_length_in_ws`` (bool):  [Read-Write] Where Length of screen space ray trace for sharp contact shadows is in world space units or in screen space units.
- ``contact_shadow_non_casting_intensity`` (float):  [Read-Write] Intensity of the shadows cast by primitives with "cast contact shadow" disabled. 0 (default) = no shadow, 1 = fully shadowed.
- ``deep_shadow_layer_distribution`` (float):  [Read-Write] Change the deep shadow layers distribution 0:linear distribution (uniform layer distribution), 1:exponential (more details on near small details).
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``diffuse_scale`` (float):  [Read-Write] Multiplier on diffuse lighting. Use only with great care! Any value besides 1 is not physical!
- ``disabled_brightness`` (float):  [Read-Write] Brightness factor applied to the light when the light function is specified but disabled, for example in scene captures that use SceneCapView_LitNoShadows.
  This should be set to the average brightness of the light function material's emissive input, which should be between 0 and 1.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``enable_light_shaft_bloom`` (bool):  [Read-Write] Whether to render light shaft bloom from this light.
  For directional lights, the color around the light direction will be blurred radially and added back to the scene.
  for point lights, the color on pixels closer than the light's SourceRadius will be blurred radially and added back to the scene.
- ``force_cached_shadows_for_movable_primitives`` (bool):  [Read-Write] Enables cached shadows for movable primitives for this light even if r.shadow.cachedshadowscastfrommovableprimitives is 0
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``ies_brightness_scale`` (float):  [Read-Write] Global scale for IES brightness contribution. Only available when "Use IES Brightness" is selected, and a valid IES profile texture is set
- ``ies_texture`` (TextureLightProfile):  [Read-Write] IES texture (light profiles from real world measured data)
- ``indirect_lighting_intensity`` (float):  [Read-Write] Scales the indirect lighting contribution from this light.
  A value of 0 disables any GI from this light. Default is 1.
- ``inner_cone_angle`` (float):  [Read-Write] Degrees.
- ``intensity`` (float):  [Read-Write] Total energy that the light emits.
- ``intensity_units`` (LightUnits):  [Read-Write] Units used for the intensity.
  The peak luminous intensity is measured in candelas,
  while the luminous power is measured in lumens.
- ``inverse_exposure_blend`` (float):  [Read-Write] Blend Factor used to blend between Intensity and Intensity/Exposure.
  This is useful for gameplay lights that should have constant brighness on screen independent of current exposure.
  This feature can cause issues with exposure particularly when used on the primary light on a scene, as such it's usage should be limited.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``light_color`` (Color):  [Read-Write] Filter color of the light.
  Note that this can change the light's effective intensity.
- ``light_falloff_exponent`` (float):  [Read-Write] Controls the radial falloff of the light when UseInverseSquaredFalloff is disabled.
  2 is almost linear and very unrealistic and around 8 it looks reasonable.
  With large exponents, the light has contribution to only a small area of its influence radius but still costs the same as low exponents.
- ``light_function_fade_distance`` (float):  [Read-Write] Distance at which the light function should be completely faded to DisabledBrightness.
  This is useful for hiding aliasing from light functions applied in the distance.
- ``light_function_material`` (MaterialInterface):  [Read-Write] The light function material to be applied to this light.
  Note that only non-lightmapped lights (UseDirectLightMap=False) can have a light function.
  Light functions are supported within VolumetricFog, but only for Directional, Point and Spot lights. Rect lights are not supported.
- ``light_function_scale`` (Vector):  [Read-Write] Scales the light function projection.  X and Y scale in the directions perpendicular to the light's direction, Z scales along the light direction.
- ``lighting_channels`` (LightingChannels):  [Read-Write] Channels that this light should affect.
  These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing.
  Lighting channels are only supported on translucent materials using forward shading (i.e. when not using the translucency lighting volume).
- ``lightmass_settings`` (LightmassPointLightSettings):  [Read-Write] The Lightmass settings for this object.
- ``max_distance_fade_range`` (float):  [Read-Write]
- ``max_draw_distance`` (float):  [Read-Write]
- ``mega_lights_shadow_method`` (MegaLightsShadowMethod):  [Read-Write] Selects which shadowing method should MegaLights use for this light.
  RayTracing - Preferred method, which guarantees fixed MegaLights cost and correct area shadows, but is dependent on the BVH representation quality.
  VirtualShadowMap - Has a significant per light cost, but can cast shadows directly from the Nanite geometry using rasterization.
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``outer_cone_angle`` (float):  [Read-Write] Degrees.
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``ray_start_offset_depth_scale`` (float):  [Read-Write] Controls how large of an offset ray traced shadows have from the receiving surface as the camera gets further away.
  This can be useful to hide self-shadowing artifacts from low resolution distance fields on huge static meshes.
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``samples_per_pixel`` (int32):  [Read-Write] Samples per pixel for ray tracing
- ``shadow_bias`` (float):  [Read-Write] Controls how accurate self shadowing of whole scene shadows from this light are.
  At 0, shadows will start at the their caster surface, but there will be many self shadowing artifacts.
  larger values, shadows will start further from their caster, and there won't be self shadowing artifacts but object might appear to fly.
  around 0.5 seems to be a good tradeoff. This also affects the soft transition of shadows
- ``shadow_resolution_scale`` (float):  [Read-Write] Scales the resolution of shadowmaps used to shadow this light.  By default shadowmap resolution is chosen based on screen size of the caster.
  Setting the scale to zero disables shadow maps, but does not disable, e.g., contact shadows.
  Note: shadowmap resolution is still clamped by 'r.Shadow.MaxResolution'
- ``shadow_sharpen`` (float):  [Read-Write] Amount to sharpen shadow filtering
- ``shadow_slope_bias`` (float):  [Read-Write] Controls how accurate self shadowing of whole scene shadows from this light are. This works in addition to shadow bias, by increasing the
  amount of bias depending on the slope of a surface.
  At 0, shadows will start at the their caster surface, but there will be many self shadowing artifacts.
  larger values, shadows will start further from their caster, and there won't be self shadowing artifacts but object might appear to fly.
  around 0.5 seems to be a good tradeoff. This also affects the soft transition of shadows
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``soft_source_radius`` (float):  [Read-Write] Soft radius of light source shape.
  Note that light sources shapes which intersect shadow casting geometry can cause shadowing artifacts.
- ``source_length`` (float):  [Read-Write] Length of light source shape.
  Note that light sources shapes which intersect shadow casting geometry can cause shadowing artifacts.
- ``source_radius`` (float):  [Read-Write] Radius of light source shape.
  Note that light sources shapes which intersect shadow casting geometry can cause shadowing artifacts.
- ``specular_scale`` (float):  [Read-Write] Multiplier on specular highlights. Use only with great care! Any value besides 1 is not physical!
  Can be used to artistically remove highlights mimicking polarizing filters or photo touch up.
- ``temperature`` (float):  [Read-Write] Color temperature in Kelvin of the blackbody illuminant.
  White (D65) is 6500K.
- ``transmission`` (bool):  [Read-Write] Whether light from this light transmits through surfaces with subsurface scattering profiles. Requires light to be movable.
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``use_ies_brightness`` (bool):  [Read-Write] true: take light brightness from IES profile, false: use the light brightness - the maximum light in one direction is used to define no masking. Use with InverseSquareFalloff. Will be disabled if a valid IES profile texture is not supplied.
- ``use_inverse_squared_falloff`` (bool):  [Read-Write] Whether to use physically based inverse squared distance falloff, where AttenuationRadius is only clamping the light's contribution.
  Disabling inverse squared falloff can be useful when placing fill lights (don't want a super bright spot near the light).
  When enabled, the light's Intensity is in units of lumens, where 1700 lumens is a 100W lightbulb.
  When disabled, the light's Intensity is a brightness scale.
- ``use_ray_traced_distance_field_shadows`` (bool):  [Read-Write] Whether to use ray traced distance field area shadows.  The project setting bGenerateMeshDistanceFields must be enabled for this to have effect.
  Distance field shadows support area lights so they create soft shadows with sharp contacts.
  They have less aliasing artifacts than standard shadowmaps, but inherit all the limitations of distance field representations (only uniform scale, no deformation).
  These shadows have a low per-object cost (and don't depend on triangle count) so they are effective for distant shadows from a dynamic sun.
- ``use_temperature`` (bool):  [Read-Write] false: use white (D65) as illuminant.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.
- ``volumetric_scattering_intensity`` (float):  [Read-Write] Intensity of the volumetric scattering from this light.  This scales Intensity and LightColor.

<a id="unreal.SpotLightComponent.inner_cone_angle"></a>

#### inner_cone_angle

```python
@property
def inner_cone_angle() -> float
```

(float):  [Read-Only] Degrees.

<a id="unreal.SpotLightComponent.outer_cone_angle"></a>

#### outer_cone_angle

```python
@property
def outer_cone_angle() -> float
```

(float):  [Read-Only] Degrees.

<a id="unreal.SpotLightComponent.set_outer_cone_angle"></a>

#### set_outer_cone_angle

```python
def set_outer_cone_angle(new_outer_cone_angle: float) -> None
```

x.set_outer_cone_angle(new_outer_cone_angle) -> None
Set Outer Cone Angle

Args:
    new_outer_cone_angle (float):

<a id="unreal.SpotLightComponent.set_inner_cone_angle"></a>

#### set_inner_cone_angle

```python
def set_inner_cone_angle(new_inner_cone_angle: float) -> None
```

x.set_inner_cone_angle(new_inner_cone_angle) -> None
Set Inner Cone Angle

Args:
    new_inner_cone_angle (float):

<a id="unreal.VolumetricCloudComponent"></a>