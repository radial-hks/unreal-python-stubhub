## LightmassWorldInfoSettings Objects

```python
class LightmassWorldInfoSettings(StructBase)
```

Lightmass World Info Settings

**C++ Source:**

- **Module**: Engine
- **File**: WorldSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``compress_lightmaps`` (bool):  [Read-Write] Whether to compress lightmap textures.  Disabling lightmap texture compression will reduce artifacts but increase memory and disk size by 4x.
  Use caution when disabling this.
- ``diffuse_boost`` (float):  [Read-Write] Scales the diffuse contribution of all materials in the scene.
- ``direct_illumination_occlusion_fraction`` (float):  [Read-Write] How much of the AO to apply to direct lighting.
- ``environment_color`` (Color):  [Read-Write] Represents a constant color light surrounding the upper hemisphere of the level, like a sky.
  This light source currently does not get bounced as indirect lighting and causes reflection capture brightness to be incorrect.  Prefer using a Static Skylight instead.
- ``environment_intensity`` (float):  [Read-Write] Scales EnvironmentColor to allow independent color and brightness controls.
- ``fully_occluded_samples_fraction`` (float):  [Read-Write] Fraction of samples taken that must be occluded in order to reach full occlusion.
- ``generate_ambient_occlusion_material_mask`` (bool):  [Read-Write] Whether to generate textures storing the AO computed by Lightmass.
  These can be accessed through the PrecomputedAOMask material node,
  Which is useful for blending between material layers on environment assets.
  Be sure to set DirectIlluminationOcclusionFraction and IndirectIlluminationOcclusionFraction to 0 if you only want the PrecomputedAOMask!
- ``indirect_illumination_occlusion_fraction`` (float):  [Read-Write] How much of the AO to apply to indirect lighting.
- ``indirect_lighting_quality`` (float):  [Read-Write] Warning: Setting this higher than 1 will greatly increase build times!
  Can be used to increase the GI solver sample counts in order to get higher quality for levels that need it.
  It can be useful to reduce IndirectLightingSmoothness somewhat (~.75) when increasing quality to get defined indirect shadows.
  Note that this can't affect compression artifacts, UV seams or other texture based artifacts.
- ``indirect_lighting_smoothness`` (float):  [Read-Write] Smoothness factor to apply to indirect lighting.  This is useful in some lighting conditions when Lightmass cannot resolve accurate indirect lighting.
  1 is default smoothness tweaked for a variety of lighting situations.
  Higher values like 3 smooth out the indirect lighting more, but at the cost of indirect shadows losing detail.
- ``max_occlusion_distance`` (float):  [Read-Write] Maximum distance for an object to cause occlusion on another object.
- ``num_indirect_lighting_bounces`` (int32):  [Read-Write] Number of light bounces to simulate for point / spot / directional lights, starting from the light source.
  0 is direct lighting only, 1 is one bounce, etc.
  Bounce 1 takes the most time to calculate and contributes the most to visual quality, followed by bounce 2.
  Successive bounces don't really affect build times, but have a much lower visual impact, unless the material diffuse colors are close to 1.
- ``num_sky_lighting_bounces`` (int32):  [Read-Write] Number of skylight and emissive bounces to simulate.
  Lightmass uses a non-distributable radiosity method for skylight bounces whose cost is proportional to the number of bounces.
- ``occlusion_exponent`` (float):  [Read-Write] Higher exponents increase contrast.
- ``static_lighting_level_scale`` (float):  [Read-Write] Warning: Setting this to less than 1 will greatly increase build times!
  Scale of the level relative to real world scale (1 Unreal Unit = 1 cm).
  All scale-dependent Lightmass setting defaults have been tweaked to work well with real world scale,
  Any levels with a different scale should use this scale to compensate.
  For large levels it can drastically reduce build times to set this to 2 or 4.
- ``use_ambient_occlusion`` (bool):  [Read-Write] If true, AmbientOcclusion will be enabled.
- ``visualize_ambient_occlusion`` (bool):  [Read-Write] If true, override normal direct and indirect lighting with just the AO term.
- ``visualize_material_diffuse`` (bool):  [Read-Write] If true, override normal direct and indirect lighting with just the exported diffuse term.
- ``volume_light_sample_placement_scale`` (float):  [Read-Write] Scales the distances at which volume lighting samples are placed.  Volume lighting samples are computed by Lightmass and are used for GI on movable components.
  Using larger scales results in less sample memory usage and reduces Indirect Lighting Cache update times, but less accurate transitions between lighting areas.
