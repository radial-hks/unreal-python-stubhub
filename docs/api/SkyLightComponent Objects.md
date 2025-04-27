## SkyLightComponent Objects

```python
class SkyLightComponent(LightComponentBase)
```

Sky Light Component

**C++ Source:**

- **Module**: Engine
- **File**: SkyLightComponent.h

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
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``capture_emissive_only`` (bool):  [Read-Write] Only capture emissive materials. Skips all lighting making the capture cheaper. Recomended when using CaptureEveryFrame
- ``cast_deep_shadow`` (bool):  [Read-Write] Whether the light should cast high quality hair-strands self-shadowing. When this option is enabled, an extra GPU cost for this light.
- ``cast_dynamic_shadows`` (bool):  [Read-Write] Whether the light should cast shadows from dynamic objects.  Also requires Cast Shadows to be set to True.
- ``cast_raytraced_shadow`` (CastRayTracedShadow):  [Read-Write]
- ``cast_shadows`` (bool):  [Read-Write] Whether the light should cast any shadows.
- ``cast_static_shadows`` (bool):  [Read-Write] Whether the light should cast shadows from static objects.  Also requires Cast Shadows to be set to True.
- ``cast_volumetric_shadow`` (bool):  [Read-Write] Whether the light shadows volumetric fog.  Disabling this can save GPU time.
- ``cloud_ambient_occlusion`` (bool):  [Read-Write] Whether the cloud should occlude sky contribution within the atmosphere (progressively fading multiple scattering out) or not.
- ``cloud_ambient_occlusion_aperture_scale`` (float):  [Read-Write] Controls the cone aperture angle over which the sky occlusion due to volumetric clouds is evaluated. A value of 1 means `take into account the entire hemisphere` resulting in blurry occlusion, while a value of 0 means `take into account a single up occlusion direction up` resulting in sharp occlusion.
- ``cloud_ambient_occlusion_extent`` (float):  [Read-Write] The world space radius of the cloud ambient occlusion map around the camera in kilometers.
- ``cloud_ambient_occlusion_map_resolution_scale`` (float):  [Read-Write] Scale the cloud ambient occlusion map resolution, base resolution is 512. The resolution is still clamped to 'r.VolumetricCloud.SkyAO.MaxResolution'.
- ``cloud_ambient_occlusion_strength`` (float):  [Read-Write] The strength of the ambient occlusion, higher value will block more light.
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``contrast`` (float):  [Read-Write] Contrast S-curve applied to the computed AO.  A value of 0 means no contrast increase, 1 is a significant contrast increase.
- ``cubemap`` (TextureCube):  [Read-Write] Cubemap to use for sky lighting if SourceType is set to SLS_SpecifiedCubemap.
- ``cubemap_resolution`` (int32):  [Read-Write] Maximum resolution for the very top processed cubemap mip. Must be a power of 2.
- ``deep_shadow_layer_distribution`` (float):  [Read-Write] Change the deep shadow layers distribution 0:linear distribution (uniform layer distribution), 1:exponential (more details on near small details).
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``indirect_lighting_intensity`` (float):  [Read-Write] Scales the indirect lighting contribution from this light.
  A value of 0 disables any GI from this light. Default is 1.
- ``intensity`` (float):  [Read-Write] Total energy that the light emits.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``light_color`` (Color):  [Read-Write] Filter color of the light.
  Note that this can change the light's effective intensity.
- ``lower_hemisphere_color`` (LinearColor):  [Read-Write]
- ``lower_hemisphere_is_black`` (bool):  [Read-Write] Whether all distant lighting from the lower hemisphere should be set to LowerHemisphereColor.
  Enabling this is accurate when lighting a scene on a planet where the ground blocks the sky,
  However disabling it can be useful to approximate skylight bounce lighting (eg Movable light).
- ``min_occlusion`` (float):  [Read-Write] Controls the darkest that a fully occluded area can get.  This tends to destroy contact shadows, use Contrast or OcclusionExponent instead.
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``occlusion_combine_mode`` (OcclusionCombineMode):  [Read-Write] Controls how occlusion from Distance Field Ambient Occlusion is combined with Screen Space Ambient Occlusion.
- ``occlusion_exponent`` (float):  [Read-Write] Exponent applied to the computed AO.  Values lower than 1 brighten occlusion overall without losing contact shadows.
- ``occlusion_max_distance`` (float):  [Read-Write] Max distance that the occlusion of one point will affect another.
  Higher values increase the cost of Distance Field AO exponentially.
