## PathTracingBufferTextureId Objects

```python
class PathTracingBufferTextureId(EnumBase)
```

EPath Tracing Buffer Texture Id

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionPathTracingBufferTexture.h

<a id="unreal.PathTracingBufferTextureId.PTBT_RADIANCE"></a>

#### PTBT_RADIANCE

0: Radiance (Path Tracing). The raw radiance.

<a id="unreal.PathTracingBufferTextureId.PTBT_DENOISED_RADIANCE"></a>

#### PTBT_DENOISED_RADIANCE

1: Normal (Path Tracing). Stores the denoised radiance if denoising is turned on and complete for the current frame, otherwise, black.

<a id="unreal.PathTracingBufferTextureId.PTBT_ALBEDO"></a>

#### PTBT_ALBEDO

2: Albedo (Path Tracing). Average albedo at the current sample count.

<a id="unreal.PathTracingBufferTextureId.PTBT_NORMAL"></a>

#### PTBT_NORMAL

3: Normal (Path Tracing). Average normal at the current sample count.

<a id="unreal.PathTracingBufferTextureId.PTBT_VARIANCE"></a>

#### PTBT_VARIANCE

4: Variance (Path Tracing). Path tracing variance stored as standard derivation. Variance can be per channel variance or
              variance of luminance, albedo, and normal based on the path tracing configuration. Hooking up this buffer can increase additional
              cost.

<a id="unreal.RuntimeVirtualTextureMaterialType"></a>