- ``volume_lighting_method`` (VolumeLightingMethod):  [Read-Write] Technique to use for providing precomputed lighting at all positions inside the Lightmass Importance Volume
- ``volumetric_lightmap_detail_cell_size`` (float):  [Read-Write] Size of an Volumetric Lightmap voxel at the highest density (used around geometry), in world space units.
  This setting has a large impact on build times and memory, use with caution.
  Halving the DetailCellSize can increase memory by up to a factor of 8x.
- ``volumetric_lightmap_loading_cell_size`` (float):  [Read-Write] Size of an Volumetric Lightmap high detail loading cell.
- ``volumetric_lightmap_maximum_brick_memory_mb`` (float):  [Read-Write] Maximum amount of memory to spend on Volumetric Lightmap Brick data.  High density bricks will be discarded until this limit is met, with bricks furthest from geometry discarded first.
- ``volumetric_lightmap_spherical_harmonic_smoothing`` (float):  [Read-Write] Controls how much smoothing should be done to Volumetric Lightmap samples during Spherical Harmonic de-ringing.
  Whenever highly directional lighting is stored in a Spherical Harmonic, a ringing artifact occurs which manifests as unexpected black areas on the opposite side.
  Smoothing can reduce this artifact.  Smoothing is only applied when the ringing artifact is present.
  0 = no smoothing, 1 = strong smooth (little directionality in lighting).

<a id="unreal.LightmassWorldInfoSettings.__init__"></a>

#### __init__

```python
def __init__(
        static_lighting_level_scale: float = 0.000000,
        num_indirect_lighting_bounces: int = 0,
        num_sky_lighting_bounces: int = 0,
        indirect_lighting_quality: float = 0.000000,
        indirect_lighting_smoothness: float = 0.000000,
        environment_color: Color = [0, 0, 0, 0],
        environment_intensity: float = 0.000000,
        diffuse_boost: float = 0.000000,
        volume_lighting_method: VolumeLightingMethod = VolumeLightingMethod.
    VLM_VOLUMETRIC_LIGHTMAP,
        use_ambient_occlusion: bool = False,
        generate_ambient_occlusion_material_mask: bool = False,
        visualize_material_diffuse: bool = False,
        visualize_ambient_occlusion: bool = False,
        compress_lightmaps: bool = False,
        volumetric_lightmap_detail_cell_size: float = 0.000000,
        volumetric_lightmap_maximum_brick_memory_mb: float = 0.000000,
        volumetric_lightmap_loading_cell_size: float = 0.000000,
        volumetric_lightmap_spherical_harmonic_smoothing: float = 0.000000,
        volume_light_sample_placement_scale: float = 0.000000,
        direct_illumination_occlusion_fraction: float = 0.000000,
        indirect_illumination_occlusion_fraction: float = 0.000000,
        occlusion_exponent: float = 0.000000,
        fully_occluded_samples_fraction: float = 0.000000,
        max_occlusion_distance: float = 0.000000) -> None
```

<a id="unreal.LightmassWorldInfoSettings.static_lighting_level_scale"></a>

#### static_lighting_level_scale

```python
@property
def static_lighting_level_scale() -> float
```

(float):  [Read-Write] Warning: Setting this to less than 1 will greatly increase build times!
Scale of the level relative to real world scale (1 Unreal Unit = 1 cm).
All scale-dependent Lightmass setting defaults have been tweaked to work well with real world scale,
Any levels with a different scale should use this scale to compensate.
For large levels it can drastically reduce build times to set this to 2 or 4.

<a id="unreal.LightmassWorldInfoSettings.static_lighting_level_scale"></a>

#### static_lighting_level_scale

```python
@static_lighting_level_scale.setter
def static_lighting_level_scale(value: float) -> None
```

<a id="unreal.LightmassWorldInfoSettings.num_indirect_lighting_bounces"></a>

#### num_indirect_lighting_bounces

```python
@property
def num_indirect_lighting_bounces() -> int
```

(int32):  [Read-Write] Number of light bounces to simulate for point / spot / directional lights, starting from the light source.
0 is direct lighting only, 1 is one bounce, etc.
Bounce 1 takes the most time to calculate and contributes the most to visual quality, followed by bounce 2.
Successive bounces don't really affect build times, but have a much lower visual impact, unless the material diffuse colors are close to 1.

<a id="unreal.LightmassWorldInfoSettings.num_indirect_lighting_bounces"></a>

#### num_indirect_lighting_bounces

```python
@num_indirect_lighting_bounces.setter
def num_indirect_lighting_bounces(value: int) -> None
```

<a id="unreal.LightmassWorldInfoSettings.num_sky_lighting_bounces"></a>

