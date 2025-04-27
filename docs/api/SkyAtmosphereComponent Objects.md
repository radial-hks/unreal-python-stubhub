## SkyAtmosphereComponent Objects

```python
class SkyAtmosphereComponent(SceneComponent)
```

A component that represents a planet atmosphere material and simulates sky and light scattering within it.
see: https://docs.unrealengine.com/en-US/Engine/Actors/FogEffects/SkyAtmosphere/index.html

**C++ Source:**

- **Module**: Engine
- **File**: SkyAtmosphereComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``aerial_perspective_start_depth`` (float):  [Read-Write] The distance (kilometers) at which we start evaluating the aerial perspective. Having the aerial perspective starts away from the camera can help with performance: pixels not affected by the aerial perspective will have their computation skipped using early depth test.
- ``aerial_pespective_view_distance_scale`` (float):  [Read-Write] Makes the aerial perspective look thicker by scaling distances from view to surfaces (opaque and translucent).
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``atmosphere_height`` (float):  [Read-Write] The height of the atmosphere layer above the ground in kilometers.
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``bottom_radius`` (float):  [Read-Write] The radius in kilometers from the center of the planet to the ground level.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``ground_albedo`` (Color):  [Read-Write] The ground albedo that will tint the atmosphere when the sun light will bounce on it. Only taken into account when MultiScattering>0.0.
- ``height_fog_contribution`` (float):  [Read-Write] Scale the sky and atmosphere lights contribution to the height fog when SupportSkyAtmosphereAffectsHeightFog project setting is true.
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``holdout`` (bool):  [Read-Write] If this is True, this primitive will render black with an alpha of 0, but all secondary effects (shadows, reflections, indirect lighting) remain. This feature requires activating the project setting(s) "Alpha Output", and "Support Primitive Alpha Holdout" if using the deferred renderer.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``mie_absorption`` (LinearColor):  [Read-Write] The Mie absorption coefficients resulting from particles in the air at an altitude of 0 kilometer. As it becomes higher, light will be absorbed more.
- ``mie_absorption_scale`` (float):  [Read-Write] Mie absorption coefficient scale.
- ``mie_anisotropy`` (float):  [Read-Write] A value of 0 mean light is uniformly scattered. A value closer to 1 means lights will scatter more forward, resulting in halos around light sources.
- ``mie_exponential_distribution`` (float):  [Read-Write] The altitude in kilometer at which Mie effects are reduced to 40%.
- ``mie_scattering`` (LinearColor):  [Read-Write] The Mie scattering coefficients resulting from particles in the air at an altitude of 0 kilometer. As it becomes higher, light will be scattered more.
- ``mie_scattering_scale`` (float):  [Read-Write] Mie scattering coefficient scale.
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``multi_scattering_factor`` (float):  [Read-Write] Factor applied to multiple scattering only (after the sun light has bounced around in the atmosphere at least once).
  Multiple scattering is evaluated using a dual scattering approach.
  A value of 2 is recommended to better represent default atmosphere when r.SkyAtmosphere.MultiScatteringLUT.HighQuality=0.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``other_absorption`` (LinearColor):  [Read-Write] Absorption coefficients for another atmosphere layer. Density increase from 0 to 1 between 10 to 25km and decreases from 1 to 0 between 25 to 40km. The default values represents ozone molecules absorption in the Earth atmosphere.