- ``occlusion_tint`` (Color):  [Read-Write] Tint color on occluded areas, artistic control.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``real_time_capture`` (bool):  [Read-Write] When enabled, the sky will be captured and convolved to achieve dynamic diffuse and specular environment lighting.
  SkyAtmosphere, VolumetricCloud Components as well as sky domes with Sky materials are taken into account.
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``samples_per_pixel`` (int32):  [Read-Write] Samples per pixel for ray tracing
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``sky_distance_threshold`` (float):  [Read-Write] Distance from the sky light at which any geometry should be treated as part of the sky.
  This is also used by reflection captures, so update reflection captures to see the impact.
- ``source_cubemap_angle`` (float):  [Read-Write] Angle to rotate the source cubemap when SourceType is set to SLS_SpecifiedCubemap.
- ``source_type`` (SkyLightSourceType):  [Read-Write] Indicates where to get the light contribution from.
- ``transmission`` (bool):  [Read-Write] Whether light from this light transmits through surfaces with subsurface scattering profiles. Requires light to be movable.
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.
- ``volumetric_scattering_intensity`` (float):  [Read-Write] Intensity of the volumetric scattering from this light.  This scales Intensity and LightColor.

<a id="unreal.SkyLightComponent.real_time_capture"></a>

#### real_time_capture

```python
@property
def real_time_capture() -> bool
```

(bool):  [Read-Only] When enabled, the sky will be captured and convolved to achieve dynamic diffuse and specular environment lighting.
SkyAtmosphere, VolumetricCloud Components as well as sky domes with Sky materials are taken into account.

<a id="unreal.SkyLightComponent.source_type"></a>

#### source_type

```python
@property
def source_type() -> SkyLightSourceType
```

(SkyLightSourceType):  [Read-Only] Indicates where to get the light contribution from.

<a id="unreal.SkyLightComponent.cubemap"></a>

#### cubemap

```python
@property
def cubemap() -> TextureCube
```

(TextureCube):  [Read-Only] Cubemap to use for sky lighting if SourceType is set to SLS_SpecifiedCubemap.

<a id="unreal.SkyLightComponent.source_cubemap_angle"></a>

#### source_cubemap_angle

```python
@property
def source_cubemap_angle() -> float
```

(float):  [Read-Only] Angle to rotate the source cubemap when SourceType is set to SLS_SpecifiedCubemap.

<a id="unreal.SkyLightComponent.cubemap_resolution"></a>

#### cubemap_resolution

```python
@property
def cubemap_resolution() -> int
```

(int32):  [Read-Only] Maximum resolution for the very top processed cubemap mip. Must be a power of 2.

<a id="unreal.SkyLightComponent.sky_distance_threshold"></a>

#### sky_distance_threshold

```python
@property
def sky_distance_threshold() -> float
```

(float):  [Read-Only] Distance from the sky light at which any geometry should be treated as part of the sky.
This is also used by reflection captures, so update reflection captures to see the impact.

<a id="unreal.SkyLightComponent.capture_emissive_only"></a>

#### capture_emissive_only

```python
@property
def capture_emissive_only() -> bool
```

(bool):  [Read-Only] Only capture emissive materials. Skips all lighting making the capture cheaper. Recomended when using CaptureEveryFrame

<a id="unreal.SkyLightComponent.lower_hemisphere_is_black"></a>

#### lower_hemisphere_is_black

```python
@property
def lower_hemisphere_is_black() -> bool
```

(bool):  [Read-Only] Whether all distant lighting from the lower hemisphere should be set to LowerHemisphereColor.
Enabling this is accurate when lighting a scene on a planet where the ground blocks the sky,
However disabling it can be useful to approximate skylight bounce lighting (eg Movable light).

<a id="unreal.SkyLightComponent.lower_hemisphere_color"></a>

#### lower_hemisphere_color

```python
@property
def lower_hemisphere_color() -> LinearColor
```

(LinearColor):  [Read-Only]

<a id="unreal.SkyLightComponent.occlusion_max_distance"></a>

#### occlusion_max_distance

```python
@property
def occlusion_max_distance() -> float
```

(float):  [Read-Only] Max distance that the occlusion of one point will affect another.
Higher values increase the cost of Distance Field AO exponentially.

