## OnSynthEnvelopeValue Objects

```python
class OnSynthEnvelopeValue(MulticastDelegateBase)
```

Called by a synth component and returns the sound's envelope value (using an envelope follower in the audio renderer).
This only works in the audio mixer.

Args:
    envelope_value (float):

**C++ Source:**

- **Module**: AudioMixer
- **File**: SynthComponent.h

<a id="unreal.OnSynthEnvelopeValue.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.OnMediaPlayerMediaEvent"></a>