- ``other_absorption_scale`` (float):  [Read-Write] Absorption coefficients for another atmosphere layer. Density increase from 0 to 1 between 10 to 25km and decreases from 1 to 0 between 25 to 40km. This approximates ozone molecules distribution in the Earth atmosphere.
- ``other_tent_distribution`` (TentDistribution):  [Read-Write] Represents the altitude based tent distribution of absorption particles in the atmosphere.
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``rayleigh_exponential_distribution`` (float):  [Read-Write] The altitude in kilometer at which Rayleigh scattering effect is reduced to 40%.
- ``rayleigh_scattering`` (LinearColor):  [Read-Write] The Rayleigh scattering coefficients resulting from molecules in the air at an altitude of 0 kilometer.
- ``rayleigh_scattering_scale`` (float):  [Read-Write] Rayleigh scattering coefficient scale.
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``render_in_main_pass`` (bool):  [Read-Write] If true, this component will be rendered in the main pass (basepass, transparency)
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``sky_luminance_factor`` (LinearColor):  [Read-Write] Scales the luminance of pixels representing the sky. This will impact the captured sky light.
- ``trace_sample_count_scale`` (float):  [Read-Write] Scale the atmosphere tracing sample count. Quality level scalability
  The sample count is still clamped according to scalability setting to 'r.SkyAtmosphere.SampleCountMax' when 'r.SkyAtmosphere.FastSkyLUT' is 0.
  The sample count is still clamped according to scalability setting to 'r.SkyAtmosphere.FastSkyLUT.SampleCountMax' when 'r.SkyAtmosphere.FastSkyLUT' is 1.
  The sample count is still clamped for aerial perspective according to  'r.SkyAtmosphere.AerialPerspectiveLUT.SampleCountMaxPerSlice'.
- ``transform_mode`` (SkyAtmosphereTransformMode):  [Read-Write] The ground albedo that will tint the atmosphere when the sun light will bounce on it. Only taken into account when MultiScattering>0.0.
- ``transmittance_min_light_elevation_angle`` (float):  [Read-Write] The minimum elevation angle in degree that should be used to evaluate the sun transmittance to the ground. Useful to maintain a visible sun light and shadow on meshes even when the sun has started going below the horizon. This does not affect the aerial perspective.
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.SkyAtmosphereComponent.transform_mode"></a>

#### transform_mode

```python
@property
def transform_mode() -> SkyAtmosphereTransformMode
```

(SkyAtmosphereTransformMode):  [Read-Only] The ground albedo that will tint the atmosphere when the sun light will bounce on it. Only taken into account when MultiScattering>0.0.

<a id="unreal.SkyAtmosphereComponent.bottom_radius"></a>

#### bottom_radius

```python
@property
def bottom_radius() -> float
```

(float):  [Read-Only] The radius in kilometers from the center of the planet to the ground level.

<a id="unreal.SkyAtmosphereComponent.ground_albedo"></a>

#### ground_albedo

```python
@property
def ground_albedo() -> Color
```

(Color):  [Read-Only] The ground albedo that will tint the atmosphere when the sun light will bounce on it. Only taken into account when MultiScattering>0.0.

<a id="unreal.SkyAtmosphereComponent.atmosphere_height"></a>

#### atmosphere_height

```python
@property
def atmosphere_height() -> float
```

(float):  [Read-Only] The height of the atmosphere layer above the ground in kilometers.

<a id="unreal.SkyAtmosphereComponent.multi_scattering_factor"></a>

#### multi_scattering_factor

```python
@property
def multi_scattering_factor() -> float
```

(float):  [Read-Only] Factor applied to multiple scattering only (after the sun light has bounced around in the atmosphere at least once).
Multiple scattering is evaluated using a dual scattering approach.
A value of 2 is recommended to better represent default atmosphere when r.SkyAtmosphere.MultiScatteringLUT.HighQuality=0.

<a id="unreal.SkyAtmosphereComponent.trace_sample_count_scale"></a>

#### trace_sample_count_scale

```python
@property
def trace_sample_count_scale() -> float
```

(float):  [Read-Only] Scale the atmosphere tracing sample count. Quality level scalability
The sample count is still clamped according to scalability setting to 'r.SkyAtmosphere.SampleCountMax' when 'r.SkyAtmosphere.FastSkyLUT' is 0.
The sample count is still clamped according to scalability setting to 'r.SkyAtmosphere.FastSkyLUT.SampleCountMax' when 'r.SkyAtmosphere.FastSkyLUT' is 1.
The sample count is still clamped for aerial perspective according to  'r.SkyAtmosphere.AerialPerspectiveLUT.SampleCountMaxPerSlice'.

