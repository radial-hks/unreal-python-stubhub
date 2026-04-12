## AutoExposureMethod Objects

```python
class AutoExposureMethod(EnumBase)
```

Used by FPostProcessSettings Auto Exposure

**C++ Source:**

- **Module**: Engine
- **File**: Scene.h

<a id="unreal.AutoExposureMethod.AEM_HISTOGRAM"></a>

#### AEM\_HISTOGRAM

0: requires compute shader to construct 64 bin histogram

<a id="unreal.AutoExposureMethod.AEM_BASIC"></a>

#### AEM\_BASIC

1: faster method that computes single value by downsampling

<a id="unreal.AutoExposureMethod.AEM_MANUAL"></a>

#### AEM\_MANUAL

2: Uses camera settings.

<a id="unreal.TemperatureMethod"></a>