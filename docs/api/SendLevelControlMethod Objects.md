## SendLevelControlMethod Objects

```python
class SendLevelControlMethod(EnumBase)
```

ESend Level Control Method

**C++ Source:**

- **Module**: Engine
- **File**: SoundSubmixSend.h

<a id="unreal.SendLevelControlMethod.LINEAR"></a>

#### LINEAR

0: A send based on linear interpolation between a distance range and send-level range

<a id="unreal.SendLevelControlMethod.CUSTOM_CURVE"></a>

#### CUSTOM_CURVE

1: A send based on a supplied curve

<a id="unreal.SendLevelControlMethod.MANUAL"></a>

#### MANUAL

2: A manual send level (Uses the specified constant send level value. Useful for 2D sounds.)

<a id="unreal.SubmixSendMethod"></a>