<a id="unreal.SkyAtmosphereComponent.rayleigh_scattering_scale"></a>

#### rayleigh_scattering_scale

```python
@property
def rayleigh_scattering_scale() -> float
```

(float):  [Read-Only] Rayleigh scattering coefficient scale.

<a id="unreal.SkyAtmosphereComponent.rayleigh_scattering"></a>

#### rayleigh_scattering

```python
@property
def rayleigh_scattering() -> LinearColor
```

(LinearColor):  [Read-Only] The Rayleigh scattering coefficients resulting from molecules in the air at an altitude of 0 kilometer.

<a id="unreal.SkyAtmosphereComponent.rayleigh_exponential_distribution"></a>

#### rayleigh_exponential_distribution

```python
@property
def rayleigh_exponential_distribution() -> float
```

(float):  [Read-Only] The altitude in kilometer at which Rayleigh scattering effect is reduced to 40%.

<a id="unreal.SkyAtmosphereComponent.mie_scattering_scale"></a>

#### mie_scattering_scale

```python
@property
def mie_scattering_scale() -> float
```

(float):  [Read-Only] Mie scattering coefficient scale.

<a id="unreal.SkyAtmosphereComponent.mie_scattering"></a>

#### mie_scattering

```python
@property
def mie_scattering() -> LinearColor
```

(LinearColor):  [Read-Only] The Mie scattering coefficients resulting from particles in the air at an altitude of 0 kilometer. As it becomes higher, light will be scattered more.

<a id="unreal.SkyAtmosphereComponent.mie_absorption_scale"></a>

#### mie_absorption_scale

```python
@property
def mie_absorption_scale() -> float
```

(float):  [Read-Only] Mie absorption coefficient scale.

<a id="unreal.SkyAtmosphereComponent.mie_absorption"></a>

#### mie_absorption

```python
@property
def mie_absorption() -> LinearColor
```

(LinearColor):  [Read-Only] The Mie absorption coefficients resulting from particles in the air at an altitude of 0 kilometer. As it becomes higher, light will be absorbed more.

<a id="unreal.SkyAtmosphereComponent.mie_anisotropy"></a>

#### mie_anisotropy

```python
@property
def mie_anisotropy() -> float
```

(float):  [Read-Only] A value of 0 mean light is uniformly scattered. A value closer to 1 means lights will scatter more forward, resulting in halos around light sources.

<a id="unreal.SkyAtmosphereComponent.mie_exponential_distribution"></a>

#### mie_exponential_distribution

```python
@property
def mie_exponential_distribution() -> float
```

(float):  [Read-Only] The altitude in kilometer at which Mie effects are reduced to 40%.

<a id="unreal.SkyAtmosphereComponent.other_absorption_scale"></a>

#### other_absorption_scale

```python
@property
def other_absorption_scale() -> float
```

(float):  [Read-Only] Absorption coefficients for another atmosphere layer. Density increase from 0 to 1 between 10 to 25km and decreases from 1 to 0 between 25 to 40km. This approximates ozone molecules distribution in the Earth atmosphere.

<a id="unreal.SkyAtmosphereComponent.other_absorption"></a>

#### other_absorption

```python
@property
def other_absorption() -> LinearColor
```

(LinearColor):  [Read-Only] Absorption coefficients for another atmosphere layer. Density increase from 0 to 1 between 10 to 25km and decreases from 1 to 0 between 25 to 40km. The default values represents ozone molecules absorption in the Earth atmosphere.

<a id="unreal.SkyAtmosphereComponent.other_tent_distribution"></a>

#### other_tent_distribution

```python
@property
def other_tent_distribution() -> TentDistribution
```

(TentDistribution):  [Read-Only] Represents the altitude based tent distribution of absorption particles in the atmosphere.

<a id="unreal.SkyAtmosphereComponent.sky_luminance_factor"></a>

#### sky_luminance_factor

```python
@property
def sky_luminance_factor() -> LinearColor
```