<a id="unreal.SkyLightComponent.contrast"></a>

#### contrast

```python
@property
def contrast() -> float
```

(float):  [Read-Only] Contrast S-curve applied to the computed AO.  A value of 0 means no contrast increase, 1 is a significant contrast increase.

<a id="unreal.SkyLightComponent.occlusion_exponent"></a>

#### occlusion_exponent

```python
@property
def occlusion_exponent() -> float
```

(float):  [Read-Only] Exponent applied to the computed AO.  Values lower than 1 brighten occlusion overall without losing contact shadows.

<a id="unreal.SkyLightComponent.min_occlusion"></a>

#### min_occlusion

```python
@property
def min_occlusion() -> float
```

(float):  [Read-Only] Controls the darkest that a fully occluded area can get.  This tends to destroy contact shadows, use Contrast or OcclusionExponent instead.

<a id="unreal.SkyLightComponent.occlusion_tint"></a>

#### occlusion_tint

```python
@property
def occlusion_tint() -> Color
```

(Color):  [Read-Only] Tint color on occluded areas, artistic control.

<a id="unreal.SkyLightComponent.cloud_ambient_occlusion"></a>

#### cloud_ambient_occlusion

```python
@property
def cloud_ambient_occlusion() -> bool
```

(bool):  [Read-Only] Whether the cloud should occlude sky contribution within the atmosphere (progressively fading multiple scattering out) or not.

<a id="unreal.SkyLightComponent.cloud_ambient_occlusion_strength"></a>

#### cloud_ambient_occlusion_strength

```python
@property
def cloud_ambient_occlusion_strength() -> float
```

(float):  [Read-Only] The strength of the ambient occlusion, higher value will block more light.

<a id="unreal.SkyLightComponent.cloud_ambient_occlusion_extent"></a>

#### cloud_ambient_occlusion_extent

```python
@property
def cloud_ambient_occlusion_extent() -> float
```

(float):  [Read-Only] The world space radius of the cloud ambient occlusion map around the camera in kilometers.

<a id="unreal.SkyLightComponent.cloud_ambient_occlusion_map_resolution_scale"></a>

#### cloud_ambient_occlusion_map_resolution_scale

```python
@property
def cloud_ambient_occlusion_map_resolution_scale() -> float
```

(float):  [Read-Only] Scale the cloud ambient occlusion map resolution, base resolution is 512. The resolution is still clamped to 'r.VolumetricCloud.SkyAO.MaxResolution'.

<a id="unreal.SkyLightComponent.cloud_ambient_occlusion_aperture_scale"></a>

#### cloud_ambient_occlusion_aperture_scale

```python
@property
def cloud_ambient_occlusion_aperture_scale() -> float
```

(float):  [Read-Only] Controls the cone aperture angle over which the sky occlusion due to volumetric clouds is evaluated. A value of 1 means `take into account the entire hemisphere` resulting in blurry occlusion, while a value of 0 means `take into account a single up occlusion direction up` resulting in sharp occlusion.

<a id="unreal.SkyLightComponent.occlusion_combine_mode"></a>

#### occlusion_combine_mode

```python
@property
def occlusion_combine_mode() -> OcclusionCombineMode
```

(OcclusionCombineMode):  [Read-Only] Controls how occlusion from Distance Field Ambient Occlusion is combined with Screen Space Ambient Occlusion.

<a id="unreal.SkyLightComponent.set_volumetric_scattering_intensity"></a>

#### set_volumetric_scattering_intensity

```python
def set_volumetric_scattering_intensity(new_intensity: float) -> None
```

x.set_volumetric_scattering_intensity(new_intensity) -> None
Set Volumetric Scattering Intensity

Args:
    new_intensity (float):

<a id="unreal.SkyLightComponent.set_source_cubemap_angle"></a>

#### set_source_cubemap_angle

```python
def set_source_cubemap_angle(new_value: float) -> None
```

x.set_source_cubemap_angle(new_value) -> None
Sets the angle of the cubemap used when SourceType is set to SpecifiedCubemap and it is non static. It will cause the skylight to update on the next tick.

Args:
    new_value (float):

<a id="unreal.SkyLightComponent.set_real_time_capture"></a>

#### set_real_time_capture

```python
def set_real_time_capture(real_time_capture: bool) -> None
```

x.set_real_time_capture(real_time_capture) -> None
Set Real Time Capture

