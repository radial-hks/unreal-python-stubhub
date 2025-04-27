## OnAudioMultiEnvelopeValue Objects

```python
class OnAudioMultiEnvelopeValue(MulticastDelegateBase)
```

Called while a sound plays and returns the sound's average and max envelope value (using an envelope follower in the audio renderer per wave instance).
This only works in the audio mixer.

Args:
    average_envelope_value (float): 
    max_envelope (float): 
    num_wave_instances (int32):

**C++ Source:**

- **Module**: Engine
- **File**: AudioComponent.h

<a id="unreal.OnAudioMultiEnvelopeValue.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.OnAudioPlaybackPercent"></a>