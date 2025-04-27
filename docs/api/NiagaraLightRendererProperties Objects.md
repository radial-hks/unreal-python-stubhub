## NiagaraLightRendererProperties Objects

```python
class NiagaraLightRendererProperties(NiagaraRendererProperties)
```

Niagara Light Renderer Properties

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraLightRendererProperties.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``affects_translucency`` (bool):  [Read-Write] Whether lights from this renderer should affect translucency.
  Use with caution - if enabled, create only a few particle lights at most, and the smaller they are, the less they will cost.
- ``allow_in_cull_proxies`` (bool):  [Read-Write]
- ``alpha_scales_brightness`` (bool):  [Read-Write] When checked, will treat the alpha value of the particle's color as a multiplier of the light's brightness.
- ``color_add`` (Vector3f):  [Read-Write] A static color shift applied to each rendered light
- ``color_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for light color when generating lights?
- ``default_exponent`` (float):  [Read-Write] The exponent to use for all lights if no exponent binding was found
- ``diffuse_scale`` (float):  [Read-Write] The diffuse scale to use for all lights if no binding was found
- ``diffuse_scale_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for the diffuse scale when generating lights?
- ``inverse_exposure_blend`` (float):  [Read-Write] Blend Factor used to blend between Intensity and Intensity/Exposure.
  This is useful for gameplay lights that should have constant brighness on screen independent of current exposure.
  This feature can cause issues with exposure particularly when used on the primary light on a scene, as such it's usage should be limited.
- ``light_exponent_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for the light's exponent when inverse squared falloff is disabled?
- ``light_rendering_enabled_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use to check if light rendering should be enabled for a particle? This can be used to control the spawn-rate on a per-particle basis.
- ``motion_vector_setting`` (NiagaraRendererMotionVectorSetting):  [Read-Write] Hint about how to generate motion (velocity) vectors for this renderer.
- ``override_inverse_exposure_blend`` (bool):  [Read-Write] When enabled we will override the project default setting with our local setting.
- ``platforms`` (NiagaraPlatformSet):  [Read-Write] Platforms on which this renderer is enabled.
- ``position_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for position when generating lights?
- ``radius_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for light radius when generating lights?
- ``radius_scale`` (float):  [Read-Write] A factor used to scale each particle light radius
- ``renderer_enabled_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Binding to control if the renderer is enabled or disabled.
  When disabled the renderer does not generate or render any particle data.
  When disabled via a static bool the renderer will be removed in cooked content.
- ``renderer_visibility`` (int32):  [Read-Write] If a render visibility tag is present, particles whose tag matches this value will be visible in this renderer.
- ``renderer_visibility_tag_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for the renderer visibility tag?
- ``sort_order_hint`` (int32):  [Read-Write] By default, emitters are drawn in the order that they are added to the system. This value will allow you to control the order in a more fine-grained manner.
        Materials of the same type (i.e. Transparent) will draw in order from lowest to highest within the system. The default value is 0.
- ``source_mode`` (NiagaraRendererSourceDataMode):  [Read-Write] Whether or not to draw a single element for the Emitter or to draw the particles.
- ``specular_scale`` (float):  [Read-Write] The specular scale to use for all lights if no binding was found
- ``specular_scale_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for the specular scale when generating lights?
- ``use_inverse_squared_falloff`` (bool):  [Read-Write] Whether to use physically based inverse squared falloff from the light.  If unchecked, the value from the LightExponent binding will be used instead.
- ``volumetric_scattering_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Which attribute should we use for the intensity of the volumetric scattering from this light? This scales the light's intensity and color.

<a id="unreal.NiagaraLightRendererProperties.inverse_exposure_blend"></a>

#### inverse_exposure_blend

```python
@property
def inverse_exposure_blend() -> float
```

(float):  [Read-Only] Blend Factor used to blend between Intensity and Intensity/Exposure.
This is useful for gameplay lights that should have constant brighness on screen independent of current exposure.
This feature can cause issues with exposure particularly when used on the primary light on a scene, as such it's usage should be limited.

<a id="unreal.NiagaraParameterCollectionInstance"></a>