Args:
    real_time_capture (bool):

<a id="unreal.SkyLightComponent.set_occlusion_tint"></a>

#### set_occlusion_tint

```python
def set_occlusion_tint(tint: Color) -> None
```

x.set_occlusion_tint(tint) -> None
Set Occlusion Tint

Args:
    tint (Color):

<a id="unreal.SkyLightComponent.set_occlusion_exponent"></a>

#### set_occlusion_exponent

```python
def set_occlusion_exponent(occlusion_exponent: float) -> None
```

x.set_occlusion_exponent(occlusion_exponent) -> None
Set Occlusion Exponent

Args:
    occlusion_exponent (float):

<a id="unreal.SkyLightComponent.set_occlusion_contrast"></a>

#### set_occlusion_contrast

```python
def set_occlusion_contrast(occlusion_contrast: float) -> None
```

x.set_occlusion_contrast(occlusion_contrast) -> None
Set Occlusion Contrast

Args:
    occlusion_contrast (float):

<a id="unreal.SkyLightComponent.set_min_occlusion"></a>

#### set_min_occlusion

```python
def set_min_occlusion(min_occlusion: float) -> None
```

x.set_min_occlusion(min_occlusion) -> None
Set Min Occlusion

Args:
    min_occlusion (float):

<a id="unreal.SkyLightComponent.set_lower_hemisphere_color"></a>

#### set_lower_hemisphere_color

```python
def set_lower_hemisphere_color(lower_hemisphere_color: LinearColor) -> None
```

x.set_lower_hemisphere_color(lower_hemisphere_color) -> None
Set Lower Hemisphere Color

Args:
    lower_hemisphere_color (LinearColor):

<a id="unreal.SkyLightComponent.set_light_color"></a>

#### set_light_color

```python
def set_light_color(new_light_color: LinearColor) -> None
```

x.set_light_color(new_light_color) -> None
Set color of the light

Args:
    new_light_color (LinearColor):

<a id="unreal.SkyLightComponent.set_intensity"></a>

#### set_intensity

```python
def set_intensity(new_intensity: float) -> None
```

x.set_intensity(new_intensity) -> None
Set Intensity

Args:
    new_intensity (float):

<a id="unreal.SkyLightComponent.set_brightness"></a>

#### set_brightness

```python
def set_brightness(new_intensity: float) -> None
```

deprecated: 'set_brightness' was renamed to 'set_intensity'.

<a id="unreal.SkyLightComponent.set_indirect_lighting_intensity"></a>

#### set_indirect_lighting_intensity

```python
def set_indirect_lighting_intensity(new_intensity: float) -> None
```

x.set_indirect_lighting_intensity(new_intensity) -> None
Set Indirect Lighting Intensity

Args:
    new_intensity (float):

<a id="unreal.SkyLightComponent.set_cubemap_blend"></a>

#### set_cubemap_blend

```python
def set_cubemap_blend(source_cubemap: TextureCube,
                      destination_cubemap: TextureCube,
                      blend_fraction: float) -> None
```

x.set_cubemap_blend(source_cubemap, destination_cubemap, blend_fraction) -> None
Creates sky lighting from a blend between two cubemaps, which is only valid when SourceType is set to SpecifiedCubemap.
This can be used to seamlessly transition sky lighting between different times of day.
The caller should continue to update the blend until BlendFraction is 0 or 1 to reduce rendering cost.
The caller is responsible for avoiding pops due to changing the source or destination.

Args:
    source_cubemap (TextureCube): 
    destination_cubemap (TextureCube): 
    blend_fraction (float):

<a id="unreal.SkyLightComponent.set_cubemap"></a>

#### set_cubemap

```python
def set_cubemap(new_cubemap: TextureCube) -> None
```

x.set_cubemap(new_cubemap) -> None
Sets the cubemap used when SourceType is set to SpecifiedCubemap, and causes a skylight update on the next tick.

Args:
    new_cubemap (TextureCube):

<a id="unreal.SkyLightComponent.recapture_sky"></a>

#### recapture_sky

```python
def recapture_sky() -> None
```

x.recapture_sky() -> None
Recaptures the scene for the skylight.
This is useful for making sure the sky light is up to date after changing something in the world that it would capture.
Warning: this is very costly and will definitely cause a hitch.

<a id="unreal.SoundAttenuation"></a>