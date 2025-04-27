## OnLatestSpectrumResults Objects

```python
class OnLatestSpectrumResults(MulticastDelegateBase)
```

Delegate to receive only the most recent overall spectrum result per channel. If bDownmixToMono setting is true, results will be in channel index 0.

Args:
    channel_index (int32): 
    latest_spectrum_results (SynesthesiaSpectrumResults):

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: SynesthesiaSpectrumAnalysis.h

<a id="unreal.OnLatestSpectrumResults.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.OnOverallLoudnessResults"></a>