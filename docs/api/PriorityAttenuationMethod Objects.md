## PriorityAttenuationMethod Objects

```python
class PriorityAttenuationMethod(EnumBase)
```

EPriority Attenuation Method

**C++ Source:**

- **Module**: Engine
- **File**: SoundAttenuation.h

<a id="unreal.PriorityAttenuationMethod.LINEAR"></a>

#### LINEAR

0: A priority attenuation based on linear interpolation between a distance range and priority attenuation range

<a id="unreal.PriorityAttenuationMethod.CUSTOM_CURVE"></a>

#### CUSTOM_CURVE

1: A priority attenuation based on a supplied curve

<a id="unreal.PriorityAttenuationMethod.MANUAL"></a>

#### MANUAL

2: A manual priority attenuation (Uses the specified constant value. Useful for 2D sounds.)

<a id="unreal.NonSpatializedRadiusSpeakerMapMode"></a>