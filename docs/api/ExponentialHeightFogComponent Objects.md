## ExponentialHeightFogComponent Objects

```python
class ExponentialHeightFogComponent(SceneComponent)
```

Used to create fogging effects such as clouds but with a density that is related to the height of the fog.

**C++ Source:**

- **Module**: Engine
- **File**: ExponentialHeightFogComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``directional_inscattering_exponent`` (float):  [Read-Write] Controls the size of the directional inscattering cone, which is used to approximate inscattering from a directional light.
  Note:
    - there must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used.
    - When r.SupportExpFogMatchesVolumetricFog = 1, this value is ignored and the volumetric fog Scattering Distribution is used instead.
- ``directional_inscattering_luminance`` (LinearColor):  [Read-Write] Controls the color of the directional inscattering, which is used to approximate inscattering from a directional light.
  Note:
    - there must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used.
    - When r.SupportExpFogMatchesVolumetricFog = 1, this value is ignored.
- ``directional_inscattering_start_distance`` (float):  [Read-Write] Controls the start distance from the viewer of the directional inscattering, which is used to approximate inscattering from a directional light.
  Note:
    - There must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used.
    - When r.SupportExpFogMatchesVolumetricFog = 1, this value is ignored.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``enable_volumetric_fog`` (bool):  [Read-Write] Whether to enable Volumetric fog.  Scalability settings control the resolution of the fog simulation.
  Note that Volumetric fog currently does not support StartDistance, FogMaxOpacity and FogCutoffDistance.
  Volumetric fog also can't match exponential height fog in general as exponential height fog has non-physical behavior.
- ``end_distance`` (float):  [Read-Write] Distance from the camera, on the horizontal XY plane, that the fog will end integrating the lighting and transmittance. Disabled when 0.
- ``fog_cutoff_distance`` (float):  [Read-Write] Scene elements past this distance will not have fog applied.  This is useful for excluding skyboxes which already have fog baked in.
- ``fog_density`` (float):  [Read-Write] Global density factor.
- ``fog_height_falloff`` (float):  [Read-Write] Height density factor, controls how the density increases as height decreases.
  Smaller values make the visible transition larger.
- ``fog_inscattering_luminance`` (LinearColor):  [Read-Write] Note: when r.SupportExpFogMatchesVolumetricFog = 1, this value is ignored and the volumetric fog Emissive is used instead.
- ``fog_max_opacity`` (float):  [Read-Write] Maximum opacity of the fog.
  A value of 1 means the fog can become fully opaque at a distance and replace scene color completely,
  A value of 0 means the fog color will not be factored in at all.
- ``fully_directional_inscattering_color_distance`` (float):  [Read-Write] Distance at which InscatteringColorCubemap should be used directly for the Inscattering Color.
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``holdout`` (bool):  [Read-Write] If this is True, this primitive will render black with an alpha of 0, but all secondary effects (shadows, reflections, indirect lighting) remain. This feature requires activating the project setting(s) "Alpha Output", and "Support Primitive Alpha Holdout" if using the deferred renderer.
- ``inscattering_color_cubemap`` (TextureCube):  [Read-Write] Cubemap that can be specified for fog color, which is useful to make distant, heavily fogged scene elements match the sky.
  When the cubemap is specified, FogInscatteringColor is ignored and Directional inscattering is disabled.
- ``inscattering_color_cubemap_angle`` (float):  [Read-Write] Angle to rotate the InscatteringColorCubemap around the Z axis.
- ``inscattering_texture_tint`` (LinearColor):  [Read-Write] Tint color used when InscatteringColorCubemap is specified, for quick edits without having to reimport InscatteringColorCubemap.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``non_directional_inscattering_color_distance`` (float):  [Read-Write] Distance at which only the average color of InscatteringColorCubemap should be used as Inscattering Color.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``override_light_colors_with_fog_inscattering_colors`` (bool):  [Read-Write] Whether to use FogInscatteringColor for the Sky Light volumetric scattering color and DirectionalInscatteringColor for the Directional Light scattering color.
  Make sure your directional light has 'Atmosphere Sun Light' enabled!
  Enabling this allows Volumetric fog to better match Height fog in the distance, but produces non-physical volumetric lighting that may not match surface lighting.
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``render_in_main_pass`` (bool):  [Read-Write] If true, this component will be rendered in the main pass (basepass, transparency)
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``second_fog_data`` (ExponentialHeightFogData):  [Read-Write] Settings for the second fog. Setting the density of this to 0 means it doesn't have any influence.
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``sky_atmosphere_ambient_contribution_color_scale`` (LinearColor):  [Read-Write] Color used to modulate the SkyAtmosphere component contribution to the non directional component of the fog. Only effective when r.SupportSkyAtmosphereAffectsHeightFog>0
- ``start_distance`` (float):  [Read-Write] Distance from the camera that the fog will start, in world units.
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.
- ``volumetric_fog_albedo`` (Color):  [Read-Write] The height fog particle reflectiveness used by volumetric fog.
  Water particles in air have an albedo near white, while dust has slightly darker value.