#### num_sky_lighting_bounces

```python
@property
def num_sky_lighting_bounces() -> int
```

(int32):  [Read-Write] Number of skylight and emissive bounces to simulate.
Lightmass uses a non-distributable radiosity method for skylight bounces whose cost is proportional to the number of bounces.

<a id="unreal.LightmassWorldInfoSettings.num_sky_lighting_bounces"></a>

#### num_sky_lighting_bounces

```python
@num_sky_lighting_bounces.setter
def num_sky_lighting_bounces(value: int) -> None
```

<a id="unreal.LightmassWorldInfoSettings.indirect_lighting_quality"></a>

#### indirect_lighting_quality

```python
@property
def indirect_lighting_quality() -> float
```

(float):  [Read-Write] Warning: Setting this higher than 1 will greatly increase build times!
Can be used to increase the GI solver sample counts in order to get higher quality for levels that need it.
It can be useful to reduce IndirectLightingSmoothness somewhat (~.75) when increasing quality to get defined indirect shadows.
Note that this can't affect compression artifacts, UV seams or other texture based artifacts.

<a id="unreal.LightmassWorldInfoSettings.indirect_lighting_quality"></a>

#### indirect_lighting_quality

```python
@indirect_lighting_quality.setter
def indirect_lighting_quality(value: float) -> None
```

<a id="unreal.LightmassWorldInfoSettings.indirect_lighting_smoothness"></a>

#### indirect_lighting_smoothness

```python
@property
def indirect_lighting_smoothness() -> float
```

(float):  [Read-Write] Smoothness factor to apply to indirect lighting.  This is useful in some lighting conditions when Lightmass cannot resolve accurate indirect lighting.
1 is default smoothness tweaked for a variety of lighting situations.
Higher values like 3 smooth out the indirect lighting more, but at the cost of indirect shadows losing detail.

<a id="unreal.LightmassWorldInfoSettings.indirect_lighting_smoothness"></a>

#### indirect_lighting_smoothness

```python
@indirect_lighting_smoothness.setter
def indirect_lighting_smoothness(value: float) -> None
```

<a id="unreal.LightmassWorldInfoSettings.environment_color"></a>

#### environment_color

```python
@property
def environment_color() -> Color
```

(Color):  [Read-Write] Represents a constant color light surrounding the upper hemisphere of the level, like a sky.
This light source currently does not get bounced as indirect lighting and causes reflection capture brightness to be incorrect.  Prefer using a Static Skylight instead.

<a id="unreal.LightmassWorldInfoSettings.environment_color"></a>

#### environment_color

```python
@environment_color.setter
def environment_color(value: Color) -> None
```

<a id="unreal.LightmassWorldInfoSettings.environment_intensity"></a>

#### environment_intensity

```python
@property
def environment_intensity() -> float
```

(float):  [Read-Write] Scales EnvironmentColor to allow independent color and brightness controls.

<a id="unreal.LightmassWorldInfoSettings.environment_intensity"></a>

#### environment_intensity

```python
@environment_intensity.setter
def environment_intensity(value: float) -> None
```

<a id="unreal.LightmassWorldInfoSettings.diffuse_boost"></a>

#### diffuse_boost

```python
@property
def diffuse_boost() -> float
```

(float):  [Read-Write] Scales the diffuse contribution of all materials in the scene.

<a id="unreal.LightmassWorldInfoSettings.diffuse_boost"></a>

#### diffuse_boost

```python
@diffuse_boost.setter
def diffuse_boost(value: float) -> None
```

<a id="unreal.LightmassWorldInfoSettings.volume_lighting_method"></a>

#### volume_lighting_method

```python
@property
def volume_lighting_method() -> VolumeLightingMethod
```

(VolumeLightingMethod):  [Read-Write] Technique to use for providing precomputed lighting at all positions inside the Lightmass Importance Volume

<a id="unreal.LightmassWorldInfoSettings.volume_lighting_method"></a>

#### volume_lighting_method

```python
@volume_lighting_method.setter
def volume_lighting_method(value: VolumeLightingMethod) -> None
```

<a id="unreal.LightmassWorldInfoSettings.use_ambient_occlusion"></a>

#### use_ambient_occlusion

```python
@property
def use_ambient_occlusion() -> bool
```

(bool):  [Read-Write] If true, AmbientOcclusion will be enabled.

<a id="unreal.LightmassWorldInfoSettings.use_ambient_occlusion"></a>

#### use_ambient_occlusion

```python
@use_ambient_occlusion.setter
def use_ambient_occlusion(value: bool) -> None
```