(LinearColor):  [Read-Only] Scales the luminance of pixels representing the sky. This will impact the captured sky light.

<a id="unreal.SkyAtmosphereComponent.aerial_pespective_view_distance_scale"></a>

#### aerial_pespective_view_distance_scale

```python
@property
def aerial_pespective_view_distance_scale() -> float
```

(float):  [Read-Only] Makes the aerial perspective look thicker by scaling distances from view to surfaces (opaque and translucent).

<a id="unreal.SkyAtmosphereComponent.height_fog_contribution"></a>

#### height_fog_contribution

```python
@property
def height_fog_contribution() -> float
```

(float):  [Read-Only] Scale the sky and atmosphere lights contribution to the height fog when SupportSkyAtmosphereAffectsHeightFog project setting is true.

<a id="unreal.SkyAtmosphereComponent.transmittance_min_light_elevation_angle"></a>

#### transmittance_min_light_elevation_angle

```python
@property
def transmittance_min_light_elevation_angle() -> float
```

(float):  [Read-Only] The minimum elevation angle in degree that should be used to evaluate the sun transmittance to the ground. Useful to maintain a visible sun light and shadow on meshes even when the sun has started going below the horizon. This does not affect the aerial perspective.

<a id="unreal.SkyAtmosphereComponent.aerial_perspective_start_depth"></a>

#### aerial_perspective_start_depth

```python
@property
def aerial_perspective_start_depth() -> float
```

(float):  [Read-Only] The distance (kilometers) at which we start evaluating the aerial perspective. Having the aerial perspective starts away from the camera can help with performance: pixels not affected by the aerial perspective will have their computation skipped using early depth test.

<a id="unreal.SkyAtmosphereComponent.holdout"></a>

#### holdout

```python
@property
def holdout() -> bool
```

(bool):  [Read-Only] If this is True, this primitive will render black with an alpha of 0, but all secondary effects (shadows, reflections, indirect lighting) remain. This feature requires activating the project setting(s) "Alpha Output", and "Support Primitive Alpha Holdout" if using the deferred renderer.

<a id="unreal.SkyAtmosphereComponent.render_in_main_pass"></a>

#### render_in_main_pass

```python
@property
def render_in_main_pass() -> bool
```

(bool):  [Read-Only] If true, this component will be rendered in the main pass (basepass, transparency)

<a id="unreal.SkyAtmosphereComponent.set_sky_luminance_factor"></a>

#### set_sky_luminance_factor

```python
def set_sky_luminance_factor(new_value: LinearColor) -> None
```

x.set_sky_luminance_factor(new_value) -> None
Set Sky Luminance Factor

Args:
    new_value (LinearColor):

<a id="unreal.SkyAtmosphereComponent.set_render_in_main_pass"></a>

#### set_render_in_main_pass

```python
def set_render_in_main_pass(value: bool) -> None
```

x.set_render_in_main_pass(value) -> None
Set Render in Main Pass

Args:
    value (bool):

<a id="unreal.SkyAtmosphereComponent.set_rayleigh_scattering_scale"></a>

#### set_rayleigh_scattering_scale

```python
def set_rayleigh_scattering_scale(new_value: float) -> None
```

x.set_rayleigh_scattering_scale(new_value) -> None
Set Rayleigh Scattering Scale

Args:
    new_value (float):

<a id="unreal.SkyAtmosphereComponent.set_rayleigh_scattering"></a>

#### set_rayleigh_scattering

```python
def set_rayleigh_scattering(new_value: LinearColor) -> None
```

x.set_rayleigh_scattering(new_value) -> None
Set Rayleigh Scattering

Args:
    new_value (LinearColor):

<a id="unreal.SkyAtmosphereComponent.set_rayleigh_exponential_distribution"></a>

#### set_rayleigh_exponential_distribution

```python
def set_rayleigh_exponential_distribution(new_value: float) -> None
```

x.set_rayleigh_exponential_distribution(new_value) -> None
Set Rayleigh Exponential Distribution

