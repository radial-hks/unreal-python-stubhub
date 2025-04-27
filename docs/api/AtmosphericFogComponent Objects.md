## AtmosphericFogComponent Objects

```python
class AtmosphericFogComponent(SkyAtmosphereComponent)
```

Used to create fogging effects such as clouds.

**C++ Source:**

- **Module**: Engine
- **File**: AtmosphericFogComponent.h

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

<a id="unreal.AtmosphericFogComponent.set_sun_multiplier"></a>

#### set_sun_multiplier

```python
def set_sun_multiplier(new_sun_multiplier: float) -> None
```

x.set_sun_multiplier(new_sun_multiplier) -> None
Deprecated

Args:
    new_sun_multiplier (float):

<a id="unreal.AtmosphericFogComponent.set_start_distance"></a>

#### set_start_distance

```python
def set_start_distance(new_start_distance: float) -> None
```

x.set_start_distance(new_start_distance) -> None
Deprecated

Args:
    new_start_distance (float):

<a id="unreal.AtmosphericFogComponent.set_precompute_params"></a>

#### set_precompute_params

```python
def set_precompute_params(density_height: float, max_scattering_order: int,
                          inscatter_altitude_sample_num: int) -> None
```

x.set_precompute_params(density_height, max_scattering_order, inscatter_altitude_sample_num) -> None
Deprecated

Args:
    density_height (float): 
    max_scattering_order (int32): 
    inscatter_altitude_sample_num (int32):

<a id="unreal.AtmosphericFogComponent.set_fog_multiplier"></a>

#### set_fog_multiplier

```python
def set_fog_multiplier(new_fog_multiplier: float) -> None
```

x.set_fog_multiplier(new_fog_multiplier) -> None
Deprecated

Args:
    new_fog_multiplier (float):

<a id="unreal.AtmosphericFogComponent.set_distance_scale"></a>

#### set_distance_scale

```python
def set_distance_scale(new_distance_scale: float) -> None
```

x.set_distance_scale(new_distance_scale) -> None
Deprecated

Args:
    new_distance_scale (float):

<a id="unreal.AtmosphericFogComponent.set_distance_offset"></a>

#### set_distance_offset

```python
def set_distance_offset(new_distance_offset: float) -> None
```

x.set_distance_offset(new_distance_offset) -> None
Deprecated

Args:
    new_distance_offset (float):

<a id="unreal.AtmosphericFogComponent.set_density_offset"></a>

#### set_density_offset

```python
def set_density_offset(new_density_offset: float) -> None
```

x.set_density_offset(new_density_offset) -> None
Deprecated

Args:
    new_density_offset (float):

<a id="unreal.AtmosphericFogComponent.set_density_multiplier"></a>

#### set_density_multiplier

```python
def set_density_multiplier(new_density_multiplier: float) -> None
```

x.set_density_multiplier(new_density_multiplier) -> None
Deprecated

Args:
    new_density_multiplier (float):

<a id="unreal.AtmosphericFogComponent.set_default_light_color"></a>

#### set_default_light_color

```python
def set_default_light_color(new_light_color: LinearColor) -> None
```

x.set_default_light_color(new_light_color) -> None
Deprecated

Args:
    new_light_color (LinearColor):

<a id="unreal.AtmosphericFogComponent.set_default_brightness"></a>

#### set_default_brightness

```python
def set_default_brightness(new_brightness: float) -> None
```

x.set_default_brightness(new_brightness) -> None
Deprecated

Args:
    new_brightness (float):

<a id="unreal.AtmosphericFogComponent.set_altitude_scale"></a>

#### set_altitude_scale

```python
def set_altitude_scale(new_altitude_scale: float) -> None
```

x.set_altitude_scale(new_altitude_scale) -> None
Deprecated

Args:
    new_altitude_scale (float):

<a id="unreal.AtmosphericFogComponent.disable_sun_disk"></a>

#### disable_sun_disk

```python
def disable_sun_disk(new_sun_disk: bool) -> None
```

x.disable_sun_disk(new_sun_disk) -> None
Deprecated

Args:
    new_sun_disk (bool):

<a id="unreal.AtmosphericFogComponent.disable_ground_scattering"></a>

#### disable_ground_scattering

```python
def disable_ground_scattering(new_ground_scattering: bool) -> None
```

x.disable_ground_scattering(new_ground_scattering) -> None
Deprecated

Args:
    new_ground_scattering (bool):

<a id="unreal.AudioBus"></a>