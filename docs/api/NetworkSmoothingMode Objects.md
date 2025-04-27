## NetworkSmoothingMode Objects

```python
class NetworkSmoothingMode(EnumBase)
```

Smoothing approach used by network interpolation for Characters.

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.NetworkSmoothingMode.DISABLED"></a>

#### DISABLED

0: No smoothing, only change position as network position updates are received.

<a id="unreal.NetworkSmoothingMode.LINEAR"></a>

#### LINEAR

1: Linear interpolation from source to target.

<a id="unreal.NetworkSmoothingMode.EXPONENTIAL"></a>

#### EXPONENTIAL

2: Exponential. Faster as you are further from target.

<a id="unreal.OverlapFilterOption"></a>