## ReflectionMethod Objects

```python
class ReflectionMethod(EnumBase)
```

Note: Must match r.ReflectionMethod, this is used in URendererSettings

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.ReflectionMethod.NONE"></a>

#### NONE

0: No global reflection method will be used. Reflections can still come from Reflection Captures, Planar Reflections or a Skylight placed in the level.

<a id="unreal.ReflectionMethod.LUMEN"></a>

#### LUMEN

1: Use Lumen Reflections, which supports Screen / Software / Hardware Ray Tracing together and integrates with Lumen Global Illumination for rough reflections and Global Illumination seen in reflections.

<a id="unreal.ReflectionMethod.SCREEN_SPACE"></a>

#### SCREEN_SPACE

2: Standalone Screen Space Reflections.  Low cost, but limited by screen space information.

<a id="unreal.LocalExposureMethod"></a>