<a id="unreal.LightmassWorldInfoSettings.generate_ambient_occlusion_material_mask"></a>

#### generate_ambient_occlusion_material_mask

```python
@property
def generate_ambient_occlusion_material_mask() -> bool
```

(bool):  [Read-Write] Whether to generate textures storing the AO computed by Lightmass.
These can be accessed through the PrecomputedAOMask material node,
Which is useful for blending between material layers on environment assets.
Be sure to set DirectIlluminationOcclusionFraction and IndirectIlluminationOcclusionFraction to 0 if you only want the PrecomputedAOMask!

<a id="unreal.LightmassWorldInfoSettings.generate_ambient_occlusion_material_mask"></a>

#### generate_ambient_occlusion_material_mask

```python
@generate_ambient_occlusion_material_mask.setter
def generate_ambient_occlusion_material_mask(value: bool) -> None
```

<a id="unreal.LightmassWorldInfoSettings.visualize_material_diffuse"></a>

#### visualize_material_diffuse

```python
@property
def visualize_material_diffuse() -> bool
```

(bool):  [Read-Write] If true, override normal direct and indirect lighting with just the exported diffuse term.

<a id="unreal.LightmassWorldInfoSettings.visualize_material_diffuse"></a>

#### visualize_material_diffuse

```python
@visualize_material_diffuse.setter
def visualize_material_diffuse(value: bool) -> None
```

<a id="unreal.LightmassWorldInfoSettings.visualize_ambient_occlusion"></a>

#### visualize_ambient_occlusion

```python
@property
def visualize_ambient_occlusion() -> bool
```

(bool):  [Read-Write] If true, override normal direct and indirect lighting with just the AO term.

<a id="unreal.LightmassWorldInfoSettings.visualize_ambient_occlusion"></a>

#### visualize_ambient_occlusion

```python
@visualize_ambient_occlusion.setter
def visualize_ambient_occlusion(value: bool) -> None
```

<a id="unreal.LightmassWorldInfoSettings.compress_lightmaps"></a>

#### compress_lightmaps

```python
@property
def compress_lightmaps() -> bool
```

(bool):  [Read-Write] Whether to compress lightmap textures.  Disabling lightmap texture compression will reduce artifacts but increase memory and disk size by 4x.
Use caution when disabling this.

<a id="unreal.LightmassWorldInfoSettings.compress_lightmaps"></a>

#### compress_lightmaps

```python
@compress_lightmaps.setter
def compress_lightmaps(value: bool) -> None
```

<a id="unreal.LightmassWorldInfoSettings.volumetric_lightmap_detail_cell_size"></a>

#### volumetric_lightmap_detail_cell_size

```python
@property
def volumetric_lightmap_detail_cell_size() -> float
```

(float):  [Read-Write] Size of an Volumetric Lightmap voxel at the highest density (used around geometry), in world space units.
This setting has a large impact on build times and memory, use with caution.
Halving the DetailCellSize can increase memory by up to a factor of 8x.

<a id="unreal.LightmassWorldInfoSettings.volumetric_lightmap_detail_cell_size"></a>

#### volumetric_lightmap_detail_cell_size

```python
@volumetric_lightmap_detail_cell_size.setter
def volumetric_lightmap_detail_cell_size(value: float) -> None
```

<a id="unreal.LightmassWorldInfoSettings.volumetric_lightmap_maximum_brick_memory_mb"></a>

#### volumetric_lightmap_maximum_brick_memory_mb

```python
@property
def volumetric_lightmap_maximum_brick_memory_mb() -> float
```

(float):  [Read-Write] Maximum amount of memory to spend on Volumetric Lightmap Brick data.  High density bricks will be discarded until this limit is met, with bricks furthest from geometry discarded first.

<a id="unreal.LightmassWorldInfoSettings.volumetric_lightmap_maximum_brick_memory_mb"></a>

#### volumetric_lightmap_maximum_brick_memory_mb

```python
@volumetric_lightmap_maximum_brick_memory_mb.setter
def volumetric_lightmap_maximum_brick_memory_mb(value: float) -> None
```

<a id="unreal.LightmassWorldInfoSettings.volumetric_lightmap_loading_cell_size"></a>

#### volumetric_lightmap_loading_cell_size

```python
@property
def volumetric_lightmap_loading_cell_size() -> float
```

(float):  [Read-Write] Size of an Volumetric Lightmap high detail loading cell.

<a id="unreal.LightmassWorldInfoSettings.volumetric_lightmap_loading_cell_size"></a>

#### volumetric_lightmap_loading_cell_size

