## LocalExposureMethod Objects

```python
class LocalExposureMethod(EnumBase)
```

ELocal Exposure Method

**C++ Source:**

- **Module**: Engine
- **File**: Scene.h

<a id="unreal.LocalExposureMethod.BILATERAL"></a>

#### BILATERAL

0: Decompose image into base and detail layers using a bilateral blur. Only the base layer contrast is reduced in order to preserve details.

<a id="unreal.LocalExposureMethod.FUSION"></a>

#### FUSION

1: Fuse multiple exposures according to quality measures. Local Exposure is calculated using the fused exposures.

<a id="unreal.TranslucencyType"></a>