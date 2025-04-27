## OnSpectrumResults Objects

```python
class OnSpectrumResults(MulticastDelegateBase)
```

Delegate to receive all spectrum results per channel (time-stamped in an array) since last delegate call. If bDownmixToMono setting is true, results will be in channel index 0.

Args:
    channel_index (int32): 
    spectrum_results (Array[SynesthesiaSpectrumResults]):

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: SynesthesiaSpectrumAnalysis.h

<a id="unreal.OnSpectrumResults.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.LocationServicesData_OnLocationChanged"></a>