Args:
    new_value (float):

<a id="unreal.SkyAtmosphereComponent.set_other_absorption_scale"></a>

#### set_other_absorption_scale

```python
def set_other_absorption_scale(new_value: float) -> None
```

x.set_other_absorption_scale(new_value) -> None
Set Other Absorption Scale

Args:
    new_value (float):

<a id="unreal.SkyAtmosphereComponent.set_other_absorption"></a>

#### set_other_absorption

```python
def set_other_absorption(new_value: LinearColor) -> None
```

x.set_other_absorption(new_value) -> None
Set Other Absorption

Args:
    new_value (LinearColor):

<a id="unreal.SkyAtmosphereComponent.set_multi_scattering_factor"></a>

#### set_multi_scattering_factor

```python
def set_multi_scattering_factor(new_value: float) -> None
```

x.set_multi_scattering_factor(new_value) -> None
Set Multi Scattering Factor

Args:
    new_value (float):

<a id="unreal.SkyAtmosphereComponent.set_mie_scattering_scale"></a>

#### set_mie_scattering_scale

```python
def set_mie_scattering_scale(new_value: float) -> None
```

x.set_mie_scattering_scale(new_value) -> None
Set Mie Scattering Scale

Args:
    new_value (float):

<a id="unreal.SkyAtmosphereComponent.set_mie_scattering"></a>

#### set_mie_scattering

```python
def set_mie_scattering(new_value: LinearColor) -> None
```

x.set_mie_scattering(new_value) -> None
Set Mie Scattering

Args:
    new_value (LinearColor):

<a id="unreal.SkyAtmosphereComponent.set_mie_exponential_distribution"></a>

#### set_mie_exponential_distribution

```python
def set_mie_exponential_distribution(new_value: float) -> None
```

x.set_mie_exponential_distribution(new_value) -> None
Set Mie Exponential Distribution

Args:
    new_value (float):

<a id="unreal.SkyAtmosphereComponent.set_mie_anisotropy"></a>

#### set_mie_anisotropy

```python
def set_mie_anisotropy(new_value: float) -> None
```

x.set_mie_anisotropy(new_value) -> None
Set Mie Anisotropy

Args:
    new_value (float):

<a id="unreal.SkyAtmosphereComponent.set_mie_absorption_scale"></a>

#### set_mie_absorption_scale

```python
def set_mie_absorption_scale(new_value: float) -> None
```

x.set_mie_absorption_scale(new_value) -> None
Set Mie Absorption Scale

Args:
    new_value (float):

<a id="unreal.SkyAtmosphereComponent.set_mie_absorption"></a>

#### set_mie_absorption

```python
def set_mie_absorption(new_value: LinearColor) -> None
```

x.set_mie_absorption(new_value) -> None
Set Mie Absorption

Args:
    new_value (LinearColor):

<a id="unreal.SkyAtmosphereComponent.set_holdout"></a>

#### set_holdout

```python
def set_holdout(new_holdout: bool) -> None
```

x.set_holdout(new_holdout) -> None
Set Holdout

Args:
    new_holdout (bool):

<a id="unreal.SkyAtmosphereComponent.set_height_fog_contribution"></a>

#### set_height_fog_contribution

```python
def set_height_fog_contribution(new_value: float) -> None
```

x.set_height_fog_contribution(new_value) -> None
Set Height Fog Contribution

Args:
    new_value (float):

<a id="unreal.SkyAtmosphereComponent.set_ground_albedo"></a>

#### set_ground_albedo

```python
def set_ground_albedo(new_value: Color) -> None
```

x.set_ground_albedo(new_value) -> None
Set Ground Albedo

Args:
    new_value (Color):

<a id="unreal.SkyAtmosphereComponent.set_bottom_radius"></a>

#### set_bottom_radius

```python
def set_bottom_radius(new_value: float) -> None
```

x.set_bottom_radius(new_value) -> None
Set Bottom Radius

Args:
    new_value (float):

