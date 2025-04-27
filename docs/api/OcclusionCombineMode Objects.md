## OcclusionCombineMode Objects

```python
class OcclusionCombineMode(EnumBase)
```

Controls how occlusion from Distance Field Ambient Occlusion is combined with Screen Space Ambient Occlusion.

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.OcclusionCombineMode.OCM_MINIMUM"></a>

#### OCM_MINIMUM

0: Take the minimum occlusion value.  This is effective for avoiding over-occlusion from multiple methods, but can result in indoors looking too flat.

<a id="unreal.OcclusionCombineMode.OCM_MULTIPLY"></a>

#### OCM_MULTIPLY

1: Multiply together occlusion values from Distance Field Ambient Occlusion and Screen Space Ambient Occlusion.
This gives a good sense of depth everywhere, but can cause over-occlusion.
SSAO should be tweaked to be less strong compared to Minimum.

<a id="unreal.PixelFormat"></a>