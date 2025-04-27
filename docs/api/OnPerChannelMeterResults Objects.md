## OnPerChannelMeterResults Objects

```python
class OnPerChannelMeterResults(MulticastDelegateBase)
```

Delegate to receive all meter results per channel (time-stamped in an array) since last delegate call.

Args:
    channel_index (int32): 
    meter_results (Array[MeterResults]):

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: Meter.h

<a id="unreal.OnPerChannelMeterResults.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.OnSpectrumResults"></a>