- ``volumetric_fog_distance`` (float):  [Read-Write] Distance over which volumetric fog should be computed, after the start distance.  Larger values extend the effect into the distance but expose under-sampling artifacts in details.
- ``volumetric_fog_emissive`` (LinearColor):  [Read-Write] Light emitted by height fog.  This is a density so more light is emitted the further you are looking through the fog.
  In most cases skylight is a better choice, however right now volumetric fog does not support precomputed lighting,
  So stationary skylights are unshadowed and static skylights don't affect volumetric fog at all.
- ``volumetric_fog_extinction_scale`` (float):  [Read-Write] Scales the height fog particle extinction amount used by volumetric fog.  Values larger than 1 cause fog particles everywhere absorb more light.
- ``volumetric_fog_near_fade_in_distance`` (float):  [Read-Write] Distance over which volumetric fog will fade in from the start distance.
- ``volumetric_fog_scattering_distribution`` (float):  [Read-Write] Controls the scattering phase function - how much incoming light scatters in various directions.
  A distribution value of 0 scatters equally in all directions, while .9 scatters predominantly in the light direction.
  In order to have visible volumetric fog light shafts from the side, the distribution will need to be closer to 0.
- ``volumetric_fog_start_distance`` (float):  [Read-Write] Distance from the camera that the volumetric fog will start, in world units.
- ``volumetric_fog_static_lighting_scattering_intensity`` (float):  [Read-Write]

<a id="unreal.ExponentialHeightFogComponent.fog_density"></a>

#### fog_density

```python
@property
def fog_density() -> float
```

(float):  [Read-Only] Global density factor.

<a id="unreal.ExponentialHeightFogComponent.fog_height_falloff"></a>

#### fog_height_falloff

```python
@property
def fog_height_falloff() -> float
```

(float):  [Read-Only] Height density factor, controls how the density increases as height decreases.
Smaller values make the visible transition larger.

<a id="unreal.ExponentialHeightFogComponent.second_fog_data"></a>

#### second_fog_data

```python
@property
def second_fog_data() -> ExponentialHeightFogData
```

(ExponentialHeightFogData):  [Read-Only] Settings for the second fog. Setting the density of this to 0 means it doesn't have any influence.

<a id="unreal.ExponentialHeightFogComponent.fog_inscattering_luminance"></a>

#### fog_inscattering_luminance

```python
@property
def fog_inscattering_luminance() -> LinearColor
```

(LinearColor):  [Read-Only] Note: when r.SupportExpFogMatchesVolumetricFog = 1, this value is ignored and the volumetric fog Emissive is used instead.

<a id="unreal.ExponentialHeightFogComponent.sky_atmosphere_ambient_contribution_color_scale"></a>

#### sky_atmosphere_ambient_contribution_color_scale

```python
@property
def sky_atmosphere_ambient_contribution_color_scale() -> LinearColor
```

(LinearColor):  [Read-Only] Color used to modulate the SkyAtmosphere component contribution to the non directional component of the fog. Only effective when r.SupportSkyAtmosphereAffectsHeightFog>0

<a id="unreal.ExponentialHeightFogComponent.inscattering_color_cubemap"></a>

#### inscattering_color_cubemap

```python
@property
def inscattering_color_cubemap() -> TextureCube
```

(TextureCube):  [Read-Only] Cubemap that can be specified for fog color, which is useful to make distant, heavily fogged scene elements match the sky.
When the cubemap is specified, FogInscatteringColor is ignored and Directional inscattering is disabled.

<a id="unreal.ExponentialHeightFogComponent.inscattering_color_cubemap_angle"></a>

#### inscattering_color_cubemap_angle

```python
@property
def inscattering_color_cubemap_angle() -> float
```

(float):  [Read-Only] Angle to rotate the InscatteringColorCubemap around the Z axis.

