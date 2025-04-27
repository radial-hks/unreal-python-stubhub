## OnSamplePlaybackProgress Objects

```python
class OnSamplePlaybackProgress(MulticastDelegateBase)
```

Called while a sample player is playing back. Indicates the playhead progress in percent and as absolute time value (within the file).

Args:
    progress_percent (float): 
    progress_time_seconds (float):

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SynthComponentWaveTable.h

<a id="unreal.OnSamplePlaybackProgress.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.OnTableAltered"></a>