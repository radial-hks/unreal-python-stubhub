## SourceBusSendLevelControlMethod Objects

```python
class SourceBusSendLevelControlMethod(EnumBase)
```

ESource Bus Send Level Control Method

**C++ Source:**

- **Module**: Engine
- **File**: SoundSourceBusSend.h

<a id="unreal.SourceBusSendLevelControlMethod.LINEAR"></a>

#### LINEAR

0: A send based on linear interpolation between a distance range and send-level range

<a id="unreal.SourceBusSendLevelControlMethod.CUSTOM_CURVE"></a>

#### CUSTOM_CURVE

1: A send based on a supplied curve

<a id="unreal.SourceBusSendLevelControlMethod.MANUAL"></a>

#### MANUAL

2: A manual send level (Uses the specified constant send level value. Useful for 2D sounds.)

<a id="unreal.SoundWaveFFTSize"></a>