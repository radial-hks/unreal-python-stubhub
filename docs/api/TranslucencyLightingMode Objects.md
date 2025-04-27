## TranslucencyLightingMode Objects

```python
class TranslucencyLightingMode(EnumBase)
```

Describes how to handle lighting of translucent objets

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.TranslucencyLightingMode.TLM_VOLUMETRIC_NON_DIRECTIONAL"></a>

#### TLM_VOLUMETRIC_NON_DIRECTIONAL

0: Lighting will be calculated for a volume, without directionality.  Use this on particle effects like smoke and dust.
This is the cheapest per-pixel lighting method, however the material normal is not taken into account.

<a id="unreal.TranslucencyLightingMode.TLM_VOLUMETRIC_DIRECTIONAL"></a>

#### TLM_VOLUMETRIC_DIRECTIONAL

1: Lighting will be calculated for a volume, with directionality so that the normal of the material is taken into account.
Note that the default particle tangent space is facing the camera, so enable bGenerateSphericalParticleNormals to get a more useful tangent space.

<a id="unreal.TranslucencyLightingMode.TLM_VOLUMETRIC_PER_VERTEX_NON_DIRECTIONAL"></a>

#### TLM_VOLUMETRIC_PER_VERTEX_NON_DIRECTIONAL

2: Same as Volumetric Non Directional, but lighting is only evaluated at vertices so the pixel shader cost is significantly less.
Note that lighting still comes from a volume texture, so it is limited in range.  Directional lights become unshadowed in the distance.

<a id="unreal.TranslucencyLightingMode.TLM_VOLUMETRIC_PER_VERTEX_DIRECTIONAL"></a>

#### TLM_VOLUMETRIC_PER_VERTEX_DIRECTIONAL

3: Same as Volumetric Directional, but lighting is only evaluated at vertices so the pixel shader cost is significantly less.
Note that lighting still comes from a volume texture, so it is limited in range.  Directional lights become unshadowed in the distance.

<a id="unreal.TranslucencyLightingMode.TLM_SURFACE"></a>

#### TLM_SURFACE

4: Lighting will be calculated for a surface. The light is accumulated in a volume so the result is blurry,
limited distance but the per pixel cost is very low. Use this on translucent surfaces like glass and water.
Only diffuse lighting is supported.

<a id="unreal.TranslucencyLightingMode.TLM_SURFACE_PER_PIXEL_LIGHTING"></a>

#### TLM_SURFACE_PER_PIXEL_LIGHTING

5: Lighting will be calculated for a surface. Use this on translucent surfaces like glass and water.
This is implemented with forward shading so specular highlights from local lights are supported, however many deferred-only features are not.
This is the most expensive translucency lighting method as each light's contribution is computed per-pixel.

<a id="unreal.MaterialFloatPrecisionMode"></a>