<a id="unreal.ExponentialHeightFogComponent.inscattering_texture_tint"></a>

#### inscattering_texture_tint

```python
@property
def inscattering_texture_tint() -> LinearColor
```

(LinearColor):  [Read-Only] Tint color used when InscatteringColorCubemap is specified, for quick edits without having to reimport InscatteringColorCubemap.

<a id="unreal.ExponentialHeightFogComponent.fully_directional_inscattering_color_distance"></a>

#### fully_directional_inscattering_color_distance

```python
@property
def fully_directional_inscattering_color_distance() -> float
```

(float):  [Read-Only] Distance at which InscatteringColorCubemap should be used directly for the Inscattering Color.

<a id="unreal.ExponentialHeightFogComponent.non_directional_inscattering_color_distance"></a>

#### non_directional_inscattering_color_distance

```python
@property
def non_directional_inscattering_color_distance() -> float
```

(float):  [Read-Only] Distance at which only the average color of InscatteringColorCubemap should be used as Inscattering Color.

<a id="unreal.ExponentialHeightFogComponent.directional_inscattering_exponent"></a>

#### directional_inscattering_exponent

```python
@property
def directional_inscattering_exponent() -> float
```

(float):  [Read-Only] Controls the size of the directional inscattering cone, which is used to approximate inscattering from a directional light.
Note:
  - there must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used.
  - When r.SupportExpFogMatchesVolumetricFog = 1, this value is ignored and the volumetric fog Scattering Distribution is used instead.

<a id="unreal.ExponentialHeightFogComponent.directional_inscattering_start_distance"></a>

#### directional_inscattering_start_distance

```python
@property
def directional_inscattering_start_distance() -> float
```

(float):  [Read-Only] Controls the start distance from the viewer of the directional inscattering, which is used to approximate inscattering from a directional light.
Note:
  - There must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used.
  - When r.SupportExpFogMatchesVolumetricFog = 1, this value is ignored.

<a id="unreal.ExponentialHeightFogComponent.directional_inscattering_luminance"></a>

#### directional_inscattering_luminance

```python
@property
def directional_inscattering_luminance() -> LinearColor
```

(LinearColor):  [Read-Only] Controls the color of the directional inscattering, which is used to approximate inscattering from a directional light.
Note:
  - there must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used.
  - When r.SupportExpFogMatchesVolumetricFog = 1, this value is ignored.

<a id="unreal.ExponentialHeightFogComponent.fog_max_opacity"></a>

#### fog_max_opacity

```python
@property
def fog_max_opacity() -> float
```

(float):  [Read-Only] Maximum opacity of the fog.
A value of 1 means the fog can become fully opaque at a distance and replace scene color completely,
A value of 0 means the fog color will not be factored in at all.

<a id="unreal.ExponentialHeightFogComponent.start_distance"></a>

#### start_distance

```python
@property
def start_distance() -> float
```

(float):  [Read-Only] Distance from the camera that the fog will start, in world units.

<a id="unreal.ExponentialHeightFogComponent.end_distance"></a>

#### end_distance

```python
@property
def end_distance() -> float
```

(float):  [Read-Only] Distance from the camera, on the horizontal XY plane, that the fog will end integrating the lighting and transmittance. Disabled when 0.

<a id="unreal.ExponentialHeightFogComponent.fog_cutoff_distance"></a>

#### fog_cutoff_distance

```python
@property
def fog_cutoff_distance() -> float
```

(float):  [Read-Only] Scene elements past this distance will not have fog applied.  This is useful for excluding skyboxes which already have fog baked in.

<a id="unreal.ExponentialHeightFogComponent.enable_volumetric_fog"></a>

#### enable_volumetric_fog

```python
@property
def enable_volumetric_fog() -> bool
```

(bool):  [Read-Only] Whether to enable Volumetric fog.  Scalability settings control the resolution of the fog simulation.
Note that Volumetric fog currently does not support StartDistance, FogMaxOpacity and FogCutoffDistance.
Volumetric fog also can't match exponential height fog in general as exponential height fog has non-physical behavior.

<a id="unreal.ExponentialHeightFogComponent.volumetric_fog_scattering_distribution"></a>

#### volumetric_fog_scattering_distribution

```python
@property
def volumetric_fog_scattering_distribution() -> float
```

(float):  [Read-Only] Controls the scattering phase function - how much incoming light scatters in various directions.
A distribution value of 0 scatters equally in all directions, while .9 scatters predominantly in the light direction.
In order to have visible volumetric fog light shafts from the side, the distribution will need to be closer to 0.

