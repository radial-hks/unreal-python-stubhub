## OnAudioSingleEnvelopeValue Objects

```python
class OnAudioSingleEnvelopeValue(MulticastDelegateBase)
```

Called while a sound plays and returns the sound's envelope value (using an envelope follower in the audio renderer).
This only works in the audio mixer.

Args:
    playing_sound_wave (SoundWave): 
    envelope_value (float):

**C++ Source:**

- **Module**: Engine
- **File**: AudioComponent.h

<a id="unreal.OnAudioSingleEnvelopeValue.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.OnAudioVirtualizationChanged"></a>