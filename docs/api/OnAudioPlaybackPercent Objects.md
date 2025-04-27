## OnAudioPlaybackPercent Objects

```python
class OnAudioPlaybackPercent(MulticastDelegateBase)
```

Called as a sound plays on the audio component to allow BP to perform actions based on playback percentage.
Computed as samples played divided by total samples, taking into account pitch.
Not currently implemented on all platforms.

Args:
    playing_sound_wave (SoundWave): 
    playback_percent (float):

**C++ Source:**

- **Module**: Engine
- **File**: AudioComponent.h

<a id="unreal.OnAudioPlaybackPercent.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.OnAudioPlayStateChanged"></a>