<a id="unreal.ExponentialHeightFogComponent.volumetric_fog_albedo"></a>

#### volumetric_fog_albedo

```python
@property
def volumetric_fog_albedo() -> Color
```

(Color):  [Read-Only] The height fog particle reflectiveness used by volumetric fog.
Water particles in air have an albedo near white, while dust has slightly darker value.

<a id="unreal.ExponentialHeightFogComponent.volumetric_fog_emissive"></a>

#### volumetric_fog_emissive

```python
@property
def volumetric_fog_emissive() -> LinearColor
```

(LinearColor):  [Read-Only] Light emitted by height fog.  This is a density so more light is emitted the further you are looking through the fog.
In most cases skylight is a better choice, however right now volumetric fog does not support precomputed lighting,
So stationary skylights are unshadowed and static skylights don't affect volumetric fog at all.

<a id="unreal.ExponentialHeightFogComponent.volumetric_fog_extinction_scale"></a>

#### volumetric_fog_extinction_scale

```python
@property
def volumetric_fog_extinction_scale() -> float
```

(float):  [Read-Only] Scales the height fog particle extinction amount used by volumetric fog.  Values larger than 1 cause fog particles everywhere absorb more light.

<a id="unreal.ExponentialHeightFogComponent.volumetric_fog_distance"></a>

#### volumetric_fog_distance

```python
@property
def volumetric_fog_distance() -> float
```

(float):  [Read-Only] Distance over which volumetric fog should be computed, after the start distance.  Larger values extend the effect into the distance but expose under-sampling artifacts in details.

<a id="unreal.ExponentialHeightFogComponent.volumetric_fog_start_distance"></a>

#### volumetric_fog_start_distance

```python
@property
def volumetric_fog_start_distance() -> float
```

(float):  [Read-Only] Distance from the camera that the volumetric fog will start, in world units.

<a id="unreal.ExponentialHeightFogComponent.volumetric_fog_near_fade_in_distance"></a>

#### volumetric_fog_near_fade_in_distance

```python
@property
def volumetric_fog_near_fade_in_distance() -> float
```

(float):  [Read-Only] Distance over which volumetric fog will fade in from the start distance.

<a id="unreal.ExponentialHeightFogComponent.volumetric_fog_static_lighting_scattering_intensity"></a>

#### volumetric_fog_static_lighting_scattering_intensity

```python
@property
def volumetric_fog_static_lighting_scattering_intensity() -> float
```

(float):  [Read-Only]

<a id="unreal.ExponentialHeightFogComponent.override_light_colors_with_fog_inscattering_colors"></a>

#### override_light_colors_with_fog_inscattering_colors

```python
@property
def override_light_colors_with_fog_inscattering_colors() -> bool
```

(bool):  [Read-Only] Whether to use FogInscatteringColor for the Sky Light volumetric scattering color and DirectionalInscatteringColor for the Directional Light scattering color.
Make sure your directional light has 'Atmosphere Sun Light' enabled!
Enabling this allows Volumetric fog to better match Height fog in the distance, but produces non-physical volumetric lighting that may not match surface lighting.

<a id="unreal.ExponentialHeightFogComponent.holdout"></a>

#### holdout

```python
@property
def holdout() -> bool
```

(bool):  [Read-Only] If this is True, this primitive will render black with an alpha of 0, but all secondary effects (shadows, reflections, indirect lighting) remain. This feature requires activating the project setting(s) "Alpha Output", and "Support Primitive Alpha Holdout" if using the deferred renderer.

<a id="unreal.ExponentialHeightFogComponent.render_in_main_pass"></a>

#### render_in_main_pass

```python
@property
def render_in_main_pass() -> bool
```

(bool):  [Read-Only] If true, this component will be rendered in the main pass (basepass, transparency)

<a id="unreal.ExponentialHeightFogComponent.set_volumetric_fog_start_distance"></a>

#### set_volumetric_fog_start_distance

```python
def set_volumetric_fog_start_distance(new_value: float) -> None
```

x.set_volumetric_fog_start_distance(new_value) -> None
Set Volumetric Fog Start Distance

Args:
    new_value (float):

<a id="unreal.ExponentialHeightFogComponent.set_volumetric_fog_scattering_distribution"></a>

#### set_volumetric_fog_scattering_distribution

```python
def set_volumetric_fog_scattering_distribution(new_value: float) -> None
```

