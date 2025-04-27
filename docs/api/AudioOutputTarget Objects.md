## AudioOutputTarget Objects

```python
class AudioOutputTarget(EnumBase)
```

EAudio Output Target

**C++ Source:**

- **Module**: Engine
- **File**: AudioOutputTarget.h

<a id="unreal.AudioOutputTarget.SPEAKER"></a>

#### SPEAKER

0: Sound plays only from speakers.

<a id="unreal.AudioOutputTarget.CONTROLLER"></a>

#### CONTROLLER

1: Sound plays only from controller if present.

<a id="unreal.AudioOutputTarget.CONTROLLER_FALLBACK_TO_SPEAKER"></a>

#### CONTROLLER_FALLBACK_TO_SPEAKER

2: Sound plays on the controller if present. If not present, it plays from speakers.

<a id="unreal.SoundWaveLoadingBehavior"></a>