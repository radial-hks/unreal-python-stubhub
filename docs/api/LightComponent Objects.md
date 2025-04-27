## LightComponent Objects

```python
class LightComponent(LightComponentBase)
```

Light Component

**C++ Source:**

- **Module**: Engine
- **File**: LightComponent.h

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
- ``intensity`` (float):  [Read-Write] Total energy that the light emits.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``light_color`` (Color):  [Read-Write] Filter color of the light.
  Note that this can change the light's effective intensity.
- ``light_function_fade_distance`` (float):  [Read-Write] Distance at which the light function should be completely faded to DisabledBrightness.
  This is useful for hiding aliasing from light functions applied in the distance.
- ``light_function_material`` (MaterialInterface):  [Read-Write] The light function material to be applied to this light.
  Note that only non-lightmapped lights (UseDirectLightMap=False) can have a light function.
  Light functions are supported within VolumetricFog, but only for Directional, Point and Spot lights. Rect lights are not supported.
- ``light_function_scale`` (Vector):  [Read-Write] Scales the light function projection.  X and Y scale in the directions perpendicular to the light's direction, Z scales along the light direction.
- ``lighting_channels`` (LightingChannels):  [Read-Write] Channels that this light should affect.
  These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing.
  Lighting channels are only supported on translucent materials using forward shading (i.e. when not using the translucency lighting volume).
- ``max_distance_fade_range`` (float):  [Read-Write]
- ``max_draw_distance`` (float):  [Read-Write]
- ``mega_lights_shadow_method`` (MegaLightsShadowMethod):  [Read-Write] Selects which shadowing method should MegaLights use for this light.
  RayTracing - Preferred method, which guarantees fixed MegaLights cost and correct area shadows, but is dependent on the BVH representation quality.
  VirtualShadowMap - Has a significant per light cost, but can cast shadows directly from the Nanite geometry using rasterization.
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
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
- ``specular_scale`` (float):  [Read-Write] Multiplier on specular highlights. Use only with great care! Any value besides 1 is not physical!
  Can be used to artistically remove highlights mimicking polarizing filters or photo touch up.
- ``temperature`` (float):  [Read-Write] Color temperature in Kelvin of the blackbody illuminant.
  White (D65) is 6500K.
