## DynamicGlobalIlluminationMethod Objects

```python
class DynamicGlobalIlluminationMethod(EnumBase)
```

Note: Must match r.DynamicGlobalIlluminationMethod, this is used in URendererSettings

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.DynamicGlobalIlluminationMethod.NONE"></a>

#### NONE

0: No dynamic Global Illumination method will be used. Global Illumination can still be baked into lightmaps.

<a id="unreal.DynamicGlobalIlluminationMethod.LUMEN"></a>

#### LUMEN

1: Use Lumen Global Illumination for all lights, emissive materials casting light and SkyLight Occlusion.  Requires 'Generate Mesh Distance Fields' enabled for Software Ray Tracing and 'Support Hardware Ray Tracing' enabled for Hardware Ray Tracing.

<a id="unreal.DynamicGlobalIlluminationMethod.SCREEN_SPACE"></a>

#### SCREEN_SPACE

2: Standalone Screen Space Global Illumination.  Low cost, but limited by screen space information.

<a id="unreal.DynamicGlobalIlluminationMethod.PLUGIN"></a>

#### PLUGIN

3: Use a plugin for Global Illumination

<a id="unreal.LumenRayLightingModeOverride"></a>