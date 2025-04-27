## AutoExposureMethod Objects

```python
class AutoExposureMethod(EnumBase)
```

Used by FPostProcessSettings Auto Exposure

**C++ Source:**

- **Module**: Engine
- **File**: Scene.h

<a id="unreal.AutoExposureMethod.AEM_HISTOGRAM"></a>

#### AEM_HISTOGRAM

0: requires compute shader to construct 64 bin histogram

<a id="unreal.AutoExposureMethod.AEM_BASIC"></a>

#### AEM_BASIC

1: faster method that computes single value by downsampling

<a id="unreal.AutoExposureMethod.AEM_MANUAL"></a>

#### AEM_MANUAL

2: Uses camera settings.

<a id="unreal.TemperatureMethod"></a>