x.set_volumetric_fog_scattering_distribution(new_value) -> None
Set Volumetric Fog Scattering Distribution

Args:
    new_value (float):

<a id="unreal.ExponentialHeightFogComponent.set_volumetric_fog_near_fade_in_distance"></a>

#### set_volumetric_fog_near_fade_in_distance

```python
def set_volumetric_fog_near_fade_in_distance(new_value: float) -> None
```

x.set_volumetric_fog_near_fade_in_distance(new_value) -> None
Set Volumetric Fog Near Fade in Distance

Args:
    new_value (float):

<a id="unreal.ExponentialHeightFogComponent.set_volumetric_fog_extinction_scale"></a>

#### set_volumetric_fog_extinction_scale

```python
def set_volumetric_fog_extinction_scale(new_value: float) -> None
```

x.set_volumetric_fog_extinction_scale(new_value) -> None
Set Volumetric Fog Extinction Scale

Args:
    new_value (float):

<a id="unreal.ExponentialHeightFogComponent.set_volumetric_fog_emissive"></a>

#### set_volumetric_fog_emissive

```python
def set_volumetric_fog_emissive(new_value: LinearColor) -> None
```

x.set_volumetric_fog_emissive(new_value) -> None
Set Volumetric Fog Emissive

Args:
    new_value (LinearColor):

<a id="unreal.ExponentialHeightFogComponent.set_volumetric_fog_distance"></a>

#### set_volumetric_fog_distance

```python
def set_volumetric_fog_distance(new_value: float) -> None
```

x.set_volumetric_fog_distance(new_value) -> None
Set Volumetric Fog Distance

Args:
    new_value (float):

<a id="unreal.ExponentialHeightFogComponent.set_volumetric_fog_albedo"></a>

#### set_volumetric_fog_albedo

```python
def set_volumetric_fog_albedo(new_value: Color) -> None
```

x.set_volumetric_fog_albedo(new_value) -> None
Set Volumetric Fog Albedo

Args:
    new_value (Color):

<a id="unreal.ExponentialHeightFogComponent.set_volumetric_fog"></a>

#### set_volumetric_fog

```python
def set_volumetric_fog(new_value: bool) -> None
```

x.set_volumetric_fog(new_value) -> None
Set Volumetric Fog

Args:
    new_value (bool):

<a id="unreal.ExponentialHeightFogComponent.set_start_distance"></a>

#### set_start_distance

```python
def set_start_distance(value: float) -> None
```

x.set_start_distance(value) -> None
Set Start Distance

Args:
    value (float):

<a id="unreal.ExponentialHeightFogComponent.set_second_fog_height_offset"></a>

#### set_second_fog_height_offset

```python
def set_second_fog_height_offset(value: float) -> None
```

x.set_second_fog_height_offset(value) -> None
Set Second Fog Height Offset

Args:
    value (float):

<a id="unreal.ExponentialHeightFogComponent.set_second_fog_height_falloff"></a>

#### set_second_fog_height_falloff

```python
def set_second_fog_height_falloff(value: float) -> None
```

x.set_second_fog_height_falloff(value) -> None
Set Second Fog Height Falloff

Args:
    value (float):

<a id="unreal.ExponentialHeightFogComponent.set_second_fog_density"></a>

#### set_second_fog_density

```python
def set_second_fog_density(value: float) -> None
```

x.set_second_fog_density(value) -> None
Set Second Fog Density

Args:
    value (float):

<a id="unreal.ExponentialHeightFogComponent.set_second_fog_data"></a>

#### set_second_fog_data

```python
def set_second_fog_data(new_value: ExponentialHeightFogData) -> None
```

x.set_second_fog_data(new_value) -> None
Set Second Fog Data

Args:
    new_value (ExponentialHeightFogData):

<a id="unreal.ExponentialHeightFogComponent.set_render_in_main_pass"></a>

#### set_render_in_main_pass

```python
def set_render_in_main_pass(value: bool) -> None
```

x.set_render_in_main_pass(value) -> None
Set Render in Main Pass

Args:
    value (bool):

<a id="unreal.ExponentialHeightFogComponent.set_non_directional_inscattering_color_distance"></a>

#### set_non_directional_inscattering_color_distance

```python
def set_non_directional_inscattering_color_distance(value: float) -> None
```

x.set_non_directional_inscattering_color_distance(value) -> None
Set Non Directional Inscattering Color Distance

Args:
    value (float):

