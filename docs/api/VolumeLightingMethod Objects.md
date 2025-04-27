## VolumeLightingMethod Objects

```python
class VolumeLightingMethod(EnumBase)
```

EVolume Lighting Method

**C++ Source:**

- **Module**: Engine
- **File**: WorldSettings.h

<a id="unreal.VolumeLightingMethod.VLM_VOLUMETRIC_LIGHTMAP"></a>

#### VLM_VOLUMETRIC_LIGHTMAP

0: Lighting samples are computed in an adaptive grid which covers the entire Lightmass Importance Volume.  Higher density grids are used near geometry.
The Volumetric Lightmap is interpolated efficiently on the GPU per-pixel, allowing accurate indirect lighting for dynamic objects and volumetric fog.
Positions outside of the Importance Volume reuse the border texels of the Volumetric Lightmap (clamp addressing).
On mobile, interpolation is done on the CPU at the center of each object's bounds.

<a id="unreal.VolumeLightingMethod.VLM_SPARSE_VOLUME_LIGHTING_SAMPLES"></a>

#### VLM_SPARSE_VOLUME_LIGHTING_SAMPLES

1: Volume lighting samples are placed on top of static surfaces at medium density, and everywhere else in the Lightmass Importance Volume at low density.  Positions outside of the Importance Volume will have no indirect lighting.
This method requires CPU interpolation so the Indirect Lighting Cache is used to interpolate results for each dynamic object, adding Rendering Thread overhead.
Volumetric Fog cannot be affected by precomputed lighting with this method.

<a id="unreal.MontageBlendMode"></a>