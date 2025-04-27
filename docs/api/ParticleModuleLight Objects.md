## ParticleModuleLight Objects

```python
class ParticleModuleLight(ParticleModuleLightBase)
```

Particle Module Light

**C++ Source:**

- **Module**: Engine
- **File**: ParticleModuleLight.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``affects_translucency`` (bool):  [Read-Write] Whether lights from this module should affect translucency.
  Use with caution.  Modules enabling this should only make a few particle lights at most, and the smaller they are, the less they will cost.
- ``b3d_draw_mode`` (bool):  [Read-Write] If true, the module should render its 3D visualization helper
- ``brightness_over_life`` (RawDistributionFloat):  [Read-Write] Brightness scale for the light, which can be setup as a curve over the particle's lifetime.
- ``color_scale_over_life`` (RawDistributionVector):  [Read-Write] Scale that is applied to the particle's color to calculate the light's color, and can be setup as a curve over the particle's lifetime.
- ``high_quality_lights`` (bool):  [Read-Write] Converts the particle lights into high quality lights as if they came from a PointLightComponent.  High quality lights cost significantly more on both CPU and GPU.
- ``inverse_exposure_blend`` (float):  [Read-Write] Blend Factor used to blend between Intensity and Intensity/Exposure.
  This is useful for gameplay lights that should have constant brighness on screen independent of current exposure.
  This feature can cause issues with exposure particularly when used on the primary light on a scene, as such it's usage should be limited.
- ``light_exponent`` (RawDistributionFloat):  [Read-Write] Provides the light's exponent when inverse squared falloff is disabled.
- ``lighting_channels`` (LightingChannels):  [Read-Write] Channels that this light should affect.
  Only affect high quality lights
  These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing.
- ``module_editor_color`` (Color):  [Read-Write] The color to draw the modules curves in the curve editor.
      If bCurvesAsColor is true, it overrides this value.
- ``override_inverse_exposure_blend`` (bool):  [Read-Write] When enabled we will override the project default setting with our local setting.
- ``preview_light_radius`` (bool):  [Read-Write] Will draw wireframe spheres to preview the light radius if enabled.
  Note: this is intended for previewing and the value will not be saved, it will always revert to disabled.
- ``radius_scale`` (RawDistributionFloat):  [Read-Write] Scales the particle's radius, to calculate the light's radius.
- ``shadow_casting_lights`` (bool):  [Read-Write] Whether to cast shadows from the particle lights.  Requires High Quality Lights to be enabled.
  Warning: This can be incredibly expensive on the GPU - use with caution.
- ``spawn_fraction`` (float):  [Read-Write] Fraction of particles in this emitter to create lights on.
- ``use_inverse_squared_falloff`` (bool):  [Read-Write] Whether to use physically based inverse squared falloff from the light.  If unchecked, the LightExponent distribution will be used instead.
- ``volumetric_scattering_intensity`` (float):  [Read-Write] Intensity of the volumetric scattering from this light.  This scales Intensity and LightColor.

<a id="unreal.ParticleModuleLight.inverse_exposure_blend"></a>

#### inverse_exposure_blend

```python
@property
def inverse_exposure_blend() -> float
```

(float):  [Read-Only] Blend Factor used to blend between Intensity and Intensity/Exposure.
This is useful for gameplay lights that should have constant brighness on screen independent of current exposure.
This feature can cause issues with exposure particularly when used on the primary light on a scene, as such it's usage should be limited.

<a id="unreal.ParticleModuleLight.lighting_channels"></a>

#### lighting_channels

```python
@property
def lighting_channels() -> LightingChannels
```

(LightingChannels):  [Read-Only] Channels that this light should affect.
Only affect high quality lights
These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing.

<a id="unreal.ParticleModuleLight.volumetric_scattering_intensity"></a>

#### volumetric_scattering_intensity

```python
@property
def volumetric_scattering_intensity() -> float
```

(float):  [Read-Only] Intensity of the volumetric scattering from this light.  This scales Intensity and LightColor.

<a id="unreal.ParticleModuleLight_Seeded"></a>