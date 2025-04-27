## OnPerChannelLoudnessResults Objects

```python
class OnPerChannelLoudnessResults(MulticastDelegateBase)
```

Delegate to receive all loudness results per channel (time-stamped in an array) since last delegate call.

Args:
    channel_index (int32): 
    loudness_results (Array[LoudnessResults]):

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: Loudness.h

<a id="unreal.OnPerChannelLoudnessResults.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.OnPerChannelMeterResults"></a>