<a id="unreal.SkyAtmosphereComponent.set_atmosphere_height"></a>

#### set_atmosphere_height

```python
def set_atmosphere_height(new_value: float) -> None
```

x.set_atmosphere_height(new_value) -> None
Set Atmosphere Height

Args:
    new_value (float):

<a id="unreal.SkyAtmosphereComponent.set_aerial_pespective_view_distance_scale"></a>

#### set_aerial_pespective_view_distance_scale

```python
def set_aerial_pespective_view_distance_scale(new_value: float) -> None
```

x.set_aerial_pespective_view_distance_scale(new_value) -> None
Set Aerial Pespective View Distance Scale

Args:
    new_value (float):

<a id="unreal.SkyAtmosphereComponent.reset_atmosphere_light_direction_override"></a>

#### reset_atmosphere_light_direction_override

```python
def reset_atmosphere_light_direction_override(
        atmosphere_light_index: int) -> None
```

x.reset_atmosphere_light_direction_override(atmosphere_light_index) -> None
Reset Atmosphere Light Direction Override

Args:
    atmosphere_light_index (int32):

<a id="unreal.SkyAtmosphereComponent.override_atmosphere_light_direction"></a>

#### override_atmosphere_light_direction

```python
def override_atmosphere_light_direction(atmosphere_light_index: int,
                                        light_direction: Vector) -> None
```

x.override_atmosphere_light_direction(atmosphere_light_index, light_direction) -> None
Override Atmosphere Light Direction

Args:
    atmosphere_light_index (int32): 
    light_direction (Vector):

<a id="unreal.SkyAtmosphereComponent.is_atmosphere_light_direction_overriden"></a>

#### is_atmosphere_light_direction_overriden

```python
def is_atmosphere_light_direction_overriden(
        atmosphere_light_index: int) -> bool
```

x.is_atmosphere_light_direction_overriden(atmosphere_light_index) -> bool
Is Atmosphere Light Direction Overriden

Args:
    atmosphere_light_index (int32): 

Returns:
    bool:

<a id="unreal.SkyAtmosphereComponent.get_overriden_atmosphere_light_direction"></a>

#### get_overriden_atmosphere_light_direction

```python
def get_overriden_atmosphere_light_direction(
        atmosphere_light_index: int) -> Vector
```

x.get_overriden_atmosphere_light_direction(atmosphere_light_index) -> Vector
Get Overriden Atmosphere Light Direction

Args:
    atmosphere_light_index (int32): 

Returns:
    Vector:

<a id="unreal.SkyAtmosphereComponent.get_atmospheric_light_to_match_illuminance_on_ground"></a>

#### get_atmospheric_light_to_match_illuminance_on_ground

```python
def get_atmospheric_light_to_match_illuminance_on_ground(
        light_direction: Vector = [0.000000, 0.000000, 1.000000],
        illuminance_on_ground: float = 1.000000) -> float
```

x.get_atmospheric_light_to_match_illuminance_on_ground(light_direction=[0.000000, 0.000000, 1.000000], illuminance_on_ground=1.000000) -> float
This function can be used for instance in order to evaluate a directional atmospheric light outer space illuminance for a desired illuminance on ground given a direction.
This is given for the position at the top of the virtual planet. Plus the output outer space illuminance into the light intensity.

Args:
    light_direction (Vector): 
    illuminance_on_ground (float): 

Returns:
    float:

<a id="unreal.SkyAtmosphereComponent.get_atmosphere_transmitance_on_ground_at_planet_top"></a>

#### get_atmosphere_transmitance_on_ground_at_planet_top

```python
def get_atmosphere_transmitance_on_ground_at_planet_top(
        directional_light: DirectionalLightComponent) -> LinearColor
```

x.get_atmosphere_transmitance_on_ground_at_planet_top(directional_light) -> LinearColor
Get Atmosphere Transmitance on Ground at Planet Top

Args:
    directional_light (DirectionalLightComponent): 

Returns:
    LinearColor:

<a id="unreal.AtmosphericFogComponent"></a>