```python
@volumetric_lightmap_loading_cell_size.setter
def volumetric_lightmap_loading_cell_size(value: float) -> None
```

<a id="unreal.LightmassWorldInfoSettings.volumetric_lightmap_spherical_harmonic_smoothing"></a>

#### volumetric_lightmap_spherical_harmonic_smoothing

```python
@property
def volumetric_lightmap_spherical_harmonic_smoothing() -> float
```

(float):  [Read-Write] Controls how much smoothing should be done to Volumetric Lightmap samples during Spherical Harmonic de-ringing.
Whenever highly directional lighting is stored in a Spherical Harmonic, a ringing artifact occurs which manifests as unexpected black areas on the opposite side.
Smoothing can reduce this artifact.  Smoothing is only applied when the ringing artifact is present.
0 = no smoothing, 1 = strong smooth (little directionality in lighting).

<a id="unreal.LightmassWorldInfoSettings.volumetric_lightmap_spherical_harmonic_smoothing"></a>

#### volumetric_lightmap_spherical_harmonic_smoothing

```python
@volumetric_lightmap_spherical_harmonic_smoothing.setter
def volumetric_lightmap_spherical_harmonic_smoothing(value: float) -> None
```

<a id="unreal.LightmassWorldInfoSettings.volume_light_sample_placement_scale"></a>

#### volume_light_sample_placement_scale

```python
@property
def volume_light_sample_placement_scale() -> float
```

(float):  [Read-Write] Scales the distances at which volume lighting samples are placed.  Volume lighting samples are computed by Lightmass and are used for GI on movable components.
Using larger scales results in less sample memory usage and reduces Indirect Lighting Cache update times, but less accurate transitions between lighting areas.

<a id="unreal.LightmassWorldInfoSettings.volume_light_sample_placement_scale"></a>

#### volume_light_sample_placement_scale

```python
@volume_light_sample_placement_scale.setter
def volume_light_sample_placement_scale(value: float) -> None
```

<a id="unreal.LightmassWorldInfoSettings.direct_illumination_occlusion_fraction"></a>

#### direct_illumination_occlusion_fraction

```python
@property
def direct_illumination_occlusion_fraction() -> float
```

(float):  [Read-Write] How much of the AO to apply to direct lighting.

<a id="unreal.LightmassWorldInfoSettings.direct_illumination_occlusion_fraction"></a>

#### direct_illumination_occlusion_fraction

```python
@direct_illumination_occlusion_fraction.setter
def direct_illumination_occlusion_fraction(value: float) -> None
```

<a id="unreal.LightmassWorldInfoSettings.indirect_illumination_occlusion_fraction"></a>

#### indirect_illumination_occlusion_fraction

```python
@property
def indirect_illumination_occlusion_fraction() -> float
```

(float):  [Read-Write] How much of the AO to apply to indirect lighting.

<a id="unreal.LightmassWorldInfoSettings.indirect_illumination_occlusion_fraction"></a>

#### indirect_illumination_occlusion_fraction

```python
@indirect_illumination_occlusion_fraction.setter
def indirect_illumination_occlusion_fraction(value: float) -> None
```

<a id="unreal.LightmassWorldInfoSettings.occlusion_exponent"></a>

#### occlusion_exponent

```python
@property
def occlusion_exponent() -> float
```

(float):  [Read-Write] Higher exponents increase contrast.

<a id="unreal.LightmassWorldInfoSettings.occlusion_exponent"></a>

#### occlusion_exponent

```python
@occlusion_exponent.setter
def occlusion_exponent(value: float) -> None
```

<a id="unreal.LightmassWorldInfoSettings.fully_occluded_samples_fraction"></a>

#### fully_occluded_samples_fraction

```python
@property
def fully_occluded_samples_fraction() -> float
```

(float):  [Read-Write] Fraction of samples taken that must be occluded in order to reach full occlusion.

<a id="unreal.LightmassWorldInfoSettings.fully_occluded_samples_fraction"></a>

#### fully_occluded_samples_fraction

```python
@fully_occluded_samples_fraction.setter
def fully_occluded_samples_fraction(value: float) -> None
```

<a id="unreal.LightmassWorldInfoSettings.max_occlusion_distance"></a>

#### max_occlusion_distance

```python
@property
def max_occlusion_distance() -> float
```

(float):  [Read-Write] Maximum distance for an object to cause occlusion on another object.

<a id="unreal.LightmassWorldInfoSettings.max_occlusion_distance"></a>

#### max_occlusion_distance

```python
@max_occlusion_distance.setter
def max_occlusion_distance(value: float) -> None
```

<a id="unreal.QuartzPulseOverrideStep"></a>