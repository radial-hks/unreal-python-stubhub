## MegaLightsShadowMethod Objects

```python
class MegaLightsShadowMethod(EnumBase)
```

MegaLights Shadow type for a light component.

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.MegaLightsShadowMethod.DEFAULT"></a>

#### DEFAULT

0: Recommended. Uses the default MegaLights shadow method.

<a id="unreal.MegaLightsShadowMethod.RAY_TRACING"></a>

#### RAY_TRACING

1: Preferred method, which guarantees fixed MegaLights cost and correct area shadows, but is dependent on the BVH representation quality.

<a id="unreal.MegaLightsShadowMethod.VIRTUAL_SHADOW_MAP"></a>

#### VIRTUAL_SHADOW_MAP

2: Has a significant per light cost, but can cast shadows directly from the Nanite geometry using rasterization.

<a id="unreal.LightUnits"></a>