- ``transmission`` (bool):  [Read-Write] Whether light from this light transmits through surfaces with subsurface scattering profiles. Requires light to be movable.
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``use_ies_brightness`` (bool):  [Read-Write] true: take light brightness from IES profile, false: use the light brightness - the maximum light in one direction is used to define no masking. Use with InverseSquareFalloff. Will be disabled if a valid IES profile texture is not supplied.
- ``use_ray_traced_distance_field_shadows`` (bool):  [Read-Write] Whether to use ray traced distance field area shadows.  The project setting bGenerateMeshDistanceFields must be enabled for this to have effect.
  Distance field shadows support area lights so they create soft shadows with sharp contacts.
  They have less aliasing artifacts than standard shadowmaps, but inherit all the limitations of distance field representations (only uniform scale, no deformation).
  These shadows have a low per-object cost (and don't depend on triangle count) so they are effective for distant shadows from a dynamic sun.
- ``use_temperature`` (bool):  [Read-Write] false: use white (D65) as illuminant.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.
- ``volumetric_scattering_intensity`` (float):  [Read-Write] Intensity of the volumetric scattering from this light.  This scales Intensity and LightColor.

<a id="unreal.LightComponent.temperature"></a>

#### temperature

```python
@property
def temperature() -> float
```

(float):  [Read-Only] Color temperature in Kelvin of the blackbody illuminant.
White (D65) is 6500K.

<a id="unreal.LightComponent.use_temperature"></a>

#### use_temperature

```python
@property
def use_temperature() -> bool
```

(bool):  [Read-Only] false: use white (D65) as illuminant.

<a id="unreal.LightComponent.specular_scale"></a>

#### specular_scale

```python
@property
def specular_scale() -> float
```

(float):  [Read-Only] Multiplier on specular highlights. Use only with great care! Any value besides 1 is not physical!
Can be used to artistically remove highlights mimicking polarizing filters or photo touch up.

<a id="unreal.LightComponent.diffuse_scale"></a>

#### diffuse_scale

```python
@property
def diffuse_scale() -> float
```

(float):  [Read-Only] Multiplier on diffuse lighting. Use only with great care! Any value besides 1 is not physical!

<a id="unreal.LightComponent.shadow_resolution_scale"></a>

#### shadow_resolution_scale

```python
@property
def shadow_resolution_scale() -> float
```

(float):  [Read-Only] Scales the resolution of shadowmaps used to shadow this light.  By default shadowmap resolution is chosen based on screen size of the caster.
Setting the scale to zero disables shadow maps, but does not disable, e.g., contact shadows.
Note: shadowmap resolution is still clamped by 'r.Shadow.MaxResolution'

<a id="unreal.LightComponent.shadow_bias"></a>

#### shadow_bias

```python
@property
def shadow_bias() -> float
```

(float):  [Read-Only] Controls how accurate self shadowing of whole scene shadows from this light are.
At 0, shadows will start at the their caster surface, but there will be many self shadowing artifacts.
larger values, shadows will start further from their caster, and there won't be self shadowing artifacts but object might appear to fly.
around 0.5 seems to be a good tradeoff. This also affects the soft transition of shadows

<a id="unreal.LightComponent.shadow_slope_bias"></a>

#### shadow_slope_bias

```python
@property
def shadow_slope_bias() -> float
```

(float):  [Read-Only] Controls how accurate self shadowing of whole scene shadows from this light are. This works in addition to shadow bias, by increasing the
amount of bias depending on the slope of a surface.
At 0, shadows will start at the their caster surface, but there will be many self shadowing artifacts.
larger values, shadows will start further from their caster, and there won't be self shadowing artifacts but object might appear to fly.
around 0.5 seems to be a good tradeoff. This also affects the soft transition of shadows

<a id="unreal.LightComponent.shadow_sharpen"></a>

#### shadow_sharpen

```python
@property
def shadow_sharpen() -> float
```

(float):  [Read-Only] Amount to sharpen shadow filtering

<a id="unreal.LightComponent.contact_shadow_length"></a>

#### contact_shadow_length

```python
@property
def contact_shadow_length() -> float
```

(float):  [Read-Write] Length of screen space ray trace for sharp contact shadows. Zero is disabled.

<a id="unreal.LightComponent.contact_shadow_length"></a>

#### contact_shadow_length

```python
@contact_shadow_length.setter
def contact_shadow_length(value: float) -> None
```

<a id="unreal.LightComponent.contact_shadow_length_in_ws"></a>

#### contact_shadow_length_in_ws

```python
@property
def contact_shadow_length_in_ws() -> bool
```

(bool):  [Read-Write] Where Length of screen space ray trace for sharp contact shadows is in world space units or in screen space units.

<a id="unreal.LightComponent.contact_shadow_length_in_ws"></a>

#### contact_shadow_length_in_ws

```python
@contact_shadow_length_in_ws.setter
def contact_shadow_length_in_ws(value: bool) -> None
```

<a id="unreal.LightComponent.contact_shadow_casting_intensity"></a>

#### contact_shadow_casting_intensity

```python
@property
def contact_shadow_casting_intensity() -> float
```

(float):  [Read-Write] Intensity of the shadows cast by primitives with "cast contact shadow" enabled. 0 = no shadow, 1 (default) = fully shadowed.

<a id="unreal.LightComponent.contact_shadow_casting_intensity"></a>

#### contact_shadow_casting_intensity

```python
@contact_shadow_casting_intensity.setter
def contact_shadow_casting_intensity(value: float) -> None
```

<a id="unreal.LightComponent.contact_shadow_non_casting_intensity"></a>

#### contact_shadow_non_casting_intensity

```python
@property
def contact_shadow_non_casting_intensity() -> float
```

(float):  [Read-Write] Intensity of the shadows cast by primitives with "cast contact shadow" disabled. 0 (default) = no shadow, 1 = fully shadowed.

<a id="unreal.LightComponent.contact_shadow_non_casting_intensity"></a>

#### contact_shadow_non_casting_intensity

```python
@contact_shadow_non_casting_intensity.setter
def contact_shadow_non_casting_intensity(value: float) -> None
```

<a id="unreal.LightComponent.cast_translucent_shadows"></a>

#### cast_translucent_shadows

```python
@property
def cast_translucent_shadows() -> bool
```

(bool):  [Read-Only] Whether the light is allowed to cast dynamic shadows from translucency.

<a id="unreal.LightComponent.cast_shadows_from_cinematic_objects_only"></a>

#### cast_shadows_from_cinematic_objects_only

```python
@property
def cast_shadows_from_cinematic_objects_only() -> bool
```

(bool):  [Read-Only] Whether the light should only cast shadows from components marked as bCastCinematicShadows.
This is useful for setting up cinematic Movable spotlights aimed at characters and avoiding the shadow depth rendering costs of the background.
Note: this only works with dynamic shadow maps, not with static shadowing or Ray Traced Distance Field shadows.

<a id="unreal.LightComponent.force_cached_shadows_for_movable_primitives"></a>

#### force_cached_shadows_for_movable_primitives

```python
@property
def force_cached_shadows_for_movable_primitives() -> bool
```

(bool):  [Read-Only] Enables cached shadows for movable primitives for this light even if r.shadow.cachedshadowscastfrommovableprimitives is 0

<a id="unreal.LightComponent.allow_mega_lights"></a>

#### allow_mega_lights

```python
@property
def allow_mega_lights() -> bool
```

(bool):  [Read-Only] Whether to allow this light to use MegaLights, if it is enabled in the project settings or Post Process Volume.
When disabled, the renderer will no longer use stochastic sampling to solve this light's lighting, and will fall back to other shadowing methods, adding significant GPU cost.

<a id="unreal.LightComponent.mega_lights_shadow_method"></a>

#### mega_lights_shadow_method

```python
@property
def mega_lights_shadow_method() -> MegaLightsShadowMethod
```

(MegaLightsShadowMethod):  [Read-Only] Selects which shadowing method should MegaLights use for this light.
RayTracing - Preferred method, which guarantees fixed MegaLights cost and correct area shadows, but is dependent on the BVH representation quality.
VirtualShadowMap - Has a significant per light cost, but can cast shadows directly from the Nanite geometry using rasterization.

<a id="unreal.LightComponent.lighting_channels"></a>

#### lighting_channels

```python
@property
def lighting_channels() -> LightingChannels
```

(LightingChannels):  [Read-Only] Channels that this light should affect.
These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing.
Lighting channels are only supported on translucent materials using forward shading (i.e. when not using the translucency lighting volume).

<a id="unreal.LightComponent.light_function_material"></a>

#### light_function_material

```python
@property
def light_function_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Only] The light function material to be applied to this light.
Note that only non-lightmapped lights (UseDirectLightMap=False) can have a light function.
Light functions are supported within VolumetricFog, but only for Directional, Point and Spot lights. Rect lights are not supported.

<a id="unreal.LightComponent.light_function_scale"></a>

#### light_function_scale

```python
@property
def light_function_scale() -> Vector
```

(Vector):  [Read-Only] Scales the light function projection.  X and Y scale in the directions perpendicular to the light's direction, Z scales along the light direction.

<a id="unreal.LightComponent.ies_texture"></a>

#### ies_texture

```python
@property
def ies_texture() -> TextureLightProfile
```

(TextureLightProfile):  [Read-Only] IES texture (light profiles from real world measured data)

<a id="unreal.LightComponent.use_ies_brightness"></a>

#### use_ies_brightness

```python
@property
def use_ies_brightness() -> bool
```

(bool):  [Read-Only] true: take light brightness from IES profile, false: use the light brightness - the maximum light in one direction is used to define no masking. Use with InverseSquareFalloff. Will be disabled if a valid IES profile texture is not supplied.

<a id="unreal.LightComponent.ies_brightness_scale"></a>

#### ies_brightness_scale

```python
@property
def ies_brightness_scale() -> float
```

(float):  [Read-Only] Global scale for IES brightness contribution. Only available when "Use IES Brightness" is selected, and a valid IES profile texture is set

<a id="unreal.LightComponent.light_function_fade_distance"></a>

#### light_function_fade_distance

```python
@property
def light_function_fade_distance() -> float
```

(float):  [Read-Only] Distance at which the light function should be completely faded to DisabledBrightness.
This is useful for hiding aliasing from light functions applied in the distance.

<a id="unreal.LightComponent.disabled_brightness"></a>

#### disabled_brightness

```python
@property
def disabled_brightness() -> float
```

(float):  [Read-Only] Brightness factor applied to the light when the light function is specified but disabled, for example in scene captures that use SceneCapView_LitNoShadows.
This should be set to the average brightness of the light function material's emissive input, which should be between 0 and 1.

<a id="unreal.LightComponent.enable_light_shaft_bloom"></a>

#### enable_light_shaft_bloom

```python
@property
def enable_light_shaft_bloom() -> bool
```

(bool):  [Read-Only] Whether to render light shaft bloom from this light.
For directional lights, the color around the light direction will be blurred radially and added back to the scene.
for point lights, the color on pixels closer than the light's SourceRadius will be blurred radially and added back to the scene.

<a id="unreal.LightComponent.bloom_scale"></a>

#### bloom_scale

```python
@property
def bloom_scale() -> float
```

(float):  [Read-Only] Scales the additive color.

<a id="unreal.LightComponent.bloom_threshold"></a>

#### bloom_threshold

```python
@property
def bloom_threshold() -> float
```

(float):  [Read-Only] Scene color must be larger than this to create bloom in the light shafts.

<a id="unreal.LightComponent.bloom_max_brightness"></a>

#### bloom_max_brightness

```python
@property
def bloom_max_brightness() -> float
```

(float):  [Read-Only] After exposure is applied, scene color brightness larger than BloomMaxBrightness will be rescaled down to BloomMaxBrightness.

<a id="unreal.LightComponent.bloom_tint"></a>

#### bloom_tint

```python
@property
def bloom_tint() -> Color
```

(Color):  [Read-Only] Multiplies against scene color to create the bloom color.

<a id="unreal.LightComponent.use_ray_traced_distance_field_shadows"></a>

#### use_ray_traced_distance_field_shadows

```python
@property
def use_ray_traced_distance_field_shadows() -> bool
```

(bool):  [Read-Only] Whether to use ray traced distance field area shadows.  The project setting bGenerateMeshDistanceFields must be enabled for this to have effect.
Distance field shadows support area lights so they create soft shadows with sharp contacts.
They have less aliasing artifacts than standard shadowmaps, but inherit all the limitations of distance field representations (only uniform scale, no deformation).
These shadows have a low per-object cost (and don't depend on triangle count) so they are effective for distant shadows from a dynamic sun.

<a id="unreal.LightComponent.ray_start_offset_depth_scale"></a>

#### ray_start_offset_depth_scale

```python
@property
def ray_start_offset_depth_scale() -> float
```

(float):  [Read-Only] Controls how large of an offset ray traced shadows have from the receiving surface as the camera gets further away.
This can be useful to hide self-shadowing artifacts from low resolution distance fields on huge static meshes.

<a id="unreal.LightComponent.set_volumetric_scattering_intensity"></a>

#### set_volumetric_scattering_intensity

```python
def set_volumetric_scattering_intensity(new_intensity: float) -> None
```

x.set_volumetric_scattering_intensity(new_intensity) -> None
Set Volumetric Scattering Intensity

Args:
    new_intensity (float):

<a id="unreal.LightComponent.set_use_temperature"></a>

#### set_use_temperature

```python
def set_use_temperature(new_value: bool) -> None
```

x.set_use_temperature(new_value) -> None
Set Use Temperature

Args:
    new_value (bool):

<a id="unreal.LightComponent.set_use_ray_traced_distance_field_shadows"></a>

#### set_use_ray_traced_distance_field_shadows

```python
def set_use_ray_traced_distance_field_shadows(new_value: bool) -> None
```

x.set_use_ray_traced_distance_field_shadows(new_value) -> None
Set Use Ray Traced Distance Field Shadows

Args:
    new_value (bool):

<a id="unreal.LightComponent.set_use_ies_brightness"></a>

#### set_use_ies_brightness

```python
def set_use_ies_brightness(new_value: bool) -> None
```

x.set_use_ies_brightness(new_value) -> None
Set Use IESBrightness

Args:
    new_value (bool):

<a id="unreal.LightComponent.set_transmission"></a>

#### set_transmission

```python
def set_transmission(new_value: bool) -> None
```

x.set_transmission(new_value) -> None
Set Transmission

Args:
    new_value (bool):

<a id="unreal.LightComponent.set_temperature"></a>

#### set_temperature

```python
def set_temperature(new_temperature: float) -> None
```

x.set_temperature(new_temperature) -> None
Set Temperature

Args:
    new_temperature (float):

<a id="unreal.LightComponent.set_specular_scale"></a>

#### set_specular_scale

```python
def set_specular_scale(new_value: float) -> None
```

x.set_specular_scale(new_value) -> None
Set Specular Scale

Args:
    new_value (float):

<a id="unreal.LightComponent.set_shadow_slope_bias"></a>

#### set_shadow_slope_bias

```python
def set_shadow_slope_bias(new_value: float) -> None
```

x.set_shadow_slope_bias(new_value) -> None
Set Shadow Slope Bias

Args:
    new_value (float):

<a id="unreal.LightComponent.set_shadow_bias"></a>

#### set_shadow_bias

```python
def set_shadow_bias(new_value: float) -> None
```

x.set_shadow_bias(new_value) -> None
Set Shadow Bias

Args:
    new_value (float):

<a id="unreal.LightComponent.set_lighting_channels"></a>

#### set_lighting_channels

```python
def set_lighting_channels(channel0: bool, channel1: bool,
                          channel2: bool) -> None
```

x.set_lighting_channels(channel0, channel1, channel2) -> None
Set Lighting Channels

Args:
    channel0 (bool): 
    channel1 (bool): 
    channel2 (bool):

<a id="unreal.LightComponent.set_light_function_scale"></a>

#### set_light_function_scale

```python
def set_light_function_scale(new_light_function_scale: Vector) -> None
```

x.set_light_function_scale(new_light_function_scale) -> None
Set Light Function Scale

Args:
    new_light_function_scale (Vector):

<a id="unreal.LightComponent.set_light_function_material"></a>

#### set_light_function_material

```python
def set_light_function_material(
        new_light_function_material: MaterialInterface) -> None
```

x.set_light_function_material(new_light_function_material) -> None
Set Light Function Material

Args:
    new_light_function_material (MaterialInterface):

<a id="unreal.LightComponent.set_light_function_fade_distance"></a>

#### set_light_function_fade_distance

```python
def set_light_function_fade_distance(
        new_light_function_fade_distance: float) -> None
```

x.set_light_function_fade_distance(new_light_function_fade_distance) -> None
Set Light Function Fade Distance

Args:
    new_light_function_fade_distance (float):

<a id="unreal.LightComponent.set_light_function_disabled_brightness"></a>

#### set_light_function_disabled_brightness

```python
def set_light_function_disabled_brightness(new_value: float) -> None
```

x.set_light_function_disabled_brightness(new_value) -> None
Set Light Function Disabled Brightness

Args:
    new_value (float):

<a id="unreal.LightComponent.set_light_color"></a>

#### set_light_color

```python
def set_light_color(new_light_color: LinearColor, srgb: bool = True) -> None
```

x.set_light_color(new_light_color, srgb=True) -> None
Set color of the light

Args:
    new_light_color (LinearColor): 
    srgb (bool):

<a id="unreal.LightComponent.set_intensity"></a>

#### set_intensity

```python
def set_intensity(new_intensity: float) -> None
```

x.set_intensity(new_intensity) -> None
Set intensity of the light

Args:
    new_intensity (float):

<a id="unreal.LightComponent.set_brightness"></a>

#### set_brightness

```python
def set_brightness(new_intensity: float) -> None
```

deprecated: 'set_brightness' was renamed to 'set_intensity'.

<a id="unreal.LightComponent.set_indirect_lighting_intensity"></a>

#### set_indirect_lighting_intensity

```python
def set_indirect_lighting_intensity(new_intensity: float) -> None
```

x.set_indirect_lighting_intensity(new_intensity) -> None
Set Indirect Lighting Intensity

Args:
    new_intensity (float):

<a id="unreal.LightComponent.set_ies_texture"></a>

#### set_ies_texture

```python
def set_ies_texture(new_value: TextureLightProfile) -> None
```

x.set_ies_texture(new_value) -> None
Set IESTexture

Args:
    new_value (TextureLightProfile):

<a id="unreal.LightComponent.set_ies_brightness_scale"></a>

#### set_ies_brightness_scale

```python
def set_ies_brightness_scale(new_value: float) -> None
```

x.set_ies_brightness_scale(new_value) -> None
Set IESBrightness Scale

Args:
    new_value (float):

<a id="unreal.LightComponent.set_force_cached_shadows_for_movable_primitives"></a>

#### set_force_cached_shadows_for_movable_primitives

```python
def set_force_cached_shadows_for_movable_primitives(new_value: bool) -> None
```

x.set_force_cached_shadows_for_movable_primitives(new_value) -> None
Set Force Cached Shadows for Movable Primitives

Args:
    new_value (bool):

<a id="unreal.LightComponent.set_enable_light_shaft_bloom"></a>

#### set_enable_light_shaft_bloom

```python
def set_enable_light_shaft_bloom(new_value: bool) -> None
```

x.set_enable_light_shaft_bloom(new_value) -> None
Set Enable Light Shaft Bloom

Args:
    new_value (bool):

<a id="unreal.LightComponent.set_diffuse_scale"></a>

#### set_diffuse_scale

```python
def set_diffuse_scale(new_value: float) -> None
```

x.set_diffuse_scale(new_value) -> None
Set Diffuse Scale

Args:
    new_value (float):

<a id="unreal.LightComponent.set_bloom_tint"></a>

#### set_bloom_tint

```python
def set_bloom_tint(new_value: Color) -> None
```

x.set_bloom_tint(new_value) -> None
Set Bloom Tint

Args:
    new_value (Color):

<a id="unreal.LightComponent.set_bloom_threshold"></a>

#### set_bloom_threshold

```python
def set_bloom_threshold(new_value: float) -> None
```

x.set_bloom_threshold(new_value) -> None
Set Bloom Threshold

Args:
    new_value (float):

<a id="unreal.LightComponent.set_bloom_scale"></a>

#### set_bloom_scale

```python
def set_bloom_scale(new_value: float) -> None
```

x.set_bloom_scale(new_value) -> None
Set Bloom Scale

Args:
    new_value (float):

<a id="unreal.LightComponent.set_bloom_max_brightness"></a>

#### set_bloom_max_brightness

```python
def set_bloom_max_brightness(new_value: float) -> None
```

x.set_bloom_max_brightness(new_value) -> None
Set Bloom Max Brightness

Args:
    new_value (float):

<a id="unreal.LightComponent.set_affect_translucent_lighting"></a>

#### set_affect_translucent_lighting

```python
def set_affect_translucent_lighting(new_value: bool) -> None
```

x.set_affect_translucent_lighting(new_value) -> None
Set Affect Translucent Lighting

Args:
    new_value (bool):

<a id="unreal.DirectionalLightComponent"></a>