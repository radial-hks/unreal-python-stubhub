## ReverbSendMethod Objects

```python
class ReverbSendMethod(EnumBase)
```

EReverb Send Method

**C++ Source:**

- **Module**: Engine
- **File**: SoundAttenuation.h

<a id="unreal.ReverbSendMethod.LINEAR"></a>

#### LINEAR

0: A reverb send based on linear interpolation between a distance range and send-level range

<a id="unreal.ReverbSendMethod.CUSTOM_CURVE"></a>

#### CUSTOM_CURVE

1: A reverb send based on a supplied curve

<a id="unreal.ReverbSendMethod.MANUAL"></a>

#### MANUAL

2: A manual reverb send level (Uses the specified constant send level value. Useful for 2D sounds.)

<a id="unreal.PriorityAttenuationMethod"></a>