<a id="unreal.ExponentialHeightFogComponent.set_inscattering_texture_tint"></a>

#### set_inscattering_texture_tint

```python
def set_inscattering_texture_tint(value: LinearColor) -> None
```

x.set_inscattering_texture_tint(value) -> None
Set Inscattering Texture Tint

Args:
    value (LinearColor):

<a id="unreal.ExponentialHeightFogComponent.set_inscattering_color_cubemap_angle"></a>

#### set_inscattering_color_cubemap_angle

```python
def set_inscattering_color_cubemap_angle(value: float) -> None
```

x.set_inscattering_color_cubemap_angle(value) -> None
Set Inscattering Color Cubemap Angle

Args:
    value (float):

<a id="unreal.ExponentialHeightFogComponent.set_inscattering_color_cubemap"></a>

#### set_inscattering_color_cubemap

```python
def set_inscattering_color_cubemap(value: TextureCube) -> None
```

x.set_inscattering_color_cubemap(value) -> None
Set Inscattering Color Cubemap

Args:
    value (TextureCube):

<a id="unreal.ExponentialHeightFogComponent.set_holdout"></a>

#### set_holdout

```python
def set_holdout(new_holdout: bool) -> None
```

x.set_holdout(new_holdout) -> None
Set Holdout

Args:
    new_holdout (bool):

<a id="unreal.ExponentialHeightFogComponent.set_fully_directional_inscattering_color_distance"></a>

#### set_fully_directional_inscattering_color_distance

```python
def set_fully_directional_inscattering_color_distance(value: float) -> None
```

x.set_fully_directional_inscattering_color_distance(value) -> None
Set Fully Directional Inscattering Color Distance

Args:
    value (float):

<a id="unreal.ExponentialHeightFogComponent.set_fog_max_opacity"></a>

#### set_fog_max_opacity

```python
def set_fog_max_opacity(value: float) -> None
```

x.set_fog_max_opacity(value) -> None
Set Fog Max Opacity

Args:
    value (float):

<a id="unreal.ExponentialHeightFogComponent.set_fog_inscattering_color"></a>

#### set_fog_inscattering_color

```python
def set_fog_inscattering_color(value: LinearColor) -> None
```

x.set_fog_inscattering_color(value) -> None
Set Fog Inscattering Color

Args:
    value (LinearColor):

<a id="unreal.ExponentialHeightFogComponent.set_fog_height_falloff"></a>

#### set_fog_height_falloff

```python
def set_fog_height_falloff(value: float) -> None
```

x.set_fog_height_falloff(value) -> None
Set Fog Height Falloff

Args:
    value (float):

<a id="unreal.ExponentialHeightFogComponent.set_fog_density"></a>

#### set_fog_density

```python
def set_fog_density(value: float) -> None
```

x.set_fog_density(value) -> None
Set Fog Density

Args:
    value (float):

<a id="unreal.ExponentialHeightFogComponent.set_fog_cutoff_distance"></a>

#### set_fog_cutoff_distance

```python
def set_fog_cutoff_distance(value: float) -> None
```

x.set_fog_cutoff_distance(value) -> None
Set Fog Cutoff Distance

Args:
    value (float):

<a id="unreal.ExponentialHeightFogComponent.set_end_distance"></a>

#### set_end_distance

```python
def set_end_distance(value: float) -> None
```

x.set_end_distance(value) -> None
Set End Distance

Args:
    value (float):

<a id="unreal.ExponentialHeightFogComponent.set_directional_inscattering_start_distance"></a>

#### set_directional_inscattering_start_distance

```python
def set_directional_inscattering_start_distance(value: float) -> None
```

x.set_directional_inscattering_start_distance(value) -> None
Set Directional Inscattering Start Distance

Args:
    value (float):

<a id="unreal.ExponentialHeightFogComponent.set_directional_inscattering_exponent"></a>

#### set_directional_inscattering_exponent

```python
def set_directional_inscattering_exponent(value: float) -> None
```

x.set_directional_inscattering_exponent(value) -> None
Set Directional Inscattering Exponent

Args:
    value (float):

<a id="unreal.ExponentialHeightFogComponent.set_directional_inscattering_color"></a>

#### set_directional_inscattering_color

```python
def set_directional_inscattering_color(value: LinearColor) -> None
```

x.set_directional_inscattering_color(value) -> None
Set Directional Inscattering Color

Args:
    value (LinearColor):

<a id="unreal.DataLayerAsset"></a>